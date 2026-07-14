# GhostCode — eladlevi013/GhostCode

<https://github.com/eladlevi013/GhostCode>

**~2 stelle · JavaScript (React/Redux) · ultimo push nov 2023 · licenza MIT** · "Where programming meets the supernatural in a chilling coding adventure."

## Cosa fa

Gioco-puzzle browser a tema horror in cui scrivi codice per guidare un fantasma attraverso livelli labirintici a raccogliere gemme nel minor numero di mosse. È un "coding game" educativo/ludico: il giocatore scrive comandi in un piccolo linguaggio, il gioco li interpreta e li traduce nei movimenti del fantasma sulla scacchiera. Nessuna AI, nessun LLM — è omonimo del filone "ghost/undetectable" ma non ha niente a che vedere con esso. Deployato su Vercel (`ghostcode.vercel.app`); il repo non include gli asset grafici (licenziati separatamente).

## Come è fatto

Frontend **React + Redux** per UI e stato, con il motore di gioco su **Phaser.js** (canvas/WebGL). Il pezzo tecnicamente interessante è il parser: il codice scritto dal giocatore viene interpretato con **PEG.js** (parser generator a grammatica PEG), che trasforma il testo in un albero di istruzioni eseguibili → sequenza di movimenti del fantasma. C'è un `CodeEditor` component, un `CodeHelper`, livelli selezionabili (`LevelSelector`), badge/gamification (`BadgeModal`), auth panel. Presente un curioso `client/public/secret_answers.txt` — le soluzioni dei livelli in chiaro nel bundle pubblico (una piccola svista di occultamento, involontariamente a tema).

## Cosa possiamo notare di utile per noi

Sia onesto: rilevanza per il tuo lavoro **quasi nulla**. Nessun vuoto, nessuna emergenza, nessuna memoria, nessuna coscienza. È finito in lista solo per omonimia con il filone ghost. I pochi spunti tangenziali, presi per quel che valgono:

- **Codice-come-controllo di un agente in un mondo.** Il loop "scrivi un linguaggio → un interprete lo traduce in azioni di un personaggio in un mondo simulato" è, in miniatura e senza AI, la stessa forma del world-model-come-sogno pilotato da un attore. Ma qui l'interprete è deterministico e il "mondo" è una scacchiera: manca tutto ciò che ti interessa (nessun modello appreso, nessun sogno, nessuna sorpresa). Serve al più come promemoria del contrasto: un agente scriptato in un mondo giocattolo *non* è nulla di ciò che stai cercando.
- **PEG.js come strato interprete.** Se mai ti servisse un piccolo DSL per pilotare esperimenti nell'arena (comandi umani → azioni sulle particelle), un parser PEG è la via leggera. Spunto puramente strumentale, non concettuale.
- **`secret_answers.txt` nel bundle pubblico.** Involontario ma a tema occultamento: mostra il fallimento banale dello "steganografare" nascondendo in un file col nome ovvio dentro un artefatto pubblico. Antipattern da citare quando ragioni su occultamento reale vs apparente.

Dove diverge: praticamente ovunque. È un artefatto di intrattenimento del 2023, non un sistema di ricerca.

## Da rubare

- **Nulla di sostanziale.** Al massimo, se in futuro vorrai un DSL testuale per comandare l'arena del vuoto, tieni a mente **PEG.js** come parser minimale testo→azioni. Per il resto, questo progetto vale come voce di dis-ambiguazione nel dossier ("l'altro GhostCode, il gioco, non c'entra"), non come fonte di idee.
