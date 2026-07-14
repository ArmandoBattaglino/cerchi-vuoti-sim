# MarioGPT — shyamsn97/mario-gpt

Link: https://github.com/shyamsn97/mario-gpt

1145 stelle · Python · ultimo push 2024 · licenza MIT · paper NeurIPS 2023 (arXiv 2302.05981)

## Cosa fa
MarioGPT genera livelli giocabili di Super Mario Bros a partire da un prompt testuale ("many pipes, many enemies, some blocks, high elevation"). E' un distilgpt2 finetunato sui livelli del Video Game Level Corpus, dove ogni livello e' serializzato come stringa di colonne di tile. Ma il contributo centrale del paper non e' il generatore: e' il loop di **generazione open-ended** che avvolge il modello — una novelty search che esplora lo spazio dei livelli producendo un archivio di artefatti diversi tra loro, invece di collassare su un unico "livello ottimo". Ogni livello candidato viene testato con un agente A* per verificare che sia effettivamente attraversabile, quindi qualita e diversita sono misurate insieme.

## Come e' fatto
Tre pezzi che valgono la pena isolare:
- **Encoding come linguaggio**: il livello 2D e' letto colonna per colonna e appiattito in una sequenza di token; generare un livello = generare testo autoregressivo. La griglia diventa una frase, la morfologia diventa sintassi. La temperatura del sampling (~2.0-2.4) e' la manopola che scambia stocasticita contro giocabilita.
- **Prompt via cross-attention a caratteristiche contate**: il prompt non e' free-form arbitrario, e' ancorato a conteggi reali di elementi (numero di pipe, nemici, blocchi, elevazione) estratti dai livelli di training, cosi il condizionamento e' verificabile a posteriori.
- **Novelty search + MAP-Elites-like**: il loop mantiene un archivio; nuovi livelli vengono accettati non se "migliori" ma se abbastanza *diversi* dai vicini gia presenti (distanza su un embedding/feature del livello). L'agente A* fa da filtro di validita. Il risultato e' una collezione che copre lo spazio invece di un singolo picco.

## Cosa possiamo notare di utile per noi
Questo e' il ponte piu pulito tra un generatore e la tua **memoria novelty-gated**: MarioGPT non scrive nell'archivio tutto cio che produce, scrive solo cio che e' *sufficientemente nuovo rispetto a quello che gia possiede*. E' esattamente il gate che ti serve per l'arena del vuoto — non "memorizza tutto", ma "memorizza se sorprende". La metrica di novelty qui e' una distanza su feature del livello; nella tua arena l'analogo e' una distanza su stati/configurazioni di particelle o del campo. Il secondo insegnamento e' la coppia **generatore + verificatore**: l'A* che cammina il livello e' un oscilloscopio esterno che decide se l'artefatto e' "vivo" (percorribile) prima di ammetterlo — un pattern trasferibile per validare che una configurazione emergente sia genuina e non rumore. Terzo, la serializzazione griglia→sequenza mostra che una dinamica spaziale puo essere trattata come linguaggio e data in pasto a un modello autoregressivo: se un giorno vuoi che il sistema *racconti/predica* la propria arena, questo e' il modo minimale.
Dove diverge dal tuo lavoro: il modello e' congelato dopo il finetune, la novelty search e' offline (un batch job che riempie un archivio), e non c'e' nessuna nozione di ricorsione o auto-modello — il generatore non guarda se stesso, guarda solo la distanza tra artefatti. La "sorpresa" e' calcolata da fuori, non sentita da dentro.

## Da rubare
1. **Novelty gate sull'archivio**: ammetti una nuova configurazione nella memoria solo se la sua distanza dal k-esimo vicino gia archiviato supera una soglia. E' 20 righe di codice e converte "log di tutto" in "cartografia del nuovo" — il cuore della tua memoria novelty-gated.
2. **Generatore + verificatore separati**: accoppia ogni proposta a un test di validita indipendente (per te: la configurazione e' stabile? conserva una quantita? sopravvive N step?) che filtra prima dell'archiviazione. Diversita e correttezza misurate insieme, non una dopo l'altra.
3. **Temperatura come asse esplicito diversita↔coerenza**: esponi un singolo scalare che regola quanto stocastico e' il campionamento della prossima configurazione, e usalo per spazzare lo spettro ordine-caos in modo riproducibile.
