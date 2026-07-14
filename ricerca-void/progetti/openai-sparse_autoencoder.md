# sparse_autoencoder (OpenAI) — SAE su GPT-2 small + visualizer ([repo](https://github.com/openai/sparse_autoencoder))

Stelle: ~590 · Linguaggio: Python (PyTorch) · Ultima attività: luglio 2024 · Licenza: MIT

## Cosa fa
È il repo di riferimento di OpenAI che accompagna il lavoro sulle feature monosemantiche: ospita **sparse autoencoder pre-addestrati sulle attivazioni di GPT-2 small** (a diverse locazioni — post-MLP, residual stream, attn out — e diversi layer, con dizionari fino a 32k latenti) più un **visualizer web** per esplorare le feature scoperte. È più un artefatto didattico/di riferimento che una libreria di training completa: dà il modello, i pesi pre-addestrati scaricabili da blob storage, il codice di training minimale, e uno strumento per *vedere* cosa ogni feature latente rappresenta (quali token/contesti la fanno accendere). È il punto di partenza canonico per capire "come si decompone l'attivazione densa di un transformer in feature interpretabili".

## Come è fatto
L'architettura (`model.py`) è il template pulito e minimale del SAE:
```
latents = activation(encoder(x - pre_bias) + latent_bias)
recons  = decoder(latents) + pre_bias
```
Dettagli che contano:
- **`pre_bias` sottratto all'input e riaggiunto alla ricostruzione**: centra i dati, così l'encoder lavora sulle *deviazioni* dallo stato medio, non sui valori assoluti. Il "punto zero" è il baricentro dell'attività.
- **Normalizzazione opzionale (LayerNorm)** che salva μ e σ per de-normalizzare in output — la ricostruzione avviene nello spazio normalizzato e poi si riscala.
- **Buffer di statistiche per latente**: `stats_last_nonzero` (da quanti step una feature è spenta — serve a rilevare le "dead latents"), `latents_activation_frequency`, `latents_mean_square`. Questi tracciano la *salute* del dizionario: le feature morte (mai attive) sono capacità sprecata.
- **Decoder come matrice di feature**: ogni colonna del decoder è la "direzione" nello spazio di attivazione che quella feature rappresenta; decodificare = sommare le direzioni delle poche feature accese, pesate. La ricostruzione è letteralmente *una manciata di vettori-concetto sommati*.
La sparsità è imposta da una TopK/attivazione sparsa; il grosso del lavoro è nella qualità dei pesi pre-addestrati e nel visualizer che li rende ispezionabili.

## Cosa possiamo notare di utile per noi
Rispetto a EleutherAI/sparsify (il fratello "libreria di training scalabile"), questo repo di OpenAI vale soprattutto per **due cose trasferibili al tuo lavoro**: il *visualizer* e la *contabilità delle dead latents*.

Il **visualizer** è il pezzo più direttamente rilevante per i tuoi **oscilloscopi su stati interni**. Il problema che risolve è: hai migliaia di feature latenti — come fai a *capirle*? La risposta di OpenAI è mostrare, per ogni feature, gli input che la massimizzano e il pattern di attivazione nel contesto. Trasposto alla tua arena: per ogni feature SAE scoperta sugli stati dell'arena, l'oscilloscopio dovrebbe mostrarti *quali configurazioni dell'arena la fanno accendere* — dandoti il vocabolario interpretativo del vuoto. È la differenza tra "l'arena ha 32k gradi di libertà nascosti" e "questa feature = enti che collidono, quest'altra = fronte d'onda, quest'altra = quiescenza". Il visualizer è il ponte tra rappresentazione sparsa e comprensione umana.

Il concetto di **`pre_bias` come baricentro** è sottile ma prezioso per il tuo "vuoto". Il SAE non modella lo stato assoluto, modella la *deviazione dallo stato medio*. Cioè: definisce implicitamente un "vuoto di riferimento" (il pre_bias, lo stato tipico) e rappresenta tutto il resto come scostamenti sparsi da quel vuoto. Questa è esattamente la struttura ontologica che cerchi — c'è un fondo neutro (il vuoto/baricentro) e il *qualcosa* sono le poche deviazioni codificate. Se costruisci un SAE sull'arena, il `pre_bias` appreso *è* la definizione operativa, data-driven, di "stato-vuoto" della tua arena.

Le **dead latents** (`stats_last_nonzero`) hanno una lettura interessante per la novelty. Una feature morta è capacità mai usata; una feature che *risveglia* dopo lunghissimo silenzio segnala che l'arena è entrata in un regime prima inesplorato — il segnale di novelty più forte possibile. Il buffer che OpenAI usa per igiene del training diventa, nelle tue mani, un rilevatore di *transizioni di fase* dell'arena.

Dove diverge: questo repo è più vecchio (2024), specifico per GPT-2 small, con codice di training minimale e non scalabile — per addestrare SAE seri userai sparsify di EleutherAI, non questo. Il visualizer è web-app per feature testuali, va riscritto per stati spaziali/continui. E come tutti i SAE, è atemporale e non ricorsivo: fotografa stati isolati, non cattura dinamica né auto-riferimento. Prendilo come **template dell'architettura minimale + design del visualizer**, non come motore di produzione.

## Da rubare
1. **Il pattern del visualizer feature→esempi-massimizzanti**: per ogni feature latente scoperta sugli stati dell'arena, mostra le configurazioni che la fanno accendere. È l'oscilloscopio che traduce il codice sparso in un vocabolario umano ("questa feature = collisione", ecc.).
2. **`pre_bias` come definizione operativa di stato-vuoto**: modella l'arena come *deviazioni sparse da un baricentro appreso* — il pre_bias diventa la tua definizione data-driven, non postulata, del "vuoto di riferimento" da cui emerge il qualcosa.
3. **`stats_last_nonzero` come rilevatore di transizioni di fase**: monitora le feature morte/dormienti; il risveglio di una feature dopo lungo silenzio è il segnale di novelty più netto — l'arena è entrata in un regime nuovo. Gate della memoria e allarme di transizione dallo stesso buffer.
