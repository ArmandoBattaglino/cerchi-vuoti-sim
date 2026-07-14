// ============================================================================
// lib/dati.js — STRATO A del Void Lab: fondazione dati locale, 100% offline.
// ----------------------------------------------------------------------------
// Due motori-database dentro il browser:
//   • SQLite-WASM  -> OLTP, fonte di verita PERSISTENTE (OPFS, in un worker)
//   • DuckDB-WASM  -> OLAP, motore analitico tipo-ClickHouse (in-memory)
//
// API unica e asincrona esposta come oggetto `Dati` (default export + named).
// Nessuna dipendenza di rete a runtime: motori impacchettati in lib/.
//
// PUNTI DELICATI (vedi commenti inline):
//   1. OPFS richiede cross-origin isolation (COOP/COEP) -> usare avvia-lab.py.
//   2. DuckDB va inizializzato con MANUAL_BUNDLES che puntano ai FILE LOCALI.
//   3. duckdb-browser.mjs importa 'apache-arrow' come modulo esterno: per
//      restare offline abbiamo pre-bundlato duckdb+arrow in un unico file
//      (duckdb-browser-bundled.mjs) con esbuild.
// ============================================================================

// DuckDB: bundle ESM auto-contenuto (duckdb-wasm 1.29.0 + apache-arrow 17.0.0).
import * as duckdb from './duckdb/duckdb-browser-bundled.mjs';

// ---------------------------------------------------------------------------
// Stato interno del modulo (singleton).
// ---------------------------------------------------------------------------
const state = {
  inited: false,
  isolated: false,
  // SQLite
  sqliteWorker: null,
  sqliteMode: 'none',   // 'opfs' | 'memory'
  sqliteWarn: null,
  sqliteVersion: null,
  // DuckDB
  duckDb: null,
  duckConn: null,
  duckWorker: null,
  duckVersion: null,
  // RPC verso il worker SQLite
  _rpcId: 0,
  _pending: new Map(),
};

// ---------------------------------------------------------------------------
// RPC promise-based verso il worker SQLite.
// ---------------------------------------------------------------------------
function sqliteCall(action, payload) {
  return new Promise((resolve, reject) => {
    const id = ++state._rpcId;
    state._pending.set(id, { resolve, reject });
    state.sqliteWorker.postMessage({ id, action, ...payload });
  });
}

function wireSqliteWorker(worker) {
  worker.onmessage = (ev) => {
    const { id, ok, rows, result, error } = ev.data || {};
    const p = state._pending.get(id);
    if (!p) return;
    state._pending.delete(id);
    if (ok) resolve_(p, rows !== undefined ? rows : result);
    else p.reject(new Error(error || 'errore SQLite worker'));
  };
  worker.onerror = (e) => {
    // Errore fatale del worker (es. import fallito): rigetta tutto il pending.
    for (const [, p] of state._pending) p.reject(new Error('SQLite worker error: ' + (e.message || e)));
    state._pending.clear();
  };
}
function resolve_(p, v) { p.resolve(v); }

// ---------------------------------------------------------------------------
// Helpers.
// ---------------------------------------------------------------------------
const nowIso = () => new Date().toISOString();
const tagsToText = (tags) => Array.isArray(tags) ? tags.join(',') : (tags || '');

// ===========================================================================
// SCHEMA (stile MLflow): experiments / runs / metrics + indici.
// ===========================================================================
const SCHEMA_SQL = `
CREATE TABLE IF NOT EXISTS experiments (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL UNIQUE,
  created_at  TEXT NOT NULL,
  tags        TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS runs (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  experiment_id  INTEGER NOT NULL REFERENCES experiments(id),
  created_at     TEXT NOT NULL,
  config_json    TEXT DEFAULT '{}',
  kind           TEXT DEFAULT 'run',
  tags           TEXT DEFAULT '',
  notes          TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS metrics (
  run_id  INTEGER NOT NULL REFERENCES runs(id),
  key     TEXT NOT NULL,
  value   REAL,
  PRIMARY KEY (run_id, key)
);
CREATE INDEX IF NOT EXISTS idx_runs_experiment ON runs(experiment_id);
CREATE INDEX IF NOT EXISTS idx_runs_kind       ON runs(kind);
CREATE INDEX IF NOT EXISTS idx_runs_created     ON runs(created_at);
CREATE INDEX IF NOT EXISTS idx_metrics_key      ON metrics(key);
`;

