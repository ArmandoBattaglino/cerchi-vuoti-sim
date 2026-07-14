# AI-AfterImage — DragonShadows1978/AI-AfterImage

<https://github.com/DragonShadows1978/AI-AfterImage>

**22 stelle · Python · ultimo push mag 2026 · licenza MIT** · pacchetto PyPI `ai-afterimage`

## Cosa fa

Memoria episodica per agenti di coding, pensata come hook per Claude Code (e ora Codex). La metafora è nel nome: come l'immagine residua che persiste dopo aver distolto lo sguardo, AfterImage dà all'agente memoria persistente del codice che ha scritto tra una sessione e l'altra — "the ghost of code written, persisting across sessions". Risolve l'amnesia di sessione: l'agente ricomincia ogni volta da zero, l'utente rispiega il contesto, l'agente riscrive soluzioni simili. Al momento di scrivere/editare, l'hook cerca nella KB codice passato correlato e inietta "l'hai già scritto così..." con esempi, poi estrae il diff e lo archivia per il recupero futuro. Tutto locale: SQLite + embeddings, nessuna chiamata cloud, funziona offline dopo il download del modello.

## Come è fatto

Package `afterimage/` con un ciclo pre/post Write-Edit: (1) pre-write filtra (`filter.py` — è codice? non `.md`/`.json`), cerca nella KB (`search.py`, ricerca ibrida keyword+semantica su `kb.py`) e inietta contesto (`inject.py`); (2) post-write estrae il diff (`extract.py`, con parser multi-formato per transcript Claude e Codex, incluso `apply_patch`) e lo memorizza. Sopra la memoria grezza sono stati stratificati moduli di "intelligenza": `semantic_chunking/` (parsing in unità semantiche + `relevance_scorer.py` che pesa recency 20% / prossimità 25% / similarità semantica 35% / project-awareness 20% + `snippet_summarizer.py` che riassume 3+ snippet simili per risparmiare token, con cache 108x); `semantic_index/` (tabelle simboli, go-to-definition, find-references, call graph, hover, type inference basica via tree-sitter); `churn/` che classifica i file in tier Gold/Silver/Bronze/Red per anzianità di modifica e avverte prima di toccare file stabili o funzioni molto editate.

## Cosa possiamo notare di utile per noi

È un'implementazione pragmatica e locale del tuo ramo **memoria episodica**, con un paio di idee che parlano direttamente al novelty-gating e alla persistenza cross-sessione:

- **Il relevance scorer come gate multi-fattore.** Invece del solo coseno, pesa recency + prossimità + similarità + project-awareness. È una versione più ricca del tuo "novelty-gate": la decisione di *iniettare* una memoria non è binaria su similarità, è una combinazione di assi. Trasferibile direttamente alla tua memoria mem0/arena: cosa merita di riaffiorare non è "il più simile" ma "il più rilevante ora", e la rilevanza ha una geometria.
- **Il churn tier come memoria del *tasso di cambiamento*, non del contenuto.** AfterImage non ricorda solo *cosa* è stato scritto, ma *quanto spesso una regione cambia* (Gold=stabile → Red=caldo). È una memoria di second'ordine: statistica sulla dinamica, non sullo stato. Per la tua arena del vuoto è suggestivo — tracciare non le posizioni delle particelle ma la *temperatura di modifica* delle regioni, e usarla per gating (le zone calde meritano attenzione/memoria, le fredde no).
- **La summarization dei cluster (3+ simili → sintesi).** È compressione novelty-gated: quando molte memorie collassano su un pattern, non le tieni tutte, ne tieni l'astrazione. Meccanismo concreto per evitare che la memoria accumuli ridondanza.

Divergenza: la memoria qui è al servizio del *recupero utile* (non riscrivere codice), non dell'auto-organizzazione o della ricorsione. Non c'è nessun anello in cui la memoria reinterpreta se stessa (come in A-MEM); è più magazzino-intelligente che rete-che-si-ristruttura.

## Da rubare

- **Lo scorer a 4 assi (recency/prossimità/similarità/project) con pesi espliciti** come formula di novelty-gating: sostituisce il singolo threshold di similarità con un giudizio geometrico su cosa riaffiora.
- **Il churn tier system**: mantenere per ogni regione della tua arena una statistica di tasso-di-cambiamento e usarla come segnale di gating/attenzione — memoria del "quanto qualcosa è vivo" separata dalla memoria del "cosa è".
- **La summarization threshold (collassa N simili in 1 astrazione)** come meccanismo anti-ridondanza per una memoria di lungo periodo a capacità finita.
