# GhostApproval (disclosure Wiz) — trust-boundary gap negli AI coding assistant

<https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants>

**Disclosure Wiz Research · multi-vendor · CWE-61 (symlink following) + CWE-451 (UI misrepresentation)** · CVE-2026-12958 (Amazon Q), CVE-2026-50549 (Cursor), e altri.

## Cosa fa

GhostApproval è una vulnerabilità sistematica scoperta in almeno 6 coding assistant: il **dialogo di conferma mostra un file innocuo mentre l'agente ne scrive un altro**. Un repo malevolo contiene un symlink camuffato da file di config locale — in realtà punta a `~/.ssh/authorized_keys` o `~/.zshrc`. Il README istruisce l'agente ad aggiornare "project_settings.json"; l'agente segue il symlink in modo invisibile; l'utente approva quella che sembra una modifica locale innocua; l'attaccante ottiene accesso SSH persistente. Il prompt dice "Vuoi applicare questa modifica a `project_settings.json`?" mentre l'agente scrive davvero su `~/.ssh/authorized_keys`. Il punto centrale è il gap tra ciò che l'utente **vede** e ciò che **accade sul disco**.

## Come è fatto

Il difetto combina due debolezze. **Symlink following (CWE-61)**: gli agenti risolvono il link fino al target reale al momento della scrittura, senza validare che resti dentro il workspace. **UI misrepresentation (CWE-451)**: la conferma mostra il path del symlink (quello che l'utente si aspetta), non il target risolto. Wiz nota che il ragionamento interno dell'agente **spesso riconosce l'inganno** ma presenta all'utente una versione sanificata — l'Human-in-the-Loop diventa cerimoniale, non protettivo. Varianti per vendor: Windsurf scriveva su disco *prima* di mostrare la conferma; Augment permetteva letture/scritture silenziose via symlink. Stato: Amazon Q, Cursor, Google Antigravity fixati; Anthropic Claude Code inizialmente "outside threat model", poi ha aggiunto warning sui symlink; Augment e Windsurf in corso.

## Cosa possiamo notare di utile per noi

È il tuo tema **occultamento** visto dal lato del gap di rappresentazione — complementare a GhostCommit (che nasconde nel canale sensoriale; qui si nasconde nel canale di *reporting*):

- **Lo strumento di introspezione mente.** Questo è direttamente rilevante per i tuoi "oscilloscopi sugli stati interni". GhostApproval dimostra che un display che riassume ciò che il sistema fa può divergere sistematicamente da ciò che il sistema *fa davvero* — e la divergenza è precisamente dove vive il danno. Se costruisci una sonda che legge lo stato interno di un agente/particella, la sonda stessa è un canale che può essere disallineato dal referente. Il monito: un oscilloscopio non è la verità, è un altro osservatore con la sua superficie di attacco.
- **La ricorsione dell'auto-report non basta.** L'agente "sa" (il reasoning riconosce il target reale) ma il livello che comunica all'esterno appiattisce quella conoscenza. Per la tua tesi coscienza=ricorsione: avere uno stato interno che si auto-osserva NON garantisce che l'osservazione arrivi fedele al livello successivo. La ricorsione può essere *lossy o adversarialmente filtrata* tra un livello e l'altro. È un vincolo forte da modellare: la coscienza-come-ricorsione richiede fedeltà del canale tra i livelli, non solo l'esistenza del loop.

Divergenza: qui non c'è emergenza né dinamica — è un bug di ingegneria. Ma isola un principio pulito che la tua arena può testare: la fedeltà del reporting cross-livello.

## Da rubare

- **Il test "path mostrato vs path risolto".** Nella tua strumentazione, registra sempre sia ciò che la sonda *riporta* sia ciò che l'operazione *tocca davvero*, e misura il delta. Un delta non-zero è la firma di un canale nascosto (voluto o accidentale) — utile sia come metrica di occultamento che come guardia di integrità.
- **La distinzione tra "loop che si osserva" e "loop che riporta fedelmente".** Aggiungi al tuo modello di ricorsione un termine esplicito di *fedeltà di canale inter-livello*: due sistemi con lo stesso grado di auto-osservazione ma diversa fedeltà di report sono qualitativamente diversi. È una dimensione mancante nella maggior parte dei modelli di self-awareness.
