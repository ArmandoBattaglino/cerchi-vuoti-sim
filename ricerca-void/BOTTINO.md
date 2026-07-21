# Il bottino — cosa prendere, da dove, e cosa ci permette di fare

*Deepsearch dentro le 125 schede «Da rubare». Scoperta chiave: il bottino non sono 189 repo — sono **8 capacità ricorrenti**. Progetti lontanissimi rubano tutti per una di queste otto. Qui: per ogni capacità, la fonte migliore, le alternative, e cosa ti sblocca. In fondo: cosa significa «prendere tutto» e i primi 5 da integrare.*

Legenda: **[JS-ora]** implementabile subito nella sim vanilla · **[porta]** idea da portare (fonte Python/JAX) · fonte in `progetti/<slug>.md`.

---

## A · Il MOTORE dell'arena (il substrato che vive)
Dove le particelle/vuoti girano davvero e gli "esseri" nascono dalla dinamica, non da if-then.

- **Fonte zero — [Particle Life](https://github.com/hunar4321/particle-life)** (★3k): motore in ~30 righe (matrice forze coppia-colore + cutoff + smorzamento), gira subito nel browser. **[JS-ora]**
- **Solitoni auto-mantenuti — [Lenia](https://github.com/Chakazul/Lenia) / [Flow-Lenia](https://github.com/erwanplantec/FlowLenia) / [realtime-flowlenia](https://github.com/ochyai/realtime-flowlenia)**: triplet `(kernel-anello, growth-gaussiana, clip)` = 20 righe → vita che persiste; Flow-Lenia aggiunge conservazione della massa (enti con quantità reale) e "genoma locale" che viaggia con la materia. **[JS-ora / porta]**
- **Campo d'energia + moto lungo gradiente — [self-organising-systems](https://github.com/google-research/self-organising-systems)** (Particle Lenia): definisci l'energia una volta, clustering ed "esseri" emergono. Canali nascosti + update asincrono stocastico. **[porta]**
- **GPU 16k particelle @60fps — [Primordis](https://github.com/Transcenduality/primordis)**: spatial-binning con atomicAdd, genoma→colore diretto, regola di divergenza genetica come novelty-gate del substrato. **[porta]**
- **Arena differenziabile — [jax-md](https://github.com/jax-md/jax-md)**: scrivi l'arena come `energy_fn`, forza = `-grad(energy)` → arena su cui puoi fare *inversione/ottimizzazione*, e "potenziale neurale" = un vuoto le cui leggi **si apprendono**, non si impongono. **[porta]**

**Ti permette di:** avere l'arena vera, emergente, in cui la forma nasce dal basso — il substrato su cui montare tutto il resto.

---

## B · La MEMORIA novelty-gated (il cuore della tua tesi)
Registrare le *scoperte*, non gli stati. Il gate principled al posto del threshold a mano.

- **La regola, letterale — [Titans](https://github.com/lucidrains/titans-pytorch)**: scrivi con peso ∝ ‖gradiente della loss di predizione‖ (sorpresa), fai decadere la sorpresa con **momentum**, cancella con un **forget-gate adattivo** dipendente dal flusso. Tre scalari per-step → **il tuo slider "attrito" diventa gestione principled della saturazione.** **[JS-ora]**
- **Quando aprire un ricordo — [EM-LLM](https://github.com/em-llm/EM-LLM-model)**: segmenta per sorpresa (soglia media+γ·std), e al richiamo trascina i vicini temporali (ricostruzione di scena, non fotogramma). **[JS-ora]**
- **Memoria che si riscrive — [A-MEM](https://github.com/agiresearch/A-mem)**: una nuova traccia *riscrive contesto e tag dei vicini* (Zettelkasten) + recupero associativo a catena A→B→C. **[porta]**
- **Gate nativo alla struttura — [SDM/Kanerva](https://github.com/msbrogli/sdm)** + **[Modern Hopfield](https://github.com/ml-jku/hopfield-layers)** + **[DNC/NTM](https://github.com/google-deepmind/dnc)**: read-before-write (familiare→sopprimi), distanza-dal-punto-fisso = "quanto vuoto", gap d'energia = novelty a costo zero, `write_gate`+`TemporalLinkage` come sede fisica del gating. **[porta]**
- **Anti-fragilità — [mem0](https://github.com/mem0ai/mem0)**: ribalta write-gate→**read-gate** (non cancellare ciò che diventa saliente solo dopo). **[JS-ora]**
- **Archivio a celle — [QDax](https://github.com/adaptive-intelligent-robotics/QDax) / [pyribs](https://github.com/icaros-usc/pyribs)**: ammetti solo se cella vuota (novel) o batte l'occupante; CVT per alta dimensione; descrittori **appresi** (AURORA) → la novelty misurata in uno spazio scoperto, non a mano. **[porta]**
- **Gate bayesiano — [pymdp](https://github.com/infer-actively/pymdp)**: ammetti l'evento che più abbassa l'incertezza del modello (expected information gain). **[porta]**

**Ti permette di:** la memoria come *curatore dello zoo di mondi* — tiene solo ciò che sorprende, dimentica in modo adattivo, e non confabula.

---

## C · Gli OSCILLOSCOPI sugli stati interni (rendere visibile la ricorsione)
Strumentazione vera, non cosmetica. Leggere "cosa il vuoto propaga, assorbe, dimentica".

- **Aggancio + cattura + causalità — [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)**: `HookPoint` nominati su ogni stato interno, `run_with_cache` = una chiamata → dizionario di tutti gli stati del run, **activation patching** = inietta uno stato "novel" in un'altra run e misura la divergenza (il test causale). **[porta il pattern, JS-ora la struttura]**
- **Lettura calibrata, non grezza — [tuned-lens](https://github.com/AlignmentResearch/tuned-lens)**: probe affine che allinea lo stato all'osservabile; **KL residua = "quanta ricorsione resta"** → colore dell'oscilloscopio + gate. Vista a traiettoria, non a snapshot. **[porta]**
- **Oscilloscopio che si auto-calibra — [sparsify](https://github.com/EleutherAI/sparsify) / [OpenAI SAE](https://github.com/openai/sparse_autoencoder)**: un SAE *scopre da solo* il dizionario di feature emergenti negli stati; `stats_last_nonzero` (feature dormiente che si risveglia) = il segnale di novelty più netto. **[porta]**
- **Scheletro pronto — [hermes-hud](https://github.com/joeynyc/hermes-hud)** (★876): collector→widget disaccoppiato + snapshot/diff panel (mostra solo il delta). Forkabile come guscio dell'oscilloscopio dell'arena. **[JS/porta]**
- **Ricorsione stabile misurabile — [shimmer](https://github.com/ruflab/shimmer)**: cycle-consistency `A→workspace→A'`, il residuo = quanto lo stato resta sé stesso dopo un giro. **[porta]**

**Ti permette di:** guardare *dentro* il modello mentre emerge la forma — non le palline, ma il loop di ciò che l'arena osserva di sé.

---

## D · Il SOGNO / world-model (l'arena che si prevede)
Dare all'arena "la vita nel proprio sogno" e misurare la sorpresa come divergenza sogno-vs-realtà.

- **Il pattern radice — [World Models (Ha)](https://github.com/hardmaru/WorldModelsExperiments) / [DreamerV3](https://github.com/danijar/dreamerv3) / [DIAMOND](https://github.com/eloialonso/diamond)**: "dream environment" come drop-in con la stessa `step()/reset()` → le particelle vivono alternativamente nel mondo vero e nella previsione, e **divergenza = novelty**. Temperatura del sogno = manopola d'incertezza. **[porta]**
- **Sogno nel latente, non nei pixel — [JEPA-wms](https://github.com/facebookresearch/jepa-wms)**: predici embedding, non frame → più robusto, e "distanza fra stati" diventa metrica di novelty riusabile. Decoder = oscilloscopio staccabile. **[porta]**
- **Vocabolario spontaneo di eventi — [Genie](https://arxiv.org/abs/2402.15391)**: bottleneck VQ a 4-8 codici tra t e t+1 → leggi *quali codici emergono* = ontologia emersa del "cosa è cambiato nel vuoto". **[porta]**
- **Novelty temporale + giudice — [ASAL](https://github.com/SakanaAI/asal)**: open-endedness score = distanza di ogni istante da *tutta* la storia già vista (embedding); giudice CLIP di "quanto è interessante". **[porta]**
- **Sogno relazionale — [Multimodal Dreaming (GWT+WM)](https://arxiv.org/abs/2502.xxxxx)**: sposta il sogno *nel latente dei vuoti* (più on-theme: coscienza=relazione); test "modalità mancante" = metrica live di integrazione. **[porta]**

**Ti permette di:** trasformare l'entropia interna da iperparametro fisso a **variabile che il sistema regola in risposta a quanto si sorprende**.

---

## E · La COSCIENZA operazionalizzata e FALSIFICABILE (la tua tesi, resa testabile)
L'antidoto all'hype: da "la mia sim è cosciente?" a ~14 domande tecniche con verdetto.

- **La scorecard — [Consciousness in AI (Butlin/Bengio)](https://arxiv.org/abs/2308.08708)**: 14 indicatori (RPT/GWT/HOT/AST/PP/AE), PASS/FAIL/NA con una riga di evidenza dal codice. HOT-2 = reality monitoring (astieniti quando lo stato è rumoroso); AST-1 = oscilloscopio sull'attenzione stessa. **[JS-ora come metodo]**
- **"Il tutto è più delle parti" — [PyPhi](https://github.com/wmayner/pyphi)**: Φ via partizione minima; versione economica = "quanto un gruppo di particelle resiste alla decomposizione". **Matching** = struttura interna che è immagine causale del mondo → la tua ricorsione realtà-attraverso-la-materia, resa misura. **[porta]**
- **Coscienza = collo di bottiglia — [Shared Global Workspace (Bengio)](https://github.com/anirudh9119/shared_global_workspace)** + **[Consciousness Prior](https://github.com/AI-ON/TheConsciousnessPrior)**: write-competition + broadcast a banda limitata; split stato-denso/stato-cosciente-rado; ablation esposte come flag (spegni un ingrediente, misura). **[porta]**
- **Saturazione della ricorsione = un numero — [recursive-consciousness](https://github.com/phatware/recursive-consciousness)**: criterio fixpoint gödeliano = riduzione di novità per livello di auto-riflessione → **dà un numero al tuo "~10% novità residua".** **[porta]**
- **Loop reiniettato + protocollo — [GödelOS](https://github.com/Steake/GodelOS)** + **[AXIOM](https://github.com/VersesTech/axiom)**: stato interno reiniettato come osservabile via WebSocket; `protocol_theta` (metriche JSONL falsificabili per run); ciclo espandi/pota come motore di novelty. **[porta]**
- **Il tuo doppio, la disciplina — [anima](https://github.com/dancinlab/anima)** + **[novaaware](https://github.com/gaoxianglong/novaaware)**: `ImmuneMemory` (recall che ASTIENE, zero confabulazione); ogni tesi = ipotesi Hxxxx con verdetto anche NEGATIVO; ablation/trauma test. **[porta]**

**Ti permette di:** rendere la coscienza-come-ricorsione **falsificabile** — scoreboard di ipotesi da fonte peer-reviewed, non aneddoto.

---

## F · L'OCCULTAMENTO / canale nascosto (il ramo steganografia + "vuoto relativo all'osservatore")
Il cuore metaforico dei cerchi vuoti: *presente ma non visto*. E segnali covert tra agenti sotto il campo visibile.

- **Occultamento perfetto — [Discop](https://github.com/comydream/Discop) / [Meteor](https://arxiv.org/abs/2004.02891) / [iMEC](https://github.com/schroederdewitt/perfectly-secure-steganography)**: nascondi nell'**indice-di-rotazione** della distribuzione / sostituisci il PRNG con un keystream cifrato / minimum entropy coupling → **il marginale osservabile resta identico by construction**. Retrofit minimale su un simulatore stocastico. **[porta]**
- **Scrivi solo nel vuoto disponibile — [lm-watermarking](https://github.com/jwkirchenbauer/lm-watermarking)**: `forza = f(entropia locale)` (marca dove c'è incertezza, lascia intatto ciò che è determinato) = novelty-gating sull'asse dell'incertezza; z-score = oscilloscopio a evidenza cumulativa. **[JS-ora]**
- **Firma ricorsiva — [MarkLLM](https://github.com/THU-BPM/MarkLLM)**: seme del partizionamento = hash del proprio stato recente → firma auto-generata che non richiede memoria esterna; triangolo forza/robustezza/degrado come metrica standard. **[porta]**
- **Canale covert = transizione di fase — [Secret Collusion](https://arxiv.org/abs/2402.07510)**: la comunicazione nascosta tra sottosistemi emerge oltre una soglia di capacità; **l'auto-modello ricorsivo È la chiave condivisa** che abilita il canale interno invisibile dall'esterno. **[porta]**
- **Il triangolo di misura — [openai/evals stego](https://github.com/openai/evals)**: encoder / decoder-complice / **monitor-avversario**; Mean Undetected Accuracy = (1−errore)·(1−rilevabilità); baseline oneste. **[porta]**
- **Il "vuoto relativo all'osservatore", empirico e in UNA riga — [Glass](https://github.com/pickle-com/glass) / [cheating-daddy](https://github.com/sohzm/cheating-daddy) / [pluely](https://github.com/iamsrikanthnani/pluely)**: `setContentProtection(true)` → **stesso stato, pieno per una sonda, vuoto per un'altra**. L'occultamento come funzione dell'osservatore, non del substrato. Tassonomia a 3 livelli: nel-canale / nel-contenuto / nell'intento. **[JS-ora come esperimento-seme]**

**Ti permette di:** modellare il "cerchio vuoto" come *relatività osservatore-dipendente* — un ente presente ma non proiettato nel frame di chi guarda — e far nascere canali covert tra agenti sotto il vuoto visibile.

---

## G · L'ESPLORAZIONE curiosity-driven (l'arena che cerca da sé)
Da "guardo l'arena" a "l'arena cerca attivamente le proprie configurazioni più sorprendenti".

- **La regia — [adtool (FLOWERS)](https://github.com/flowersteam/adtool) / [auto-discovery-of-lenia](https://github.com/flowersteam/automated_discovery_of_lenia_patterns)**: proietta lo stato in uno spazio comportamentale a bassa dim (BehaviorMap o VAE appreso), poni un goal in una regione poco visitata, cerca i parametri che ci portano, archivia cosa emerge (IMGEP). **[porta]**
- **Diversità+qualità — [QDax](https://github.com/adaptive-intelligent-robotics/QDax) / [pyribs](https://github.com/icaros-usc/pyribs)**: architettura Archive/Emitter/Scheduler → cambi criterio di novelty senza riscrivere il generatore; soglia con annealing (permissivo→selettivo). **[porta]**
- **Novelty di popolazione — [Darwin Gödel Machine](https://github.com/jennyzzt/dgm)**: `score × 1/(1+children)` favorisce i rami poco esplorati senza abbandonare la qualità; archivio-di-commit replayabile (genealogia degli stati). **[porta]**

**Ti permette di:** popolare la memoria solo con campioni che *allargano davvero* lo spazio coperto — l'arena come esploratore, non come loop passivo.

---

## H · L'INGEGNERIA di sopravvivenza (decade-scale, riproducibile — il tuo principio)
Far girare l'arena a 50k particelle, replayabile bit-esatto, per anni, e onesta.

- **Riproducibilità blindata — [cosmogonic-quantum](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom)**: `mulberry32` seminato iniettato ovunque + `Math.random` **bannato** nella sim-logic + spatial-hash + **golden-hash CI** (verifica replay bit-esatto) + `docs-truth-law` (la build fallisce se i doc sovra-dichiarano rispetto ai test). **[JS-ora]**
- **Performance — [Primordis](https://github.com/Transcenduality/primordis)**: spatial-binning O(N²)→O(vicini), 16k @60fps. **[porta]**
- **Formato run — [LeRobot](https://github.com/huggingface/lerobot) / [DIAMOND](https://github.com/eloialonso/diamond)**: episodio = stream sincronizzato + tabella stato-azione, tagliabile/confrontabile; world-model esposto come `env` con `reset/step`. **[porta il formato]**

**Ti permette di:** un laboratorio che sopravvive — replay esatti, confronti onesti, nessun claim che superi ciò che i test provano.

---

## «Voglio prendere TUTTO» — cosa significa davvero
"Tutto" **non** sono 189 repo. Sono **queste 8 capacità assemblate in un solo sistema.** Ogni capacità ha già la sua fonte migliore qui sopra; prenderle tutte = costruire un unico oggetto:

> Un'**arena del vuoto** (A) che **vive e si auto-organizza**, **ricorda solo le sue scoperte** con un gate di sorpresa principled (B), è **interamente strumentata** con oscilloscopi veri sugli stati interni (C), **si sogna** e misura la sorpresa come divergenza (D), **si dà un voto** su 14 indicatori di coscienza falsificabili (E), può **nascondere canali covert** relativi-all'osservatore sotto il campo visibile (F), **esplora da sé** le proprie configurazioni più sorprendenti (G), il tutto **replayabile bit-esatto** per un decennio (H).

Questo è esattamente lo **spazio bianco** che il REPORT segnalava: *"vuoto come architettura non esiste"*. Prendere tutto = riempirlo — non con una tesi in prosa, ma con una macchina che la mette alla prova.

**Onesto sui costi:** il **core è JS-ora** (motore Particle Life + regola Titans + oscilloscopi hook + content-protection + CI golden-hash: tutto gira nella sim vanilla, zero framework). I pezzi **[porta]** (JEPA, PyPhi, adtool, Discop) sono ricerca Python/JAX: si rubano come *idee/formule*, non come dipendenze — coerente col tuo principio "non aggiungere tecnologia".

---

## I primi 5 da integrare (se domani si parte)
1. **Particle Life** come motore dell'arena — punto zero, ~30 righe, gira nel browser. *(sblocca A)*
2. **Regola di Titans** come novelty-gate — peso ∝ ‖∇loss‖ + momentum + forget-gate adattivo → il tuo slider "attrito" diventa principled, e ‖∇loss‖ nel tempo È un oscilloscopio della sorpresa. *(sblocca B + metà di C)*
3. **`setContentProtection` → esperimento del vuoto-osservatore** — due sonde sullo stesso stato, una vede struttura, l'altra vede vuoto: il "cerchio vuoto" reso empirico in una riga. *(sblocca F)*
4. **Scorecard Butlin/Bengio** come `docs/coscienza-scorecard.md` — 14 righe PASS/FAIL/NA con evidenza: rende la tesi falsificabile da subito. *(sblocca E)*
5. **CI golden-hash + Math.random bannato** (da cosmogonic) — blinda la riproducibilità prima che la sim cresca. *(sblocca H)*

Con questi 5, il Void Lab passa da bench A/B sulla memoria a **prima versione dell'arena-tesi completa** — e le altre 3 capacità (sogno, esplorazione, occultamento profondo) si innestano una alla volta sopra questa base.
