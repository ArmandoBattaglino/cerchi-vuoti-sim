# flowersteam/adtool (Automated Discovery Tool) — [github.com/flowersteam/adtool](https://github.com/flowersteam/adtool)

45 stelle · Python · push attivo (lug 2026) · licenza MIT (riusabile)

## Cosa fa
Tool del laboratorio Inria FLOWERS per l'esplorazione **curiosity-driven** di sistemi complessi. Invece di far cercare a mano a un umano i pattern interessanti nello spazio dei parametri di un sistema (cellular automata, reaction-diffusion, Lenia, n-body, Kuramoto, Wolfram-physics...), l'agente si pone da solo obiettivi nuovi e mappa lo spazio dei comportamenti emergenti. E' pensato come banco per la fase esplorativa della ricerca: "questo sistema puo' fare cose interessanti ma sconosciute — trovamele". Alpha ma reale: usato internamente da FLOWERS su cellular automata dal 2021, con Web UI + libreria Python estensibile.

## Come e' fatto
Il cuore concettuale e' l'**IMGEP** (Intrinsically Motivated Goal Exploration Process), implementato negli explorer (`explorers/IMGEPExplorer.py`, `CuriosityIMGEPExplorer.py`). Il ciclo:
- un **System** (`systems/System.py`) — il sistema complesso da esplorare (Gray-Scott, particle-Lenia, ecc., configurato via JSON);
- un **ParameterMap** che campiona i parametri di input (uniforme, o generativi via CPPN/NEAT — `maps/cppn/`);
- un **BehaviorMap** (`maps/MeanBehaviorMap.py`, `IdentityBehaviorMap.py`) che proietta l'output del sistema in uno spazio di "comportamenti" a bassa dimensione;
- l'explorer che pone un goal nello spazio dei comportamenti, cerca i parametri che ci si avvicinano, osserva cosa emerge davvero, e ripete — privilegiando le regioni nuove/curiose.
Attorno c'e' una `ExperimentPipeline` con un fitto sistema di **callback** (on_discovery, on_save, on_finished, report generation) e una Web UI per visualizzare la progressione della scoperta. Gli esempi coprono un bestiario di sistemi emergenti (incluso particle-Lenia, che e' proprio "particelle che si auto-organizzano").

## Perche' riguarda te
Questo e' l'infrastruttura della **novelty-gated** applicata all'esplorazione: l'intera macchina esiste per cercare *cio' che e' nuovo/sorprendente* nello spazio dei comportamenti, non per ottimizzare un reward esterno. E' il ponte diretto fra due tuoi assi — "particelle-emergenza" (i sistemi target sono letteralmente arene di auto-organizzazione, particle-Lenia in testa) e "memoria novelty-gated" (l'archivio delle scoperte e' popolato per novita', e il curiosity explorer decide dove guardare in base a quanto una regione e' inesplorata). Il pattern BehaviorMap e' esattamente quello che ti serve per l'arena: come comprimi uno stato ricco (migliaia di particelle) in poche coordinate leggibili su cui definire "nuovo" e su cui puntare gli oscilloscopi. Dove diverge dai tuoi temi: nessuna coscienza, nessuna ricorsione riflessiva — e' un motore di scoperta scientifica, l'"osservatore" e' fuori dal sistema, non dentro. Ma e' l'unico della lista con licenza MIT: qui puoi davvero riusare codice, non solo idee.

## Da rubare
1. **BehaviorMap + goal nello spazio comportamentale.** Non definire "novita'" sui parametri grezzi ne' sui pixel: proietta lo stato dell'arena in uno spazio comportamentale a bassa dimensione (con una MeanBehaviorMap o un encoder) e misura/gatta la novita' *li'*. E' la mossa che rende la memoria novelty-gated praticabile e gli oscilloscopi interpretabili.
2. **Loop IMGEP come regia dell'arena.** Invece di far girare l'arena passivamente, mettici sopra un explorer curiosity-driven: poni un goal in una regione poco visitata dello spazio comportamentale, cerca le condizioni iniziali/parametri che ci portano, archivia cosa emerge davvero. Trasforma "guardo l'arena" in "l'arena cerca attivamente le proprie configurazioni piu' sorprendenti" — e con la Web UI + callback di adtool hai gia' lo scheletro per registrarle e rivederle.
