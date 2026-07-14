# World Models — Ha & Schmidhuber

Link: https://arxiv.org/abs/1803.10122 · sito interattivo: https://worldmodels.github.io

Paper NeurIPS 2018 · David Ha, Jürgen Schmidhuber · fondativo (world model come sogno interno)

## Cosa fa
E' il paper-radice della linea "world model come sogno interno". Un agente impara un modello compresso e predittivo del proprio ambiente (i giochi CarRacing e VizDoom-TakeCover) e poi si addestra *dentro* quel modello invece che nell'ambiente reale. Nel caso Doom, la policy viene allenata quasi interamente nelle allucinazioni generate dal modello ricorrente e poi trasferita con successo al gioco vero. E' la dimostrazione minimale e concreta che un agente puo vivere, apprendere e agire dentro la propria simulazione compressa della realta.

## Come e' fatto
Architettura a tre blocchi, deliberatamente piccola:
- **V (Vision)** — un VAE convoluzionale comprime ogni frame in un vettore latente `z` di poche decine di dimensioni. E' l'occhio: butta via i pixel e tiene l'essenza.
- **M (Memory)** — una RNN con output a Mixture Density (MDN-RNN) predice la *distribuzione* di `z` al passo successivo dato `z` corrente, l'azione e lo stato nascosto `h`. Modella la dinamica come distribuzione, non come punto: puo quindi campionare traiettorie plausibili — "sognare".
- **C (Controller)** — una rete lineare minuscola che mappa `[z, h]` in azioni, ottimizzata con evoluzione (CMA-ES), non con backprop. Tenendo il controller minuscolo, quasi tutta la capacita e la conoscenza del mondo stanno in V e M.
Il pezzo chiave e' l'**ambiente-sogno**: un ambiente fittizio che espone la stessa interfaccia dell'ambiente reale ma il cui `step()` fa girare la MDN-RNN invece del gioco. Un parametro di **temperatura** regola quanto e' rumoroso il sogno; alzarlo rende il mondo interno piu incerto e — paradossalmente — allena policy piu robuste, perche impedisce all'agente di sfruttare i difetti del modello.

## Cosa possiamo notare di utile per noi
E' l'aggancio piu diretto alla tua tesi **world-model-come-sogno** e alla ricorsione realta-attraverso-la-materia. Qui la fattorizzazione percezione (V) / dinamica generativa (M) / azione (C) e' resa esplicita e abbastanza piccola da leggerla in un pomeriggio. Per l'arena del vuoto il punto notevole e' che l'agente **non ha bisogno del mondo reale per vivere**: gli basta la propria simulazione compressa — esattamente la chiusura auto-referenziale che ti interessa, il sistema che gira su un modello di se stesso. La separazione MDN (distribuzione, non punto) e' rilevante per i tuoi oscilloscopi: modellare la dinamica come distribuzione ti da gratis una misura di *incertezza per-passo*, che e' materia prima per un segnale di sorpresa/novelty. E la temperatura e' la manopola entropia-interna resa esplicita.
Dove diverge nettamente: non c'e' nessun novelty-gating ne emergenza aperta — il sogno serve solo a massimizzare una reward fissa; il modello e' congelato dopo il training; la temperatura e' un iperparametro impostato a mano, non una grandezza che il sistema misura su se stesso. E' un oscilloscopio calibrato una volta e poi spento, non uno strumento vivo che il sistema legge in tempo reale. Il tuo salto rispetto a questo paper e' rendere dinamiche e auto-osservate proprio le quantita che qui sono fisse.

## Da rubare
1. **Il "dream environment" come drop-in dell'ambiente reale**: un wrapper con la stessa interfaccia `step()/reset()` che internamente fa girare il modello generativo. Per la tua arena: far vivere le particelle/agenti alternativamente nel mondo vero e nella loro previsione con lo stesso codice, e usare la **divergenza sogno-vs-realta come segnale di novelty/sorpresa**.
2. **La dinamica modellata come distribuzione (MDN)** invece che come punto singolo: ti regala una misura di incertezza per-passo, cheap da calcolare, da mandare direttamente all'oscilloscopio come indicatore di quanto il sistema "sa" del suo prossimo stato.
3. **La temperatura da iperparametro a variabile auto-regolata**: qui e' fissa; il tuo contributo e' chiudere il loop — il sistema alza/abbassa il rumore del proprio sogno in risposta a quanto si sorprende, trasformando l'entropia interna in una manopola che il sistema gira da solo.
