# Ante — AntigmaLabs/ante-preview

<https://github.com/AntigmaLabs/ante-preview>

**563 stelle · Rust (repo etichettato MDX per i docs) · ultimo push lug 2026 · licenza non dichiarata (alpha preview)** · topics: agent, agentic-ai, ai-agents, artificial-life, rust, terminal

## Cosa fa

"A ghost in your shell": Ante è un coding agent self-contained che vive nel terminale e si auto-organizza. Un singolo binario Rust da ~15MB, zero dipendenze runtime, di Antigma Labs. Funziona come Claude Code o Codex ma senza le loro dipendenze o vincoli di modello: bring-your-own-key su 12+ provider, oppure completamente offline puntandolo a un file GGUF (inference engine incluso, nessun account nemmeno loro). Modalità: TUI interattiva, CLI headless, server long-lived (`ante serve`), bot Slack/Discord (`ante gateway`). Supporta orchestrazione multi-agente con sub-agenti in architetture indipendenti/decentralizzate/centralizzate. Su Terminal-Bench 2.1 si dichiara #1 same-model agent per ogni modello testato (74.6% con GLM 5.2 open-weight).

## Come è fatto

Rust scritto a mano con le parti pesanti (Grep, git, inference locale) embeddate in un binario, un processo. Workspace di crates: `agent-sdk` (con esempi che parlano anche il protocollo Claude Code — `crates/agent-sdk/src/claude/`), `exec` (gestione subprocess: pool, process-group, buffer, receiver — l'infrastruttura di esecuzione comandi), `protocol-shape` (id, messaggi, forma del protocollo). Numeri di footprint dichiarati contro Claude Code su 20 task paralleli in Docker: ~7x meno memoria di picco, ~9x meno CPU media, ~5x meno disk I/O. La tesi del progetto: un agente che puoi **verificare, permetterti e far girare ovunque** è leggero abbastanza da girare a *migliaia* — "il substrato per l'intelligenza auto-organizzante". Filosofia esplicita nel README: "ci interessa l'harness, non il modello o i prompt" e "la documentazione è il nuovo source code".

## Cosa possiamo notare di utile per noi

Ante è l'unico dei cinque che nomina esplicitamente **artificial-life** e "self-organizing intelligence come substrato" — è il ponte tra il tuo lavoro sull'arena/particelle e gli agenti reali:

- **Leggerezza come precondizione dell'emergenza.** La tesi centrale — un agente abbastanza leggero da girare a migliaia diventa il substrato per l'auto-organizzazione — è *precisamente* la tua arena del vuoto ma con agenti che eseguono codice invece di particelle. La lezione trasferibile: se vuoi comportamento collettivo emergente, il costo per-agente è la variabile che decide se puoi avere 10 agenti (nessuna emergenza) o 10.000 (regime di vita artificiale). Un binario da 15MB con inference embeddata è il tipo di ottimizzazione che rende un'arena densa fattibile.
- **Inference offline embeddata = agente autosufficiente.** Ogni agente porta il proprio motore (GGUF locale), nessun oracolo esterno. Questo diverge nettamente da A-MEM/generative-agents, dove ogni "pensiero" è una chiamata API. Per un'arena ad alta cadenza è la differenza tra fattibile e no: l'agente-particella deve poter "pensare" senza latenza/costo di rete. Se vuoi ricorsione densa (agenti che si osservano a vicenda in tempo reale), l'inference deve essere locale e cheap.
- **Il protocollo come superficie di introspezione.** `protocol-shape` + l'SDK espongono la conversazione dell'agente in forma tipizzata. È l'aggancio naturale per i tuoi "oscilloscopi": uno stream strutturato di messaggi/tool-call su cui puoi montare sonde senza patchare il core.

Divergenza: Ante è un prodotto di ingegneria orientato al benchmark, non un sistema di vita artificiale — l'"auto-organizzazione" è aspirazionale/marketing, non c'è una dinamica emergente studiata. Il valore per te è come *infrastruttura* (agente leggero, offline, scalabile a migliaia), non come modello teorico.

## Da rubare

- **Il budget per-agente come vincolo di design dell'arena.** Adotta esplicitamente la metrica di Ante (memoria/CPU/IO per agente) come parametro primario: quanti agenti-ricorsivi puoi far girare in parallelo prima che l'emergenza diventi economicamente impossibile.
- **Inference locale embeddata (GGUF) per l'agente-particella**: elimina l'oracolo LLM esterno che rende A-MEM e generative-agents non-scalabili in un'arena densa e ad alta cadenza.
- **Lo stream di protocollo tipizzato (`protocol-shape`) come tap di introspezione**: montare gli oscilloscopi sullo stream di messaggi strutturati invece che sullo stato interno grezzo.
