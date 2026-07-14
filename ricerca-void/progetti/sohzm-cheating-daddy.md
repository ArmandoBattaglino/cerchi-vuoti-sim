# Cheating Daddy — sohzm/cheating-daddy

<https://github.com/sohzm/cheating-daddy>

**~5.400 stelle · JavaScript (Electron) · ultimo push giu 2026 · licenza GPL-3.0** · "A free and opensource app that lets you gain an unfair advantage."

## Cosa fa

Assistente AI real-time che gira come overlay trasparente sempre-in-primo-piano durante videochiamate, colloqui, presentazioni e meeting: cattura schermo + audio, li manda a un LLM live, e mostra risposte contestuali sopra a tutto. È il progetto fondativo del filone ghost/undetectable open-source (Glass di Pickle ne è un fork dichiarato). Ha "profili" che cambiano il comportamento — Interview, Sales Call, Business Meeting, Presentation, Negotiation — ciascuno con un system prompt su misura. Il punto di vendita è la copertura: la finestra è invisibile alla cattura schermo di chi condivide/registra, e diventa click-through a comando. Nota onesta del README: durante il test non risponde a domande generiche, devi *simulare* l'intervistatore che chiede — è tarato per reagire allo speech dell'interlocutore.

## Come è fatto

**Electron** essenziale (`src/index.js` main, `src/utils/`), UI con **Lit** (web components leggeri, `lit-core`), niente framework pesante. Audio: `SystemAudioDump` (binario nativo) su macOS per catturare l'audio di sistema, loopback su Windows, microfono su Linux. Il cervello è **Gemini 2.0 Flash Live** (`utils/gemini.js`), con astrazioni per cloud e localai (`utils/cloud.js`, `utils/localai.js`) e i system prompt per profilo in `utils/prompts.js`. Il meccanismo di occultamento sta in `utils/window.js`: `frame:false`, `transparent:true`, `alwaysOnTop:true`, poi le tre chiavi — **`setContentProtection(true)`** (esclude la finestra dalla cattura a livello di compositor OS), **`setSkipTaskbar(true)`** (via dalla taskbar), **`setAlwaysOnTop(true, 'screen-saver', 1)`** (sopra quasi tutto), e **`setIgnoreMouseEvents(true, {forward:true})`** per il click-through che lascia passare mouse alla finestra sotto. Storage locale (`storage.js`), zero backend cloud proprietario: porti la tua API key.

## Cosa possiamo notare di utile per noi

Stessa famiglia di Glass, e stesso aggancio profondo per te sull'asse **occultamento**, ma qui in forma più nuda e leggibile (meno prodotto, più meccanismo).

- **L'occultamento come singola primitiva dell'OS.** Tutta la "magia invisibile" si riduce a `setContentProtection(true)`: una bandiera che divide il mondo in due osservatori — l'occhio umano (che vede) e il frame-grabber (che vede nero). È l'esempio più pulito che tu abbia in lista del principio "il vuoto è relativo alla sonda": lo stesso oggetto è pieno o assente a seconda del canale che lo interroga. Concettualmente più forte di qualsiasi stego, perché non nasconde *dentro* qualcosa — semplicemente esiste per un misuratore e non per l'altro. Per l'arena: modella particelle/strutture che rispondono a un canale di lettura e sono trasparenti a un altro.
- **Profili = stesso substrato, comportamento diverso su intento diverso.** I cinque profili sono system prompt intercambiabili sopra lo stesso motore: un unico sistema che si "occulta" dietro maschere di scopo diverse a seconda del contesto. È occultamento dell'intento, non del segnale — utile come terzo tipo nel tuo bestiario (canale / contenuto / intento).
- **Reagisce all'*altro*, non a sé.** La nota "risponde solo se simuli l'interlocutore" dice tutto sul limite: è un sistema puramente eterodiretto, tarato sullo stimolo esterno, senza alcun anello su di sé. Ennesimo controesempio pulito alla tesi coscienza=ricorsione: sofisticato nel percepire il mondo, cieco a sé stesso.

Dove diverge: nessuna memoria novelty-gated (storage piatto), nessuna emergenza, nessun world-model appreso. Il valore è tutto nel meccanismo di invisibilità e nella tassonomia di occultamento che ne ricavi.

## Da rubare

- **`setContentProtection(true)` come dimostrazione minima di "vuoto relativo all'osservatore".** Una riga che realizza empiricamente l'idea: stesso stato, pieno per una sonda, vuoto per un'altra. Da usare come esperimento-seme sull'occultamento osservatore-dipendente nell'arena.
- **La tassonomia a tre livelli** che questo progetto rende esplicita: occultamento-nel-canale (content-protection), occultamento-nel-contenuto (stego classica), occultamento-nell'intento (profili/maschere sopra lo stesso motore). Utile come griglia per organizzare tutto il tuo ramo occultamento.
- **Overlay Electron + Lit minimale con click-through** (`setIgnoreMouseEvents(..., {forward:true})`): scheletro leggero se mai volessi un HUD/oscilloscopio sempre-sopra e non-intrusivo che galleggia sull'arena senza rubarle il focus.
