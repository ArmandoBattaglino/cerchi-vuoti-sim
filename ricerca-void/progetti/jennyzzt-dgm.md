# Darwin Gödel Machine — jennyzzt/dgm

<https://github.com/jennyzzt/dgm>

**2.2k stelle · Python · ultimo push ago 2025 · licenza Apache-2.0** · paper arXiv:2505.22954 (Zhang, Hu, Lu, Lange, Clune — Sakana AI / UBC / Vector Institute)

## Cosa fa

Un agente di coding che riscrive il proprio sorgente e valida ogni modifica in modo empirico su benchmark reali (SWE-bench, Polyglot). Non un solo agente che migliora se stesso in linea retta: mantiene un **archivio** (una popolazione) di versioni dell'agente, ne pesca una come "genitore", la fa mutare (l'agente modifica il proprio codice), misura l'accuratezza sul benchmark e reinserisce il figlio nell'archivio. Nel paper l'accuratezza SWE-bench sale dal ~20% al ~50% lungo le generazioni. È la realizzazione pratica e parziale della Gödel-machine di Schmidhuber: dove Schmidhuber pretendeva una prova formale che una modifica sia migliorativa, la DGM sostituisce la prova con la **validazione empirica** sul benchmark.

## Come è fatto

Loop esterno in `DGM_outer.py`, agente iniziale in `coding_agent.py`, tool dei foundation model in `tools/`, valutazione in `swe_bench/` e `polyglot/`. Ogni nodo dell'archivio è un commit con il suo `metadata` (accuracy_score, id risolti/irrisolti, `parent_commit`). Il cuore è `choose_selfimproves(...)`: sceglie i genitori da cui ramificare. I metodi di selezione sono la parte interessante:
- `score_prop` — probabilità ∝ sigmoide dello score (sfrutta i migliori).
- `score_child_prop` — probabilità ∝ score × 1/(1+numero_di_figli). Cioè penalizza i rami già molto esplorati e favorisce nodi ancora "vergini". È di fatto **quality-diversity / open-endedness**: non collassa sul singolo migliore, tiene viva la varietà.

Ogni figlio parte da un genitore, tenta un self-improvement su issue che il genitore ha fallito (empty/unresolved), e sopravvive nell'archivio anche se non è il migliore in assoluto. Nota di sicurezza esplicita nel README: esegue codice generato dal modello, va sandboxato (Docker).

## Perché riguarda te

Questo è il ramo **ricorsione / self-reference** allo stato più concreto che esista in OSS. Due agganci onesti:

1. **Coscienza-ricorsione.** La tua tesi capstone ("coscienza = ricorsione della realtà attraverso la materia") qui ha un analogo operativo: un sistema che si include nel proprio dominio di modifica. Ma attenzione alla divergenza — la DGM non "sente" nulla e non ha un modello di sé; la ricorsione è puramente strumentale (codice che riscrive codice per alzare uno score). È un ottimo caso di studio di *dove la ricorsione self-referente NON basta a produrre interiorità*. Utile come contro-esempio nel dossier.

2. **Archivio open-ended = particelle-emergenza.** L'archivio che ramifica e mantiene diversità è esattamente una popolazione da cui emerge struttura non pianificata. Se l'arena del vuoto ha "particelle" che si riproducono e mutano, `score_child_prop` è la legge di selezione già scritta e testata.

Divergenza da tenere presente: la validazione è ancorata a un benchmark esterno fisso. Nella tua arena non hai un SWE-bench — la "fitness" andrebbe definita internamente (novelty, coerenza, sopravvivenza), il che è molto più fragile.

## Da rubare

- **La formula di selezione `score × 1/(1+children_count)`** come legge di novelty-gating per una popolazione: favorisce esplicitamente i rami poco esplorati senza abbandonare la qualità. Trapiantabile 1:1 su una memoria o un'arena dove vuoi evitare il collasso sul singolo attrattore.
- **Il pattern archivio-di-commit**: ogni stato è un commit con metadata (score, parent, cosa ha risolto/fallito). Rende l'intera storia evolutiva ispezionabile e "replayabile" — utile per un oscilloscopio che voglia mostrare la genealogia degli stati, non solo l'ultimo.
