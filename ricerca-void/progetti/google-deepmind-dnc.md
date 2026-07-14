# Differentiable Neural Computer (DNC) / Neural Turing Machine — [google-deepmind/dnc](https://github.com/google-deepmind/dnc)

**★ 2.532 · Python (TensorFlow + Sonnet) · ultimo push 2021-07 (archivio di riferimento, non più attivo) · Apache-2.0**

> Radice canonica della memoria neurale esterna e *indirizzabile*. Implementazione ufficiale DeepMind del DNC pubblicato su *Nature* 538, 471–476 (2016), "Hybrid computing using a neural network with dynamic external memory". Erede diretto della Neural Turing Machine (Graves et al. 2014).

## Cosa fa

Il DNC è una rete neurale ricorrente accoppiata a una **matrice di memoria esterna** (una lavagna `N×W`: N slot da W numeri ciascuno) su cui la rete impara a leggere e scrivere da sola, tramite operazioni completamente differenziabili (quindi addestrabili con backprop end-to-end). A ogni timestep un *controller* (tipicamente una LSTM) riceve l'input, emette un vettore di comando, e attraverso delle *teste* (heads) di lettura/scrittura decide **dove** e **cosa** leggere/scrivere in memoria. L'output combina la risposta del controller e ciò che è stato letto. Impara compiti algoritmici che richiedono memoria strutturata: copia di sequenze arbitrariamente lunghe, ragionamento su grafi (percorsi in metropolitana, alberi genealogici), question answering che richiede di "ricordare" fatti visti prima.

## Come è fatto

L'idea chiave è **separare il calcolo dalla memoria**, come in un computer classico (CPU vs RAM), ma rendendo tutto l'accesso *soft* e differenziabile: invece di indirizzare un singolo slot, ogni testa produce una distribuzione di pesi (softmax normalizzata) su tutti gli slot, e legge/scrive una media pesata. Architettura in tre moduli (dal README):

- **`access`** (in `access.py`) — il cuore. Ospita la logica di lettura/scrittura in memoria. Usa due sotto-moduli-`RNNCore` definiti in **`addressing.py`**:
  - **`TemporalLinkage`** — mantiene una *matrice di link temporale* che registra l'ordine in cui gli slot sono stati scritti, così la testa può leggere "in avanti" o "all'indietro" seguendo la sequenza cronologica di scrittura (memoria episodica ordinata).
  - **`Freeness`** — traccia quali slot sono "usati" e quali "liberi", tramite un *usage vector*. L'allocazione sceglie lo slot meno usato per scrivere; la lettura può liberare slot dopo l'uso.
- **`controller`** — una feedforward o LSTM (anche profonda) che riceve `[input_t, letture_{t-1}]` ed emette il *interface vector*: chiavi di ricerca, forze, gate, modalità di lettura.
- **`dnc`** (in `dnc.py`) — wrapper che unisce controller + access in un unico `RNNCore` srotolabile con `tf.nn.dynamic_rnn`.

