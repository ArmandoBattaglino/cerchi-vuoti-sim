# AriGraph — [AIRI-Institute/AriGraph](https://github.com/AIRI-Institute/AriGraph)

171 stelle · Python (env in Inform 7) · fermo (push set 2024) · licenza MIT

## Cosa fa
Memoria esterna per agenti LLM costruita come knowledge graph che l'agente edifica dal basso mentre esplora un ambiente testuale (giochi TextWorld: Treasure Hunt, Cleaning, Cooking). Il grafo integra memoria semantica (fatti come triple) e memoria episodica (vertici/archi che registrano eventi), e il recupero graph-based alimenta un modulo di decisione/pianificazione. L'agente "Ariadne" cosi costruito batte tutte le baseline (Full History, Summary, RAG) e regge il confronto con giocatori umani. Testato anche su QA multi-hop (MuSiQue, HotpotQA) senza modifiche d'architettura.

## Come e fatto
Il cuore e `TripletGraph` (in `parent_graph.py`) con grafi che lo ereditano. Ogni pipeline (`pipeline*.py`) accoppia lo stesso modulo decisionale a implementazioni di memoria diverse — la variabile e solo la memoria. L'agente estrae triple dal testo osservato, le inserisce nel grafo, aggiunge vertici episodici per gli eventi, e al momento di agire fa retrieval graph-based (semantico + episodico) per costruire il contesto del prompt. La memoria non e un log: e *letteralmente un modello del mondo* che l'agente naviga.

## Perche riguarda te
E la mappatura piu diretta del tema "memoria = modello del mondo costruito e navigato". Rispetto alla tua idea di memoria novelty-gated, AriGraph mostra il lato struttura (cosa memorizzare e come collegarlo) ma NON il lato gating: qui si accumula tutto, senza una soglia di novita che decide cosa merita di entrare. Il contrasto e utile — la loro vittoria contro "Full History" e "Summary" dimostra che *la struttura del ricordo conta piu della quantita*, che e proprio l'argomento a favore di una memoria selettiva. Diverge molto dall'arena vuoto/particelle: qui non c'e fisica ne emergenza, e tutto simbolico e LLM-mediato. Utile come architettura di memoria, non come sostrato.

## Da rubare
1. La separazione semantico/episodico nello stesso grafo: nodi-fatto stabili + nodi-evento datati, con retrieval che li combina — un modello concreto per la tua memoria a due tempi (cosa e vero / quando e successo).
2. Il protocollo di ablation "stesso decisore, memoria diversa": per misurare onestamente se il tuo gating di novita aggiunge valore, tieni fisso tutto il resto e scambia solo il modulo memoria, come fanno loro contro RAG/Summary.