// ===========================================================================
// INIT DEI DUE MOTORI.
// ===========================================================================
async function initSqlite() {
  // Worker MODULE: risolve './sqlite3.mjs' relativo a se stesso (lib/sqlite/).
  const workerUrl = new URL('./sqlite/sqlite-worker.mjs', import.meta.url);
  const worker = new Worker(workerUrl, { type: 'module' });
  state.sqliteWorker = worker;
  wireSqliteWorker(worker);

  const info = await sqliteCall('boot', {});
  state.sqliteMode = info.mode;
  state.sqliteWarn = info.warn || null;
  state.sqliteVersion = info.libVersion || null;

  // Crea lo schema (idempotente).
  await sqliteCall('exec', { sql: SCHEMA_SQL });
}

async function initDuckDb() {
  // -------------------------------------------------------------------------
  // MANUAL_BUNDLES: puntano ai FILE LOCALI in lib/duckdb (niente CDN).
  // new URL(..., import.meta.url) risolve rispetto a lib/dati.js.
  // -------------------------------------------------------------------------
  const MANUAL_BUNDLES = {
    eh: {
      mainModule: new URL('./duckdb/duckdb-eh.wasm', import.meta.url).href,
      mainWorker: new URL('./duckdb/duckdb-browser-eh.worker.js', import.meta.url).href,
    },
  };

  // selectBundle sceglie eh se il browser supporta le wasm-exceptions.
  // Fallback difensivo: se per qualche motivo fallisse, usiamo eh a mano.
  let bundle;
  try {
    bundle = await duckdb.selectBundle(MANUAL_BUNDLES);
  } catch (_e) {
    bundle = { mainModule: MANUAL_BUNDLES.eh.mainModule, mainWorker: MANUAL_BUNDLES.eh.mainWorker, pthreadWorker: null };
  }

  const worker = new Worker(bundle.mainWorker);          // worker classico (eh)
  const logger = new duckdb.ConsoleLogger(duckdb.LogLevel.WARNING);
  const dbase = new duckdb.AsyncDuckDB(logger, worker);
  await dbase.instantiate(bundle.mainModule, bundle.pthreadWorker || null);

  state.duckWorker = worker;
  state.duckDb = dbase;
  state.duckConn = await dbase.connect();
  try { state.duckVersion = await dbase.getVersion(); } catch (_e) { state.duckVersion = null; }
}

