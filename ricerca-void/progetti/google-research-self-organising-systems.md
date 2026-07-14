# google-research/self-organising-systems

Link: https://github.com/google-research/self-organising-systems

Stelle: ~420 · Linguaggio: Jupyter Notebook (JAX/TF/PyTorch) · Attivita: viva (push gen 2026, repo aggiornato lug 2026) · Licenza: Apache-2.0

## Cosa fa
E' il monorepo del gruppo di Mordvintsev / Randazzo / Niklasson (Google) dietro la serie Distill sulla self-organization. Raccoglie il codice di Growing Neural Cellular Automata, Self-classifying MNIST, Texture NCA, Particle Lenia, la formulazione energy-based e vari esperimenti collaterali (grafting, reprogramming avversariale, differentiable FSM/logic CA, versioni JAX con EvoJax). Il filo conduttore e' uno solo: come la struttura globale emerge da regole locali identiche applicate ovunque.

## Come e fatto
Non e' una libreria unica ma una collezione di notebook autonomi piu qualche sottopacchetto (`mplp/`, `isotropic_nca/`, `notebooks/particle_lenia.ipynb`). L'idea chiave ricorrente: ogni cella e' un piccolo vettore di stato (alcuni canali "visibili" tipo RGBA + canali nascosti); una singola rete condivisa legge il vicinato locale (percezione via convoluzioni/Sobel) e produce un incremento di stato; si itera nel tempo con aggiornamenti stocastici asincroni. Il tutto e' differenziabile end-to-end, quindi la "regola locale" si allena per gradiente verso un target globale (un'immagine, una classificazione, una texture). Particle Lenia sposta la stessa filosofia dal grid alle particelle: campo di energia continuo + dinamica di gradiente da cui emergono pattern viventi.

## Perche riguarda te
E' probabilmente il repo piu vicino in spirito all'arena del vuoto e alle particelle-emergenza. Qui "coscienza=ricorsione della realta attraverso la materia" ha una controparte concreta e minimale: la stessa regola locale, iterata ricorsivamente su un substrato, genera e ripara struttura globale (i Growing NCA rigenerano dopo il danno - morfogenesi robusta). Il punto onesto di divergenza: loro allenano la regola per gradiente verso un target esterno, mentre la tua arena del vuoto cerca emergenza senza target, per regole poste a mano. Quindi il valore per te non e' il training, ma il substrato: stato multicanale con canali nascosti, percezione locale, update asincrono, e la scoperta empirica che poche regole locali bastano per morfogenesi + rigenerazione. Particle Lenia in particolare e' il ponte diretto verso un modello a particelle con campo di energia, piu adatto a "oscilloscopi/particelle" di un grid rigido.

## Da rubare
1. Il pattern "canali nascosti + update asincrono stocastico": non tutte le celle si aggiornano ad ogni step (maschera random), e i canali extra oltre a RGBA fanno da memoria/segnale interno. E' un modo economico per dare stato latente e stabilita a un'arena di particelle senza aggiungere regole globali.
2. La formulazione di Particle Lenia (campo di energia scalare + moto lungo il gradiente) come cuore fisico dell'arena: la definisci una volta e l'emergenza di "esseri" e clustering viene dalla dinamica, non da if-then codificati - piu vicino all'idea di ricorsione della materia che a uno scripting di comportamenti.
