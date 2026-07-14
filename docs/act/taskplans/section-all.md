# Taskplan — Void Lab v1 (sezioni 1–6)

Modalità: /act default autonomo + ultracode (Workflow: implementer → 5 reviewer avversariali → fixer),
poi verifica runtime Playwright fatta dall'orchestratore (lezione arena: il runtime trova ciò che la
revisione statica non vede). Commit atomici per sezione. Gate type: tutti [AUTO] (no --gate);
i task UI sono marcati [UI-GATE] per il test plan della PR, degradati ad [AUTO] in esecuzione.

## Section 1 — Core + Memoria pluggable
- s1/t1 [AUTO] Scaffold void-lab.html col motore arena (rng, field, perceive, metabolismo, sociale).
  AC: file si apre senza errori console; motore gira headless.
- s1/t2 [AUTO] makeMemory('A'|'B') interfaccia unica {write, surprise, size, reset}.
  AC: agente usa solo agent.mem.*; nessun accesso diretto ad array memoria.
- s1/t3 [AUTO] A = novelty-gated (porting fedele: WRITE_S=0.13, VAR_THR=0.0045, MEMCAP=200).
  B = store-all (scrive ogni percetto; cap tecnico alto solo anti-OOM, documentato).
  AC: con B, |mem| cresce ~ogni passo; con A resta ≪.
- s1/t4 [AUTO] Regression guard: goal-agent seed fisso con A ≈ comportamento arena
  (raggiunge il goal; metriche nello stesso ordine di grandezza).
  AC: dist finale < 8 su seed 1337 come in arena.

## Section 2 — Runner + metriche
- s2/t1 [AUTO] runExperiment(cfg)→{reached, steps, memSize, finalDist}. Deterministico.
  AC: due run stesso cfg → oggetti identici.
- s2/t2 [AUTO] pair(cfg)→{A, B, delta}. Stesso seed/mondo/innate per entrambi.
  AC: A e B differiscono solo per memory kind.
- s2/t3 [AUTO] noise parametrico in cfg.run. AC: noise=0 e 0.12 → risultati diversi.
- s2/t4 [AUTO] window.__runExperiment/__pair. AC: chiamabili headless, JSON-serializzabili.

## Section 3 — Sweep + curve
- s3/t1 [AUTO] sweep(cfg)→[{value, A:{...}, B:{...}}] su param configurabile (noise default).
  AC: 10 punti in <60s; array coerente.
- s3/t2 [UI-GATE] Plotter Canvas: 2 curve (A teal, B arancione), assi, legenda, metrica selezionabile.
  AC: curva visibile e leggibile per steps e memSize.
- s3/t3 [AUTO] window.__sweep. AC: headless ok.

## Section 4 — UI del banco
- s4/t1 [UI-GATE] Layout 3 zone: arena live · config (seed, rumore, maxSteps, memoria A/B/pair,
  parametro sweep) · risultati (tabella verdetto + plot). Stile fosforo coerente.
- s4/t2 [UI-GATE] Run → esegue pair, riempie tabella verdetto (passi, |mem|, raggiunto, delta).
- s4/t3 [UI-GATE] Sweep → esegue sweep, disegna curve, mostra sintesi ("A vince su N/10 punti").
- s4/t4 [AUTO] Render live durante run osservata (arena + agente + scia).
  AC per tutti: nessun errore console; interazioni funzionanti via Playwright.

## Section 5 — Persistenza + export
- s5/t1 [AUTO] Save/Load esperimento JSON (textarea/download+file input).
  AC: load(save(cfg)) → run identica (stessi numeri).
- s5/t2 [AUTO] Export CSV dei risultati sweep + snapshot PNG del plot.
  AC: CSV parsabile con header; PNG non vuoto.

## Section 6 — Test canonico + verifica
- s6/t1 [AUTO] Bottone "Test canonico": corre pair su seed 1337, mostra verdetto e PASS/FAIL
  vs attese registrate. AC: esito visibile, ripetibile.
- s6/t2 [AUTO] Verifica Playwright completa: determinismo, A≠B, sweep→curva, export.
  Fix di ciò che emerge (max 3 iterazioni per finding).

## Decisioni default
- Sweep default: noise 0→0.12, 10 punti.
- B cap tecnico 20000 (anti-OOM), dichiarato in UI.
- Un solo file void-lab.html; arena-vuoto.html intatto.