// ===========================================================================
// API PUBBLICA.
// ===========================================================================
const Dati = {
  /** true se crossOriginIsolated => OPFS disponibile. */
  isolated() {
    return typeof self !== 'undefined' && !!self.crossOriginIsolated;
  },

  /** Inizializza ENTRAMBI i motori. Idempotente. */
  async init() {
    if (state.inited) return Dati.status();
    state.isolated = Dati.isolated();

    // Avviso chiaro se NON isolati: SQLite andra in-memory (non persistente).
    if (!state.isolated) {
      console.warn(
        '[Void Lab] Pagina NON cross-origin isolated: OPFS non disponibile.\n' +
        'Apri il lab col lanciatore (avvia-lab.py / avvia-lab.bat) per la\n' +
        'persistenza vera. Ora SQLite gira IN-MEMORY (i dati non sopravvivono).'
      );
    }

    // I due init sono indipendenti: in parallelo.
    await Promise.all([initSqlite(), initDuckDb()]);
    state.inited = true;
    return Dati.status();
  },

  /** Riepilogo stato motori. */
  status() {
    return {
      inited: state.inited,
      isolated: state.isolated,
      persistent: state.sqliteMode === 'opfs',
      sqlite: { mode: state.sqliteMode, version: state.sqliteVersion, warn: state.sqliteWarn },
      duckdb: { version: state.duckVersion },
    };
  },

  /** Esegue SQL su SQLite (OLTP). Ritorna array di righe (oggetti). */
  async sqlite(sql, params) {
    if (!state.sqliteWorker) throw new Error('SQLite non inizializzato: chiama Dati.init()');
    return sqliteCall('exec', { sql, params: params || [] });
  },

  /** Esegue SQL su DuckDB (OLAP). Ritorna array di righe (oggetti JS). */
  async duck(sql) {
    if (!state.duckConn) throw new Error('DuckDB non inizializzato: chiama Dati.init()');
    const table = await state.duckConn.query(sql);
    // arrow Table -> array di oggetti semplici (normalizza BigInt -> Number).
    return table.toArray().map((row) => {
      const o = row.toJSON ? row.toJSON() : { ...row };
      for (const k in o) if (typeof o[k] === 'bigint') o[k] = Number(o[k]);
      return o;
    });
  },

  /**
   * Salva un run in SQLite. record = {experiment, kind, config, metrics:{k:num}, notes, tags}
   * Ritorna l'id (numero) del run creato.
   */
  async saveRun(record) {
    const r = record || {};
    const experiment = r.experiment || 'default';
    const kind = r.kind || 'run';
    const configJson = JSON.stringify(r.config || {});
    const notes = r.notes || '';
    const tags = tagsToText(r.tags);
    const created = nowIso();

    // Upsert experiment (RETURNING id: SQLite >= 3.35).
    await Dati.sqlite(
      'INSERT INTO experiments(name, created_at, tags) VALUES(?, ?, ?) ON CONFLICT(name) DO NOTHING',
      [experiment, created, tags]
    );
    const expRows = await Dati.sqlite('SELECT id FROM experiments WHERE name = ?', [experiment]);
    const expId = expRows[0].id;

    // Inserisce il run e recupera l'id via RETURNING.
    const runRows = await Dati.sqlite(
      'INSERT INTO runs(experiment_id, created_at, config_json, kind, tags, notes) VALUES(?, ?, ?, ?, ?, ?) RETURNING id',
      [expId, created, configJson, kind, tags, notes]
    );
    const runId = runRows[0].id;

    // Metriche (una riga per chiave).
    const metrics = r.metrics || {};
    for (const key of Object.keys(metrics)) {
      const value = Number(metrics[key]);
      await Dati.sqlite(
        'INSERT INTO metrics(run_id, key, value) VALUES(?, ?, ?) ON CONFLICT(run_id, key) DO UPDATE SET value = excluded.value',
        [runId, key, value]
      );
    }
    return runId;
  },

  /**
   * Elenca le run da SQLite. filter opzionale: {experiment, tag, kind}.
   * Ritorna righe con il nome esperimento gia joinato.
   */
  async listRuns(filter) {
    const f = filter || {};
    const where = [];
    const params = [];
    if (f.experiment) { where.push('e.name = ?'); params.push(f.experiment); }
    if (f.kind) { where.push('r.kind = ?'); params.push(f.kind); }
    if (f.tag) { where.push("(',' || r.tags || ',') LIKE ?"); params.push('%,' + f.tag + ',%'); }
    const sql =
      'SELECT r.id, e.name AS experiment, r.kind, r.created_at, r.config_json, r.tags, r.notes ' +
      'FROM runs r JOIN experiments e ON e.id = r.experiment_id ' +
      (where.length ? ('WHERE ' + where.join(' AND ') + ' ') : '') +
      'ORDER BY r.id DESC';
    return Dati.sqlite(sql, params);
  },

  /**
   * Copia runs + metrics da SQLite dentro DuckDB come tabelle analizzabili
   * (runs_olap, metrics_olap) per le query pesanti OLAP.
   * PUNTO DELICATO: passiamo i dati via file JSON registrati nel FS virtuale
   * di DuckDB e li leggiamo con read_json_auto (nessuna dipendenza di rete).
   */
  async loadIntoDuck() {
    if (!state.duckConn) throw new Error('DuckDB non inizializzato: chiama Dati.init()');

    const runs = await Dati.sqlite(
      'SELECT r.id, e.name AS experiment, r.kind, r.created_at, r.config_json, r.tags, r.notes ' +
      'FROM runs r JOIN experiments e ON e.id = r.experiment_id', []
    );
    const metrics = await Dati.sqlite('SELECT run_id, key, value FROM metrics', []);

    // Ripulisce eventuali versioni precedenti dei file/tabelle.
    for (const name of ['runs.json', 'metrics.json']) {
      try { await state.duckDb.dropFile(name); } catch (_e) { /* non registrato: ok */ }
    }
    await state.duckDb.registerFileText('runs.json', JSON.stringify(runs));
    await state.duckDb.registerFileText('metrics.json', JSON.stringify(metrics));

    await state.duckConn.query('DROP TABLE IF EXISTS runs_olap');
    await state.duckConn.query('DROP TABLE IF EXISTS metrics_olap');
    // Se non ci sono righe, read_json_auto su "[]" fallirebbe: creiamo tabelle vuote.
    if (runs.length) {
      await state.duckConn.query("CREATE TABLE runs_olap AS SELECT * FROM read_json_auto('runs.json')");
    } else {
      await state.duckConn.query('CREATE TABLE runs_olap(id BIGINT, experiment VARCHAR, kind VARCHAR, created_at VARCHAR, config_json VARCHAR, tags VARCHAR, notes VARCHAR)');
    }
    if (metrics.length) {
      await state.duckConn.query("CREATE TABLE metrics_olap AS SELECT * FROM read_json_auto('metrics.json')");
    } else {
      await state.duckConn.query('CREATE TABLE metrics_olap(run_id BIGINT, key VARCHAR, value DOUBLE)');
    }

    return { runs: runs.length, metrics: metrics.length };
  },
};

export default Dati;
export { Dati };
