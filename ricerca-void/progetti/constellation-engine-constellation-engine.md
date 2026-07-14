# Constellation Engine — CONSTELLATION-ENGINE/constellation-engine

<https://github.com/CONSTELLATION-ENGINE/constellation-engine>

**60 stelle · JavaScript (Node 20+, Electron) · ultimo push giu 2026 · licenza AGPL-3.0** · sito constellation-engine.com

## Cosa fa

Dà a un agente LLM di lunga vita un "ippocampo" esterno: una mappa stellare vivente di nodi tipizzati e archi pesati che non è un magazzino da interrogare ma un **processo** che si attiva, si revisiona, dimentica, consolida e cresce. A ogni turno il messaggio dell'utente non viene usato per un top-k e basta: viene embeddato e iniettato come **segnale di attivazione** che si diffonde nel grafo, sveglia nodi vicini e lontani, seleziona una "pool di attenzione", compila un briefing strutturato e solo allora lo passa all'LLM. Il punto centrale è la separazione netta tra i due strati: l'LLM è la *voce* (linguaggio, ragionamento, tool), il grafo è il *substrato cognitivo* (identità, memoria, esperienza) che sopravvive al cambio di modello. Tra una conversazione e l'altra il grafo continua a vivere: un demone in background diffonde attivazione, decade gli archi inutilizzati e ri-clusterizza le zone anche mentre nessuno parla con l'agente.

## Come è fatto

Il cuore è la **star map**: ogni nodo ha ID stabile, tipo/sottotipo, tre risoluzioni (L0 handle breve / L1 sommario compresso / L2 contenuto pieno), embedding BGE-M3 1024-dim, stato (active/dormant/superseded/deprecated), timestamp bi-temporali, peso e storico accessi. Gli archi sono tipizzati e pesati e determinano *come* fluisce l'attivazione.

Il demone **Mímir** gira su heartbeat da 500ms: fa **Multi-SA** (spreading activation) su tre canali (K=0.50 knowledge, L=0.25 language, S=0.25 scaffold), tre round di inibizione ping-pong, fonde, e calcola `delta = A_fast − baseline`. Ogni 180s fa **Hebbian writeback** con rinforzo asimmetrico stile BCM. Ogni ora: edge-decay (×0.998/h oltre le 24h) e ricalcolo delle **zone Leiden**. Modello mentale semplificato: `A(t+1) ≈ decay·A(t) + diffusion·W·A(t) + input`.

La **attention pool** è uno strato competitivo: punteggio grezzo `0.80·δ + 0.10·slow + 0.05·mass + 0.05·bridge`, per un moltiplicatore di tipo-nodo, con slot permanenti per identità/principi che restano visibili a prescindere. Il **Narrative IR** è un compilatore che trasforma i nodi attivati in un *briefing* (ruoli, tensioni/contraddizioni, reasoning path, episodi) con budget di contesto a 4 livelli (fixed 10% / constellation 28% / summary 10% / active 52%) e tier di precisione (min/med/full). Poi tre loop di feedback — Ratatoskr, Anamnesis, Sleipnir — fanno il debrief post-turno e riscrivono il grafo con ciò che è stato appreso.

## Cosa possiamo notare di utile per noi

Questo è il progetto che rende **operativa** la frase "memoria come campo di attivazione con gating", e ha diretta parentela con il tuo asse arena-del-vuoto e con l'idea di oscilloscopi sugli stati interni:

- **Il grafo È un'arena di attivazione, non un DB.** Mímir è letteralmente un campo che diffonde attivazione tra particelle-nodo, con decadimento, inibizione laterale e soglie. È lo stesso schema mentale della tua arena del vuoto/particelle, ma applicato alla memoria invece che al mondo: i nodi sono particelle, gli archi sono il campo, `A(t+1) ≈ decay·A(t) + diffusion·W·A(t) + input` è la fisica. Trasferibile: puoi far girare la stessa dinamica sopra i tuoi stati interni e leggere `delta = A_fast − baseline` come segnale di "cosa si è svegliato", che è esattamente una lettura da oscilloscopio.

- **Novelty-gating implicito via delta e supersession.** Non usano un giudice-LLM per il gate (come A-MEM) ma una grandezza *interna*: `delta` (quanto un nodo si discosta dal suo baseline lento) e gli stati dormant/superseded/reconsolidation. È novelty-gating fatto con dinamica, non con un oracolo esterno — più vicino a ciò che vuoi tu (la rete che si auto-modifica per dinamica interna). Divergenza netta dal ramo A-MEM: qui il segnale di novità è misurato, deterministico e a costo zero, non una chiamata LLM.

- **Oscilloscopi già montati.** La riga "Auditability: Nodes, edges, activations, pool, injections" e il fatto che ogni turno esponga δ/slow/mass/bridge per ogni nodo è *già* un cruscotto di stati interni. Il loro cruscotto guarda la memoria; il tuo dovrebbe guardare il world-model/percezione. La struttura del pannello (attivazione fast vs slow, mass, bridge value, staleness) è direttamente rubabile come layout di un oscilloscopio sugli stati della tua rete.

- **Coscienza=ricorsione, versione onesta e minima.** Il loop "leggi il grafo → attiva → campiona → rendi → *riscrivi il grafo con quello che hai imparato*" è un anello ricorsivo reale: il presente reinterpreta e riscrive il passato, che cambia come sarà letto il futuro. Non è mistica: è consolidamento post-turno. È un buon esempio di come rendere "ricorsione della realtà attraverso la materia" un meccanismo verificabile invece di uno slogan.

Dove diverge da te: è tutto agganciato a un LLM come "voce" e a un caso d'uso assistant/chat; il grafo non ha un mondo fisico, non c'è percezione, non c'è sogno/world-model generativo. La ricorsione è sulla *memoria testuale*, non su uno stato di mondo simulato. La licenza AGPL è un vincolo se mai volessi riusare codice.

## Da rubare

- **La formula di attention-pool come scoring di salienza per la tua arena**: `raw = 0.80·δ + 0.10·slow + 0.05·mass + 0.05·bridge`, con δ = attivazione-veloce meno baseline-lento. È un modo pulito di combinare novità istantanea + rilevanza persistente + centralità + valore-ponte in un unico numero. Trapiantabile come funzione di salienza per decidere quali particelle/eventi entrano nella "coscienza" (workspace) del tuo sistema.
- **Il ciclo a due velocità di Mímir** (500ms diffusione, 180s Hebbian writeback, 1h decay/reclustering): separare la dinamica veloce di attivazione dalla plasticità lenta degli archi è il pattern giusto per una memoria che si riorganizza senza collassare nel rumore. È il "novelty-gated" fatto come gerarchia di scale temporali, non come flag.
- **Il cruscotto di auditabilità per-turno** (nodi/archi/attivazioni/pool/iniezioni esposti a ogni tick) come modello concreto per i tuoi oscilloscopi: non un log testuale, ma uno snapshot ispezionabile dello stato interno a ogni passo, con δ/slow/mass per elemento.
