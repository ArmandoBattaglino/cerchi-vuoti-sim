// ============================================================================
// sqlite-worker.mjs — Worker dedicato per SQLite-WASM (OLTP / fonte di verita)
// ----------------------------------------------------------------------------
// Gira come MODULE WORKER. Carica il build ufficiale sqlite.org e apre il DB
// tramite il VFS OPFS (persistente). Se la pagina NON e cross-origin isolated
// (manca COOP/COEP -> niente SharedArrayBuffer/Atomics -> niente OPFS async
// proxy) ripiega su un DB in-memory, cosi il lab non crasha mai.
//
// PUNTO DELICATO: sqlite3.mjs individua da solo, via import.meta.url, i file
// fratelli "sqlite3.wasm" e "sqlite3-opfs-async-proxy.js". Per questo i tre
// file DEVONO stare nella stessa cartella (lib/sqlite/). L'async proxy viene
// avviato come sub-worker dal runtime sqlite: e un worker annidato, permesso.
// ============================================================================

import sqlite3InitModule from './sqlite3.mjs';

let db = null;
let mode = 'none';       // 'opfs' | 'memory'
let bootWarn = null;     // eventuale motivo del fallback
let libVersion = null;
let bootPromise = null;  // boot idempotente

// Nome del file DB dentro OPFS (radice del filesystem origin-private).
const DB_FILE = '/voidlab.sqlite3';

async function boot() {
  const sqlite3 = await sqlite3InitModule({
    // Silenziamo il rumore in console del runtime; gli errori li propaghiamo noi.
    print: () => {},
    printErr: (msg) => { if (String(msg).toLowerCase().includes('error')) console.warn('[sqlite]', msg); },
  });
  libVersion = sqlite3.version && sqlite3.version.libVersion;

  // Tentiamo OPFS solo se abbiamo isolation e il VFS opfs e stato compilato.
  const opfsAvailable = !!(self.crossOriginIsolated && sqlite3.oo1 && sqlite3.oo1.OpfsDb);
  if (opfsAvailable) {
    try {
      // 'c' = create-if-needed + read/write. Usa il VFS "opfs" (async proxy).
      db = new sqlite3.oo1.OpfsDb(DB_FILE, 'c');
      mode = 'opfs';
    } catch (e) {
      bootWarn = 'OPFS non inizializzabile (' + (e && e.message || e) + '), fallback in-memory';
      db = new sqlite3.oo1.DB(DB_FILE, 'c'); // VFS di default: transiente in memoria
      mode = 'memory';
    }
  } else {
    bootWarn = self.crossOriginIsolated
      ? 'VFS opfs non presente in questo build, fallback in-memory'
      : 'pagina non cross-origin isolated: OPFS non disponibile, fallback in-memory';
    db = new sqlite3.oo1.DB(DB_FILE, 'c');
    mode = 'memory';
  }

  // Pragma sensati per un DB locale operativo.
  db.exec('PRAGMA journal_mode=WAL; PRAGMA foreign_keys=ON;');
  return { mode, libVersion, warn: bootWarn };
}

function ensureBoot() {
  if (!bootPromise) bootPromise = boot();
  return bootPromise;
}

// Esegue SQL (anche multi-statement) e raccoglie le righe come oggetti.
// Con bind positional (?) o nominato ($x): passiamo params cosi come arrivano.
function run(sql, params) {
  const rows = [];
  db.exec({
    sql,
    bind: (params && params.length) ? params : undefined,
    rowMode: 'object',
    resultRows: rows,
  });
  return rows;
}

self.onmessage = async (ev) => {
  const { id, action, sql, params } = ev.data || {};
  try {
    if (action === 'boot') {
      const info = await ensureBoot();
      self.postMessage({ id, ok: true, result: info });
      return;
    }
    await ensureBoot();
    if (action === 'exec') {
      const rows = run(sql, params);
      self.postMessage({ id, ok: true, rows });
      return;
    }
    if (action === 'info') {
      self.postMessage({ id, ok: true, result: { mode, libVersion, warn: bootWarn } });
      return;
    }
    throw new Error('azione sconosciuta: ' + action);
  } catch (err) {
    self.postMessage({ id, ok: false, error: String(err && err.message || err) });
  }
};
