# hzy312/Awesome-LLM-Watermark

<https://github.com/hzy312/Awesome-LLM-Watermark>

Stelle: ~375 · Formato: lista curata (solo README) · Ultimo push: dic 2024 · Licenza: nessuna dichiarata

## Cosa fa

È una bibliografia viva e curata del settore watermarking, divisa in **Text watermark** e **Image watermark**, con centinaia di paper raccolti con autori, venue (ICLR/ACL/NeurIPS/preprint) e link arXiv. Copre l'intero spettro del filone: schemi di embedding (KGW e derivati, distortion-free, multi-bit, error-correcting), analisi statistica dei watermark (framework di detection efficiency, regole ottimali, pivot), il fenomeno della **radioattività** (i watermark che sopravvivono al training/distillation), e soprattutto un ricco sottofilone di **attacchi** (watermark stealing, collision, spoofing, paraphrasing, "attacking watermarks by exploiting their strengths"). Non contiene codice: è una mappa per orientarsi nel campo e trovare il paper giusto per ogni sotto-problema. Fermo a fine 2024, quindi utile come snapshot storico più che come tracker in tempo reale.

## Come è fatto

È un singolo `README.md` organizzato per bullet, ogni voce con titolo in grassetto, venue, autori e URL. Il valore è la **curation e la tassonomia implicita**: leggendola si ricostruisce la struttura del campo — da un lato chi costruisce canali (embedding schemes con i loro trade-off), dall'altro chi li rompe (attack surface). Emergono cluster ricorrenti: watermark semantici vs sintattici, distortion-free vs biased, single-bit vs multi-bit, robustezza cross-lingua, e la tensione centrale rilevabilità/robustezza/qualità che ogni paper prova a spostare. Alcune voci notevoli per il nostro sguardo: "Excuse me, sir? Your language model is leaking (information)" (leakage), "Watermarking Makes Language Models Radioactive", "Lost in Overlap: Watermark Collision", "Proving membership in LLM pretraining data via data watermarks".

## Cosa possiamo notare di utile per noi

Il repo in sé è una lista, quindi il suo valore per te non è codice ma **cartografia del possibile** nel dominio occultamento/rilevamento — un modo per non reinventare concetti che il campo ha già nominato.

- **Vocabolario di attacchi = catalogo di modi in cui un segnale nascosto muore.** Per la tua arena del vuoto ti serve sapere *come* un occultamento fallisce sotto perturbazione: paraphrasing (rumore semantico), collision (due segnali che si sovrascrivono, "Lost in Overlap"), stealing (l'osservatore ricostruisce la chiave dalle statistiche). Ognuno è una legge di robustezza da simulare: il vuoto/rumore come parafrasi continua, la collisione come interferenza tra particelle che marchiano lo stesso spazio.
- **"Radioattività" = memoria che sopravvive alla trasmissione.** Il concetto che una firma iniettata nell'output sopravvive quando un altro sistema apprende da quell'output è profondamente rilevante al tuo world-model-come-sogno e alla memoria novelty-gated: un pattern abbastanza saliente si *eredita* attraverso il ricampionamento. La radioattività è la versione fisica di "una traccia che persiste attraverso generazioni di stati".
- **"Language model is leaking information" e data-watermark per membership** toccano il tuo oscilloscopio: sono tecniche per leggere, dall'esterno e senza chiave, se uno stato interno *contiene* qualcosa che non dovrebbe. È esattamente la lettura anomalia-based che ti serve (rilevare occultamento senza conoscere il segreto).
- **Statistical framework of watermarks (pivot, detection efficiency, optimal rules):** questi paper danno la matematica del rilevatore ottimale dato un budget di entropia — utile se vuoi che gli oscilloscopi dell'arena siano provabilmente ottimali e non euristici.
- **Dove diverge:** tutto NLP-centrico e fermo al 2024; nessuna nozione di arena/particelle/sogno. Usalo come indice per pescare 3-4 paper chiave (radioactivity, collision, statistical-optimal-detection, leaking) e leggere quelli, non l'intera lista.

## Da rubare

1. **Tassonomia degli attacchi come suite di stress-test:** codifica paraphrase/collision/stealing come tre perturbazioni distinte nell'arena e misura la sopravvivenza della firma sotto ciascuna — così i tuoi canali nascosti hanno un profilo di robustezza multi-asse, non un singolo numero.
2. **Concetto di radioattività per la memoria novelty-gated:** testa se una firma iniettata in uno stato sopravvive quando un secondo sistema apprende/ricampiona da quello stato — un esperimento diretto di ereditarietà del pattern (sogno che si tramanda).
3. **Rilevatore statisticamente ottimale (pivot/optimal-rule) invece di soglia euristica:** per l'oscilloscopio, deriva la regola di decisione ottimale dato il budget di entropia dello stato, così la lettura è fondata e non tarata a mano.
