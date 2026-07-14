# The Consciousness Prior — [AI-ON/TheConsciousnessPrior](https://github.com/AI-ON/TheConsciousnessPrior)

99 stelle · Jupyter Notebook / Python · fermo dal 2018 · nessuna licenza dichiarata

## Cosa fa
Tentativo comunitario (AI-ON, con William Fedus, Sherjil Ozair, Yoshua Bengio tra i contatti) di implementare in codice il "Consciousness Prior" di Bengio (arXiv:1709.08568, 2017). La tesi del paper: la coscienza come *collo di bottiglia attenzionale* che a ogni istante seleziona pochi elementi da uno stato di rappresentazione ad alta dimensione e li "broadcasta" — un prior per apprendere concetti di alto livello (il ragionamento "System 2"). Il repo esplora questo in setting puramente osservazionale: tracciare oggetti in ambienti sintetici quando l'osservazione e complicata da alta entropia nello spazio dei pixel (task Billiards, Moving MNIST).

## Come e fatto
Struttura minimale in `src/`: `environments/` (billiards.py, moving_mnist.py — generatori sintetici), `models/` (`representation.py` lo stato ad alta dimensione, `consciousness.py` il modulo di selezione/attenzione, `generator.py`), `losses.py`, `train_model.py`. L'idea chiave e la separazione tra uno *stato di rappresentazione* denso (h) e uno *stato cosciente* rado (c) ottenuto per attenzione: c e una manciata di variabili selezionate, e l'obiettivo di training preme perche quel piccolo insieme basti a predire/ricostruire l'evoluzione futura. Notebook di commento esplorano lo scenario osservazionale e l'oscillatore rumoroso.

## Perche riguarda te
E la radice teorica "coscienza = selezione ricorsiva di pochi elementi rilevanti", parente stretto della tua idea di ricorsione e soprattutto di *memoria novelty-gated*: il bottleneck attenzionale E' un gate che lascia passare solo cio che conta. Il task "tracking sotto osservazioni ad alta entropia" e vicino ai tuoi oscilloscopi/particelle: distillare segnale (oggetti, stato coerente) da rumore visivo. Diverge in modo onesto su due fronti: (1) e un progetto abbandonato del 2018, codice largamente scaffold/in-development, piu utile come lettura che come base eseguibile; (2) qui la "coscienza" e un modulo attenzionale in una rete supervisionata, non una dinamica emergente da campi/vuoto — la ricorsione e nell'obiettivo di training, non nel sostrato fisico. Vale piu il paper del codice.

## Da rubare
1. Lo split esplicito stato-denso (h) / stato-cosciente-rado (c) con c = attenzione su h: un modo pulito di implementare il tuo gate di novita come "pochi elementi broadcastati" invece che come filtro binario.
2. L'obiettivo "il piccolo insieme cosciente deve bastare a predire il futuro": usa la predicibilita come pressione selettiva — cio che entra nella memoria/coscienza e cio che riduce l'errore di predizione a valle, criterio misurabile e non arbitrario.
