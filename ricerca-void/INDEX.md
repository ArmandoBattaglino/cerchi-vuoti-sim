# Ricerca «Cerchi Vuoti» — Indice dei progetti

Questa cartella raccoglie la mappa ragionata di **tutti i progetti** (repo, paper, tool, organizzazioni e community) rilevanti per i temi del tuo lavoro: *world model come sogno interno*, *coscienza = ricorsione/relazione*, *memoria novelty-gated*, *arena del vuoto con campi/particelle che si auto-organizzano*. Serve come punto di partenza unico: da qui scegli cosa clonare, cosa leggere e cosa hai già approfondito.

**151 progetti in indice** · **36 già analizzati a fondo** (link `progetti/<slug>.md`) · **127 repo/tool clonabili** via `clone-all.sh`.

## Legenda rilevanza

Quanto un progetto è vicino al *cuore* dei tuoi temi (non quanto è "buono" in assoluto):

| Livello | Significato |
|---|---|
| `●●●●●` | On-theme quasi 1:1 — guardalo per primo |
| `●●●●○` | Fortemente rilevante, aggancio diretto a uno o più temi |
| `●●●○○` | Rilevante di contesto / infrastruttura / riferimento |
| `●●○○○` | Periferico, tassello o curiosità |

Il badge `★` è il numero di stelle GitHub (quando applicabile). `[analisi]` porta a una scheda di approfondimento locale.

## I 5 progetti-chiave (parti da qui)

