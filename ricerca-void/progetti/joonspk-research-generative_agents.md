# Generative Agents (Stanford Smallville) — [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents)

Stelle: ~21.7k · Linguaggio: Python (backend) + Django/JS (frontend) · Ultima attivita: ago 2024 · Licenza: Apache-2.0

## Cosa fa
Simula 25 agenti "credibili" in un mondo sandbox 2D (Smallville). Ogni agente ha un LLM che gli fa percepire l'ambiente, ricordare, riflettere e pianificare la giornata. Da vincoli minimi (una seed-line di identita per personaggio) emergono comportamenti sociali non programmati: una festa di San Valentino si organizza da sola via passaparola, nascono conversazioni, appuntamenti, una candidatura alle elezioni. E' il paper-reference sul "memory stream" recuperato per punteggio.

## Come e fatto
Il cuore e in `reverie/backend_server`: un loop a game-step (1 step = 10s di gioco) dove ogni agente esegue percepisci -> recupera -> pianifica -> agisci -> riflette. La **memoria associativa** (vedi le cartelle `bootstrap_memory/associative_memory` con `nodes.json`, `embeddings.json`, `kw_strength.json`) e uno stream di nodi (osservazioni, riflessioni, piani). Il **retrieval** pesca i ricordi rilevanti combinando tre punteggi normalizzati: **recency** (decadimento esponenziale), **importance** (voto di salienza 1-10 chiesto all'LLM al momento dell'inserimento) e **relevance** (similarita coseno tra embedding del ricordo e della query). La **reflection** scatta quando la somma delle importance recenti supera una soglia: l'agente si ferma, si pone domande su se stesso e sintetizza i ricordi grezzi in insight di livello superiore, che rientrano nello stream come nuovi nodi (ricorsione). Il frontend Django serve la mappa Tiled e fa il replay/demo dei movimenti salvati.

## Perche riguarda te
Questo e il ponte piu diretto tra la tua "memoria novelty-gated" e un sistema che gira davvero. Tre agganci onesti:
- **Importance-gate = tuo novelty-gate.** Loro non salvano tutto uguale: ogni ricordo entra con un voto di salienza, e solo l'accumulo di salienza triggera la reflection. E' il pattern "non tutto merita di essere ricordato/consolidato" che cerchi, gia implementato.
- **Reflection ricorsiva = coscienza-ricorsione applicata.** La sintesi di ricordi in insight che rientrano nello stream ed diventano materiale per altre sintesi e letteralmente "ricorsione della realta attraverso una traccia". E' un modello concreto, sporco ma funzionante, del ciclo che teorizzi.
- **Dove diverge:** qui non c'e "arena del vuoto" ne emergenza da particelle/fisica. L'emergenza e mediata da un LLM costoso, non da regole locali povere. Le feste emergono perche c'e gia semantica dentro l'LLM, non da dinamiche minime. Se il tuo interesse e l'emergenza da nulla, questo e l'estremo opposto (emergenza da tantissima struttura pre-esistente). Utile come contrappunto: mostra quanto lavoro fa la memoria strutturata vs quanto fa il substrato.

## Da rubare
1. **La formula di retrieval a tre pesi** (recency-decay × importance-score × relevance-cosine, normalizzati e sommati): e' un gate di richiamo memoria pronto da adattare al tuo "cosa riaffiora nell'arena". Sostituisci l'importance dell'LLM con la tua metrica di novelty/sorpresa e hai un memory-stream novelty-gated.
2. **Il trigger di reflection a soglia di salienza accumulata:** invece di consolidare a intervalli fissi, consolidi solo quando abbastanza "roba saliente" si e' accumulata. E' un buon meccanismo per decidere *quando* un oscilloscopio/osservatore deve fermarsi e sintetizzare, anziche macinare a vuoto.
