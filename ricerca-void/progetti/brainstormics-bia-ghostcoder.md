# BIA-Ghostcoder — BrainStOrmics/BIA-Ghostcoder

<https://github.com/BrainStOrmics/BIA-Ghostcoder>

**~2 stelle · Jupyter Notebook / Python · ultimo push set 2025 · licenza MIT** · "Bioinformatics workflow coding agent."

## Cosa fa

Agente di coding dominio-specifico per la bioinformatica: prende un task in linguaggio naturale ("analizza questi dati scRNA-seq") più i file di dati grezzi, e produce ed esegue autonomamente uno script di analisi completo. Non è un chatbot generico: è specializzato su workflow bio (l'unica guida presente è `scRNAseq.md`) e ha un suo database di "reference codeblocks" (`RefCodeDB.csv`) da cui recupera snippet validati per il dominio. Il ciclo è: percepisce i dati, pianifica, recupera codice di riferimento, scrive, esegue in Docker, valuta il risultato, e se fallisce riprova (fino a `max_retry`). Il nome "Ghost" è casuale/tematico, non ha nulla a che vedere con occultamento — è "il coder fantasma che lavora al posto tuo".

## Come è fatto

È un grafo **LangGraph** (`create_ghostcoder_agent`) con uno `State` tipizzato che scorre tra nodi specializzati. Il flusso: `File manager` (ispeziona i file di dati e costruisce `env_profiles`) → `Task parser` (estrae istruzione + `criteria` di successo) → router `use_RAG` → `Retriever` (interroga `RefCodeDB`, un vector DB di codeblock bio) → `Coder` → `Evaluator` → router condizionale che rimanda al Coder se `eval_decision` è falso → `Output parser`. Due dettagli notevoli: (1) un nodo **`data_perception_coder`** separato che genera prima un codeblock il cui solo scopo è *ispezionare* la forma dei dati (shape, colonne, tipi) prima di scrivere l'analisi vera — cioè "percepisce" il dato eseguendo codice, non assumendo; (2) l'**Evaluator** confronta l'output di esecuzione contro i `criteria` estratti dal task e ritorna `improvements` testuali che rientrano nel prompt del Coder al giro dopo. Ogni nodo ha il suo prompt versionato in `prompts/` (planer, coder, evaluator, retriever, crawler...), con varianti `.critisim.md` per l'auto-critica. Esecuzione sandboxata via Docker (`BIA_dockers.json`), web-search opzionale via Tavily/webcrawler.

## Cosa possiamo notare di utile per noi

Qui l'aggancio non è tematico (niente vuoto, niente occultamento — il "ghost" è marketing) ma **architetturale**, sul come si costruisce un anello percezione→azione→valutazione chiuso e onesto:

- **Data-perception come atto motorio, non come assunzione.** Il pattern del nodo `data_perception_coder` è esattamente il contrario dell'allucinare lo stato: l'agente scrive ed esegue codice il cui unico fine è *guardare* il dato, poi condiziona il piano sull'osservazione reale. È il gemello procedurale dell'oscilloscopio sugli stati interni: prima di agire, sonda e leggi. Per l'arena del vuoto è trasferibile come principio — un modulo che, prima di generare la prossima mossa, produce una lettura misurata dello stato delle particelle e ci condiziona sopra, invece di operare su una rappresentazione presunta.
- **Evaluator con `criteria` estratti + `improvements` in retroazione.** Il loop non è "riprova a caso": estrae criteri di successo dal task, li verifica sull'output di esecuzione, e ri-inietta una critica testuale specifica. È un gate di qualità con memoria di cosa è andato storto — parente stretto del novelty-gate, ma orientato alla *correttezza* invece che alla novità. Il meccanismo (giudice → verdetto → nota testuale che rientra nel contesto) è lo stesso scheletro che useresti per un gate "questa configurazione è abbastanza nuova/interessante da tenere?".
- **RAG come memoria di dominio curata, non come recupero generico.** `RefCodeDB` è una memoria di codeblock *validati a mano* per un dominio ristretto, con un router che decide se usarla. Diverge dal tuo interesse (è codice bio, non tracce di stati emergenti) ma il principio è utile: una memoria piccola e curata, con un router esplicito "serve richiamarla o no?", batte una memoria enorme e indiscriminata.

Dove diverge da te: è tutto goal-directed e verificabile (c'è un "giusto"). Il tuo lavoro sull'emergenza non ha criteri di successo esterni — quindi l'Evaluator qui va reinterpretato come *misuratore di interesse/novità*, non di correttezza.

## Da rubare

- **Il nodo "percepisci eseguendo".** Prima di ogni step generativo, un mini-step che produce ed esegue una sonda per leggere lo stato reale (shape/statistiche) e condiziona il resto su quella lettura — antidoto all'allucinazione dello stato interno.
- **Il ciclo Evaluator→improvements→Coder** come template di gate testuale con retroazione specifica: giudice che estrae criteri, verifica, e restituisce una nota mirata che rientra nel prompt. Riadattabile a gate "novelty/interessante" per l'arena.
- **Prompt versionati per-nodo con variante `.critisim.md`** dedicata all'auto-critica: separare il prompt "fai" dal prompt "critica ciò che hai fatto" è un pattern pulito per costruire l'auto-osservazione senza confonderla con l'azione.
