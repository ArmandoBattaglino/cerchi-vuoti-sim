# CodeInterviewAssist (interview-coder senza paywall) — [github.com/j4wg/interview-coder-withoupaywall-opensource](https://github.com/j4wg/interview-coder-withoupaywall-opensource)

⭐ ~1.9k stelle · TypeScript (Electron) · sviluppo fermo (ultimo push ago 2025) · licenza custom (NOASSERTION, AGPL-derivata)

## Cosa fa

È la versione open-source "senza paywall" di interview-coder: un'app desktop invisibile che ti aiuta a superare i colloqui tecnici di coding. Fai screenshot della domanda e del codice (separatamente, per un'analisi migliore), l'app estrae e analizza il problema con GPT-4o via Vision API, e genera soluzione completa con spiegazione, complessità temporale/spaziale e debugging in tempo reale. La finestra è "99% invisibile" e bypassa la maggior parte dei metodi di cattura schermo, con hotkey globali non rilevabili (Cmd/Ctrl+B per mostrare/nascondere, ecc.). Usa la tua chiave OpenAI (paghi solo il consumo) e tutto gira in locale tranne le chiamate API. Il README è onesto sui limiti: invisibile a Zoom <6.1.6 e a tutte le registrazioni browser, ma NON alle versioni Zoom recenti né alla registrazione schermo nativa macOS (Cmd+Shift+5).

## Come è fatto

App Electron classica: il codice di integrazione LLM sta tutto in `electron/ProcessingHelper.ts` (pensato per essere riscritto verso Claude/Deepseek/Llama), la UI settings in `src/components/Settings/SettingsDialog.tsx`. Due script "stealth-run" (`.bat`/`.sh`) fanno build in produzione e lanciano l'app già in modalità invisibile. L'invisibilità si regge sulle stesse API Electron degli altri cloni: finestra frameless/trasparente, always-on-top, e `setContentProtection` per l'esclusione dalla cattura. Il flusso è a due fasi (estrazione problema → generazione soluzione) con possibilità di scegliere GPT-4o vs GPT-4o-mini per bilanciare costo/qualità fra le fasi. Nessun server proprietario: config e chiavi in `config.json` nella user-data-dir.

## Cosa possiamo notare di utile per noi

L'aspetto più rilevante per te non è il codice (Electron banale, ormai superato dai cloni Tauri/Rust) ma **l'onestà del modello di minaccia**. Il README elenca esplicitamente contro *quali* osservatori l'occultamento tiene e contro quali no, versione per versione (Zoom 6.1.6 è la soglia). Questo è il modo giusto di trattare la steganografia/occultamento nel tuo lavoro: l'invisibilità non è una proprietà binaria del segnale, è una **matrice segnale × osservatore × versione-dell'osservatore**, e cambia quando l'osservatore aggiorna il suo apparato di misura. Nella tua void-arena questo si traduce in una corsa agli armamenti: il momento in cui definisci un occultatore che sfrutta un buco osservativo, hai implicitamente definito la patch che lo chiude, e quindi una dinamica evolutiva. La struttura a due fasi (estrai-poi-risolvi) è anche un piccolo esempio di **routing novelty-gated primitivo**: fai passare al modello costoso solo dopo che una prima fase più economica ha isolato l'essenziale — analogo al tuo gating della memoria, dove solo ciò che supera un filtro di rilevanza consuma la risorsa cara. Dove diverge nettamente: qui non c'è stato interno persistente né osservazione degli interni — è stateless, screenshot→risposta. Non offre nulla su oscilloscopi/ricorsione/world-model; è puro tool. Trasferibile: solo il framing "occultamento = tabella osservatore-dipendente versionata" e il pattern del filtro economico-prima-del-costoso.

## Da rubare

1. **La matrice di minaccia esplicita** come artefatto di design: per ogni meccanismo di occultamento nella sim, mantieni una tabella "tiene contro osservatore A/B/C, cade contro D" — rende l'occultamento misurabile e apre la porta alla dinamica evolutiva occultatore↔rilevatore.
2. **Il gating a due stadi economico→costoso**: filtra prima con una misura cheap, spendi la risorsa cara (memoria/compute) solo su ciò che passa — direttamente applicabile al tuo novelty-gating.
3. **La soglia versionata dell'osservatore (Zoom 6.1.6)** come idea di "arms-race clock": introduci nella sim osservatori che periodicamente aggiornano il loro apparato, invalidando gli occultamenti precedenti e forzando adattamento continuo.
