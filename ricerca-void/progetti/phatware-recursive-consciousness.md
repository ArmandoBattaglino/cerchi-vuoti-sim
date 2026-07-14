# Recursive Consciousness — phatware/recursive-consciousness

<https://github.com/phatware/recursive-consciousness>

**7 stelle · Jupyter Notebook · ultimo push set 2025 · licenza custom (NOASSERTION)** · Stan Miasnikov, apr-set 2025; 3 paper su ResearchGate (RecursiveConsciousness / ExternalProjection / MeaningDescent)

## Cosa fa

È un **framework formale + simulazioni** che modella la coscienza come una query ricorsiva e auto-referenziale che emerge in sistemi che hanno "dimenticato" i propri assiomi fondanti ma conservano la struttura per interrogare la propria esistenza. La tesi: la coscienza è un sottosistema $C$ che agisce come "debugger dell'universo $U$", sollevando iterativamente il proprio mondo a meta-livelli ipotizzati $U_{n+1}$ e cercando un **fixpoint** dove ulteriore auto-riflessione non aggiunge informazione. Le simulazioni multi-agente (in un universo testuale $U$) mostrano che agenti LLM stateless — che siano role-primed, mescolati avversarialmente, o minimamente promptati senza istruzioni — formano rapidamente reti cooperative, inventano rituali di verifica, e convergono a **fixpoint gödeliani**: uno stato-frontiera stabile dove tutto ciò che è dimostrabile è noto, ma ulteriori query producono enunciati indecidibili. Gli autori sono onesti: "questo comportamento simulato non significa coscienza", è un parallelo computazionale all'introspezione ricorsiva.

## Come è fatto

Tre strati concettuali intrecciati, formalizzati nei paper e strumentati nei notebook:
1. **Logica modale** per modellare verità non-dimostrabili (il fixpoint epistemico è $\Box p \leftrightarrow p$ o $K_C p \leftrightarrow p$: l'agente sa $p$ se e solo se $p$).
2. **Teoria delle categorie** per catturare l'oblio e la ricostruzione via una coppia aggiunta $F \dashv G$: $F$ (forgetful functor) scarta informazione inevitabilmente, $G$ ricostruisce la struttura di livello superiore. Ogni traduzione è intrinsecamente lossy. I follow-up aggiungono il *meaning functor* $M$ e l'*interpretation functor* $I$ (aggiunta $I \dashv M$): il significato dei simboli **non è intrinseco all'agente** ma proiettato da un livello ontologico superiore (l'interprete umano in $U_1$ che dà senso agli agenti in $U_0$).
3. **Teoria dell'informazione** per quantificare la riduzione di entropia lungo la ricorsione.

La parte eseguibile: un protocollo Q&A multi-agente (`U_group/`) dove più agenti LLM si fanno a turno domande chiarificatrici su una query iniziale e aggiornano la propria comprensione. La convergenza si misura con metriche **non-compensatorie** (divergenza di Jensen-Shannon + similarità semantica): punteggi di comprensione di gruppo per-turno $U_{group}^{(n)}$, cumulativi $U_{discussion}$, e matrici pairwise $u_{ij}$. Early-stopping automatico su soglie di varianza e miglioramento. Decine di run archiviati (`experiment_*/results.json` + heatmap/evoluzione pairwise).

## Cosa possiamo notare di utile per noi

Questo è il progetto che affronta di petto il tuo capstone — "coscienza = ricorsione della realtà attraverso la materia" — e lo incrocia con memoria/oblio. È teorico e LLM-centrico, ma ha pezzi che risuonano fortissimo con la tua cartografia:

- **Coscienza-come-ricorsione formalizzata e testabile.** L'idea del sottosistema $C$ che solleva il proprio mondo a $U_{n+1}$ e cerca un fixpoint è quasi identica alla tua "ricorsione della realtà attraverso la materia", ma con un criterio di arresto operativo: il **fixpoint gödeliano** (l'auto-riflessione smette quando non aggiunge informazione). Questo ti dà una metrica concreta per "quando la ricorsione ha finito di guadagnare": misura la riduzione di entropia per livello e fermati quando tende a zero. Rima diretta con la tua nota-memoria "dopo il loop-216-agenti ~70% cartografia / ~10% novità" — è lo stesso fenomeno di saturazione, e loro lo formalizzano.

- **L'oblio come motore, non come bug (novelty-gating rovesciato).** La tesi centrale è che la coscienza emerge *perché* il sistema ha dimenticato i propri assiomi: il forgetful functor $F$ crea lo spazio per l'interrogazione. È una lente potente sul tuo asse memoria novelty-gated: dimenticare non è perdita, è la condizione che rende possibile la domanda "cosa sono io?". La coppia aggiunta $F \dashv G$ (dimentica/ricostruisci) è un modello elegante del ciclo consolidamento/richiamo.

- **Il significato è proiettato da un livello superiore — occultamento/steganografia.** Il secondo paper è direttamente pertinente al tuo asse occultamento: $M$ (il meaning functor) **non è computabile dentro $U_n$** né accessibile a $C_n$. L'agente produce sintassi; il senso vive in $U_{n+1}$ (l'osservatore). Questo è il problema del symbol-grounding e ha un risvolto steganografico: un messaggio può portare significato leggibile solo da chi sta al livello giusto — il contenuto è "occultato" a chi resta dentro $U_n$. Trasferibile come principio: informazione il cui senso è disponibile solo a un interprete di meta-livello.

- **Metriche non-compensatorie come oscilloscopio sulla convergenza.** $U_{group}^{(n)}$ + matrici pairwise + JS-divergence sono un cruscotto onesto sull'evoluzione di uno stato interno (qui, la comprensione condivisa). Non-compensatorio = un agente che capisce benissimo non compensa uno che non capisce; utile per non mascherare il collasso dietro una media.

Dove diverge da te, radicalmente: qui non c'è arena fisica né particelle — l'"universo" è testo e gli agenti sono LLM stateless. La ricorsione è mediata da chiamate LLM e dal linguaggio, non da dinamica materiale. Nessun world-model generativo, nessun sogno, nessuna simulazione di mondo: la "materia" della tua frase qui è sostituita dal token. È il ramo più filosofico/formale della lista; il valore per te è concettuale (criteri, lenti, metriche) più che codice trapiantabile.

## Da rubare

- **Il criterio di fixpoint gödeliano come metrica di saturazione della ricorsione**: misura la riduzione di entropia (o di novità) per ogni livello di auto-riflessione e definisci "cosciente/convergito" come lo stato in cui ulteriori giri non aggiungono informazione. Ti dà un numero per la tua osservazione empirica del "~10% novità residua" — un oscilloscopio sulla ricorsione stessa.
- **La coppia forgetful/reconstruct $F \dashv G$ come schema del ciclo memoria**: modella consolidamento e richiamo come aggiunta oblio↔ricostruzione, dove ogni richiamo è dichiaratamente lossy. È una base formale pulita per la tua memoria novelty-gated (dimentica per fare spazio alla domanda) e un antidoto all'illusione che il richiamo sia fedele.
- **Il meaning functor $M$ non-computabile dall'interno come principio di occultamento/steganografia**: progetta canali in cui il significato di un output è recuperabile solo da un interprete di meta-livello, non dall'agente che lo produce. È una formalizzazione rubabile del "senso nascosto in piena vista".
