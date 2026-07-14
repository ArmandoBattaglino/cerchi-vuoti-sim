# AXIOM (VERSES) — [github.com/VersesTech/axiom](https://github.com/VersesTech/axiom)

79 stelle · Python (JAX) · ultimo push giu 2025 · licenza VERSES Academic Research (non-OSI, uso accademico)

## Cosa fa
Implementazione dell'architettura AXIOM descritta nel preprint "AXIOM: Learning to Play Games in Minutes with Expanding Object-Centric Models" (arXiv 2505.24784). E' un agente che impara a giocare ai giochi del benchmark Gameworld 10k in pochi minuti, senza reti neurali addestrate a gradient descent: tutto e' inferenza bayesiana su modelli generativi. Il punto forte e' la data-efficiency estrema (minuti, non milioni di frame) e la struttura che cresce da sola man mano che scopre nuovi oggetti/dinamiche.

## Come e' fatto
Il cuore e' una pila di "mixture models" object-centric, tutti coniugati e aggiornati per variational inference (cartella `axiom/vi/`, con famiglie esponenziali, distribuzioni MVN/multinomiali, trasformazioni lineari). I modelli sono cinque, componibili:
- **sMM** (slot mixture) — segmenta la scena in slot/oggetti;
- **iMM** (identity) — assegna identita' agli oggetti;
- **tMM** (transition) — dinamica per-oggetto;
- **rMM** (recurrent/relational) — interazioni fra oggetti;
- **hsMM** — dinamica temporale a livello di sequenza.
L'idea chiave: la struttura non e' fissa. I mixture aggiungono componenti quando i dati lo richiedono ("expanding models"), e un passo di **Bayesian Model Reduction** (bmr) pota le componenti ridondanti. Niente backprop: si aprono e si chiudono ipotesi. Il planner (`planner.py`) fa rollout su questi modelli generativi — letteralmente pianifica "sognando" traiettorie nel proprio world model.

## Perche' riguarda te
E' la versione rigorosa e funzionante di "world model come sogno interno" e di "emergenza/auto-espansione della struttura" — due cose che nell'arena del vuoto tendi a mettere a mano. Qui l'apertura di nuove componenti *e'* la nascita di nuova struttura, e la Bayesian Model Reduction *e'* un gate di novelty/parsimonia: si tiene solo cio' che spiega meglio riducendo la complessita'. E' l'analogo matematico pulito della tua "memoria novelty-gated": non salvi tutto, salvi cio' che aumenta l'evidenza. Diverge dai tuoi temi su un punto onesto: AXIOM non ha nessuna pretesa di coscienza ne' di ricorsione riflessiva — e' puro controllo/percezione data-efficient. Non troverai qui l'anello che guarda se stesso; troverai il substrato che fa emergere e potare oggetti in modo principiato.

## Da rubare
1. **Il ciclo espandi/pota come motore di novelty.** Nell'arena: quando un pattern non e' spiegato dalle componenti esistenti, apri una componente nuova (emergenza); periodicamente lancia un passo tipo-BMR che fonde/elimina le componenti che non guadagnano evidenza. Diventa un criterio quantitativo — non estetico — di "cosa merita di esistere/essere ricordato".
2. **Planning come rollout dentro il modello generativo.** Invece di simulare l'ambiente reale per decidere, campiona traiettorie dal world model interno e scegli su quelle. E' il "sogno" reso operativo e leggibile su un oscilloscopio: puoi visualizzare le rollout immaginate vs quelle realizzate.
