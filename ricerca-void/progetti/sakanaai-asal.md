# ASAL — Automating the Search for Artificial Life with Foundation Models (SakanaAI/asal)

Link: https://github.com/SakanaAI/asal

476 stelle · Jupyter Notebook / Python (JAX) · attivo, ultimo push ott 2025 · licenza Apache-2.0

## Cosa fa
ASAL usa modelli fondazionali vision-language (CLIP, DINO) come *giudici automatici di "quanto e' interessante"* una simulazione di vita artificiale. Invece di progettare a mano le regole di un automa cellulare o di un sistema di particelle finche non produce qualcosa di vivo, ASAL cerca automaticamente i parametri della simulazione che (1) producono un fenomeno-target descritto a parole, (2) generano novita temporalmente aperta (open-ended novelty), oppure (3) illuminano un intero spazio di simulazioni diverse fra loro. Funziona su piu substrati: Boids, Particle Life, Game of Life, Lenia, Neural Cellular Automata. Autori da MIT, Sakana AI, OpenAI, IDSIA e Ken Stanley (padre della novelty search).

## Come e' fatto
Tutto in JAX, end-to-end jittabile, quindi velocissimo. La pipeline concettuale e' pulita:
- **Substrate** (`substrates/`) — la simulazione parametrizzata (Lenia, Boids, plife...). Espone `default_params(rng)` e una funzione di step.
- **Foundation model** (`foundation_models/`) — CLIP/DINO che trasforma ogni frame renderizzato in un embedding `z`. E' l'occhio "umano-allineato".
- **Rollout** (`rollout.py`) — fa girare la simulazione, renderizza N frame nel tempo e li passa al FM, restituendo la sequenza di embedding `z`.
- **Metriche** (`asal_metrics.py`) — il pezzo geniale. L'**open-endedness score** e' definito come la novita degli embedding nel tempo: quanto ogni stato futuro e' lontano da tutti gli stati passati nello spazio del foundation model. Un target-match invece e' la similarita fra `z` e il prompt testuale.
- **Ricerca** — tre entry point: `main_opt.py` (Sep-CMA-ES per target e open-endedness), `main_illuminate.py` (algoritmo genetico custom per riempire lo spazio di diversita), `main_sweep_gol.py` (brute force sullo spazio discreto del Game of Life).

L'idea-chiave: l'"interessante" non e' scritto a mano, e' delegato alla rappresentazione di un modello pre-addestrato su percezione umana. La novita viene misurata **nello spazio degli embedding**, non nello spazio grezzo dei pixel — cosi due frame diversi-ma-banali contano poco, mentre una transizione qualitativamente nuova conta molto.

## Perche riguarda te
Questo e' il progetto piu vicino al nucleo del tuo lavoro: unisce particelle-emergenza (i substrati sono letteralmente Particle Life / Lenia / CA), oscilloscopio (il FM e' uno strumento che legge lo stato interno della simulazione e lo proietta in uno spazio leggibile) e memoria novelty-gated (l'open-endedness score e' novelty rispetto alla storia passata — esattamente il gate che ti interessa). E' la prova che "quanto e' nuovo/vivo un sistema" puo essere una grandezza calcolabile e ottimizzabile, non solo un giudizio qualitativo. Per l'arena del vuoto: ASAL ti da una definizione operativa di novelty da agganciare al comportamento delle tue particelle. Dove diverge dalla tua tesi coscienza-ricorsione: il giudice (CLIP) e' *esterno e allineato all'umano* — la novita e' misurata rispetto alla percezione umana pre-addestrata, non rispetto alla auto-modellazione del sistema stesso. Il tuo interesse per la ricorsione richiederebbe che il metro di novita emerga *dall'interno* del sistema, non da un ViT congelato calato dall'alto. E' la differenza fra "questo mi sorprende" (interno) e "questo sorprenderebbe un umano" (ASAL).

## Da rubare
1. **L'open-endedness score come metrica di novelty temporale**: prendi lo stato del sistema, proiettalo in uno spazio di embedding, e definisci novita = distanza di ogni istante da tutti gli istanti precedenti. E' direttamente la tua "memoria novelty-gated": memorizza/premia solo cio che si allontana dalla storia gia vista. Riproducibile su qualsiasi substrato che sai renderizzare in frame.
2. **Delegare il giudizio di "interessante" a un encoder invece che a una reward hand-coded**, e usare CMA-ES / GA sui parametri della simulazione per cercarlo. Anche solo come oscilloscopio: proiettare l'arena in uno spazio di embedding e guardare la traiettoria `z(t)` ti da una lettura compatta dell'evoluzione emergente senza dover definire a priori quali feature guardare.
