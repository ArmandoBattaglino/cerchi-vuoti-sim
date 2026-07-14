# pyribs — [icaros-usc/pyribs](https://github.com/icaros-usc/pyribs)

264 stelle · Python · attivo (push lug 2026) · licenza MIT · [pyribs.org](https://pyribs.org)

## Cosa fa
pyribs è una libreria "bare-bones" per l'ottimizzazione Quality-Diversity: minimale, leggibile e didattica, pensata sia per chi entra nel campo sia per ricercatori che inventano nuovi algoritmi. È l'implementazione ufficiale di CMA-ME, CMA-MEGA, CMA-MAE e delle loro varianti scalabili. Come tutti gli algoritmi della famiglia MAP-Elites, produce come output una **heatmap/archivio** dove ogni cella contiene il miglior individuo trovato per una regione dello spazio delle "misure" (i descrittori comportamentali), massimizzando al contempo un obiettivo scalare. A differenza di QDax (che punta sulla scala via JAX), pyribs punta su chiarezza, modularità e facilità di lettura del codice — è il posto giusto per *capire* il meccanismo, non solo per farlo girare veloce.

## Come è fatto
pyribs formalizza QD nel framework **RIBS** (Rapid Illumination of Behavior Space) con tre componenti nettamente separati:
- **Archive** — salva le soluzioni nello spazio delle misure (es. `GridArchive`, `CVTArchive`); è la memoria a celle che ammette solo chi migliora la propria regione.
- **Emitter** — uno o più algoritmi che generano candidati e reagiscono al feedback su come sono stati inseriti (es. `EvolutionStrategyEmitter` basato su CMA-ES, che concentra il campionamento dove l'archivio migliora di più).
- **Scheduler** — orchestra l'interazione archivio↔emitter tramite l'interfaccia `ask()`/`tell()` presa in prestito da pycma.

Il loop: `ask()` chiede candidati agli emitter, l'utente li valuta ottenendo obiettivo + misure, `tell()` li inserisce nell'archivio e restituisce agli emitter il feedback (es. "hai scoperto una cella nuova", "hai migliorato una cella"). Cambiando i tre componenti componi decine di algoritmi QD diversi. Il focus è domini continui a dimensione fissa, come pycma.

## Cosa possiamo notare di utile per noi
Rispetto a QDax, pyribs è più utile a te come **anatomia leggibile del gating per novelty** — è il posto dove studiare *come* è fatto il meccanismo prima di reimplementarlo nella tua arena:
- **Separazione netta Archive / Emitter / Scheduler**. Questa decomposizione è la vera lezione architetturale. Trasferita al tuo sistema: l'**Archive** è la memoria novelty-gated; l'**Emitter** è ciò che genera nuovi stati/perturbazioni del vuoto e sa *dove* vale la pena esplorare in base a cosa la memoria ha già; lo **Scheduler** è il loop che li accoppia. Tenere questi tre ruoli separati rende il sistema modulare e ti permette di scambiare il criterio di novelty senza toccare il generatore.
- **Il feedback di inserimento come segnale di controllo**. Punto sottile e prezioso: in pyribs l'emitter non riceve solo la fitness, riceve *come è andato l'inserimento in archivio* — "cella nuova" vs "miglioramento" vs "scartato". CMA-ME usa questo per orientare l'esplorazione verso le frontiere di novelty. Per il tuo lavoro: il segnale "questo stato ha aperto una regione nuova della memoria" è un feedback ricco che può guidare *dove* il sistema si concentra dopo — non solo cosa memorizza, ma cosa esplora.
- **CMA-MAE e l'annealing della soglia**: invece di ammettere solo se strettamente migliore, si usa una soglia per cella che si alza gradualmente (annealing). Questo evita che l'archivio si irrigidisca troppo presto e bilancia esplorazione/consolidamento. Trasferibile a una memoria novelty-gated che all'inizio è permissiva (registra molto) e col tempo diventa selettiva.
- **Codice come oscilloscopio didattico**: essendo minimale, `GridArchive`/`CVTArchive` sono ~poche centinaia di righe leggibili — il modo più rapido per capire ed adattare la meccanica del gate senza il peso dell'infrastruttura JAX.
- **Dove diverge**: come QDax, assume un obiettivo scalare e domini continui a dimensione fissa, mentre la tua arena è dinamica e forse senza obiettivo. Prendi la *struttura del gate e del feedback*, non l'assunzione di ottimizzazione.

## Da rubare
1. **Architettura a tre ruoli Archive/Emitter/Scheduler** per la tua memoria: separa nettamente "cosa conservo" (archivio novelty-gated), "cosa genero/perturbo e dove esploro" (emitter), e "il loop che li accoppia" (scheduler) — così puoi cambiare criterio di novelty senza riscrivere il generatore.
2. **Feedback di inserimento come segnale di guida**: propaga al generatore l'esito del gating (novel / migliorato / scartato), non solo un punteggio, e usalo per orientare dove il sistema esplora dopo — è il trucco di CMA-ME.
3. **Soglia con annealing (CMA-MAE)**: rendi la memoria permissiva all'inizio e progressivamente selettiva alzando nel tempo la soglia di ammissione per cella, per evitare irrigidimento precoce dell'archivio.
