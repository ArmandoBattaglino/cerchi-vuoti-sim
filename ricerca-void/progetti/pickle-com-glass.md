# Glass — pickle-com/glass

<https://github.com/pickle-com/glass>

**~7.560 stelle · JavaScript (Electron + Next.js) · ultimo push ott 2025 · licenza GPL-3.0** · "Digital Mind Extension." Fork evoluto di CheatingDaddy.

## Cosa fa

Overlay AI da desktop che "vive" sopra tutto ciò che fai: vede lo schermo, ascolta l'audio in tempo reale, capisce il contesto, e trasforma ogni momento in conoscenza strutturata. Due modalità di punta: **Ask** (rispondi in base a tutto ciò che è passato sullo schermo e nell'audio) e **Meetings** (note in tempo reale, riassunti live, registrazioni di sessione con action item). Il claim centrale è l'invisibilità: la finestra **non compare in screen recording, screenshot, né nel dock** — nessuna cattura sempre-attiva visibile, nessuna condivisione nascosta all'utente. È il progetto più stellato del filone "covert overlay", ripulito e prodotto (branding Pickle, web companion Next.js, sync Firebase, storage locale SQLite).

## Come è fatto

App **Electron** con architettura a feature modulari e doppio backend di persistenza (locale **SQLite** + cloud **Firebase/Firestore**, selezionabili). Struttura `src/features/`: `ask/`, `listen/` (con sotto-moduli `stt/` speech-to-text e `summary/`), `settings/`, e un `common/ai/factory.js` che astrae i provider — **OpenAI, Gemini, Anthropic, Deepgram, Ollama, Whisper** dietro un'unica factory, così puoi girare tutto in locale (Ollama + Whisper) o su API cloud. Bridge Electron (`featureBridge`, `internalBridge`, `windowBridge`) tra main e renderer. Il cuore dell'occultamento è ereditato da CheatingDaddy: la finestra è `frame:false, transparent:true, alwaysOnTop:true` e soprattutto chiama **`setContentProtection(true)`** — l'API Electron che dice all'OS di escludere la finestra dalla pipeline di cattura schermo (a livello di compositor: il pixel c'è per l'occhio, non per il grabber). Più `setSkipTaskbar(true)`, `setAlwaysOnTop(true, 'screen-saver')` e `setIgnoreMouseEvents` per il click-through. `encryptionService` per i dati a riposo, `migrationService` per lo schema, prompt costruiti da `promptBuilder` + `promptTemplates`.

## Cosa possiamo notare di utile per noi

Questo è il progetto più direttamente rilevante per il tuo asse **occultamento/steganografia**, ma su un piano diverso da quello algoritmico: qui l'occultamento è **a livello di canale di osservazione dell'OS**, non nel segnale.

- **`setContentProtection` = occultamento nel canale, non nel contenuto.** È l'inverso concettuale della steganografia. La steganografia nasconde l'informazione *dentro* un portante osservabile (il messaggio è nel segnale, invisibile perché ben mescolato). Glass invece lascia il contenuto pienamente visibile all'occhio ma **lo rende assente dallo strumento di misura**: il grabber legge nero dove l'umano legge testo. Due modelli di "invisibile" da tenere distinti nel tuo dossier: nascosto-nel-segnale (stego) vs assente-dalla-sonda (content-protection). Per l'arena del vuoto, il secondo suggerisce un esperimento: uno stato che è pieno per un canale di lettura e vuoto per un altro — l'occultamento come proprietà relazionale osservatore-dipendente, non intrinseca.
- **La factory multi-provider come "oscilloscopio staccabile dalla sonda".** `common/ai/factory.js` disaccoppia il modello di ragionamento dai provider concreti (locale o cloud) esattamente come un buon HUD disaccoppia la sonda dal display. Pattern riusabile ovunque tu voglia poter scambiare il "cervello" senza toccare il resto.
- **"Digital Mind Extension" — il claim, e il suo limite.** Il framing è coscienza-adiacente (un'estensione della tua mente che ricorda e capisce), ma va detto netto: non c'è alcun anello ricorsivo. Il sistema osserva *te* e struttura il *tuo* contesto; non osserva sé, non si modella. È memoria esterna aumentata, utilissima, ma è uno specchio rivolto all'utente, non un sistema che si guarda. Ottimo oggetto di contrasto per la tua tesi coscienza=ricorsione: mostra quanto "mind extension" venduto come mente sia in realtà un registratore contestuale.

Dove diverge: è un prodotto goal-directed per l'utente umano, zero emergenza, zero auto-modello. L'unico transfer profondo è l'idea di **invisibilità relativa al canale di misura**.

## Da rubare

- **L'idea "content-protection": stato pieno per una sonda, vuoto per un'altra.** Trasferita all'arena: progetta due canali di lettura sullo stesso stato di particelle dove uno vede struttura ricca e l'altro vede vuoto — l'occultamento come funzione dell'osservatore, non del sostrato. È un esperimento concreto sulla relatività osservatore-dipendente del "vuoto".
- **La AI-factory disaccoppiata (`common/ai/factory.js`)** con provider locali (Ollama/Whisper) e cloud dietro la stessa interfaccia: scheletro pronto per rendere il "cervello" dell'arena intercambiabile senza riscrivere la pipeline.
- **Doppio storage locale-SQLite / cloud selezionabile** con `migrationService` ed `encryptionService`: pattern pulito e collaudato per persistere tracce di sessione (utile se vuoi loggare la storia degli stati emergenti in modo intercambiabile locale/remoto).
