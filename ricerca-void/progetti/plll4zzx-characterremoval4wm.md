# plll4zzx/CharacterRemoval4WM

<https://github.com/plll4zzx/CharacterRemoval4WM>

Stelle: ~9 · Linguaggio: Python · Push set 2025 · Licenza: MIT · NDSS 2026

## Cosa fa

È l'artifact del paper "Character-Level Perturbations Disrupt LLM Watermarks" (NDSS 2026): un attacco a basso costo che **rimuove i watermark LLM perturbando il testo a livello di carattere** invece che di token. Dimostra due cose: (1) a parità di tasso di editing, le perturbazioni carattere-per-carattere abbattono il watermark molto più efficacemente di quelle token-per-token (più alto Watermark score Dropping Rate e Attack Success Rate); (2) un'ottimizzazione con **algoritmo genetico** guidata da un detector di riferimento migliora ulteriormente l'attacco. Include attacchi random (baseline), Best-of-N, una variante "Sand", e il GA. Testa contro molti schemi di MarkLLM (KGW, SIR, XSIR, SWEET, Unbiased, DIP, EXP, SynthID, TS, UPV…) usando C4 come sorgente di prompt e OPT-1.3B come target.

## Come è fatto

L'intuizione centrale è un **mismatch di granularità**: i watermark LLM operano sui *token* (partizionano il vocabolario, contano token green), ma il testo può essere perturbato sotto quel livello. Una piccola alterazione di carattere (swap, inserimento, omoglifo) fa **ri-tokenizzare** la parola in modo diverso, così i token che il detector si aspettava di contare semplicemente non esistono più — con un budget di editing minuscolo distruggi la statistica su cui il detector si regge. La parte guidata addestra dei **reference detector** (BERT fine-tunato) sui dati watermarkati con data augmentation (perturbazioni casuali ripetute), poi usa quel detector come fitness per un algoritmo genetico che cerca la perturbazione minima che massimizza il calo del watermark score. Per gli attacchi a livello di frase usano DIPPER come parafrasatore. Tutto è organizzato attorno a una copia di MarkLLM inclusa nel repo, con script `collect_wm_text.py`, `test_rand_sh.py`, `train_ref_detector.py`, `test_ga_sh.py`.

## Cosa possiamo notare di utile per noi

Questo è il repo che ti insegna la cosa più sottile e trasferibile di tutto il cluster: **il livello a cui guardi determina cosa puoi nascondere e cosa puoi rompere.**

- **Mismatch di granularità = principio generale per la tua arena.** Il watermark vive al livello-token; l'attacco vive al livello-carattere, *sotto* di esso, e per questo è quasi gratis. Traslato: un occultamento definito a una certa scala dello stato interno è vulnerabile a perturbazioni a una scala più fine, e simmetricamente una firma può nascondersi in una scala che l'oscilloscopio non campiona. Ti dà un asse nuovo — la *risoluzione di osservazione* — come variabile di progetto sia per occultare sia per rilevare nel vuoto. Il tuo oscilloscopio deve dichiarare a quale grana guarda, perché sotto quella grana la firma è invisibile e distruttibile.
- **GA guidato da un detector = novelty-gating al contrario, e ottimizzazione senza gradiente.** Usano un detector appreso come *fitness landscape* e ci fanno evolvere sopra perturbazioni. È lo stesso stampo della tua memoria novelty-gated: un segnale (il detector) misura "quanto è ancora presente la struttura", e una ricerca evolutiva spinge verso il minimo. Per un'arena di particelle senza gradienti, il GA-guidato-da-sonda è un metodo di ottimizzazione già pronto: la sonda-oscilloscopio diventa la funzione di fitness che guida l'evoluzione degli agenti.
- **Fragilità del canale sotto rumore fine = legge di robustezza da simulare.** Il risultato "carattere > token a parità di budget" quantifica quanto poco serve per cancellare una firma se colpisci la scala giusta. Nel vuoto, questo dice che la sopravvivenza di una traccia dipende non dalla *quantità* di rumore ma dal suo *allineamento con la scala della firma* — un rumore fine e mirato batte un rumore grezzo abbondante.
- **Reference detector con data augmentation = come costruire un oscilloscopio robusto.** Addestrano il detector su versioni perturbate del segnale così che legga la firma anche sotto rumore. È la ricetta per rendere le tue sonde interne robuste: augmenta gli stati con perturbazioni durante il training della sonda, così l'oscilloscopio non si fa ingannare da piccole variazioni.
- **Dove diverge:** è distruttivo (rimozione), NLP, con detector che serve solo da guida offline. Tu vuoi soprattutto il *concetto di scala* e il *GA-guidato-da-sonda* come motore di ricerca, non l'obiettivo di cancellare marchi.

## Da rubare

1. **Asse "risoluzione di osservazione" nell'arena:** rendi esplicita la grana a cui occulti e la grana a cui l'oscilloscopio campiona; esplora sperimentalmente il gap — firme sotto la grana di osservazione sono invisibili e cancellabili a costo minimo (legge quantitativa da misurare).
2. **GA guidato dall'oscilloscopio come motore evolutivo gradient-free:** usa la lettura della sonda interna come fitness e fai evolvere le particelle verso occultamento (minimizza rilevabilità) o verso salienza (massimizza) — un loop di ottimizzazione senza gradienti perfetto per il simulatore.
3. **Sonde robuste via augmentation:** addestra ogni oscilloscopio su stati perturbati (rumore fine, ri-scaling) così che la lettura resti stabile — evita che la sonda scambi micro-rumore del vuoto per assenza/presenza di struttura.