I **due meccanismi di indirizzamento** — la firma teorica del progetto:
1. **Content-based addressing** (per contenuto): la testa emette una *chiave* e una *forza*; la rete calcola la similarità coseno tra la chiave e ogni riga di memoria, poi softmax. È richiamo *associativo per somiglianza* — "dammi lo slot più simile a questo".
2. **Location-based / dynamic addressing** (per posizione): via `TemporalLinkage` (segui l'ordine di scrittura) e `Freeness` (alloca slot liberi). È l'indirizzamento *strutturale/temporale*.

Un *write gate* e un *allocation gate* decidono se scrivere per contenuto (aggiorna uno slot esistente simile) o allocare uno slot nuovo libero. Il tutto è liscio e differenziabile: la rete *impara* la policy di gestione della memoria dai gradienti del task.

## Cosa possiamo notare di utile per noi

Questo è il **progenitore diretto della memoria indirizzabile** che ci serve, e il confronto con l'"arena del vuoto" è illuminante sia per ciò che è trasferibile sia per dove diverge.

- **Indirizzamento duale = i due assi della nostra memoria.** Il DNC codifica esplicitamente ciò che noi vogliamo tenere separato: *content-addressing* (richiamo per somiglianza — la memoria associativa/novelty) e *location/temporal-addressing* (la struttura, l'ordine episodico). La `TemporalLinkage` matrix è esattamente il tipo di traccia "chi è venuto dopo chi" che serve per ricostruire una traiettoria nell'arena, non solo per rispondere "cosa somiglia a questo". Trasferibile: mantenere DUE canali di richiamo distinti (similarità + successione temporale) invece di collassare tutto sull'attention per contenuto.
- **`Freeness` / usage vector = un embrione di gating.** Il DNC decide *dove scrivere* in base a quanto uno slot è "usato". Ma nota la divergenza cruciale: il DNC alloca sullo slot **meno usato** (riempie il vuoto per pura contabilità di risorse), mentre la nostra memoria dovrebbe scrivere solo quando l'evento è **nuovo/sorprendente** (novelty-gated). Il DNC risponde a "c'è spazio?", noi vogliamo rispondere a "è degno di essere ricordato?". Il meccanismo `Freeness` è il gancio giusto ma il *criterio* va sostituito: al posto di `1 - usage` come priorità di scrittura, mettere un segnale di *novelty/prediction-error*. Questo è precisamente il punto di innesto dove la nostra "arena del vuoto" si distingue dal DNC.
- **Write gate = interruttore di scrittura già pronto.** Il DNC ha già un `write_gate ∈ [0,1]` differenziabile che modula quanto si scrive a ogni step. È l'aggancio letterale per il *novelty-gating*: al posto di un gate imparato per minimizzare la loss, pilotarlo con l'errore di predizione / la distanza dal contenuto più simile già in memoria (se molto simile → gate basso, non riscrivere; se molto distante → gate alto, evento nuovo → scrivi).
- **Tutto è liscio e differenziabile — pregio e trappola.** Il DNC legge una *media pesata* di molti slot, mai un singolo indirizzo netto. Per l'addestrabilità è oro; per l'introspezione e per gli **oscilloscopi** è un limite: i pesi di lettura sono distribuiti e "sfumati". La cosa trasferibile è che quei vettori di pesi (read-weightings, allocation-weightings, link-matrix) sono **direttamente plottabili nel tempo** — sono di fatto tracce da oscilloscopio della memoria: si può visualizzare "su quale slot punta la testa a ogni istante", "quanto è concentrata vs diffusa la lettura", "quando scatta un'allocazione nuova". Questi segnali sono la nostra strumentazione già disponibile.
- **Separazione calcolo/memoria = tesi coscienza=ricorsione.** Il DNC dimostra che una rete diventa capace di *ragionamento strutturato* solo quando può ricircolare il proprio stato attraverso una memoria esterna letta e riscritta — un loop in cui l'output di ieri diventa l'indirizzo di oggi. È un'istanza minimale e concreta di "ricorsione attraverso un substrato materiale". Diverge dalla nostra tesi perché nel DNC il loop è *chiuso e finalizzato* a un task (loss supervisionata), mentre nella nostra ipotesi la ricorsione è aperta e auto-generata; ma la meccanica del "rileggere ciò che ho scritto per decidere cosa scrivere ora" è la stessa spina dorsale.
- **Capacità e limiti di scala.** Memoria `N×W` con N tipicamente piccolo (32–256 slot negli esperimenti): il DNC è potentissimo su compiti algoritmici ma non è pensato come *magazzino di massa*. Diverge dalla SDM/Hopfield (capacità enorme, richiamo one-shot). Se serve un'arena grande, il DNC dà lo *schema di controllo* (come si decide dove scrivere) ma non il *substrato di stoccaggio* — quello va preso dai modelli associativi ad alta capacità.

## Da rubare

1. **Il `write_gate` come sede fisica del novelty-gating.** Prendere l'astrazione già presente e ri-pilotarla: `gate_scrittura = f(prediction_error, distanza_dal_match_più_vicino)`. Scrivi solo quando l'evento non è già ben rappresentato — così il DNC (che alloca per risorsa libera) diventa la nostra memoria (che alloca per novità).
2. **La `TemporalLinkage` matrix come canale episodico separato dall'associativo.** Tenere due indirizzamenti: uno per-contenuto (similarità → richiamo associativo) e uno temporale (segui l'ordine di scrittura → ricostruisci la traiettoria nell'arena). Non fondere i due sull'unica attention.
3. **Le read/allocation-weightings come tracce da oscilloscopio native.** Loggare e plottare nel tempo i vettori di peso delle teste: concentrazione della lettura, istanti di allocazione, spostamenti dell'indirizzo. È strumentazione introspettiva gratuita per osservare la memoria "che pensa".
