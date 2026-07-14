#!/usr/bin/env python3
# ============================================================================
# avvia-lab.py — Lanciatore locale del Void Lab.
# ----------------------------------------------------------------------------
# Serve la cartella corrente in HTTP aggiungendo su OGNI risposta gli header
# di cross-origin isolation:
#     Cross-Origin-Opener-Policy:   same-origin
#     Cross-Origin-Embedder-Policy: require-corp
# Questi header sono OBBLIGATORI per abilitare crossOriginIsolated nel browser,
# che a sua volta abilita SharedArrayBuffer/Atomics -> OPFS async proxy di
# SQLite. Senza lanciatore, SQLite ripiega in-memory (non persistente).
#
# MIME corretti: .wasm -> application/wasm ; .mjs/.js -> text/javascript.
#
# Uso:  python avvia-lab.py [porta]      (default 8777)
# ============================================================================

import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8777
HOST = "127.0.0.1"
# Serve la cartella dove risiede questo script (robusto rispetto alla cwd).
ROOT = os.path.dirname(os.path.abspath(__file__))


class VoidLabHandler(http.server.SimpleHTTPRequestHandler):
    # MIME espliciti: WASM e moduli ESM devono avere il content-type giusto,
    # altrimenti il browser rifiuta l'istanziazione streaming del wasm o
    # l'import del modulo.
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".wasm": "application/wasm",
        ".js": "text/javascript",
        ".mjs": "text/javascript",
        ".json": "application/json",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        # Cross-origin isolation su OGNI risposta.
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        # Evita cache stantie durante lo sviluppo del lab.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Log compatto su stderr.
        sys.stderr.write("  %s - %s\n" % (self.address_string(), fmt % args))


def main():
    # allow_reuse_address evita "Address already in use" dopo un riavvio veloce.
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    httpd = http.server.ThreadingHTTPServer((HOST, PORT), VoidLabHandler)
    url = "http://%s:%d" % (HOST, PORT)
    print("=" * 60)
    print("  VOID LAB  —  lanciatore locale (cross-origin isolated)")
    print("=" * 60)
    print("  Servo:   %s" % ROOT)
    print("  URL:     %s" % url)
    print("  Lab:     %s/void-lab.html" % url)
    print("  Test A:  %s/dati-test.html" % url)
    print("  (Ctrl+C per fermare)")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Fermato.")
        httpd.server_close()


if __name__ == "__main__":
    main()
