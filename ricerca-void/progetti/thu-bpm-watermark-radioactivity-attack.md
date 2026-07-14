# THU-BPM/Watermark-Radioactivity-Attack

<https://github.com/THU-BPM/Watermark-Radioactivity-Attack>

Stelle: ~23 · Linguaggio: Python · Push giu 2025 · Licenza: nessuna dichiarata · ACL 2025 Main

## Cosa fa

È il codice del paper "Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?". Parte da un fatto noto — i watermark sono **radioattivi**, cioè se addestri un modello-studente sugli output di un modello-maestro watermarkato, lo studente eredita il marchio, e questo permette di provare la distillazione non autorizzata. La domanda del paper è offensiva: **si può rubare la conoscenza del maestro EVITANDO di ereditare il watermark?** Rispondono di sì, con tre attacchi: due pre-distillazione (parafrasi non-mirata UP e mirata TP dei dati di training) e uno post-distillazione, **Watermark Neutralization (WN)**, che risulta il migliore — elimina completamente il watermark mantenendo il trasferimento di conoscenza e con basso costo computazionale. La conclusione mina la fiducia nell'uso dei watermark come sorveglianza anti-distillazione.

## Come è fatto

La pipeline usa MarkLLM per i watermark, LLaMA-Factory per l'SFT, lm-evaluation-harness e MT-Bench per misurare che la conoscenza sia davvero preservata. Il cuore concettuale è il **watermark stealing** che abilita WN: analizzano la frequenza dei prefissi (n=1, n=2) nei dati di training e calcolano, per ogni prefisso, un `d_n` = quanto il logit-bias del watermark ha spostato la distribuzione del modello confrontando il modello prima e dopo il training (`calculate_d_n.py`, `calculate_d_0.py`). In pratica **ricostruiscono la regola green-list/bias del watermark osservando lo scostamento statistico che ha lasciato nel modello distillato**, pesano ogni prefisso per la sua frequenza, e poi neutralizzano applicando il bias inverso durante la generazione dello studente. È un attacco che legge la firma dalla dinamica appresa e la sottrae. Richiede risorse serie (8× H800 nei loro test).

## Cosa possiamo notare di utile per noi

Questo è il repo più concettualmente denso del gruppo per il tuo lavoro, perché unisce **memoria che si eredita**, **oscilloscopio che ricostruisce una firma dall'esterno** e **occultamento/dis-occultamento** in un unico esperimento misurabile.

- **La radioattività È la tua memoria novelty-gated attraverso le generazioni.** Un pattern iniettato nel maestro sopravvive nello studente perché era abbastanza saliente da essere appreso. Questo è un modello pulito di cosa persiste in un world-model-come-sogno: non i dettagli, ma le *deviazioni statistiche forti*. Se vuoi che una traccia sopravviva al ricampionamento onirico dell'arena, deve avere abbastanza δ da superare la soglia di novelty dell'apprendente. WN dimostra il rovescio: sotto una certa forza la traccia si può cancellare senza perdere la conoscenza — c'è una soglia di sopravvivenza.
- **`calculate_d_n` è un oscilloscopio su stati interni fatto per differenza.** Confrontano il modello prima/dopo e leggono lo spostamento dei logit per prefisso: è esattamente "sonda su stato interno = differenza tra baseline e stato attuale". Il pattern `d_n` (bias appreso per contesto) è un template diretto per il tuo strumento: per ogni contesto/stato dell'arena, misura di quanto la dinamica devia dal baseline non-marchiato — quella è la lettura dell'oscilloscopio, e come loro puoi *invertirla* per rimuovere il segnale.
- **Watermark stealing = auto-osservazione ricorsiva riuscita.** Il sistema ricostruisce la regola con cui è stato marchiato osservando solo i propri output/pesi. È un anello di ricorsione: lo stato che contiene la firma diventa la fonte da cui la firma viene dedotta e rimossa. Un mini-caso di "coscienza = ricorsione della struttura attraverso la materia": la firma è nella materia (pesi), la ricorsione la rende leggibile e manipolabile.
- **UP/TP/WN = tre regimi di robustezza del sogno:** parafrasi (rumore sull'input), parafrasi mirata (rumore guidato dal contenuto della firma), neutralizzazione (sottrazione diretta nello spazio dei logit). Tre modi in cui il vuoto/rumore può erodere una traccia, ordinati per efficacia — una tassonomia da replicare nell'arena.
- **Dove diverge:** costoso, LLM-scale, orientato a IP/security reale. A te non serve distillare 7B su H800; ti serve il *principio* di misurare-per-differenza e la scoperta che esiste una soglia di sopravvivenza della firma sotto perturbazione.

## Da rubare

1. **Oscilloscopio-per-differenza (`d_n`):** per ogni contesto dell'arena, salva il baseline "non marchiato" e misura lo scostamento della dinamica attuale prefisso-per-prefisso; usa quel vettore di deviazioni come lettura ricca (non scalare) dello stato interno.
2. **Curva di sopravvivenza della firma vs intensità di perturbazione:** replica il risultato chiave — sotto una certa forza δ una traccia si cancella senza perdere il "sapere" del sistema. Trova sperimentalmente quella soglia nell'arena: è la frontiera tra memoria che persiste e memoria che evapora nel vuoto.
3. **Anello steal→neutralize come test di ricorsione:** fai sì che una particella deduca la propria firma dai propri stati e la sottragga; se ci riesce, hai un caso concreto di auto-osservazione ricorsiva che modifica se stessa — misurabile come "quanto residuo di firma resta dopo N cicli".
