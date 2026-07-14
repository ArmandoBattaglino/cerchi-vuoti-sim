# GhostCode (ghostcode-cli) — amitmishrg/ghostcode

<https://github.com/amitmishrg/ghostcode>

**1 stella · TypeScript · ultimo push giu 2026 · licenza MIT** · pacchetto npm `ghostcode-cli` · topics: harness, coding-harness, bun, tui, local-first, agentic-coding

## Cosa fa

Template starter open-source per un harness di coding da terminale: "Don't rent a harness — start from one". È un harness minimale, local-first e provider-agnostic pensato per essere **forkato**, non usato come prodotto. Le tue API key, la tua macchina, sorgente completa su prompt, tool e UI, nessuno stack di account hosted. Dichiaratamente per chi vuole *capire* come funziona un coding agent (streaming, tool, persistenza) o costruirsi il proprio harness partendo da un repo piccolo (~2 package, ~5 file core da imparare). Esplicitamente NON per chi vuole subagenti/MCP/LSP oggi o autonomia benchmark-winning: è un punto di partenza, non parità di feature.

## Come è fatto

Monorepo Bun a due package: `ghostcode-cli` (TUI full-screen keyboard-driven costruita su OpenTUI + React, `LocalChatTransport`, tool locali, sessioni) e `@ghostcode/shared` (schemi dei tool, modi, system prompt, modelli). Il loop di riferimento è l'AI SDK tool loop: stream → tool call → esecuzione locale → resend → salva sessione. Due modalità gated: **PLAN** (read-only: `readFile`, `listDirectory`, `glob`, `grep`) e **BUILD** (PLAN + `writeFile`, `editFile`, `bash`), commutabili con Tab. I file da personalizzare sono espliciti: `schemas.ts`, `system-prompt.ts`, `local-tools.ts`. Memoria di progetto stratificata via file `Ghost.md` (globale, progetto, locale); persistenza di sessione in JSONL per-progetto sotto `~/.ghostcode/projects/<encoded-path>/<session-id>.jsonl`. C'è un doc dedicato `BUILD-YOUR-OWN-HARNESS.md` con "i cinque file che alimentano il loop" e una checklist di 30 minuti.

## Cosa possiamo notare di utile per noi

GhostCode non è teoria — è un **kit di dissezione**: il modo più economico per avere in mano un agente reale, minimale e completamente ispezionabile su cui montare esperimenti. Rilevante per te come banco:

- **La separazione PLAN/BUILD come gate esplicito sull'agire.** Un modo read-only che osserva senza toccare, un modo che agisce, commutati deliberatamente. È una primitiva pulita per i tuoi esperimenti: separa "l'agente che percepisce/pianifica" da "l'agente che modifica il mondo", e ti dà un punto naturale dove inserire un gate (novelty? sicurezza? checkpoint) tra i due. Molti dei tuoi temi vogliono esattamente questa cesura tra osservazione e azione.
- **Il loop in 5 file, ispezionabile.** Diverge da Ante (Rust ottimizzato, opaco) e da Claude Code (grande, chiuso). Qui l'intero ciclo stream→tool→esegui→salva è leggibile e piccolo — è dove puoi *inserire un oscilloscopio* senza combattere l'infrastruttura. Se vuoi loggare/sondare ogni transizione di stato di un agente reale, questo è il substrato più docile.
- **Sessioni come JSONL append-only per progetto.** La traccia completa di ogni Write/Edit è già lì, su disco, in formato leggibile — la stessa materia prima che AfterImage estrae. Per te è un flusso di "esperienza" grezzo su cui testare memoria novelty-gated: ogni riga è un evento, filtrabile e reiniettabile.

Divergenza: è un template embrionale (1 stella, nessuna pretesa di scala o emergenza). Zero vita artificiale, zero ricorsione — è idraulica pulita. Il valore è strumentale: la cosa più forkabile della lista.

## Da rubare

- **Il pattern gate PLAN/BUILD** come cesura riutilizzabile osservazione↔azione dove inserire il tuo novelty-gate o un checkpoint di coscienza-ricorsione, prima che l'agente tocchi il mondo.
- **Il layered memory `Ghost.md` (globale → progetto → locale)** come struttura minimale a livelli per una memoria persistente con precedenza esplicita — semplice da replicare e da rendere novelty-gated.
- **Il loop AI-SDK in 5 file come scheletro di harness** su cui montare gli oscilloscopi: forkalo, strumenta ogni transizione stream→tool→esegui, e hai un agente reale osservabile end-to-end in mezza giornata.
