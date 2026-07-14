# free-cluely — [github.com/Prat011/free-cluely](https://github.com/Prat011/free-cluely)

⭐ ~1.5k stelle · TypeScript (Electron + Vite) · attivo (push apr 2026) · Apache-2.0

## Cosa fa

free-cluely è un clone open-source e gratuito di Cluely: l'assistente desktop invisibile che dà insight e risposte in tempo reale durante meeting, colloqui e presentazioni. Fai screenshot con una hotkey (Cmd/Ctrl+H), l'app manda l'immagine a un LLM e ti restituisce la soluzione (Cmd/Enter), il tutto in una finestra togglabile (Cmd/Ctrl+B) e spostabile con le frecce. Il tratto distintivo rispetto ai cloni OpenAI-only è il supporto **Ollama locale di prima classe**: con `USE_OLLAMA=true` gira 100% offline (llama3.2, codellama, mistral…), dati mai fuori dalla macchina, zero costi API; in alternativa Google Gemini per accuratezza/velocità. Licenza Apache-2.0 (la più permissiva del gruppo). È un progetto piccolo e onesto, con un README che ammette i bug noti (il tasto X non chiude, va usato Cmd/Ctrl+Q).

## Come è fatto

Electron + Vite: dev server su porta 5180, poi lancio dell'app Electron (`npm start` orchestra i due). Usa Sharp per il processing delle immagini degli screenshot (da cui i noti problemi di build con libvips/Python, mitigati con `SHARP_IGNORE_GLOBAL_LIBVIPS=1`). L'astrazione chiave è il **provider AI intercambiabile via env**: lo stesso codepath serve Gemini (cloud) o Ollama (locale) semplicemente cambiando variabili d'ambiente (`USE_OLLAMA`, `OLLAMA_MODEL`, `OLLAMA_URL`), senza toccare il codice. Invisibilità e always-on-top via le solite API Electron di content-protection. Architettura minimale: screenshot → provider LLM → risposta in overlay, senza memoria persistente né RAG.

## Cosa possiamo notare di utile per noi

Il valore per te qui è la **sostituibilità del "cervello" via configurazione, non via codice**. Lo stesso identico flusso di percezione (screenshot) e azione (risposta) rimane invariato mentre l'organo che ci pensa dentro cambia radicalmente — da un LLM cloud gigante a un modello locale piccolo — solo cambiando tre variabili d'ambiente. Per la tua void-arena questa è la separazione pulita fra **substrato cognitivo** e **loop percezione-azione**: se tieni l'interfaccia dell'agente (cosa osserva, cosa emette) stabile, puoi swappare il motore interno e studiare come cambia il comportamento a parità di "corpo". È rilevante per la tesi coscienza=ricorsione: ti permette di isolare quanto della dinamica emergente dipende dal substrato e quanto dalla struttura del loop. Il supporto Ollama-offline è anche la prova che il loop funziona con un modello **piccolo e completamente locale** — cioè senza dipendere da un oracolo esterno onnisciente, condizione necessaria se vuoi che la tua sim sia auto-contenuta e osservabile fino in fondo (niente scatole nere remote da interrogare). Dove diverge, e parecchio: free-cluely è lo scheletro più spoglio del gruppo — nessuna memoria, nessuno stato interno persistente, nessuna osservazione degli interni, nessun world-model. È utile *proprio* come baseline minimale: è "la particella nuda", il loop percezione-azione ridotto all'osso su cui puoi poi aggiungere memoria novelty-gated, oscilloscopi e ricorsione per misurare cosa ciascuna aggiunta produce.

## Da rubare

1. **Il pattern "cervello swappabile via env, corpo fisso"**: definisci nell'arena un'interfaccia agente stabile (osservabili in, azioni out) e rendi il motore interno un plugin sostituibile — così isoli sperimentalmente il contributo del substrato dalla struttura del loop.
2. **Il vincolo "solo modelli locali/piccoli, niente oracolo remoto"**: adottalo come regola di design per mantenere la sim auto-contenuta e integralmente osservabile — nessun componente non-ispezionabile nel percorso critico.
3. **Il loop minimale percezione→cognizione→azione come baseline nuda**: parti da questo scheletro e aggiungi un modulo alla volta (memoria, poi oscilloscopio, poi ricorsione), misurando l'effetto marginale di ciascuno.
