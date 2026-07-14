# Recon — motore dati locale (2026-07-14)

## Licenze (nessun problema, tutto gratis per qualsiasi uso)
- DuckDB: MIT · ClickHouse: Apache 2.0 · SQLite: public domain. Nessun vincolo "non commerciale".

## Motori in-browser disponibili
- **DuckDB-WASM** (maturo, il più usato): OLAP colonnare in-browser, persistenza OPFS
  (Chrome/Edge pieno; Firefox/Safari memory-only). Bundle manuali locali (duckdb-eh.wasm +
  duckdb-browser-eh.worker.js + duckdb-browser.mjs) da jsdelivr @duckdb/duckdb-wasm/dist/.
- **SQLite-WASM (ufficiale, sqlite.org)**: ES module; OPFS VFS via worker (vfs=opfs).
- chDB-Wasm (ClickHouse vero): esiste ma nuovissimo/sperimentale — scartato per rischio.

## Vincolo chiave: OPFS richiede cross-origin isolation
- Servono header: `Cross-Origin-Opener-Policy: same-origin` e `Cross-Origin-Embedder-Policy: require-corp`.
- → Un semplice file:// (doppio click) NON abilita OPFS worker. Serve un server con quegli header.
- Soluzione: lanciatore locale `avvia-lab.py` (http.server sottoclassato che aggiunge gli header
  + MIME corretto per .wasm/.mjs). Costo accettato dall'utente (app da avviare, non puro doppio-click).

## Schema professionale (alla MLflow)
- **Experiment** (contenitore logico) → **Run** (una esecuzione) con: **Params** (config),
  **Metrics** (numeri), **Artifacts/Notes** (file/plot/note), **Tags** (per ricerca/filtro).
- Best practice: loggare tutto, naming consistente, tutto ciò che serve a ricreare un risultato
  sta insieme al run. Nel nostro caso: config JSON (seed+parametri) = param; risultati = metrics;
  determinismo → il run si RI-FA esatto dal solo config.

## Architettura scelta (due motori, ruoli distinti)
- **SQLite = fonte di verità (OLTP)**: salva experiments/runs/metrics/notes/tags. Persistente OPFS.
- **DuckDB = analitica (OLAP)**: ingerisce le run per query pesanti tipo-ClickHouse + grafici.
- Entrambi impacchettati in lib/, offline, caricati dal lanciatore.

Fonti: duckdb.org/docs (wasm instantiation, deploying), sqlite.org/wasm/doc (persistence),
developer.chrome.com (sqlite-wasm+opfs), mlflow.org/docs (tracking), github chdb-io/chdb.
