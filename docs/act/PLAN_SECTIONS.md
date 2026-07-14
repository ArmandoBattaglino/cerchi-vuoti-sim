# Plan Sections — Void Lab COMPLETO (locale, professionale)

Brief: portare il Void Lab a versione completa e ultra-professionale, TUTTO LOCALE.
Scelta utente (2026-07-14): due motori-dati dentro la pagina — SQLite (OLTP, cose base)
+ DuckDB (OLAP, analitica tipo-ClickHouse). Persistenza vera via OPFS → serve lanciatore
locale con header COOP/COEP. Motori impacchettati in lib/ e caricati offline (zero cloud).
Schema alla MLflow: Esperimenti → Run → Parametri, Metriche, Note, Tag.
Costruzione a strati con verifica runtime (Playwright servito dal lanciatore) tra ogni strato.
Ricerca: docs/act/recon/data-layer.md.

## Section A: Fondazione dati locale
**Goal:** due motori WASM caricati offline dal lanciatore, schema creato, persistenza OPFS.
**Dipendenze:** nessuna
**Scope:** avvia-lab.py (+ .bat) con COOP/COEP e MIME wasm; lib/duckdb + lib/sqlite scaricati;
lib/dati.js con API async unica (init, saveRun, listRuns, sqlite(sql), duck(sql)); schema MLflow;
pagina dati-test.html che prova insert+query su entrambi (PASS).
**Out of scope:** integrazione col lab, UI di analisi.

## Section B: Il lab scrive nel database
**Goal:** ogni Run/Sweep del void-lab salva un record; archivio consultabile.
**Dipendenze:** A
**Scope:** ingestione da void-lab (config+metriche+note+tag) in SQLite; pannello Archivio
(lista run, rifai deterministico, apri, elimina, modifica note); sopravvive al reload.
**Out of scope:** OLAP/grafici.

## Section C: Tavolo di analisi (DuckDB OLAP)
**Goal:** interrogare e confrontare migliaia di run con vere query + grafici.
**Dipendenze:** A,B
**Scope:** caricamento run in DuckDB; box SQL libero + tabella risultati; analisi pronte
(bottoni) + grafici (es. win-rate A vs goalPull su tutti); export CSV/Parquet/JSON.
**Out of scope:** query multi-tabella complesse oltre le run.

## Section D: Rifinitura + note per esperimento + ponte con me
**Goal:** professionale e usabile; note incollate a ogni run; export/import totale.
**Dipendenze:** A,B,C
**Scope:** note per run (la "chat allegata"); tag/filtri; export/import di tutto il lab (JSON);
istruzioni lanciatore; verifica end-to-end.
**Out of scope:** cloud, chat-widget LLM (fuori dal principio locale).
