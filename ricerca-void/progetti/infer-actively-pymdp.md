# pymdp — [github.com/infer-actively/pymdp](https://github.com/infer-actively/pymdp)

★ 721 · Python · attivo (push lug 2026) · licenza MIT

## Cosa fa

`pymdp` è la libreria di riferimento per simulare agenti ad **inferenza attiva** (active inference) in ambienti modellati come POMDP / Markov Decision Process a stati discreti. È il companion software del paper omonimo pubblicato sul Journal of Open Source Software (Heins, Millidge, Demekas, Klein, Friston, Couzin, Tschantz, 2022). Un agente pymdp non ottimizza una reward esterna alla maniera del RL classico: minimizza la **free energy attesa** (Expected Free Energy, EFE), una quantità che fonde in un unico obiettivo la ricerca di ricompensa (valore pragmatico/utilità) e la ricerca di informazione (valore epistemico, cioè "curiosità"). Il risultato emergente è un agente che esplora attivamente la struttura nascosta del mondo per ridurre la propria incertezza, e proprio così finisce per raggiungere gli obiettivi in modo più efficiente. Il README lo mostra con la demo di "epistemic chaining": un topo-agente insegue una catena di indizi, ciascuno dei quali rivela la posizione del successivo, fino alla ricompensa nascosta — nessun indizio è appreso per condizionamento, l'agente li segue per pura pulsione a disvelare informazione.

## Come è fatto

Idea chiave: un agente è definito da un insieme di **matrici categoriche** che descrivono un modello generativo del mondo, e ad ogni passo fa tre cose in ciclo — inferisce lo stato nascosto (percezione), inferisce quale policy seguire (planning), campiona un'azione.

- **A** = likelihood / modello sensoriale P(osservazione | stato). È la "mappa" che lega ciò che vedi a ciò che c'è.
- **B** = transizioni P(stato' | stato, azione). La dinamica del mondo sotto controllo.
- **C** = preferenze (prior sulle osservazioni desiderate): dove l'agente "vuole" finire, espresso come distribuzione sulle osservazioni.
- **D** = prior iniziale sugli stati.

Il ciclo API è nudo e leggibile: `agent.infer_states(obs)` → belief `qs` sugli stati nascosti (variational inference, minimizzazione della **Variational Free Energy** — restituita come diagnostica `vfe`); `agent.infer_policies(qs)` → distribuzione sulle policy `q_pi` e la negativa EFE `neg_efe`; `agent.sample_action(q_pi)`. Il package è organizzato in moduli netti: `inference.py`, `control.py` (selezione policy), `learning.py` (aggiornamento di A/B col tempo, apprendimento Dirichlet), `maths.py`, `planning/`, più `distribution.py` per i factor discreti multi-fattore (num_obs, num_states, num_controls sono liste — lo spazio è fattorizzato). Le operazioni matematiche di basso livello sono port NumPy delle funzioni SPM di Friston in MATLAB, benchmarkate contro l'originale; la versione recente ha un backend JAX per il batching.

L'EFE decompone in due termini additivi: un termine di utilità (quanto la policy porta verso le osservazioni preferite C) e un termine epistemico (quanta incertezza sugli stati la policy risolve, information gain atteso). Un solo funzionale, due pulsioni. Non c'è "esplorazione ε-greedy" bullonata sopra: l'esplorazione è la conseguenza matematica del voler ridurre la sorpresa attesa.

## Cosa possiamo notare di utile per noi

Questo è il progetto più teoreticamente vicino e insieme più metodologicamente distante dalla nostra arena del vuoto — il confronto è fecondo proprio per questo.

- **Il termine epistemico dell'EFE è la formalizzazione rigorosa della nostra "novelty gate".** Noi ammettiamo in memoria ciò che è nuovo/sorprendente; pymdp *cerca attivamente* ciò che riduce l'incertezza sugli stati nascosti. Sono la stessa intuizione da due lati: noi filtriamo la scrittura in memoria (gate a valle, sull'esperienza già avvenuta), loro pilotano l'azione a monte per generare esperienza informativa (gate a monte, sulla scelta). Trasferibile: si potrebbe definire la "novelty" non euristicamente (distanza da embedding già visti) ma come **information gain atteso** rispetto al modello generativo corrente dell'agente — una novelty gate con basi bayesiane invece che a soglia di similarità. La domanda operativa: "questa esperienza ridurrebbe la mia free energy?" invece di "questa esperienza è lontana da ciò che ho già?".
- **La free energy come segnale unico è un candidato naturale per l'asse verticale dell'oscilloscopio.** Noi visualizziamo lo stato interno; pymdp produce, ad ogni tick, una VFE (sorpresa presente) e una EFE per policy (sorpresa attesa futura). Sono scalari già normalizzati, con semantica precisa: un oscilloscopio che traccia VFE nel tempo mostrerebbe letteralmente i "picchi di sorpresa" — gli istanti in cui il mondo smentisce il modello. Questo è più informativo di una loss generica: distingue la sorpresa che si sta risolvendo (VFE che cala mentre inferisci) da quella irriducibile.
- **Dove diverge (importante):** pymdp NON ha memoria associativa né indirizzabile per contenuto. Il suo "sapere" vive interamente nelle matrici A/B (parametri densi, aggiornati per conteggio Dirichlet), non in tracce episodiche recuperabili. Non c'è un archivio di episodi da interrogare "per somiglianza": c'è un modello del mondo che si aggiorna. È l'opposto della nostra memoria indirizzabile/episodica. Questo è il limite da tenere presente: il framework free-energy è potentissimo sul *controllo* e sulla *percezione*, ma muto sul *ricordo come oggetto separato*. La nostra arena del vuoto vive esattamente nello spazio che pymdp lascia vuoto.
- **Sulla coscienza-come-ricorsione:** pymdp è "flat" — un ciclo percezione/azione senza auto-modello che si osserva. Non c'è ricorsione dell'agente su sé stesso (nessuna meta-inferenza sul proprio stato di inferenza). Ma la struttura fattorizzata degli stati nascosti offre un aggancio: si potrebbe aggiungere un fattore di stato che rappresenta *lo stato dell'agente stesso*, rendendo l'inferenza parzialmente auto-referenziale. Sarebbe la ricorsione minima innestata dentro il formalismo free-energy.

## Da rubare

1. **Novelty gate bayesiana**: sostituire (o affiancare) la soglia di similarità con un calcolo di *expected information gain* — ammetti in memoria l'esperienza che più abbasserebbe l'incertezza del modello interno corrente. Rende la gate adattiva allo stato di conoscenza, non solo alla distanza nell'embedding space.
2. **Traccia VFE sull'oscilloscopio**: esporre uno scalare di free-energy variazionale per tick come canale dedicato dell'oscilloscopio — la "curva di sorpresa" che sale quando il mondo smentisce il modello e scende mentre l'agente ri-inferisce.
3. **Decomposizione utilità/epistemico come due canali distinti**: qualsiasi metrica di "quanto vale un ricordo o un'azione" andrebbe splittata nei due termini pymdp (pragmatico vs epistemico) e mostrata separatamente, così si vede quando l'arena si muove per obiettivo e quando per pura curiosità.
