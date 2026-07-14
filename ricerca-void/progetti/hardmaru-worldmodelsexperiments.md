# World Models Experiments — hardmaru/WorldModelsExperiments

Link: https://github.com/hardmaru/WorldModelsExperiments

720 stelle · Jupyter Notebook / Python · ultimo push 2022 (progetto storico, non piu attivo) · licenza MIT

## Cosa fa
E' il codice di riferimento del paper "World Models" (Ha & Schmidhuber, NeurIPS 2018). Un agente impara un modello interno del proprio ambiente (CarRacing e VizDoom) e lo usa per addestrarsi *dentro il proprio modello* invece che nell'ambiente reale. Nel caso Doom (`doomrnn`) la policy viene allenata quasi interamente nel "sogno" generato dalla RNN, e poi trasferita con successo all'ambiente vero. E' la dimostrazione concreta e minimale dell'idea "il modello del mondo e' un sogno navigabile".

## Come e' fatto
Architettura a tre blocchi, deliberatamente semplice:
- **V (Vision)** — un VAE convoluzionale comprime ogni frame in un vettore latente `z` (`vae.py`). E' l'occhio: riduce il pixel-space a poche decine di dimensioni.
- **M (Memory)** — una RNN con Mixture Density output (MDN-RNN, `rnn.py`) predice la distribuzione di `z` al passo successivo dato `z` e l'azione. E' il cuore generativo: modella la dinamica temporale come distribuzione, non come punto singolo, quindi puo "sognare" traiettorie plausibili campionando.
- **C (Controller)** — una minuscola rete lineare che mappa `[z, h]` (latente + stato nascosto RNN) in azioni, ottimizzata con CMA-ES (evoluzione, non backprop; `es.py`).

Il pezzo chiave e' `dream_env.py` / `doomrnn.py`: un ambiente Gym fittizio dove lo "step" non tocca il gioco reale ma fa girare la MDN-RNN, che allucina il prossimo `z`. Un parametro di temperatura regola quanto e' rumoroso/incerto il sogno — alzarlo rende il mondo interno piu imprevedibile e paradossalmente allena policy piu robuste.

## Perche riguarda te
E' l'aggancio piu diretto alla tua tesi "world model come sogno interno" e alla ricorsione realta-attraverso-la-materia. Qui la separazione percezione (V) / dinamica generativa (M) / azione (C) e' resa esplicita e piccola abbastanza da leggerla in un pomeriggio. Per l'arena del vuoto e' interessante che l'agente non ha bisogno del mondo reale per vivere: gli basta la propria simulazione compressa — esattamente il tipo di chiusura auto-referenziale che ti interessa. Dove diverge: non c'e' nessuna nozione di novelty-gating ne di emergenza aperta; il sogno serve solo a massimizzare una reward fissa, il modello e' congelato dopo il training, e la temperatura e' un iperparametro manuale, non una grandezza che il sistema misura su se stesso. E' un oscilloscopio spento dopo la calibrazione, non uno strumento vivo.

## Da rubare
1. **Il "dream environment" come drop-in dell'ambiente reale**: un wrapper che espone la stessa interfaccia `step()/reset()` ma internamente fa girare il modello generativo. Per la tua arena significa poter far vivere le particelle/agenti alternativamente nel mondo vero e nella loro previsione, con lo stesso codice — e confrontare i due (divergenza sogno-vs-realta come segnale di novelty/sorpresa).
2. **La temperatura sul modello generativo come manopola di incertezza**: campionare la dinamica futura da una MDN e alzare/abbassare il rumore e' un modo cheap e concreto per rendere l'entropia interna un parametro visibile su cui agire — trasformabile da iperparametro fisso a variabile che il sistema regola in risposta a quanto "si sorprende".
