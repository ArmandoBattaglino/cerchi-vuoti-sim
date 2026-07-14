# ZugaMind — Zuga-Technologies/zugamind

<https://github.com/Zuga-Technologies/zugamind>

**10 stelle · Python (stdlib puro, zero dipendenze) · ultimo push lug 2026 · licenza Apache-2.0**

## Cosa fa

È un "sidecar di cognizione persistente": un processo always-on che sta accanto a un harness di agente (Claude Code, OpenClaw, Codex, Hermes) e lo **sveglia solo quando qualcosa merita attenzione**, invece di svegliarlo a orologio come un cron. Guarda gratis delle sorgenti (API HackerNews, feed RSS, issue GitHub) — nessuna chiamata a modello mentre è idle — fa girare su ciò che vede una **competizione di salienza stile Global Workspace Theory**, e invoca l'harness con un briefing di continuità solo quando un vincitore supera la competizione E passa un gate a budget fail-closed. La tesi economica è netta: "smetti di pagare il tuo agente per svegliarsi e non trovare nulla". In un esperimento pre-registrato (EXP-001, corpus congelato di 229 eventi reali + 10 incidenti piantati) ottiene lo stesso recall/precision del cron con il 43% di invocazioni in meno.

## Come è fatto

Pipeline deterministica: **scanner (percezione)** → ogni `WorkspaceModule.generate_bid()` produce una puntata di salienza → **attention schema** (streak dampening, diversity cap, blind-spot boost, novelty bonus) → **un solo vincitore per ciclo** (selezione pesata `salience**power`) → **broadcast** a tutti i moduli (`on_broadcast()`) → **workspace planner** (vincitore → piano-task breve) → **action gate** fail-closed, budget-clamped, con content-screen + veto umano → **Claude** (o un tier locale gratuito se il task non lo giustifica).

Tre pezzi chiudono l'anello "deciso → l'harness ci sta lavorando": `continuity/journal.py` (log episodico append-only; `build_briefing()` produce un markdown cappato ~4000 char = "perché ti sto svegliando, cosa è successo dall'ultimo risveglio, cosa resta irrisolto"); `act/command_actuator.py` (adapter che scrive il briefing su file temp, sostituisce `{briefing_file}` nell'argv dell'harness, lo lancia come sottoprocesso, rate-limited per ora E per giorno contando dal journal durevole); `stream/runner.py` (loop sempre-attivo; i vincitori in quiet-hours vengono differiti, non persi; `touch PAUSE` ferma tutto). La sicurezza è progettata assumendo che l'agente prima o poi sbaglierà: gate fail-closed, content-screen che blocca prompt-injection/comandi distruttivi/exfil di segreti prima di ogni chiamata pagata, cap di budget mensile in USD, tutto ships disabled/dry-run. `Workspace.get_stats()` restituisce ogni puntata che ha competuto, il vincitore, il secondo, e il self-model dell'attention schema (fuochi recenti, blind spot, stuck-detection, conteggio switch di attenzione).

## Cosa possiamo notare di utile per noi

Questo è il ramo **novelty-gating + Global Workspace** nella sua forma più pragmatica e onesta, ed è pieno di meccanica trasferibile alla tua memoria novelty-gated e ai tuoi oscilloscopi:

- **Gating della salienza senza LLM, misurato non dichiarato.** La competizione di salienza è pura matematica deterministica: puntate, selezione `salience**power`, e — cruciale — **habituation** (un trigger già visto viene smorzato per ore, `ZUGAMIND_HABITUATION_HOURS`) e **novelty bonus**. Questo È novelty-gating: il segnale entra nel workspace solo se è nuovo *e* out-competes tutto il resto in questo ciclo. È esattamente il meccanismo che ti serve per decidere quando un'esperienza merita di entrare in memoria, implementato come priority-queue con decadimento e non come flag LLM. Loro stessi lo ammettono onestamente: "se preferisci leggerlo come una coda a priorità con decay e rate-limit, funziona identico — il vocabolario GWT è la lineage di design, non una pretesa".

- **L'attention schema come oscilloscopio già costruito.** Il "self-model" dell'attention schema (fuochi recenti, blind spot, stuck-detection, switch count) è letteralmente un oscilloscopio sullo stato interno del sistema di attenzione — e persino un accenno di auto-modello (l'attenzione che modella la propria attenzione, un mattoncino di coscienza=ricorsione secondo Graziano). `get_stats()` che espone ogni bid, il vincitore e il runner-up è lo snapshot ispezionabile che vuoi per la tua arena.

- **La disciplina sperimentale è il vero oro.** Predizioni pre-registrate (incluse le due sbagliate pubblicate), baseline contro cron, ogni JSONL grezzo pubblicato, replay ermetico a $0 (`run_exp001.py --smoke`). Per un progetto che fa claim su "coscienza/salienza" questo è il modo di non scadere nell'hype: falsificabile, con controlli. Trasferibile direttamente al tuo lavoro dove il rischio-hype è alto.

- **Blind-spot boost e diversity cap.** L'attention schema forza attivamente attenzione verso sorgenti trascurate e impedisce a una sorgente di monopolizzare i risvegli. È un anti-collasso dell'attenzione utile per la tua arena: evitare che il sistema resti incastrato sullo stesso attrattore.

Dove diverge da te: ZugaMind è un orchestratore di *harness LLM esterni*, non una simulazione di mondo. La "percezione" sono feed RSS/HN, non particelle in un vuoto. Non c'è world-model generativo, non c'è sogno, non c'è fisica interna — la salienza opera su testo del web aperto. La ricorsione è debole (l'attention schema si auto-osserva, ma il sistema non riscrive il proprio mondo).

## Da rubare

- **Il meccanismo di habituation + novelty bonus** come cuore del tuo gate di memoria: un evento visto di recente viene smorzato per un tempo configurabile, un evento nuovo riceve un bonus, e solo il vincitore della competizione entra nel workspace. È novelty-gating deterministico, a costo zero, direttamente trapiantabile sopra la tua arena/particelle per decidere cosa consolidare.
- **Il briefing di continuità cappato** (`build_briefing()`, ~4000 char, "perché sono sveglio / cosa è successo / cosa resta aperto") come formato standard per il risveglio di un agente: orientamento, non rumore. Utile per il tuo mem0 cross-sessione — non riversare tutto, ma un briefing strutturato al risveglio.
- **`get_stats()` + attention-schema self-model** come template dell'oscilloscopio: esporre a ogni ciclo tutte le puntate in competizione, il vincitore, il secondo, i fuochi recenti e i blind spot. È il pannello che rende ispezionabile "cosa è entrato nella coscienza e perché".
