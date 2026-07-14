# Plan Sections — Void Lab v1 (banco "memoria A vs B")

Brief: laboratorio-harness per validare l'ipotesi "una memoria relazionale novelty-gated
dà a un agente più potere gestionale con meno storage di una memoria che salva tutto".
Un file nuovo `void-lab.html`, riuso del motore di `arena-vuoto.html`, vanilla JS,
zero dipendenze, deterministico. Spec completa: docs/specs/void-lab-v1.md

Decisione default (documentata): sweep di collaudo = rumore 0→0.12, 10 punti.

## Section 1: Core + Memoria pluggable
**Goal:** motore arena portato in void-lab.html con memoria come modulo commutabile A/B.
**Dipendenze:** nessuna
**Scope:** scaffold file; interfaccia makeMemory(kind); A=novelty-gated (porting), B=store-all;
regression guard (stesso seed → comportamento arena invariato con A).
**Out of scope:** UI nuova, sweep.

## Section 2: Runner + metriche
**Goal:** esperimenti eseguibili e misurabili via codice.
**Dipendenze:** 1
**Scope:** runExperiment(cfg); pair(cfg) A-vs-B stesso seed; rumore parametrico;
metriche passi-al-goal / |memoria| / raggiunto; headless __runExperiment/__pair.
**Out of scope:** grafici.

## Section 3: Sweep + curve
**Goal:** ipotesi → curva con un click.
**Dipendenze:** 2
**Scope:** sweep(param, values); plotter Canvas 2 curve (A vs B); headless __sweep.
**Out of scope:** sweep multi-parametro.

## Section 4: UI del banco
**Goal:** il laboratorio usabile da Armando senza codice.
**Dipendenze:** 2 (3 per il plot)
**Scope:** layout arena+config+risultati; controlli (memoria A/B/pair, rumore, seed, maxSteps);
Run → tabella verdetto; Sweep → curva; render live della run.
**Out of scope:** patch-bay universale, docking.

## Section 5: Persistenza + export
**Goal:** esperimenti riproducibili e portabili.
**Dipendenze:** 4
**Scope:** save/load esperimento JSON; export CSV risultati; snapshot PNG.
**Out of scope:** cloud, condivisione.

## Section 6: Test canonico + verifica headless
**Goal:** il verdetto A-vs-B diventa test ripetibile; tutto verificato a runtime.
**Dipendenze:** 1–5
**Scope:** bottone "test canonico" con esito; verifica Playwright: determinismo,
A≠B, sweep→curva, export ok; fix di ciò che emerge.
**Out of scope:** suite estesa multi-test (v2).
