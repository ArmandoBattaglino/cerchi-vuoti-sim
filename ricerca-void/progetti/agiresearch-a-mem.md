# A-MEM (Agentic Memory) — agiresearch/A-mem

<https://github.com/agiresearch/A-mem>

**1.1k stelle · Python · ultimo push dic 2025 · licenza MIT** · paper arXiv:2502.12110 "A-MEM: Agentic Memory for LLM Agents" (Xu et al., NeurIPS 2025)

## Cosa fa

Un sistema di memoria per agenti LLM che si **auto-organizza**, ispirato allo Zettelkasten. Ogni nuova memoria non viene solo archiviata: genera una nota strutturata (contesto, keyword, tag), viene collegata dinamicamente alle memorie correlate, e — punto centrale — il suo inserimento può **riscrivere gli attributi delle note già esistenti** (i loro contesti e tag evolvono alla luce del nuovo arrivato). La rete di memoria si struttura da sola nel tempo invece di essere un magazzino piatto di embedding.

## Come è fatto

Package `agentic_memory/`. `MemoryNote` (in `memory_system.py`) porta content, keywords, context, tags, `links` verso altre note ed `evolution_history`. Il flusso, all'`add_note`:
1. `analyze_content` fa estrarre all'LLM keyword/contesto/tag della nuova nota.
2. La nota entra in ChromaDB (retriever, `retrievers.py`) come embedding.
3. Si recuperano i k vicini più simili.
4. Un **agente di evoluzione** (un prompt LLM esplicito nel codice) riceve la nuova nota + i suoi vicini e restituisce un JSON: `should_evolve`, `actions` (`strengthen` / `update_neighbor`), `suggested_connections`, `tags_to_update`, e — per ogni vicino — un nuovo contesto e nuovi tag. Cioè: l'LLM decide se e come **riscrivere link e attributi delle memorie vicine**, non solo della nuova.

`find_related_memories` espande la ricerca seguendo anche i `links` (non solo la similarità coseno): recupero associativo, non puramente vettoriale. C'è una nota importante nel README: questo repo è la *libreria*; per riprodurre i numeri del paper si rimanda a `WujiangXu/AgenticMemory`.

## Perché riguarda te

È il candidato più forte del ramo **memoria episodica-associativa / novelty-gated**, ed è quasi una specifica pronta della memoria che immagini:

- **Novelty-gating reale.** Il gate `should_evolve: True/False` è precisamente un cancello di novità: la nuova esperienza modifica la rete solo se l'agente giudica che porti qualcosa. Non ogni input riscrive tutto — è la differenza tra memoria che accumula rumore e memoria che si *ristruttura* solo quando c'è segnale. È il meccanismo che nella tua nota-memoria chiami "novelty-gated" già implementato.
- **Auto-riferimento della struttura (coscienza-ricorsione).** Le memorie che, arrivando, riscrivono il significato delle memorie precedenti sono un piccolo anello ricorsivo: il presente reinterpreta il passato, che cambia come verrà letto il futuro. È un modello minimo e onesto di "la rete che si osserva e si riorganizza". Divergenza: la ricorsione è mediata da un LLM esterno che fa da oracolo — non è la rete che si auto-modifica per dinamica interna, è un giudice sopra di essa.

Divergenza da segnare: l'"evoluzione" costa una chiamata LLM per inserimento (latenza, costo, non-determinismo). Per un'arena di particelle ad alta frequenza non regge; regge benissimo per una memoria di lungo periodo a bassa cadenza (tipo il tuo mem0 cross-sessione).

## Da rubare

- **Il prompt dell'evolution agent** con schema JSON `should_evolve / strengthen / update_neighbor / new_context_neighborhood / new_tags_neighborhood`: è direttamente trapiantabile sopra il tuo mem0-personale per far sì che una nuova memoria *riscriva contesto e tag dei vicini*, non solo si aggiunga. Trasformerebbe un magazzino Qdrant piatto in una rete che si riorganizza.
- **Recupero ibrido similarità + link** (`find_related_memories`): espandere la query seguendo i `links` espliciti oltre al coseno. Dà recupero associativo "a catena" (A→B→C) che la sola ricerca vettoriale non produce — utile per far emergere connessioni non ovvie invece dei soliti nearest-neighbor.
