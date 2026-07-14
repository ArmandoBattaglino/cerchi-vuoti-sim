# Report di sintesi — la scena attorno al «cerchio vuoto»

*Sintesi narrativa della ricerca. La mappa completa (225 progetti) è in [INDEX.md](INDEX.md); le schede profonde (125) in [progetti/](progetti/). Qui: cosa stanno facendo, cosa conta per noi, e dove siamo noi. Onesto su reale vs hype.*

Metodo: 2 ricerche ultracode (web + GitHub) con ancoraggio obbligatorio (ogni repo confermato con `gh`, ogni claim col web) + verifica avversariale + agente di controllo. **225 progetti mappati, 125 analizzati a fondo, 5 voci false scartate** (attribuzioni errate a Bayne, Astera/Tsao, Anthropic-welfare, Stephen-Fry/Conscium, dettagli Odyssey).

---

## 1. I grandi filoni (cosa stanno facendo)

**World models — il più caldo e capitalizzato.** Tre generazioni convivono: la linea *Dreamer* ([DreamerV3](https://github.com/danijar/dreamerv3), Nature 2025, "l'agente si allena nel proprio sogno"), la scommessa *JEPA* di LeCun ("i world model rimpiazzano gli LLM": [V-JEPA 2](https://github.com/facebookresearch/vjepa2), e **AMI Labs** con seed da 1,03 mld $), e i *world model generativi/interattivi* (Genie 3, [NVIDIA Cosmos](https://github.com/NVIDIA/cosmos) 11k★, World Labs/Marble, [DIAMOND](https://github.com/eloialonso/diamond) che gira una CS:GO dentro un modello a diffusione).

**Coscienza artificiale — da "sì/no" a punteggi di indicatori.** Il documento fondativo è *Consciousness in AI* (Butlin/Bengio 2023, framework a 14 indicatori). Implementazioni per teoria: [PyPhi](https://github.com/wmayner/pyphi) (IIT), [GödelOS](https://github.com/Steake/GodelOS) (ricorsione/strange-loop). Orgs: Conscium, AE Studio, VERSES. *Onesto: molta scienza seria sugli indicatori, ma "AI cosciente" resta per lo più marketing.*

**Inferenza attiva / predictive coding — piccolo ma il più rigoroso.** [pymdp](https://github.com/infer-actively/pymdp), [RxInfer.jl](https://github.com/ReactiveBayes/RxInfer.jl), [ngc-learn](https://github.com/NACLab/ngc-learn), l'Active Inference Institute che standardizza tutto.

**Memoria degli agenti — mercato maturo + le sue radici.** Mercato: [mem0](https://github.com/mem0ai/mem0) (60k★, gating ADD/UPDATE/DELETE/NOOP), knowledge-graph ([cognee](https://github.com/topoteretes/cognee), [Zep](https://github.com/getzep/zep)). Frontiera latente: **[Titans/titans-pytorch](https://github.com/lucidrains/titans-pytorch)** (novelty-gating via *surprise=gradiente* + momentum + forgetting), [EM-LLM](https://github.com/em-llm/EM-LLM-model) (confini episodici via surprise). **Radici (i tuoi progenitori diretti):** [DNC/NTM](https://github.com/google-deepmind/dnc) (memoria indirizzabile), [Modern Hopfield](https://github.com/ml-jku/hopfield-layers) (richiamo per somiglianza), Sparse Distributed Memory di Kanerva.

**Artificial Life / emergenza — il territorio più letterale dell'arena del vuoto.** [Particle Life](https://github.com/hunar4321/particle-life) (motore in ~30 righe, matrice-forze-come-DNA), [Lenia](https://github.com/Chakazul/Lenia)/[Flow-Lenia](https://github.com/erwanplantec/Flowlenia), [ASAL](https://github.com/SakanaAI/asal) (automatizzare la ricerca di vita artificiale con foundation model), Neural Cellular Automata.

---

## 2. «GhostCode», disambiguato (perché non è una cosa sola)

Il nome collide su cose che non c'entrano. Due mondi separati:

- **Mondo 1 — coding.** L'unico *on-theme*: [amitmishrg/ghostcode](https://github.com/amitmishrg/ghostcode) ("ghostcode-cli", **1★**), un **harness minimale forkabile** per agenti di coding (gate PLAN/BUILD, 5 file, sessioni JSONL). Un *kit di dissezione*: un agente reale piccolo dove piazzare un oscilloscopio. Ma gli altri "GhostCode" sono scollegati: [eladlevi013/GhostCode](https://github.com/eladlevi013/GhostCode) (gioco horror 2023), [teamstreamlineapps/ghostcode](https://github.com/teamstreamlineapps/ghostcode) (mirror-fantasma di OpenCode, un solo commit e abbandonato).
- **Mondo 2 — "invisibile/Cluely".** Overlay che **si nascondono dallo screen-share** per farti arrivare risposte di nascosto a colloqui/meeting: [Glass](https://github.com/pickle-com/glass) (7,5k★), [cheating-daddy](https://github.com/sohzm/cheating-daddy) (5,4k★), [interview-coder](https://github.com/ibttf/interview-coder) (4,4k★). **Sono strumenti per barare** — la fama sta qui, il tema-nostro no. Zero coscienza/vuoto.

**Nodo chiave — due sensi di "invisibile":** l'"invisibile" alla Cluely (una finestra che evade lo screen-share, trucco d'interfaccia) è cosa diversa dal "nascosto" della **steganografia** (dati dentro altri dati, indistinguibili). Il tuo vecchio interesse per il "codice nascondibile" era il *secondo* — la scienza vera, non il cheating.

---

## 3. Steganografia / occultamento (il ramo serio del "nascondere")

22 schede. I solidi: [MarkLLM](https://github.com/THU-BPM/MarkLLM) (toolkit unificato di watermarking LLM), [Meteor](https://arxiv.org/abs/2110.07095) / [Discop](https://github.com/comydream/Discop) (steganografia *provabilmente sicura*: nascondi dati nel campionamento del modello, indistinguibile dal testo normale), [lm-watermarking](https://github.com/jwkirchenbauer/lm-watermarking) (il watermark LLM seminale, green/red list sui token), e **[Secret Collusion among AI Agents](https://arxiv.org/abs/2402.07510)** (NeurIPS 2024): agenti che colludono via canali nascosti — l'idea potente per la tua arena (segnali *covert* tra agenti sotto il vuoto visibile).

---

## 4. Dove sei tu (onesto, senza sconti)

Il tuo **doppio pubblico** è [dancinlab/anima](https://github.com/dancinlab/anima): Engine A↔G in tensione, punto fisso Ψ=1/2, `ImmuneMemory` anti-confabulazione — quasi isomorfo alla tua macchina A-B-C. Guardalo prima di rivendicare originalità sull'architettura.

Verdetto: **ogni tuo mattone ha precedenti forti.**
- *Memoria novelty-gated* → affollata (mem0, Titans, EM-LLM) e con radici canoniche (DNC, Hopfield, Kanerva). Resta tuo solo se la novelty è agganciata a una dinamica ricorsiva/relazionale dentro l'arena.
- *Coscienza = ricorsione/relazione* → esiste (GödelOS, strange-loop). Resta tua la **formulazione ontologica** ("ricorsione della realtà *attraverso la materia*").
- *Oscilloscopi su stati interni* → i "monitor" esistono ([hermes-hud](https://github.com/joeynyc/hermes-hud)), ma la metafora *forme d'onda continue di uno stato ricorsivo* (non dashboard di eventi) non l'ho trovata. Potenzialmente distintiva.
- *Arena del vuoto* → "mente nel proprio sogno" È Dreamer/JEPA; le particelle emergenti sono Particle Life/Lenia. **"Vuoto come architettura" non esiste** (verifica negativa): spazio bianco tuo, ma da formalizzare (una matrice d'interazione? un attrattore? una memoria indirizzabile?).

**L'originalità plausibile sta nella combinazione + cornice, non nei mattoni singoli.**

---

## 5. I progetti da guardare per primi

1. **[dancinlab/anima](https://github.com/dancinlab/anima)** — il tuo doppio. `[analisi](progetti/dancinlab-anima.md)`
2. **[Particle Life](https://github.com/hunar4321/particle-life)** — l'arena di particelle in ~30 righe. `[analisi](progetti/hunar4321-particle-life.md)`
3. **[titans-pytorch](https://github.com/lucidrains/titans-pytorch)** — lo stato dell'arte del novelty-gating. `[analisi](progetti/titans-learning-to-memorize-at-test-time.md)`
4. **[GödelOS](https://github.com/Steake/GodelOS)** — coscienza = ricorsione. `[analisi](progetti/steake-godelos.md)`
5. **[Secret Collusion](https://arxiv.org/abs/2402.07510)** — canali nascosti tra agenti. `[analisi](progetti/secret-collusion-among-ai-agents-neurips-2024.md)`

---

## 6. Il ponte col Void Lab (dal teorico al costruito)

Tre cose di questa ricerca si innestano dritte nel Void Lab:
1. **Particle Life** → arena di particelle emergenti dove la *novelty-gate cura lo "zoo di mondi"* (tieni solo le matrici che sorprendono) — misurabile.
2. **ImmuneMemory (anima)** → memoria che *si astiene* invece di fabbricare — la versione anti-confabulazione del tuo gate.
3. **ghostcode-cli** → un agente reale ispezionabile su cui montare gli oscilloscopi.

*Reale vs hype: world model = soldi e risultati veri + molta narrativa da provare; coscienza = ottima scienza sugli indicatori + molto marketing; inferenza attiva = piccola ma seria; memoria novelty-gated = genuinamente affollata; scena indie = vera come cultura, pochissime prove replicabili.*
