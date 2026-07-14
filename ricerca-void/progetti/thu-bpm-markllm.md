# THU-BPM/MarkLLM

<https://github.com/THU-BPM/MarkLLM>

Stelle: ~1000 · Linguaggio: Python · Attivo (push lug 2026) · Licenza: Apache-2.0 · EMNLP 2024 Demo

## Cosa fa

MarkLLM è il toolkit open-source di riferimento per il **watermarking di testo generato da LLM**: un framework unificato che implementa, sotto un'unica API, i principali schemi di watermark (KGW/Unigram, SIR, XSIR, Unbiased, DIP, EWD, SWEET, EXP/EXPEdit/EXPGumbel, SynthID-Text, SemStamp/KSemStamp, UPV, TS, Adaptive, MorphMark, STEAL…). Per ciascuno fornisce le due metà — l'incorporamento del marchio durante la generazione e il detector che verifica la presenza — più una suite di valutazione che misura le tre grandezze in tensione: **detectability** (quanto è rilevabile), **robustness** (quanto sopravvive a parafrasi/edit/traduzione) e **text quality** (quanto degrada il testo). Include anche moduli di **visualizzazione** che mostrano token per token dove e come il watermark ha spostato il campionamento. È lo stack che praticamente tutti gli altri paper del settore (inclusi gli attacchi) usano come base comune.

## Come è fatto

L'architettura è a tre livelli: `watermark/` (una classe per schema, tutte con interfaccia `generate_watermarked_text` / `detect_watermark`), `evaluation/` (pipeline di detection, quality_analysis, tool come oracle, success_rate_calculator, text_editor per simulare attacchi), e i `config/*.json` che parametrizzano ogni schema. Il meccanismo comune della famiglia KGW: a ogni step si usa un hash dei token precedenti come seed per partizionare il vocabolario in "green list" e "red list", si aggiunge un bias δ ai logit dei token green, e in detection si conta la frazione di token green — un eccesso statistico rispetto al 50% atteso è la firma. Le varianti cambiano come si sceglie la green list (SIR/XSIR la rendono semanticamente invariante e robusta alla traduzione; Unbiased/DIP puntano a non distorcere la distribuzione; EXP usa il Gumbel-trick per un campionamento watermark-and-distortion-free). Il valore del toolkit è che **standardizza il confronto**: stessa metrica, stesso dataset (C4, cnn_dailymail, wmt16), stessi attacchi per tutti.

## Cosa possiamo notare di utile per noi

Questo è il pezzo più "ingegneristicamente maturo" del filone occultamento e ti dà un vocabolario operativo per firmare stati interni senza distruggerli.

- **Il watermark KGW è esattamente il tuo "occultamento novelty-gated" applicato alla scelta:** partizioni lo spazio delle azioni/token in gruppi via un hash dello stato precedente, e sposti la scelta verso un gruppo. Traslato all'arena del vuoto: puoi marchiare la traiettoria di una particella spingendo impercettibilmente le sue transizioni verso una "green list" seedata dal proprio passato — una firma che vive nella *dinamica*, non nel contenuto. È ricorsivo per costruzione (il seed è la storia recente): un piccolo modello di coscienza-come-ricorsione dove lo stato marchia se stesso.
- **Il triangolo detectability/robustness/quality è la legge dei tre vincoli di ogni canale nascosto** — riusabile 1:1 come funzione-obiettivo nel tuo simulatore: quanto forte è il segnale iniettato vs quanto sopravvive alla perturbazione (rumore/vuoto) vs quanto degrada il comportamento naturale. Ogni schema è un punto diverso su quel Pareto.
- **La visualizzazione token-per-token è un oscilloscopio già fatto:** mostra dove il bias ha alterato la distribuzione. È il template esatto per il tuo strumento — non un allarme binario ma una traccia continua che dice "qui la dinamica interna è stata deviata di δ". Il concetto di "green fraction" è una lettura scalare pulita dell'oscilloscopio.
- **Unbiased/DIP = occultamento a distribuzione preservata:** la loro tesi (marchiare senza spostare la distribuzione attesa) è il tuo caso limite di steganografia perfetta — informazione presente ma statisticamente invisibile finché non hai la chiave/seed. Definisce il confine tra "nascosto ma rilevabile" e "nascosto e provabilmente sicuro".
- **Dove diverge:** è tutto su token discreti di linguaggio con un detector che ha la chiave. Il tuo vuoto è continuo e vuoi rilevamento *senza* chiave (scoperta di anomalia). Prendi il meccanismo di embedding e il triangolo di metriche, lascia l'assunzione del detector informato.

## Da rubare

1. **Seed ricorsivo dal proprio passato:** marchia le transizioni di una particella usando un hash del suo stato recente come seme del partizionamento — firma auto-generata, ricorsiva, che non richiede memoria esterna.
2. **Funzione-obiettivo a tre assi (forza/robustezza/degrado):** adotta il triangolo di MarkLLM come metrica standard per valutare ogni canale nascosto nell'arena, e traccia il Pareto delle particelle.
3. **Oscilloscopio "green fraction":** implementa una lettura scalare continua = frazione di transizioni cadute nel gruppo atteso; deviazione dal 50% = intensità di firma/occultamento, plottata nel tempo come traccia.