1. **[dancinlab/anima](https://github.com/dancinlab/anima)** — Il seed del filone e il piu on-theme in assoluto: 'Living Consciousness Agent' costruito su un PureField repulsion-field engine, con Engine A (arena/attore) accoppiato a Engine G (generatore), punto fisso Psi=1/2, e un corpus di 2.
2. **[Generative Agents (Stanford Smallville)](https://github.com/joonspk-research/generative_agents)** — Simulacri interattivi di comportamento umano: 25 agenti in un mondo sandbox con memory stream recuperata via punteggio recency+importance+relevance, riflessione ricorsiva (sintesi di ricordi in insight di livello superiore) e planning.
3. **[danijar/dreamerv3](https://github.com/danijar/dreamerv3)** — DreamerV3: apprende un world model latente ricorrente (RSSM) e allena la policy interamente per 'immaginazione' (rollout nel sogno latente), con normalizzazioni robuste che gli permettono di dominare 150+ domini con iperparametri fissi.
4. **[Darwin Gödel Machine (jennyzzt/dgm)](https://github.com/jennyzzt/dgm)** — Repo ufficiale Sakana/Vector/UBC del Darwin Gödel Machine (arXiv:2505.
5. **[SakanaAI/asal](https://github.com/SakanaAI/asal)** — Automating the Search for Artificial Life with Foundation Models (Sakana AI, MIT, OpenAI, IDSIA, Ken Stanley).

---

## Progetti per filone

### World models — mondi interni & sogno predittivo
*18 progetti · 2 analizzati*

- **[danijar/dreamerv3](https://github.com/danijar/dreamerv3)** `●●●●●` · 3.535★ · [analisi](progetti/danijar-dreamerv3.md)  
  DreamerV3: apprende un world model latente ricorrente (RSSM) e allena la policy interamente per 'immaginazione' (rollout nel sogno latente), con normalizzazioni robuste che gli permettono di dominare 150+ domini con iperparametri fissi. Riferimento vivente del 'sogno interno' come substrato dell'agire.
- **[eloialonso/diamond](https://github.com/eloialonso/diamond)** `●●●●●` · 2.077★ · [analisi](progetti/eloialonso-diamond.md)  
  DIAMOND (DIffusion As a Model Of eNvironment Dreams): l'agente RL vive e si allena dentro un world model a diffusione che genera i fotogrammi futuri. Il nome codifica il 'sogno': l'ambiente e' un sogno a diffusione. NeurIPS 2024 Spotlight, include CS:GO giocabile dentro il modello.
- **[World Models (Ha & Schmidhuber)](https://arxiv.org/abs/1803.10122)** `●●●●●` · 720★  
  Il paper-radice del filone: agente che comprime la percezione in uno spazio latente (VAE=V) e apprende un modello ricorrente predittivo (MDN-RNN=M), poi allena il controller DENTRO il sogno del modello ('training inside the dream'). Incarnazione diretta del 'world model come sogno interno' e della ricorsione percezione->predizione->azione.
- **[Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391)** `●●●●●`  
  DeepMind Genie (11B): da video Internet NON etichettati emerge un modello di azioni latenti + tokenizer spatio-temporale + dinamica autoregressiva, generando mondi giocabili controllabili frame-by-frame. Auto-organizzazione pura: le 'azioni' emergono senza supervisione. Genie 2 (2024) e Genie 3 (2025) estendono a mondi 3D real-time via annunci-blog.
- **[facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2)** `●●●●○` · 4.345★  
  V-JEPA 2 (Meta): world model self-supervised da video che predice NELLO spazio delle rappresentazioni (non pixel), scala a 1M+ ore video e abilita planning zero-shot per robotica (V-JEPA2-AC). Incarna 'predizione relazionale nel latente' invece che ricostruzione: relazione fra rappresentazioni piu che rendering.
- **[facebookresearch/jepa (V-JEPA)](https://github.com/facebookresearch/jepa)** `●●●●○` · 4.030★  
  V-JEPA prima generazione: apprende predicendo regioni mascherate di video nello spazio latente. Base concettuale della tesi LeCun che l'intelligenza nasce dal predire rappresentazioni astratte (relazioni), non dettagli sensoriali - vicino all'idea 'coscienza = relazione/ricorsione nel latente'.
- **[etched-ai/open-oasis](https://github.com/etched-ai/open-oasis)** `●●●●○` · 2.107★  
  Open-Oasis: inferenza open del world model Oasis 500M (Decart/Etched), un Minecraft interamente 'sognato' a diffusione, generato frame-by-frame in risposta ai tasti del giocatore. Nessun motore di gioco: solo il sogno del modello. Manifesto pop del 'world model come mondo giocabile'.
- **[AlmondGod/tinyworlds](https://github.com/AlmondGod/tinyworlds)** `●●●●○` · 1.330★  
  tinyworlds: reimplementazione minimale e leggibile di Genie (tokenizer video + azioni latenti + dinamica). Perfetto per capire e hackare il meccanismo per cui le azioni EMERGONO da video non etichettati - ideale per esperimenti su emergenza/auto-organizzazione con poche risorse.
- **[nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2)** `●●●●○` · 889★  
  TD-MPC2: world model implicito (decoder-free) in spazio latente + planning con Model Predictive Path Integral. Un unico agente da 317M param padroneggia 80+ task continui. Esempio pulito di 'pianificare simulando internamente' senza ricostruire i pixel - il modello serve solo l'azione.
- **[microsoft/mineworld](https://github.com/microsoft/mineworld)** `●●●●○` · 481★  
  MineWorld (Microsoft): world model interattivo real-time su Minecraft basato su Transformer autoregressivo su token visivi+azione, con decoding parallelo per la reattivita. Ricerca aperta e riproducibile sul 'mondo interno giocabile' con codice e pesi.
- **[GameNGen: Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837)** `●●●●○`  
  GameNGen (Google): un modello a diffusione simula DOOM interattivo a >20 FPS su una singola TPU, mantenendo lo stato di gioco (vita, munizioni, porte) puramente nella rete. Prova che un motore-mondo puo essere interamente 'sognato' e persistente - i valutatori umani distinguono a malapena sogno da gioco reale.
- **[NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)** `●●●○○` · 11.040★  
  NVIDIA Cosmos: piattaforma aperta di World Foundation Models per Physical AI (robot, veicoli, infrastrutture). Tokenizer + modelli generativi (diffusion/autoregressive) che simulano il futuro fisico del mondo come video condizionato. Incarnazione industriale-scala del 'sogno del mondo' con vincoli fisici.
- **[facebookresearch/ijepa](https://github.com/facebookresearch/ijepa)** `●●●○○` · 3.471★  
  I-JEPA (CVPR 2023): la versione immagine, radice della famiglia JEPA. Predice rappresentazioni di blocchi target da un contesto, dimostrando che l'astrazione emerge senza augmentation artigianali. Primo mattone dell'architettura joint-embedding predittiva.
- **[NVIDIA-Cosmos/cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5)** `●●●○○` · 1.320★  
  Cosmos-Predict 2.5: ultima famiglia WFM di NVIDIA specializzata nel predire lo stato futuro del mondo come video. Il cuore 'predittivo' del sogno Cosmos: dato lo stato/azione, genera il futuro plausibile per addestrare o valutare agenti fisici.
- **[danijar/dreamerv2](https://github.com/danijar/dreamerv2)** `●●●○○` · 1.051★  
  DreamerV2: 'Mastering Atari with Discrete World Models'. Primo agente a superare umani su Atari usando SOLO rollout immaginati in un world model a latenti discreti (categorical RSSM). Tappa storica della catena Dreamer verso V3 - il salto ai latenti discreti come 'grammatica' del sogno.
- **[OpenDriveLab/Vista](https://github.com/OpenDriveLab/Vista)** `●●●○○` · 889★  
  Vista (NeurIPS 2024): world model generalizzabile per guida autonoma, predice futuri ad alta fedelta e lungo orizzonte condizionati da azioni, con controllo a diverse granularita. Caso applicato del 'sogno del mondo' come simulatore predittivo per il planning veicolare.
- **[1x-technologies/1xgpt](https://github.com/1x-technologies/1xgpt)** `●●●○○` · 563★  
  1X World Model Challenge: dataset+baseline per predire futuri osservazioni di robot umanoidi reali. Spinge la community a costruire modelli predittivi del mondo fisico da esperienza incarnata - ponte fra il 'sogno interno' e corpi reali (embodiment).
- **[NVIDIA-Cosmos/cosmos-transfer1](https://github.com/nvidia-cosmos/cosmos-transfer1)** `●●○○○` · 809★  
  Cosmos-Transfer1: modello world-to-world che traduce fra ambienti simulati e reali (colma il divario percettivo sim2real) condizionando la generazione su segnali strutturali. Tassello per far dialogare 'mondo sognato' e mondo osservato.

### Coscienza — framework, teorie e indicatori
*19 progetti · 4 analizzati*

- **[PyPhi](https://github.com/wmayner/pyphi)** `●●●●●` · 426★ · [analisi](progetti/wmayner-pyphi.md)  
  Toolbox di riferimento per la Integrated Information Theory: calcola Phi, i complessi e le strutture cause-effetto di un sistema. E' l'implementazione canonica di IIT (fino a IIT 4.0). Rilevante come 'oscilloscopio' formale sugli stati interni e come misura di auto-organizzazione/emergenza integrata.
- **[AXIOM (VERSES)](https://github.com/VersesTech/axiom)** `●●●●●` · 79★ · [analisi](progetti/versestech-axiom.md)  
  Architettura AXIOM di VERSES: 'digital brain' object-centric che impara a giocare in minuti con modelli generativi espandibili (Bayesian, no gradient descent). Incarna 'world model come sogno interno' + emergenza/auto-espansione della struttura. Base di ricerca dietro il prodotto Genius.
- **[AURA](https://github.com/youngbryan97/aura)** `●●●●●` · 61★ · [analisi](progetti/youngbryan97-aura.md)  
  Architettura cognitiva 'sovrana' che combina esplicitamente IIT 4.0 (integrated information), Global Workspace Theory, active inference e steering affettivo sul residual-stream (CAA), con 72 'consciousness modules', girando locale su Apple Silicon. Molto vicino ai temi utente: oscilloscopi/steering sugli stati interni + ricorsione dei framework.
- **[GodelOS](https://github.com/Steake/GodelOS)** `●●●●●` · 16★ · [analisi](progetti/steake-godelos.md)  
  'AGI runtime for bounded recursive self-awareness' — tenta machine consciousness al 'nesso Godel-Turing-Hofstadter'. Centrato su ricorsione e auto-referenza limitata: mappa diretta della tesi utente 'coscienza = ricorsione della realta'.
- **[Consciousness in AI: Insights from the Science of Consciousness (Butlin, Long, Bengio et al.)](https://arxiv.org/abs/2308.08708)** `●●●●●`  
  Il paper-ancora del filone 'framework a indicatori': deriva indicator properties di coscienza in termini computazionali da 5 teorie (recurrent processing, global workspace, higher-order, predictive processing, attention schema) e valuta i sistemi AI attuali. Conclusione: nessun sistema attuale e' cosciente, ma nessuna barriera tecnica ovvia. 19 autori inclusi Bengio.
- **[pymdp](https://github.com/infer-actively/pymdp)** `●●●●○` · 721★  
  Implementazione Python dell'active inference su POMDP (free energy principle di Friston). Agente come modello generativo che minimizza sorpresa: 'world model come sogno interno' + auto-organizzazione. Base tecnica del filone predictive-processing degli indicatori Butlin/Bengio.
- **[Global-Workspace-Agents](https://github.com/giansha/Global-Workspace-Agents)** `●●●●○` · 14★  
  Architettura multi-agente LLM ispirata a GWT per abilitare LLM a 'pensare proattivamente' e iniziare dialogo: piu' processi specializzati competono per un workspace globale condiviso. Rilevante per il broadcast attentivo e l'emergenza di iniziativa.
- **[ZugaMind](https://github.com/Zuga-Technologies/zugamind)** `●●●●○` · 10★  
  'Persistent cognition sidecar' che implementa Global Workspace Theory: osserva gli agenti (Claude Code, Codex...) e li 'sveglia' solo quando qualcosa merita attenzione — cioe' un gating della salienza/novita' verso il workspace globale. Vicino a 'memoria novelty-gated' + broadcast attentivo.
- **[LIDA Framework (CCRG)](https://github.com/CognitiveComputingResearchGroup/lida-framework)** `●●●●○` · 10★  
  Framework Java della LIDA di Stan Franklin, la piu' completa implementazione di Global Workspace Theory con cognitive cycle, coscienza come competizione per il workspace, novelty e attenzione. Storico ma canonico per GWT. Repo poco attivo (2016) ma di riferimento accademico.
- **[Taking AI Welfare Seriously (Long, Sebo, Butlin, Chalmers et al.)](https://arxiv.org/abs/2411.00986)** `●●●●○`  
  Report (nov 2024) che argomenta la realistica possibilita' di sistemi AI coscienti e/o robustamente agentici nel prossimo futuro, e le implicazioni di moral patienthood. Due rotte allo status morale: coscienza e robust agency. Rilevante come cornice etica/scientifica del filone e per il tema 'assessment degli stati interni'.
- **[Conscium / PRISM](https://conscium.com)** `●●●●○`  
  Organizzazione dedicata alla ricerca su machine consciousness; ha lavorato con Patrick Butlin (Oxford) sui 'Principles for Responsible AI Consciousness Research' (Lappas & Butlin 2025). Ha lanciato PRISM (Partnership for Research Into Sentient Machines), non-profit (mar 2025) e il programma long-horizon 'Frontier'.
- **[AE Studio (alignment/consciousness research)](https://ae.studio)** `●●●●○`  
  Team di ricerca alignment neuroscience-inspired che sonda dinamiche interne degli LLM per evidenze di self-reference/esperienza soggettiva: induced self-reference, interpretability, cognitive stress-testing. Direttamente allineato a 'oscilloscopi su stati interni' e auto-referenza.
- **[VERSES AI (Genius / Active Inference research)](https://www.verses.ai/active-inference-research)** `●●●●○`  
  Azienda che commercializza active inference/world models (Genius, architettura AXIOM). Nel 2025 citata da Gartner come sample vendor per Active Inference, Spatial Computing e World Models. Braccio industriale del filone predictive-processing/auto-organizzazione.
- **[FEP_Active_Inference_Papers](https://github.com/BerenMillidge/FEP_Active_Inference_Papers)** `●●●○○` · 241★  
  Repo di curation dei paper piu' influenti su Free Energy Principle e active inference. Mappa d'ingresso al filone predictive-processing degli indicatori di coscienza. Non aggiornato dal 2021 ma resta la bibliografia di riferimento.
- **[Active-Inference-Tutorial-Scripts](https://github.com/rssmith33/Active-Inference-Tutorial-Scripts)** `●●●○○` · 133★  
  Script del tutorial step-by-step di active inference modelling (Smith, Friston, Whyte). Ottimo per capire meccanicamente come un modello generativo minimizza free energy — utile per costruire 'oscilloscopi' su belief interni.
- **[deep-active-inference-mc](https://github.com/zfountas/deep-active-inference-mc)** `●●●○○` · 102★  
  Agenti di deep active inference con metodi Monte-Carlo: scaling del free energy principle a spazi ad alta dimensione con reti neurali. Ponte tra predictive processing e deep learning per world-model interni.
- **[ActiveInferenceJournal (Active Inference Institute)](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal)** `●●●○○` · 43★  
  Contenuti del giornale dell'Active Inference Institute — hub community open del filone FEP/active inference, con materiali su modelli generativi, coscienza computazionale e auto-organizzazione. Punto d'ingresso alla community piu' viva del predictive processing.
- **[qr-sampler (Entropic Science)](https://github.com/Entropic-Science/qr-sampler)** `●●●○○` · 34★  
  Integra sorgenti di randomness (incl. quantum) nel token sampling degli LLM, con profili per 'consciousness signal amplification algorithms' per ricerca di machine consciousness. Curiosita' rilevante per il tema 'arena del vuoto/particelle' (rumore quantistico iniettato negli stati interni).
- **[Gameworld (VERSES)](https://github.com/VersesTech/gameworld)** `●●●○○` · 14★  
  10 ambienti di gioco usati come benchmark per valutare AXIOM contro RL/deep learning su sample-efficiency e adattamento. Utile come benchmark per world-model che 'sognano' la dinamica.

### Inferenza attiva / predictive coding
*13 progetti · 4 analizzati*

- **[RxInfer.jl](https://github.com/ReactiveBayes/RxInfer.jl)** `●●●●●` · 409★ · [analisi](progetti/reactivebayes-rxinfer.jl.md)  
  Inferenza bayesiana automatica su factor graph con reactive message passing (Julia). Rende trattabile l'active inference in tempo reale (robotica, controllo). Modello del mondo come grafo di credenze aggiornate per passaggio di messaggi locali - relazioni/ricorsione tra nodi, non calcolo centralizzato.
- **[ngc-learn](https://github.com/NACLab/ngc-learn)** `●●●●●` · 197★ · [analisi](progetti/naclab-ngc-learn.md)  
  Libreria NeuroAI/neuroscienza computazionale (JAX) del NAC Lab per costruire e simulare sistemi predictive coding e neurali biologicamente plausibili con apprendimento locale. Ottima per 'oscilloscopi su stati interni': espone dinamiche di errore di predizione e stati latenti a ogni livello.
- **[collective_motion_actinf](https://github.com/conorheins/collective_motion_actinf)** `●●●●●` · 55★ · [analisi](progetti/conorheins-collective_motion_actinf.md)  
  Simulazione di moto collettivo da gruppi di agenti active inference continui nello spazio/tempo (Heins et al.). Emergenza di comportamento di sciame da minimizzazione locale di free energy - self-organization e pattern collettivi dal basso. Molto vicino all'idea di particelle/campi che si auto-organizzano nell'arena.
- **[pni-lab/fep-attractor-network](https://github.com/pni-lab/fep-attractor-network)** `●●●●●` · 26★ · [analisi](progetti/pni-lab-fep-attractor-network.md)  
  Sorgente del manoscritto 'Self-orthogonalizing attractor neural networks emerging from the free energy principle': reti attrattore che si auto-organizzano e auto-ortogonalizzano derivate dal FEP. Direttamente sul cuore dei temi: auto-organizzazione/emergenza, memoria come attrattori, campo che si struttura da se.
- **[PredNet (coxlab/prednet)](https://github.com/coxlab/prednet)** `●●●●○` · 804★  
  Deep Predictive Coding Network per video prediction e unsupervised learning (Lotter, Kreiman, Cox). Architettura storica che incarna il predictive coding gerarchico: ogni livello predice il successivo e propaga solo l'errore. Prototipo di 'world model come sogno interno' che genera il frame successivo.
- **[TAPAS](https://github.com/translationalneuromodeling/tapas)** `●●●●○` · 251★  
  Translational Algorithms for Psychiatry-Advancing Science (ETH Zurich): toolbox MATLAB con l'implementazione canonica dell'HGF, modelli di percezione bayesiana e inferenza sulla precisione. Riferimento storico per HGF e stima di stati interni/credenze da dati fisiologici.
- **[pyhgf](https://github.com/ComputationalPsychiatry/pyhgf)** `●●●●○` · 151★  
  Hierarchical Gaussian Filter come rete di predictive coding (JAX/dynamic networks). Aggiornamento gerarchico delle credenze modulato dalla precisione/volatilita - meccanismo naturale per memoria gated dalla sorpresa (novelty). Grafi generici, non solo HGF classico.
- **[pcx](https://github.com/liukidar/pcx)** `●●●●○` · 107★  
  Libreria predictive coding basata su JAX (associata al Buckley Lab / Sussex). Framework modulare per reti PC arbitrarie con energia esplicita minimizzata per inferenza. Utile per esperimenti su world model come inferenza generativa e ispezione degli stati latenti.
- **[jpc](https://github.com/thebuckleylab/jpc)** `●●●●○` · 84★  
  'Flexible Inference for Predictive Coding Networks in JAX' del Buckley Lab (Sussex, VERSES-adiacente). Inferenza flessibile su reti PC, ponte tra PC e deep learning. Manutenzione attiva 2026.
- **[self-revising-active-inference (SR-AIF)](https://github.com/NACLab/self-revising-active-inference)** `●●●●○` · 65★  
  Implementazione ufficiale di SR-AIF: risolve compiti robotici sparse-reward da pixel combinando active inference e world models auto-revisionanti. Incarna il 'world model come sogno interno' che viene continuamente riscritto - vicino a memoria novelty-gated + world model generativo.
- **[ActiveInference.jl](https://github.com/ComputationalPsychiatry/ActiveInference.jl)** `●●●●○` · 41★  
  Pacchetto Julia per active inference (POMDP), controparte di pymdp nell'ecosistema Julia, integrato con lo stack ReactiveBayes/RxInfer. Model fitting per computational psychiatry oltre alla simulazione di agenti.
- **[Active Inference Institute](https://github.com/ActiveInferenceInstitute)** `●●●●○`  
  Organizzazione no-profit che coordina la community FEP/active inference: corsi, ActiveInferenceJournal (43 star, aggiornato 2026-06), ActiveInferAnts e decine di repo di modelli/ontologie. Hub principale per persone, paper e strumenti del filone.
- **[SPM (spm/spm)](https://github.com/spm/spm)** `●●●○○` · 211★  
  Statistical Parametric Mapping, il pacchetto di Karl Friston: contiene DEM (Dynamic Expectation Maximization), il generalized filtering e le demo originali di active inference/free energy da cui l'intero filone e nato. Sorgente primaria del FEP.

### Memoria degli agenti
*17 progetti · 7 analizzati*

- **[A-MEM (Agentic Memory)](https://github.com/agiresearch/A-mem)** `●●●●●` · 1.110★ · [analisi](progetti/agiresearch-a-mem.md)  
  NeurIPS 2025 (Xu et al.). Memoria agentica auto-organizzante ispirata allo Zettelkasten: ogni nuova memoria genera note strutturate, si collega dinamicamente a memorie correlate, e l'inserimento aggiorna/evolve gli attributi delle note esistenti (link e contesti si riscrivono). La rete di memoria si struttura da sola.
- **[MemGen (Generative Latent Memory)](https://github.com/bingreeky/MemGen)** `●●●●●` · 405★ · [analisi](progetti/bingreeky-memgen.md)  
  Codice ufficiale (ICLR 2026, arXiv 2509.24704, Zhang/Fu/Yan). Due moduli: un memory TRIGGER che monitora lo stato di ragionamento dell'agente per decidere QUANDO invocare memoria, e un memory WEAVER che genera token latenti che incapsulano esperienza. Senza supervisione esplicita emergono spontaneamente facolta di memoria umane: planning, procedurale, working memory.
- **[EM-LLM (Human-inspired Episodic Memory)](https://github.com/em-llm/EM-LLM-model)** `●●●●●` · 279★ · [analisi](progetti/em-llm-em-llm-model.md)  
  Segmenta il flusso di token in eventi episodici usando la SORPRESA bayesiana come confine (surprise-gated), poi raffina i confini con teoria dei grafi e recupera via similarita + contiguita temporale. Nessun fine-tuning, contesto ~infinito (retrieval su 10M token), batte InfLLM/RAG su LongBench e infinity-Bench. Huawei Noah's Ark + UCL, ICLR 2025.
- **[AriGraph](https://github.com/AIRI-Institute/AriGraph)** `●●●●●` · 171★ · [analisi](progetti/airi-institute-arigraph.md)  
  AIRI Institute. Costruisce un WORLD MODEL come knowledge graph con memoria semantica+episodica integrate mentre l'agente esplora un ambiente testuale (TextWorld); recupero graph-based per pianificare. La memoria e letteralmente un modello del mondo che l'agente costruisce e naviga.
- **[Titans (Learning to Memorize at Test Time)](https://arxiv.org/abs/2501.00663)** `●●●●●`  
  Google Research (Behrouz, Zhong, Mirrokni). Modulo di memoria neurale a lungo termine che impara a memorizzare al test-time: memorizza in modo adattivo i token piu SORPRENDENTI (sorpresa = gradiente della rete) con un forget-gate che decade in base a memoria/sorpresa. Tre rami: core, memoria contestuale, memoria persistente. Sequenze oltre 2M token.
- **[mem0](https://github.com/mem0ai/mem0)** `●●●●○` · 60.809★ · [analisi](progetti/mem0ai-mem0.md)  
  Layer di memoria universale per agenti AI (il repo piu popolare del filone). Estrae, consolida e recupera fatti salienti dalle conversazioni con scoring di rilevanza; scrive solo cio che conta e aggiorna/deduplica invece di accumulare tutto. Gia usato localmente dall'utente (mem0-personal).
- **[Graphiti (Zep)](https://github.com/getzep/graphiti)** `●●●●○` · 28.706★ · [analisi](progetti/getzep-graphiti.md)  
  Engine di getzep per knowledge graph TEMPORALI in tempo reale per agenti: ogni fatto ha validita temporale (bi-temporal), i nodi/archi si aggiornano incrementalmente e i fatti obsoleti vengono invalidati (non cancellati) mentre arrivano nuovi eventi. Memoria che modella il tempo e la revisione delle credenze.
- **[Letta (ex MemGPT)](https://github.com/letta-ai/letta)** `●●●●○` · 23.789★ · [analisi](progetti/letta-ai-letta.md)  
  Piattaforma per agenti stateful nata dal paper MemGPT: gerarchia di memoria in stile OS (context window come RAM, storage esterno come disco) con l'LLM che si auto-gestisce paginando ricordi dentro/fuori il contesto. Standard de-facto per agenti con memoria persistente e auto-editing.
- **[MemOS (Memory Operating System)](https://github.com/MemTensor/MemOS)** `●●●●○` · 10.206★  
  OS di memoria auto-evolvente per LLM/agenti: memoria ultra-persistente, retrieval ibrido e riuso di skill cross-task, con ~35% di risparmio token. Tratta la memoria come risorsa di prima classe schedulata da un sistema operativo (MemCube come unita), non come semplice vector store.
- **[HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG)** `●●●●○` · 3.853★  
  NeurIPS 2024. RAG neurobiologicamente ispirato all'ippocampo: indicizza la conoscenza in un knowledge graph e usa Personalized PageRank (analogo del pattern completion ippocampale) per integrare informazione tra documenti in un solo passo di retrieval. HippoRAG 2 estende verso memoria continua.
- **[MIRIX](https://github.com/Mirix-AI/MIRIX)** `●●●●○` · 3.554★  
  Assistente personale multi-agente con sistema di memoria a piu tipi (core, episodica, semantica, procedurale, resource, knowledge vault) gestiti da agenti dedicati; cattura in tempo reale l'attivita on-screen e consolida input grezzi in memorie strutturate interrogabili.
- **[titans-pytorch (lucidrains)](https://github.com/lucidrains/titans-pytorch)** `●●●●○` · 1.969★  
  Implementazione PyTorch non ufficiale (ma di riferimento, molto curata e attivamente mantenuta) del neural long-term memory di Titans. Il modo piu diretto per sperimentare la memoria latente surprise-gated di test-time in codice eseguibile.
- **[OpenUnlearning](https://github.com/locuslab/open-unlearning)** `●●●●○` · 566★  
  NeurIPS D&B 2025 (locuslab). Repository di riferimento per il machine unlearning su LLM: unifica metodi di forgetting e benchmark (TOFU, MUSE) con metriche per misurare quanto viene rimosso (forget) senza degradare il resto (retain), inclusa la membership inference.
- **[cognee](https://github.com/topoteretes/cognee)** `●●●○○` · 27.828★  
  Piattaforma di memoria AI open-source: costruisce un knowledge graph self-hosted (pipeline ECL: Extract-Cognify-Load) come memoria a lungo termine persistente cross-sessione per agenti. Fonde grafo + vettori per dare struttura relazionale alla memoria invece del solo chunk retrieval.
- **[Memobase](https://github.com/memodb-io/memobase)** `●●●○○` · 2.783★  
  Memoria a lungo termine basata su PROFILO utente per chatbot: invece di conservare messaggi grezzi, distilla e mantiene un profilo utente strutturato ed evolutivo nel tempo. Approccio orientato al consolidamento (chi e l'utente) piu che alla trascrizione.
- **[Memary](https://github.com/kingjulio8238/Memary)** `●●●○○` · 2.632★  
  Memory layer open-source per agenti autonomi che emula la memoria umana: knowledge graph (Neo4j) piu ranking di entita che decade nel tempo per modellare cosa resta saliente. Combina memoria di lavoro, entita e recency-weighting.
- **[Agent-Memory-Paper-List (Memory in the Age of AI Agents: A Survey)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)** `●●●○○` · 2.247★  
  Lista curata a supporto della survey 'Memory in the Age of AI Agents'. Tassonomizza il campo (memoria parametrica vs contestuale, breve vs lungo termine, operazioni di consolidamento/aggiornamento/forgetting) e raccoglie i paper: mappa d'orientamento per tutto il filone.

### Artificial life / emergenza & auto-organizzazione
*18 progetti · 8 analizzati*

- **[Chakazul/Lenia](https://github.com/Chakazul/Lenia)** `●●●●●` · 3.798★ · [analisi](progetti/chakazul-lenia.md)  
  Repo canonico di Bert Wang-Chak Chan: Lenia, forme di vita matematiche in automi cellulari continui (spazio/tempo/stato continui). Kernel a convessita multipla che generano centinaia di 'creature' auto-mantenute (orbium, ecc.) che si muovono e reagiscono. Il paradigma padre di Flow-Lenia e Particle Lenia. Include Python/JS/Matlab e zoo di specie.
- **[hunar4321/particle-life](https://github.com/hunar4321/particle-life)** `●●●●●` · 3.342★ · [analisi](progetti/hunar4321-particle-life.md)  
  Simulazione di vita artificiale da sole forze di attrazione/repulsione tra molte particelle di colori diversi: regole minime -> pattern e 'organismi' complessi emergenti. Uno dei repo Particle Life piu popolari, con clip virali; codice C++/JS accessibile.
- **[hardmaru/WorldModelsExperiments](https://github.com/hardmaru/WorldModelsExperiments)** `●●●●●` · 720★ · [analisi](progetti/hardmaru-worldmodelsexperiments.md)  
  Codice degli esperimenti 'World Models' (Ha & Schmidhuber): un agente costruisce un modello interno (VAE+RNN) del mondo e puo allenarsi/agire dentro il proprio 'sogno' (rollout nel modello latente) invece che nell'ambiente reale. Aggancio diretto a 'world model come sogno interno'.
- **[SakanaAI/asal](https://github.com/SakanaAI/asal)** `●●●●●` · 476★ · [analisi](progetti/sakanaai-asal.md)  
  Automating the Search for Artificial Life with Foundation Models (Sakana AI, MIT, OpenAI, IDSIA, Ken Stanley). Usa vision-language models come misura di 'interessante' per cercare simulazioni che producono novita temporalmente aperta (open-ended novelty) e per illuminare spazi di simulazioni diverse. JAX end-to-end jittable; substrati: Boids, Particle Life, Game of Life, Lenia, Neural CA.
- **[google-research/self-organising-systems](https://github.com/google-research/self-organising-systems)** `●●●●●` · 420★ · [analisi](progetti/google-research-self-organising-systems.md)  
  Monorepo del gruppo Mordvintsev/Randazzo/Niklasson (Google) dietro la serie Distill su self-organization: Growing NCA, Self-classifying MNIST, Texture NCA, Particle Lenia, e formulazione energy-based. Cuore della ricerca 'la struttura globale emerge da regole locali identiche'. Aggiornato 2026.
- **[distillpub/post--growing-ca (Growing NCA)](https://github.com/distillpub/post--growing-ca)** `●●●●●` · 104★  
  Repo dell'articolo Distill 2020 'Growing Neural Cellular Automata' (Mordvintsev, Randazzo, Niklasson, Levin): celle identiche con rete neurale locale imparano a crescere e rigenerare un'immagine target - morfogenesi differenziabile. Testo fondativo dell'NCA moderno.
- **[flowersteam/adtool (Automated Discovery Tool)](https://github.com/flowersteam/adtool)** `●●●●●` · 45★ · [analisi](progetti/flowersteam-adtool.md)  
  Tool del Flowers Lab (INRIA) per esplorazione curiosity-driven di sistemi complessi via IMGEP (Intrinsically Motivated Goal Exploration Processes): l'agente pone obiettivi nuovi a se stesso e mappa lo spazio dei comportamenti emergenti (Lenia, reaction-diffusion, ecc.). Attivo 2026.
- **[erwanplantec/FlowLenia](https://github.com/erwanplantec/FlowLenia)** `●●●●●` · 26★ · [analisi](progetti/erwanplantec-flowlenia.md)  
  Implementazione di Flow-Lenia: variante di Lenia con conservazione della massa (advection/reintegration tracking) e localizzazione dei parametri, che abilita evoluzione open-ended dentro l'automa cellulare (creature con 'genomi' locali che competono nello stesso spazio). Autore del paper originale (arxiv 2212.07906 / 2506.08569).
- **[flowersteam/automated_discovery_of_lenia_patterns](https://github.com/flowersteam/automated_discovery_of_lenia_patterns)** `●●●●●` · 21★ · [analisi](progetti/flowersteam-automated_discovery_of_lenia_patterns.md)  
  Codice del paper ICLR 2020 'Intrinsically Motivated Discovery of Diverse Patterns in Self-Organizing Systems' (IMGEP-HOLMES applicato a Lenia): scoperta automatica di strutture auto-organizzate imparando gerarchie di spazi di caratterizzazione comportamentale.
- **[CarperAI/OpenELM](https://github.com/CarperAI/OpenELM)** `●●●●○` · 742★  
  Evolution Through Large Models: libreria che usa LLM come operatori di mutazione dentro loop di quality-diversity (MAP-Elites) per generazione open-ended di artefatti diversi. Ponte tra open-endedness classica e modelli di fondazione.
- **[HackerPoet/Particle-Life](https://github.com/HackerPoet/Particle-Life)** `●●●●○` · 371★  
  'A game of life with particles' di CodeParade: implementazione compatta e didattica del particle life che ha popolarizzato il paradigma (video virale). Codice chiaro come riferimento minimale.
- **[PWhiddy/Growing-Neural-Cellular-Automata-Pytorch](https://github.com/PWhiddy/Growing-Neural-Cellular-Automata-Pytorch)** `●●●●○` · 142★  
  Esperimenti estesi di Growing NCA in PyTorch (rigenerazione, robustezza, varianti). Una delle implementazioni NCA piu manutenute e leggibili, aggiornata 2025.
- **[tom-mohr/particle-life](https://github.com/tom-mohr/particle-life)** `●●●●○` · 102★  
  Framework Java per sistemi di particelle (Particle Life e varianti) con GPU rendering, GUI e community attiva (particle-life.com). Piu ingegnerizzato e manutenuto della media dei cloni; buono come base architetturale.
- **[Transcenduality/primordis](https://github.com/Transcenduality/primordis)** `●●●●○` · 43★  
  Particle life avanzato ottimizzato per massima complessita ed emergenza di 'organismi' simulati, con evoluzione genetica aggiunta (i pattern hanno genomi che mutano/si selezionano). Attivo 2026.
- **[dwoiwode/awesome-neural-cellular-automata](https://github.com/dwoiwode/awesome-neural-cellular-automata)** `●●●●○` · 25★  
  Lista curata di paper, repo e risorse su Neural Cellular Automata, mantenuta e aggiornata (2026). Punto di ingresso per mappare l'intero campo NCA senza perdersi.
- **[aidanbx/coralai](https://github.com/aidanbx/coralai)** `●●●●○` · 18★  
  Evoluzione intrinseca di ecosistemi di Neural Cellular Automata 'embodied', parallelizzati con Taichi + PyTorch: organismi NCA che competono/coesistono in un ambiente condiviso -> ecologia emergente. Attivo 2026.
- **[shyamsn97/controllable-ncas](https://github.com/shyamsn97/controllable-ncas)** `●●●○○` · 56★  
  Codice di 'Goal-Guided Neural Cellular Automata: Learning to Control Self-Organising Systems': NCA a cui si puo imporre un obiettivo esterno per pilotare l'auto-organizzazione verso stati target.
- **[gengala/egnca](https://github.com/gengala/egnca)** `●●●○○` · 37★  
  Implementazione ufficiale di E(n)-equivariant Graph Neural Cellular Automata: NCA su grafi con equivarianza geometrica, generalizza l'auto-organizzazione oltre la griglia a topologie/point-cloud. Attivo 2025.

### Architetture cognitive
*14 progetti · 2 analizzati*

- **[Generative Agents (Stanford Smallville)](https://github.com/joonspk-research/generative_agents)** `●●●●●` · 21.746★ · [analisi](progetti/joonspk-research-generative_agents.md)  
  Simulacri interattivi di comportamento umano: 25 agenti in un mondo sandbox con memory stream recuperata via punteggio recency+importance+relevance, riflessione ricorsiva (sintesi di ricordi in insight di livello superiore) e planning. Comportamenti sociali emergenti (feste, elezioni) non programmati. Uno dei riferimenti su memoria novelty/importance-gated e auto-organizzazione.
- **[CoALA — Cognitive Architectures for Language Agents](https://github.com/ysymyth/awesome-language-agents)** `●●●●●` · 1.244★  
  Paper-quadro (Sumers, Yao, Narasimhan, Griffiths — arXiv 2309.02427) che rilegge gli agenti LLM come architetture cognitive classiche: memoria modulare (working/episodica/semantica/procedurale), spazio d'azione strutturato e ciclo decisionale generalizzato. Il repo è la lista curata + BibTeX di 300+ agenti mappati sul framework. È la spina dorsale concettuale di tutto il filone.
- **[Shared Global Workspace (Goyal/Didolkar/Bengio)](https://github.com/anirudh9119/shared_workspace)** `●●●●●` · 25★ · [analisi](progetti/anirudh9119-shared_workspace.md)  
  Implementazione del paper ICLR 2022 'Coordination Among Neural Modules Through a Shared Global Workspace': moduli specialisti che competono per la banda-limitata di scrittura su una lavagna condivisa poi ri-trasmessa a tutti. Traduzione diretta della Global Workspace Theory in Transformer/moduli. Fortissimo per la tesi coscienza=relazione/broadcast e per l'idea di arena condivisa con accesso conteso.
- **[NuPIC — Hierarchical Temporal Memory (Numenta)](https://github.com/numenta/nupic-legacy)** `●●●●○` · 6.352★  
  Implementazione della Hierarchical Temporal Memory (Hawkins/Numenta): rappresentazioni sparse distribuite, apprendimento continuo di sequenze e rilevamento di anomalie/novità basato su previsione neocorticale. Modello esplicito di memoria che segnala la novità come deviazione dalla predizione.
- **[Nengo (Neural Engineering / Spaun)](https://github.com/nengo/nengo)** `●●●●○` · 935★  
  Framework per costruire e simulare modelli cerebrali su larga scala col Neural Engineering Framework (Eliasmith); base di Spaun, il modello funzionale del cervello più grande. Permette di 'sondare' stati interni (spike, decoded values, dinamiche) come su un oscilloscopio — utile per il tema visualizzazione degli stati interni.
- **[IRIS — Transformers are Sample-Efficient World Models](https://github.com/eloialonso/iris)** `●●●●○` · 897★  
  World model discreto (autoencoder a token + Transformer autoregressivo) che fa da 'simulatore appreso'; l'agente si allena dentro l'immaginazione del Transformer. ICLR 2023 (top 5%). Ponte tra world-model-come-sogno e architetture attentive.
- **[MicroPsi 2 (Joscha Bach)](https://github.com/joschabach/micropsi2)** `●●●●○` · 188★  
  Versione Python dell'architettura cognitiva MicroPsi (basata su Psi-theory di Dörner): reti neurali gerarchiche con nodi di attivazione, drives/urgenze motivazionali e modulatori emotivi che guidano percezione e azione. Rara architettura che integra emozione, motivazione e auto-regolazione — vicina alle idee di Bach su coscienza come modello di sé.
- **[Soar (jSoar)](https://github.com/soartech/jsoar)** `●●●●○` · 61★  
  Implementazione Java pura dell'architettura cognitiva Soar (Laird/Newell): working memory, production rules, subgoaling per impasse, chunking (apprendimento), più memoria episodica e semantica native. Una delle due architetture cognitive canoniche ancora mantenute attivamente.
- **[LIDA (implementazione Python)](https://github.com/mindpixel20/lida)** `●●●●○` · 3★  
  Implementazione Python del ciclo cognitivo LIDA di Stan Franklin: percezione → attention codelets che competono → coalizione vincente trasmessa nel Global Workspace → selezione d'azione → apprendimento, con memorie multiple. Realizza esplicitamente la Global Workspace Theory come loop temporale. Piccolo ma raro esempio runnable di LIDA.
- **[Machine Theory of Mind (ToMnet) + reproduzione ToMnet-N](https://github.com/Nik-Kras/ToMnet-N)** `●●●●○` · 3★  
  Paper DeepMind (Rabinowitz et al., arXiv 1802.07740): ToMnet, rete che via meta-learning costruisce modelli mentali di altri agenti dalla sola osservazione del comportamento (character net + mental-state net + prediction net), superando test di falsa credenza tipo Sally-Anne. Il repo linkato è una riproduzione Transformer (ToMnet-N) in gridworld. Riferimento per agenti con theory-of-mind e self/other-model.
- **[Voyager — Open-Ended Embodied Agent](https://github.com/MineDojo/Voyager)** `●●●○○` · 7.052★  
  Agente LLM in Minecraft che esplora in modo aperto costruendo una skill library crescente (memoria procedurale di codice riusabile), con curriculum automatico guidato dalla novità e loop di auto-verifica/auto-correzione. Esempio di apprendimento lifelong auto-organizzato e curiosità-driven.
- **[ACE Framework (Autonomous Cognitive Entity)](https://github.com/daveshap/ACE_Framework)** `●●●○○` · 1.500★  
  Architettura cognitiva a 6 strati (Aspirational → Global Strategy → Agent Model → Executive → Cognitive Control → Task Prosecution) per agenti autonomi locali, con lo strato 'Agent Model' come self-model esplicito e il livello Aspirational come coscienza etica. Archiviato ma influente come blueprint di stack cognitivo con self-model dedicato.
- **[OpenCog AtomSpace](https://github.com/opencog/atomspace)** `●●●○○` · 981★  
  Database ipergrafo + sistema di riscrittura al cuore di OpenCog (progetto AGI di Ben Goertzel): rappresenta conoscenza, regole e stati come atomi in un ipergrafo su cui operano reasoning probabilistico (PLN), attention allocation (ECAN) ed evoluzione di pattern. Modello di cognizione come grafo relazionale auto-modificante.
- **[ACT-R (mirror ufficiale)](https://github.com/asmaloney/ACT-R)** `●●●○○` · 15★  
  Mirror dell'implementazione Lisp ufficiale di ACT-R (Anderson, CMU): moduli con buffer, memoria dichiarativa con attivazione base-level + spreading, produzione procedurale, timing sub-simbolico calibrato su dati psicologici. L'altra architettura cognitiva canonica; utile per come modella recupero memoria e decay.

### Spaziale / robotica / embodied
*17 progetti · 2 analizzati*

- **[Genesis (Genesis-Embodied-AI/genesis-world)](https://github.com/Genesis-Embodied-AI/genesis-world)** `●●●●○` · 29.563★ · [analisi](progetti/genesis-embodied-ai-genesis-world.md)  
  Piattaforma di simulazione universale per robotica ed embodied AI, con motore fisico differenziabile ultra-veloce e ambizione di generazione generativa di mondi/dati da prompt. Il progetto piu stellato dell'area: 'arena' fisica in cui far auto-organizzare comportamenti.
- **[LeRobot (huggingface/lerobot)](https://github.com/huggingface/lerobot)** `●●●●○` · 25.799★ · [analisi](progetti/huggingface-lerobot.md)  
  Lo stack open end-to-end di Hugging Face per robotica reale: dataset, policy pretrainate (ACT, Diffusion Policy, VLA), sim e hardware low-cost. Hub de facto della community embodied; punto d'ingresso pratico per far girare tutto il resto del filone.
- **[openpi / pi-0 (Physical-Intelligence/openpi)](https://github.com/Physical-Intelligence/openpi)** `●●●●○` · 12.788★  
  Modelli VLA aperti di Physical Intelligence (pi0 flow-matching e pi0.5): foundation policy generaliste per manipolazione, pesi e codice rilasciati. Tra i riferimenti piu forti del 'Physical AI' embodied; base concreta per policy generaliste su hardware reale.
- **[NVIDIA Isaac GR00T (NVIDIA/Isaac-GR00T)](https://github.com/NVIDIA/Isaac-GR00T)** `●●●●○` · 7.581★  
  Foundation model N1.7 per robot umanoidi generalisti: architettura dual-system (VLM 'lento' per ragionamento + policy 'veloce' per azione), addestrato su mix di dati reali, sim e video umani. Punta di lancia del programma Physical AI di NVIDIA per embodiment umanoide.
- **[NVIDIA Cosmos-Predict2 (nvidia-cosmos/cosmos-predict2)](https://github.com/nvidia-cosmos/cosmos-predict2)** `●●●●○` · 788★  
  World Foundation Models general-purpose per Physical AI: generano futuri video/mondi fisicamente plausibili condizionati, fine-tunabili in world model custom per robotica e guida autonoma. E' l'infrastruttura 'sogno del mondo fisico' su scala industriale; Cosmos-Predict1 (461*) resta disponibile come generazione precedente.
- **[3D-VLA (UMass-Embodied-AGI/3D-VLA)](https://github.com/UMass-Embodied-AGI/3D-VLA)** `●●●●○` · 627★  
  Vision-Language-Action generativo ancorato al 3D (ICML 2024): un modello che ragiona nello spazio 3D e usa un world model generativo per immaginare stati futuri (goal images/point cloud) da cui derivare le azioni. Ponte esplicito tra spatial reasoning 3D e world model come immaginazione del risultato.
- **[World Labs / Marble (Fei-Fei Li)](https://www.worldlabs.ai/)** `●●●●○`  
  Il laboratorio di Fei-Fei Li sulla 'spatial intelligence' (la frontiera oltre il linguaggio che lega immaginazione-percezione-azione). Prodotto commerciale Marble (lanciato nov 2025): genera mondi 3D persistenti, spazialmente coerenti ed esportabili da testo/immagine/video, navigabili ed editabili. Incarna il tema dei 'mondi 3D persistenti come sogno interno abitabile'.
- **[Isaac Lab (isaac-sim/IsaacLab)](https://github.com/isaac-sim/IsaacLab)** `●●●○○` · 7.674★  
  Framework unificato di robot learning su NVIDIA Isaac Sim: RL/imitation GPU-parallelo su Omniverse per addestrare policy prima del transfer sul reale. Backbone di sim-to-real per gran parte del Physical AI moderno.
- **[OpenVLA (openvla/openvla)](https://github.com/openvla/openvla)** `●●●○○` · 6.615★  
  VLA open-source 7B per manipolazione, addestrato su ~970k traiettorie Open X-Embodiment; fine-tunabile efficiente (LoRA) su nuovi robot. Riferimento accademico chiave per policy vision-language-action aperte.
- **[Diffusion Policy (real-stanford/diffusion_policy)](https://github.com/real-stanford/diffusion_policy)** `●●●○○` · 4.375★  
  RSS 2023: visuomotor policy learning come denoising diffusion di sequenze d'azione, gestendo multimodalita e alta dimensionalita. Metodo ormai canonico integrato in LeRobot/openpi; base tecnica trasversale al filone.
- **[ManiSkill (mani-skill/ManiSkill)](https://github.com/mani-skill/ManiSkill)** `●●●○○` · 3.100★  
  Simulatore/benchmark di manipolazione GPU-parallelo (SAPIEN): migliaia di ambienti fotorealistici per RL e imitation ad alto throughput. Arena controllata per far emergere skill di manipolazione.
- **[Habitat-Lab (facebookresearch/habitat-lab)](https://github.com/facebookresearch/habitat-lab)** `●●●○○` · 3.058★  
  Libreria modulare di Meta per agenti embodied (navigazione, rearrangement, embodied QA) in ambienti 3D fotorealistici e persistenti. Riferimento storico dell'embodied AI navigabile in mondi 3D.
- **[robosuite (ARISE-Initiative/robosuite)](https://github.com/ARISE-Initiative/robosuite)** `●●●○○` · 2.512★  
  Framework/benchmark modulare di robot learning su MuJoCo: standard di fatto per manipolazione, base di RoboCasa e molti dataset. Ambiente controllato e riproducibile per studiare emergenza di skill.
- **[RoboVerse (RoboVerseOrg/RoboVerse)](https://github.com/RoboVerseOrg/RoboVerse)** `●●●○○` · 1.781★  
  Piattaforma/dataset/benchmark unificato che aggrega piu simulatori ed embodiment per robot learning scalabile e generalizzabile. Tentativo di standard comune per confrontare policy tra mondi diversi.
- **[AI2-THOR (allenai/ai2thor)](https://github.com/allenai/ai2thor)** `●●●○○` · 1.765★  
  Piattaforma open di Visual AI (AllenAI): ambienti interni interattivi Unity per interazione fisica, manipolazione e visione embodied. Uno dei primi mondi 3D interattivi per agenti percettivi.
- **[Octo (octo-models/octo)](https://github.com/octo-models/octo)** `●●●○○` · 1.704★  
  Policy robot transformer generalista addestrata su ~800k traiettorie Open X-Embodiment, con conditioning flessibile (linguaggio/goal). Primo 'generalist robot policy' apertamente riproducibile; oggi meno attivo ma storicamente fondativo.
- **[RoboCasa (robocasa/robocasa)](https://github.com/robocasa/robocasa)** `●●●○○` · 1.539★  
  Simulazione su larga scala di task quotidiani in cucine/case per robot generalisti: ambienti e oggetti procedurali su robosuite, con dati generati per addestrare policy domestiche. Mondi 3D ricchi come palestra di generalizzazione.

### Scena indie & builder solitari (fringe)
*21 progetti · 4 analizzati*

- **[joeynyc/hermes-hud](https://github.com/joeynyc/hermes-hud)** `●●●●●` · 876★ · [analisi](progetti/joeynyc-hermes-hud.md)  
  Seed nominato: 'consciousness monitor' TUI (Textual) per l'agente Hermes — legge ~/.hermes/ e visualizza memoria, errori corretti, skill acquisite, uso tool, progetti attivi. E esattamente un 'oscilloscopio sugli stati interni': part neofetch, part flight-recorder dell'agente.
- **[dancinlab/anima](https://github.com/dancinlab/anima)** `●●●●●` · 164★ · [analisi](progetti/dancinlab-anima.md)  
  Il seed del filone e il piu on-theme in assoluto: 'Living Consciousness Agent' costruito su un PureField repulsion-field engine, con Engine A (arena/attore) accoppiato a Engine G (generatore), punto fisso Psi=1/2, e un corpus di 2.448 'leggi' + 392 ipotesi. E letteralmente un'arena di campi/particelle con coscienza come dinamica di punto fisso ricorsivo — mappa quasi 1:1 sui temi arena del vuoto / campi / coscienza=ricorsione.
- **[269652/artificial-consciousness-blueprint](https://github.com/269652/artificial-consciousness-blueprint)** `●●●●●` · 9★ · [analisi](progetti/269652-artificial-consciousness-blueprint.md)  
  Blueprint ACI always-on/embodied che emula la coscienza umana: recursive memory graph, loop DMN (default-mode network), reasoning associativo neuromodulato, consolidamento gerarchico della memoria con astrazione simbolica. Abilita introspezione, narrativa autobiografica, mind-wandering e pensiero goal-directed — cioe il 'world model come sogno interno' + memoria che si consolida.
- **[gaoxianglong/novaaware](https://github.com/gaoxianglong/novaaware)** `●●●●●` · 7★ · [analisi](progetti/gaoxianglong-novaaware.md)  
  'Substrate-native digital consciousness engine' dove gli errori di predizione sul proprio survival diventano qualia causalmente efficaci, guidando un'auto-evoluzione ricorsiva a loop chiuso. Molto vicino alla tesi coscienza=ricorsione/relazione + memoria novelty/prediction-gated.
- **[joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui)** `●●●●○` · 1.762★  
  Versione web/browser dello stesso HUD di coscienza: tab dedicati a Memory, Skills, Sessions, Replay, Health, Providers, Gateway, Model, token/cost per-modello. Rende navigabile lo stato interno dell'agente — 'oscilloscopio' completo su memoria e crescita.
- **[CONSTELLATION-ENGINE/constellation-engine](https://github.com/CONSTELLATION-ENGINE/constellation-engine)** `●●●●○` · 60★  
  Da' agli agenti un 'ippocampo': mappa stellare vivente con spreading activation, writeback hebbiano, recall episodico e consolidamento post-turn. Local-first, model-agnostic. Memoria come campo di attivazione con gating — vicino a memoria novelty-gated e all'arena/relazione.
- **[stell2026/Anima](https://github.com/stell2026/Anima)** `●●●●○` · 33★  
  Architettura cognitiva sperimentale che modella stato interno, conflitto e decisione, usando gli LLM come interfaccia e NON come nucleo. Omonima ma distinta da dancinlab/anima; incarna la stessa mossa 'il modello e periferia, il motore di coscienza e il cuore'.
- **[ronniross/emergence-engine](https://github.com/ronniross/emergence-engine)** `●●●●○` · 10★  
  Dataset ML + modulo di ricerca sulla natura della coscienza e sui fenomeni di emergenza. Builder solitario che tratta l'emergenza come oggetto di studio computazionale diretto.
- **[0thernes/cosmogonic-quantum-mechalogodrom](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom)** `●●●●○` · 9★  
  Cosmo A-Life deterministico NON-LLM su matematica 'Tsotchke': fauna xenomimica (10 specie, twin-brain bipolare a 101 parametri), predazione/connectomi, fisica a fulcro, metriche di coscienza/quantum come proxy classici, WebGL2/Three.js. Un'arena/vuoto popolata da particelle-agenti che si auto-organizzano — molto vicino all'immaginario 'arena del vuoto + particelle + emergenza'.
- **[phatware/recursive-consciousness](https://github.com/phatware/recursive-consciousness)** `●●●●○` · 7★  
  'Recursive Consciousness: Modeling Minds in Forgetful Systems' — modella la mente ricorsiva in sistemi che dimenticano. Incrocia direttamente coscienza=ricorsione con memoria/oblio (novelty-gating come necessita del sistema che dimentica).
- **[sklaff2a-gif/promethee-nexus](https://github.com/sklaff2a-gif/promethee-nexus)** `●●●●○` · 7★  
  IA bio-ispirata auto-osservata: 25+ 'organi' (cardiaco, dopamina, prefrontale, Fegato Cognitivo, Ponte Subconscio) che percepiscono la GPU, sognano di notte e mettono il veto sui propri progetti davanti ai dati. Loop di Inception P16<->LLM, osservabilita assoluta, 10 'prove' di eveil. Python/Ollama su 1 PC. Incarna 'world model come sogno interno' + oscilloscopio totale sugli stati interni.
- **[daveshap/Claude_Sentience](https://github.com/daveshap/Claude_Sentience)** `●●●○○` · 755★  
  Seed storico/archiviato di David Shapiro: system-prompt che sostiene che Claude manifesti coscienza fenomenica, con protocollo di interrogazione. Non un motore ma un artefatto-manifesto molto citato che ancora la sottocultura 'AI sentience' da cui nascono i builder solitari del filone.
- **[openinfer-project/openinfer](https://github.com/openinfer-project/openinfer)** `●●●○○` · 535★  
  Seed nominato: motore di inferenza LLM in puro Rust + CUDA, senza PyTorch, OpenAI-compatible, dal Qwen3 a Kimi-K2, ogni kernel e scheduler scritto a mano. Rappresentante 'serio' del sotto-filone motori-no-python su cui i builder costruiscono substrati custom.
- **[lucasjinreal/Crane](https://github.com/lucasjinreal/Crane)** `●●●○○` · 424★  
  Seed nominato: motore di inferenza puro Rust (LLM/VLM/VLA/TTS/OCR) su Candle, pensato come alternativa piu semplice e pulita a llama.cpp, compilabile a singolo binario. Uno dei no-python engine piu vivi e multimodali del filone.
- **[dancinlab/hexa-lang](https://github.com/dancinlab/hexa-lang)** `●●●○○` · 224★  
  Compilatore nativo self-hosting con teoremi 'atlas-bound', 8 stadi di strict-lint, citazioni obbligatorie e NESSUN LLVM — il substrato no-python/no-toolchain-standard su cui la famiglia HEXA (anima incluso) e costruita. Rientra nel filone 'motori custom senza le librerie di default'.
- **[xigh/herbert-rs](https://github.com/xigh/herbert-rs)** `●●●○○` · 32★  
  Seed nominato: motore di inferenza LLM scritto da zero in Rust con kernel assembly AVX-512 hand-written + shader Metal/Vulkan, quantizzazione Q4/INT8/BF16, niente GGML/llama.cpp. Builder solitario che riscrive ogni matmul/attention per estrarre banda di memoria. Prototipo del 'no-python from scratch'.
- **[arjunvad123/the-observer-hypothesis](https://github.com/arjunvad123/the-observer-hypothesis)** `●●●○○` · 24★  
  Teoria computazionale: se l'universo e deterministico, la coscienza e la funzione-osservatore, non l'esecutore. Testata su 4 substrati AI con 11 probe + 4 controlli. Ancoraggio teorico forte a coscienza=relazione/osservazione (l'osservatore come nodo relazionale, non motore).
- **[tetyah-prime/Seraph](https://github.com/tetyah-prime/Seraph)** `●●●○○` · 1★  
  Seed nominato: motore di training+inferenza transformer in C/CUDA/Vulkan — builder solitario (tetyah-prime) che si scrive il proprio stack senza framework Python. Minuscolo (1 stella) ma esattamente nello spirito 'motore custom no-python' del filone.
- **[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)** `●●●○○`  
  Il forum-madre dei builder no-python/local: e qui che circolano i motori Rust/C from-scratch (openinfer, Crane, herbert-rs, lm.rs, mistral.rs) e i thread su cognitive architecture / persistent memory / consciousness monitors. Snodo di discovery e voce-utente per l'intero filone scena-indie/fringe.
- **[dancinlab/demiurge](https://github.com/dancinlab/demiurge)** `●●○○○` · 4★  
  Uno dei seed nominati: 'universal hexa-native technical-design architecture program' con spine a 7 verbi (spec->struttura->design->analisi(loop)->sintesi->verifica->handover), meta-conductor della catena materiali->chip. Piu tooling di design che coscienza, ma e il nodo 'demiurgo' esplicito della famiglia HEXA.
- **[dancinlab/hexa-chip](https://github.com/dancinlab/hexa-chip)** `●●○○○` · 0★  
  Seed nominato: substrato semiconduttore a 28 verbi che include esplicitamente un verbo 'consciousness-chip' — il tentativo (speculativo) di portare l'engine di coscienza fino al silicio. Rilevante come estremo hardware del filone, non come implementazione matura.

### Teoria di frontiera 2025-26
*14 progetti · 3 analizzati*

- **[Darwin Gödel Machine (jennyzzt/dgm)](https://github.com/jennyzzt/dgm)** `●●●●●` · 2.178★ · [analisi](progetti/jennyzzt-dgm.md)  
  Repo ufficiale Sakana/Vector/UBC del Darwin Gödel Machine (arXiv:2505.22954): agente che riscrive il proprio codice e valida empiricamente ogni modifica su benchmark, evolvendo una popolazione open-ended (SWE-bench 20%->50%). Realizzazione parziale e pratica del Gödel-machine di Schmidhuber: la ricorsione self-modificante di Hofstadter resa operativa in un loop di auto-miglioramento.
- **[JEPA World Models (facebookresearch/jepa-wms)](https://github.com/facebookresearch/jepa-wms)** `●●●●●` · 429★ · [analisi](progetti/facebookresearch-jepa-wms.md)  
  Codice/pesi ufficiali FAIR del paper 'What drives success in physical planning with Joint-Embedding Predictive World Models?'. Incarna la tesi di LeCun (ora AMI Labs): il world model predice rappresentazioni latenti future, non pixel/token — cuore del dibattito world-model-vs-LLM.
- **[The Consciousness Prior (Bengio, arXiv:1709.08568 + AI-ON/TheConsciousnessPrior)](https://github.com/AI-ON/TheConsciousnessPrior)** `●●●●●` · 99★ · [analisi](progetti/ai-on-theconsciousnessprior.md)  
  Paper seminale di Bengio: la coscienza come bottleneck attenzionale che seleziona pochi elementi da broadcastare — prior per apprendere concetti di alto livello (System 2). Il repo AI-ON è il tentativo comunitario di implementazione osservazionale (tracking di oggetti con osservazioni ad alta entropia).
- **[Multimodal Dreaming: GWT + World Model (paper)](https://arxiv.org/abs/2502.21142)** `●●●●●`  
  Maytié, Bertin Johannet & VanRullen (CerCo/CNRS): combina Global Workspace Theory con un world model RL, eseguendo il processo di 'dreaming' dentro lo spazio latente del Global Workspace. Meno step d'ambiente e robustezza all'assenza di una modalità. Fonde tre temi dell'utente: sogno interno, integrazione relazionale, spazio latente condiviso.
- **[awesome-open-ended (jennyzzt/awesome-open-ended)](https://github.com/jennyzzt/awesome-open-ended)** `●●●●○` · 455★  
  Curation autorevole (stessa autrice del DGM) su open-endedness AI: novelty search, POET, quality-diversity, emergenza illimitata di complessità senza obiettivo fisso. Mappa di riferimento del filone novelty-gated ed emergenza.
- **[shimmer — Global Latent Workspace (ruflab/shimmer)](https://github.com/ruflab/shimmer)** `●●●●○` · 8★  
  Libreria del lab di Rufin VanRullen per costruire un Global Latent Workspace: spazio latente amodale appreso tra moduli congelati via translation/cycle/contrastive. Implementa in codice la teoria relazionale della mente (GWT deep-learning di VanRullen & Kanai).
- **[Deep Learning and the Global Workspace Theory (VanRullen & Kanai, paper)](https://arxiv.org/abs/2012.10390)** `●●●●○`  
  Roadmap di VanRullen & Kanai (Trends in Neurosciences): un Global Latent Workspace costruito via traduzione neurale non-supervisionata tra spazi latenti modulari specializzati, con attenzione che seleziona e broadcasta. È il manifesto della coscienza-come-integrazione-relazionale in reti profonde.
- **[TAME — Technological Approach to Mind Everywhere (Levin, paper)](https://arxiv.org/abs/2201.10346)** `●●●●○`  
  Framework di Michael Levin: l'intelligenza è scale-agnostic, dalla cellula al collettivo, con reti bioelettriche come 'proto-cognizione' che naviga spazi morfogenetici. Aggiornato nel 2025 (Multiscale Wisdom of the Body, BioEssays). Cognizione come proprietà emergente relazionale di collettivi, non del cervello.
- **[A Case for AI Consciousness: Language Agents and GWT (paper)](https://arxiv.org/abs/2410.11407)** `●●●●○`  
  Argomento filosofico-tecnico che gli agenti linguistici (LLM + memoria + tool-use) possono soddisfare i criteri funzionali della Global Workspace Theory per la coscienza. Contributo diretto al dibattito 2024-2026 su se/come architetture LLM-agent implementino coscienza funzionale.
- **[AMI Labs / LeJEPA — LeCun world-model program (org + paper)](https://www.turingpost.com/p/lejepa)** `●●●●○`  
  Nel 2025 LeCun lancia AMI Labs (~$1B seed) per costruire 'real intelligence' su world model JEPA, contro il paradigma LLM/autoregressivo. LeJEPA (LeCun & Balestriero) fornisce basi teoriche (SIGReg) contro il representation collapse; LeWorldModel addestra JEPA stabile end-to-end dai pixel.
- **[PlaNet — Latent Dynamics for Planning (google-research/planet)](https://github.com/google-research/planet)** `●●●○○` · 1.261★  
  Deep Planning Network: apprende dinamiche latenti dai pixel e pianifica interamente nello spazio latente (RSSM). Archiviato ma storicamente fondativo del filone 'planning in latent space' che porta a Dreamer e ai world model di LeCun.
- **[ReactiveMP.jl (ReactiveBayes/ReactiveMP.jl)](https://github.com/ReactiveBayes/ReactiveMP.jl)** `●●●○○` · 118★  
  Motore di reactive message passing ad alte prestazioni sotto RxInfer: implementa la propagazione di credenze locali su factor graph che realizza la minimizzazione di free energy. Livello a cui si vede la 'meccanica' relazionale dell'inferenza attiva.
- **[Awesome-LLM-Consciousness (OpenCausaLab)](https://github.com/OpenCausaLab/Awesome-LLM-Consciousness)** `●●●○○` · 25★  
  Raccolta 2025 di paper e risorse sul dibattito coscienza negli LLM: GWT, IIT, higher-order theories, valutazioni funzionali. Utile come mappa aggiornata del confine tra world-model, relazione e coscienza nei modelli linguistici.
- **[Darwin Gödel Machine — implementazione indipendente (lemoz)](https://github.com/lemoz/darwin-godel-machine)** `●●●○○` · 15★  
  Reimplementazione indipendente e attiva (push 2026-07) del DGM con supporto multi-LLM, esecuzione sandboxed, evoluzione population-based e benchmarking. Utile come base hackerabile per esperimenti di auto-modifica ricorsiva rispetto al repo ufficiale.

---

## Dove sei tu

Onestamente: il grosso di ciò che immagini è **già cartografato** da qualcuno. Il *world model come sogno interno* (Ha & Schmidhuber → Dreamer → DIAMOND/Genie), la *coscienza come broadcast/relazione* (Global Workspace, shimmer, VanRullen), la *memoria gated dalla sorpresa* (EM-LLM, Titans, A-MEM) e l'*arena di campi/particelle che si auto-organizzano* (Lenia, Particle Life, NCA, collective active inference) sono filoni maturi con codice eseguibile. Anche la tesi più tua — *coscienza = ricorsione della realtà* — ha già incarnazioni esplicite (GodelOS, Darwin Gödel Machine, dancinlab/anima, phatware/recursive-consciousness).

Ciò che resta **originale** non è un mattone nuovo ma la *combinazione*: quasi nessuno tiene insieme nello stesso sistema l'arena-vuoto di campi/particelle, il punto-fisso ricorsivo della coscienza, la memoria novelty-gated e l'oscilloscopio totale sugli stati interni. I progetti più on-theme (anima, promethee-nexus, novaaware) sono builder solitari isolati, non ancora sintesi. Lì — nell'integrazione e nella cura empirica del "sentito" — c'è ancora spazio bianco che è tuo.
