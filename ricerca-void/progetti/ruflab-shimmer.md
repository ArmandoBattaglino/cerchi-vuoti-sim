# Shimmer — Global Latent Workspace (ruflab/shimmer)

<https://github.com/ruflab/shimmer>

**8 stelle · Python (PyTorch Lightning) · ultimo push apr 2026 · licenza MIT** · lab di Rufin VanRullen (CerCo/ANITI, Toulouse); "GLoW, but very light"

## Cosa fa

È la libreria barebones per costruire un **Global Latent Workspace (GLW)**: uno spazio latente amodale e condiviso, *appreso*, che fa da hub tra più moduli specializzati e congelati (visione, linguaggio, ecc.). L'idea teorica (VanRullen & Kanai) è che la coscienza corrisponda a un workspace globale dove rappresentazioni di moduli diversi vengono tradotte in un formato comune, allineate e ri-diffuse indietro. Shimmer fornisce l'ossatura minimale in PyTorch Lightning per definire i moduli di dominio, il modulo-workspace che codifica/decodifica/fonde le rappresentazioni, e le loss (translation, contrastive, cycle-consistency) che addestrano lo spazio condiviso senza toccare i moduli sottostanti. È deliberatamente leggero: non un modello pronto, ma i mattoni tipizzati per assemblarne uno sui tuoi dati.

## Come è fatto

Quattro classi centrali in `shimmer/modules/`:
- **`DomainModule`** (`domain.py`): incapsula un modulo pre-addestrato e congelato, con encoder/decoder che mappano i dati di dominio in un vettore latente e viceversa. Definisce anche le loss specifiche del dominio.
- **`GWModule`** (`gw_module.py`): ha accesso ai domain module e definisce come *encode* un dominio nel workspace, *decode* dal workspace verso un dominio, e *merge* più domini in un'unica rappresentazione GW.
- **`GlobalWorkspaceBase`** (`global_workspace.py`): assembla tutto in un LightningModule addestrabile; c'è anche un `attention_module.py` e un `selection.py` che gestiscono come i domini vengono selezionati/pesati nella fusione.
- **`GWLosses`** (`losses.py` + `contrastive_loss.py`): definisce le loss che addestrano il workspace — traduzione (dominio A → GW → dominio B), cycle-consistency (A → GW → A ricostruisce), e contrastive (allinea coppie appaiate nello spazio latente).

L'addestramento avviene in due tempi (vedi `examples/main_example`): prima si addestrano i `DomainModule` (es. VAE per dominio), poi si congelano e si addestra solo il GW sopra di essi. Il risultato è uno spazio latente relazionale in cui puoi passare da una modalità all'altra e "broadcastare" una rappresentazione a tutti i moduli.

## Cosa possiamo notare di utile per noi

Shimmer è la **teoria relazionale della mente scritta in codice pulito**, ed è il complemento "appreso/neurale" rispetto ai global-workspace deterministici (ZugaMind). Per il tuo lavoro tocca due assi: coscienza-come-workspace e world-model-come-linguaggio-comune:

- **Lo spazio latente amodale come "vuoto" dove le modalità si incontrano.** Il GLW è concettualmente un'arena centrale in cui rappresentazioni eterogenee vengono proiettate e ri-diffuse. Se la tua arena del vuoto è lo spazio fisico dove le particelle interagiscono, il GLW è lo spazio *rappresentazionale* dove i moduli interni interagiscono. Trasferibile: potresti avere un workspace latente condiviso tra il modulo-percezione, il modulo-memoria e il modulo-world-model, con le stesse loss (translation/cycle) a tenerli allineati.

- **Cycle-consistency come test di coerenza interna (coscienza=ricorsione, versione misurabile).** La loss di cycle (A → GW → A) è un anello ricorsivo: il sistema deve poter *ricostruire* la propria rappresentazione dopo un giro attraverso il workspace. È un modo concreto e differenziabile di misurare "quanto la rappresentazione interna è auto-coerente sotto ri-elaborazione" — molto più operativo dello slogan. Un residuo di cycle basso = fixpoint semantico raggiunto (rima con il fixpoint gödeliano di phatware, ma qui appreso e continuo).

- **Moduli congelati + workspace addestrato = economia di plasticità.** Il pattern "congela gli esperti, addestra solo il ponte" è direttamente rubabile: la maggior parte della tua rete resta stabile (identità), solo lo strato di integrazione è plastico. È un altro modo di fare novelty-gating strutturale — la plasticità è confinata al workspace.

Dove diverge da te, forte: Shimmer è puro deep learning addestrato con gradient descent su dati appaiati — nessuna arena/particelle, nessuna dinamica temporale, nessun sogno, nessun oscilloscopio (è un modello, non un sistema ispezionabile in runtime). Il "workspace" è un tensore latente, non un campo di attivazione che evolve nel tempo. È teoria della coscienza *architetturale* (dove sta l'integrazione), non *dinamica* (come emerge tick per tick). E richiede dati appaiati multi-dominio, che tu potresti non avere.

## Da rubare

- **La cycle-consistency loss come oscilloscopio di auto-coerenza**: misura in continuo `A → workspace → A'` e leggi il residuo come indicatore di quanto il tuo stato interno resta se stesso dopo un giro di ri-elaborazione. È una metrica di "ricorsione stabile" differenziabile, montabile come traccia da oscilloscopio sugli stati interni.
- **Il pattern moduli-congelati + ponte-plastico**: confina la plasticità a un unico spazio latente condiviso e tieni gli "esperti" (percezione, memoria) congelati. Riduce il costo del learning e dà stabilità di identità — un novelty-gating a livello architetturale.
- **Le tre loss di traduzione/contrastive/cycle** come ricetta per costruire un vero "linguaggio comune" tra i tuoi sottosistemi eterogenei, invece di concatenarli ad hoc: allinea coppie (contrastive), garantisci reversibilità (cycle), abilita il passaggio cross-modulo (translation).
