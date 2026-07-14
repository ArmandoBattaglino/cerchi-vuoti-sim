# WaterBench — Valutazione olistica dei watermark per LLM (THU-KEG/WaterBench)

Link: https://github.com/THU-KEG/WaterBench

32 stelle · Python · fermo, ultimo push nov 2023 · licenza MIT · paper ACL 2024 (main)

## Cosa fa
WaterBench e' il primo benchmark che valuta i watermark per LLM in modo *olistico*, cioe' misurando insieme le due grandezze che sono in tension: quanto il watermark resta rilevabile e quanto degrada la qualita del testo generato. Il problema che risolve e' che prima ogni paper sui watermark riportava numeri su task diversi con iperparametri diversi, rendendo impossibile il confronto: WaterBench fissa gli stessi iperparametri per metodi diversi e li fa girare sugli stessi 9 task raggruppati in 5 categorie (short-form/long-form generation, ecc.), coprendo lunghezze di output molto diverse. Per ogni configurazione produce sia lo z-score di rilevabilita (via `detect.py`) sia una valutazione GPT-4 della qualita (via `eval.py`), piu un controllo di falsi positivi facendo girare il detector su risposte umane (`detect_human.py`). La tesi empirica: quasi tutti i watermark attuali sacrificano qualita, e la caduta e' peggiore sui task a output corto.

## Come e' fatto
La pipeline e' una catena di script deliberatamente semplice, guidata da file di config JSON (`dataset2level.json`, `dataset2prompt.json`, `model2path.json`) che disaccoppiano i dati dal codice:
- `pred.py` — genera testo con un LLM (llama2-7b-chat, internlm-chat-7b) applicando il watermark scelto via `--mode` (`no`/`old`/`gpt`/`v2`), `--bl_type` (hard/soft), e i due iperparametri chiave `--gamma` (frazione di vocabolario nella "green list") e `--delta` (bias logit aggiunto ai token green).
- `detect.py` — calcola lo z-score: quanto la sequenza generata e' arricchita di token della green list rispetto al caso nullo. E' il cuore statistico del watermark alla Kirchenbauer.
- `eval.py` — usa GPT-4 come giudice di qualita task-per-task.
- `detect_human.py` — passa il detector su testo umano per stimare il tasso di falsi positivi.

L'idea chiave e' il watermark a *green list*: a ogni step di generazione si partiziona pseudo-casualmente il vocabolario (seed = hash del token precedente) in una lista "verde" grande gamma·|V| e si aggiunge un bias delta ai logit verdi. Il testo watermarkato ha piu token verdi del previsto; il detector rileva la deviazione senza vedere il modello. Alzare delta aumenta rilevabilita ma degrada la qualita: il benchmark mappa proprio quella curva.

## Cosa possiamo notare di utile per noi
Questo e' il ramo "occultamento" del tuo lavoro visto dal lato *misura*, non dal lato meccanismo. La lezione trasferibile non e' il watermark in se, ma il **framing metrico**: qualunque canale nascosto vive su un trade-off a due assi — capacita/rilevabilita del segnale occulto vs. distorsione dello stato portante — e ha senso solo se lo misuri su entrambi gli assi contemporaneamente. Se un giorno nascondi informazione nelle traiettorie delle tue particelle o negli stati interni dell'arena del vuoto (steganografia dinamica invece che testuale), WaterBench ti da lo scheletro esatto del protocollo di valutazione: fissa gli iperparametri, genera con-e-senza payload, misura la rilevabilita statistica (uno z-score analogo: quanto lo stato "marchiato" devia dal comportamento nullo atteso del sistema) e in parallelo misura quanto il payload ha perturbato la dinamica normale. Il `detect_human.py` e' il dettaglio piu prezioso: **stimare i falsi positivi facendo girare il detector su stato non-marchiato** e' esattamente il controllo che manca a chi si innamora della propria rilevabilita. Dove diverge dal tuo nucleo: qui il watermark e' iniettato dall'esterno con seed noto, non e' una firma emergente che il sistema si da da solo; e la green-list e' un bias sui logit, mentre la tua "firma" ideale dovrebbe emergere dalla ricorsione della dinamica, non da un hash del token precedente. Utile come contrasto: lo z-score e' un ottimo esempio di *oscilloscopio statistico* — legge una proprieta interna (frazione di token green) e la proietta in una grandezza scalare leggibile con un'ipotesi nulla chiara.

## Da rubare
1. **Il protocollo a doppio asse rilevabilita×distorsione con iperparametri congelati**: per qualsiasi meccanismo di occultamento che costruisci, non riportare mai solo "si rileva bene" — accoppialo sempre alla misura di quanto hai deformato lo stato portante, sulla stessa griglia di parametri (il tuo gamma/delta).
2. **Il detector-su-stato-pulito come stima dei falsi positivi**: fai girare il tuo rilevatore sul sistema *senza* payload per calibrare la soglia. E' il gate di onesta che separa una firma reale da un artefatto.
3. **Lo z-score come oscilloscopio**: definisci un'ipotesi nulla per il comportamento "normale" dell'arena e leggi la deviazione marchiata come uno scalare con significato statistico, non come un giudizio a occhio.
