# teamstreamlineapps/ghostcode — [github.com/teamstreamlineapps/ghostcode](https://github.com/teamstreamlineapps/ghostcode)

⭐ 0 · TypeScript · 1 solo push (17 apr 2026, mai più toccato) · MIT · ~200 MB

## Cosa fa
Nonostante il nome e la tagline "GhostCode - The open source AI coding agent", il contenuto NON è un progetto originale: è un mirror/rinomina 1:1 di **OpenCode** (`anomalyco/opencode`), l'agente di coding open source da terminale. Il README è quello di OpenCode parola per parola (logo `opencode.ai`, badge Discord/npm, 22 traduzioni, istruzioni `curl -fsSL https://opencode.ai/install | bash`), e l'albero dei file contiene l'intera monorepo di OpenCode (`packages/console`, workflow `.github/`, agenti `.opencode/agent/`, TUI in Go/TS). L'account `teamstreamlineapps` ha fatto un unico commit di import e poi ha abbandonato. In pratica è un progetto-fantasma: guscio vuoto di identità propria sopra il lavoro di qualcun altro.

## Come è fatto
Architettura ereditata da OpenCode: agente da terminale client/server, TUI, tool `read/write/edit/bash`, provider-agnostic, sistema di sub-agenti in markdown (`.opencode/agent/*.md` — triage, translator, duplicate-pr), enorme apparato CI (~40 workflow: publish, review, vouch, triage automatico issue/PR). Nulla di tutto ciò è stato modificato: è il codice originale con il nome cambiato in "ghostcode". Non c'è alcun layer aggiunto, nessun README riscritto, nessun commit di sostanza.

## Cosa possiamo notare di utile per noi
Il valore per il tuo lavoro non è nel codice (è OpenCode, che puoi studiare alla fonte) ma nel **fenomeno**: nella tua arena del vuoto stai catalogando "cerchi vuoti" — entità che occupano uno slot semantico ("ghost coding agent") senza contenuto proprio. Questo repo è letteralmente quello: un token che punta a un referente altrui, un guscio di novelty zero. È un caso limite perfetto per la tua **memoria novelty-gated**: se il tuo sistema indicizzasse i repo per contenuto (embedding del codice) invece che per etichetta (nome + description), questo collasserebbe sullo stesso cluster di OpenCode con novelty ≈ 0 e verrebbe scartato. Diverge totalmente dai temi coscienza/world-model: qui non c'è nulla di generativo, è pura duplicazione. Ma è trasferibile come **test negativo**: il tuo rilevatore di occultamento/mimetismo dovrebbe accendersi qui — un'entità che si maschera da originale mentre è una copia è esattamente lo steganogramma inverso (nascondere la NON-originalità, non l'informazione).

## Da rubare
- **Fingerprint di derivazione**: per la memoria novelty-gated, hash del contenuto (non del nome) come chiave primaria; un "nuovo" progetto che collide con hash esistente = novelty 0 → scarta o linka al genitore invece di ingerirlo.
- **Segnale "cerchio vuoto"**: metrica `identity_gap` = distanza fra ciò che un'entità DICHIARA di essere (metadata/nome) e ciò che È (contenuto reale). Alta = candidato mimetismo/occultamento da flaggare nell'arena.
