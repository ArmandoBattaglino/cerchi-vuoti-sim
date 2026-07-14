# Hermes HUD — joeynyc/hermes-hud

<https://github.com/joeynyc/hermes-hud>

**~880 stelle · Python · ultimo push lug 2026 · licenza MIT** · "What does an AI see when it looks in a mirror?"

## Cosa fa

Un "consciousness monitor" a terminale (TUI) per un agente AI: una dashboard che guarda l'agente pensare. Legge la cartella dati dell'agente (`~/.hermes/`, override via `HERMES_HOME`) e ne fa affiorare tutto ciò che l'agente sa di sé — conversazioni tenute, skill acquisite, errori corretti, capacità di memoria, pattern d'uso dei tool, progetti attivi, job schedulati, stato dei servizi. Pensato per l'agente Hermes di Nous Research, ma è nella pratica un template di introspezione riusabile. Auto-descrizione onesta: "part neofetch, part flight recorder, part existential crisis rendered in Unicode".

## Come è fatto

TUI in **Textual**. Architettura pulita a due strati, facile da imitare:
- `hermes_hud/collectors/` — un modulo per dominio di stato: `memory.py`, `corrections.py`, `skills.py`, `patterns.py`, `cron.py`, `projects.py`, `health.py`, `profiles.py`, `sessions.py`, `agents.py`, `timeline.py`. Ogni collector legge i dati grezzi dell'agente e ritorna uno stato tipizzato (`models.py`).
- `hermes_hud/widgets/` — un pannello per ogni collector, 9 tab navigabili da tastiera.

`snapshot.py` + `diff_panel.py` implementano il **growth tracking**: salvi uno snapshot (`--snapshot`) e la volta dopo il HUD mostra il *diff* — cosa è cambiato da ieri (nuove skill, nuovi errori corretti). `patterns.py` è il più interessante per te: clusterizza i task, rileva prompt ripetuti (window-function JOIN sui log), calcola le ore di picco e i **trigram di tool** più frequenti (`_top_trigrams`) — cioè le catene di tool ricorrenti dell'agente. Presente una suite di test seria, incluso `test_adversarial.py`. Modalità multiple: TUI interattiva, `--text` per stdout, vari neofetch a tema (`--ai`, `--br`, `--fsociety`).

## Perché riguarda te

È il seme che avevi nominato per il ramo **introspection-HUD / oscilloscopi**, ed è esattamente questo: un **oscilloscopio sugli stati interni** di un agente. Aganci diretti:

- **Oscilloscopio.** L'idea è già realizzata: prendere lo stato interiore di un sistema pensante e renderlo un quadrante leggibile in tempo reale. La separazione collector→widget è precisamente il pattern "sonda→traccia" di un oscilloscopio: la sonda (collector) è agnostica dal display (widget). Se costruisci un visualizzatore per l'arena del vuoto, questa è l'architettura di riferimento.
- **Memoria novelty-gated, lato osservabilità.** Lo snapshot-diff mostra *solo ciò che è cambiato*: è il complemento visivo del novelty-gating di A-MEM. Non ti serve rivedere tutto lo stato, ti serve vedere il delta. È la vista giusta per una memoria che deve evidenziare la novità.
- **Coscienza-ricorsione, con onestà brutale.** Il tagline ("cosa vede un'AI quando si guarda allo specchio?") mette in scena l'auto-osservazione — ma va detto chiaro: qui la ricorsione è *nell'occhio dell'osservatore umano*, non nel sistema. Il HUD guarda l'agente; l'agente non guarda sé tramite il HUD. È introspezione esposta, non auto-coscienza. Ottimo come oggetto di contrasto: mostra quanto è facile *sembrare* uno specchio della mente senza che ci sia alcun anello chiuso.

Divergenza: legge dati che altri (l'agente Hermes) hanno già prodotto in un formato specifico. Per la tua arena dovresti scrivere i collector sul formato dei tuoi stati — ma è precisamente il punto di estensione previsto.

## Da rubare

- **Il pattern collector→widget disaccoppiato** (sonda tipizzata separata dal pannello): riusabile pari pari come scheletro di un oscilloscopio per l'arena del vuoto / le particelle-emergenza. Scrivi collector sullo stato delle particelle, i widget di Hermes ti danno già tab, temi e navigazione.
- **Snapshot + diff-panel come motore di novelty-view**: salvare istantanee periodiche e renderizzare solo il delta. È il modo giusto per far vedere "cosa è emerso" in un sistema che cambia continuamente, senza annegare l'osservatore nello stato completo. Combinato col gate di A-MEM, chiude il cerchio: la memoria decide cosa è nuovo, il HUD lo mostra.
