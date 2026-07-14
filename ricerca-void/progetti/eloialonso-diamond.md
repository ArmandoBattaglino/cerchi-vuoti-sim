# DIAMOND — eloialonso/diamond

<https://github.com/eloialonso/diamond>

**2.1k stelle · Python · ultimo push dic 2024 · licenza MIT** · paper arXiv:2405.12399 "Diffusion for World Modeling: Visual Details Matter in Atari" (NeurIPS 2024 Spotlight)

## Cosa fa

DIAMOND (DIffusion As a Model Of eNvironment Dreams) addestra un agente di reinforcement learning **interamente dentro un world model a diffusione**: invece di allenarsi nell'ambiente reale, l'agente vive in un modello che genera i fotogrammi futuri con un processo di diffusione condizionato su frame passati e azione. Il nome codifica la tesi: l'ambiente è un *sogno* a diffusione. Include world model giocabili per Atari (100k) e — sul branch `csgo` — un world model di Counter-Strike navigabile a mano, in cui premi `m` e prendi tu il controllo dentro il modello.

## Come è fatto

Struttura chiara in `src/`. Il pezzo chiave è `src/envs/world_model_env.py`: espone il world model come se fosse un normale ambiente Gym (`reset`/`step`), ma ogni `step` è un campionamento di diffusione che disegna il frame successivo. Il modello generativo sta in `src/models/diffusion/` — `denoiser.py`, `inner_model.py`, `diffusion_sampler.py` — più `rew_end_model.py` che predice ricompensa e fine-episodio. L'agente RL (`src/models/actor_critic.py`) è addestrato su rollout *immaginati* dal world model, non su dati reali. `src/game/` fornisce il loop interattivo per "entrare" nel sogno. Configurazione via Hydra (`config/trainer.yaml`), con parametri di sampling (numero di step di denoising, stocasticità, orizzonte di immaginazione) regolabili a caldo. La tesi del paper — "visual details matter" — è che la diffusione, rispetto ai world model discreti/token, preserva dettagli visivi piccoli ma decisivi per la policy.

## Perché riguarda te

Ramo **diffusion world model**, ed è l'aggancio più diretto alla metafora dell'**arena del vuoto come sogno generato**:

- **La realtà dell'agente è sintetizzata frame-per-frame.** Se la tua arena del vuoto è un mondo in cui "particelle" o agenti abitano uno spazio che non esiste fuori dal modello che lo genera, DIAMOND è la dimostrazione ingegneristica che si può fare e che ci si può *entrare dentro* interattivamente. L'orizzonte di immaginazione regolabile (premi `↑/↓`) è letteralmente un controllo su "quanto lontano sogna" il sistema.
- **Coscienza-ricorsione, con onestà.** Qui c'è un anello percezione↔azione chiuso *dentro* un modello del mondo: l'agente agisce su un mondo che è un suo (co-)prodotto. È vicino all'idea di ricorsione della realtà attraverso la materia, ma la divergenza è netta — il world model non si include: modella l'ambiente, non se stesso. Non c'è auto-riferimento, c'è solo un ambiente interiorizzato.

Divergenza pratica: è pesante (GPU, diffusione a molti step), pensato per pixel Atari/CSGO. Per un'arena astratta di "particelle-emergenza" il costo di generare pixel è probabilmente sprecato: ti serve la *struttura* (un modello latente del prossimo stato), non necessariamente il frame RGB.

## Da rubare

- **Il world model esposto come Gym env** (`world_model_env.py`): un mondo interamente generato che espone `reset`/`step` identici a un ambiente reale. Pattern d'oro per rendere la tua arena "sognata" pilotabile sia da un agente sia da un umano con la stessa interfaccia — e per staccare l'oscilloscopio/visualizzatore dal generatore.
- **L'orizzonte di immaginazione come manopola runtime**: separare "quanto in là proietto il sogno" da "quanto ne mostro" dà un controllo diretto sulla profondità della simulazione. Ottimo asse per un oscilloscopio: mostrare lo stesso stato a diversi orizzonti di previsione e vedere dove il sogno diverge.
