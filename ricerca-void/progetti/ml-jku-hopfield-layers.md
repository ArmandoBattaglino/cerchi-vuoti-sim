# Modern Hopfield Networks (hopfield-layers) — [ml-jku/hopfield-layers](https://github.com/ml-jku/hopfield-layers)

**★ 1.956 · Python (PyTorch) · ultimo push 2023-04 · licenza custom (NOASSERTION, di fatto permissiva stile BSD/EU-JKU) · [paper arXiv:2008.02217](https://arxiv.org/abs/2008.02217) · [blog](https://ml-jku.github.io/hopfield-layers/)**

> "Hopfield Networks is All You Need" (Ramsauer, Hochreiter et al., ELLIS/JKU Linz). Progenitore del **richiamo associativo per attrattori a energia** con capacità esponenziale e convergenza in un solo passo. Dimostra che l'attention del Transformer È la regola di aggiornamento di una moderna rete di Hopfield a stati continui.

## Cosa fa

Fornisce un layer PyTorch (`Hopfield`, `HopfieldPooling`, `HopfieldLayer`) che è una **memoria associativa continua**: gli dai una *query* e lui, con un unico aggiornamento, la fa "cadere" verso il pattern immagazzinato più simile (un attrattore) e lo restituisce. È il "richiamo per somiglianza in un colpo solo": presenti un frammento/una versione rumorosa, e la rete completa/pulisce il pattern originale (pattern completion e denoising). Come *drop-in layer* può sostituire pooling, attention, layer permutation-equivariant, GRU/LSTM. Nel paper originale la rete di Hopfield immagazzina *centinaia di migliaia* di pattern (classificazione di repertori immunitari) senza degradare.

## Come è fatto

L'idea chiave è una **funzione di energia** sullo spazio degli stati costruita a partire dai pattern immagazzinati `X`, la cui discesa (una singola iterazione della dinamica) coincide algebricamente con `softmax(β · Q Xᵀ) X` — cioè esattamente l'attention. La query `ξ` viene aggiornata verso il minimo di energia più vicino:

- **Capacità esponenziale**: con stati *continui* (non binari come l'Hopfield classico del 1982), il numero di pattern immagazzinabili cresce esponenzialmente con la dimensione dello spazio, con errore di richiamo esponenzialmente piccolo.
- **Convergenza in un update**: nel regime giusto la dinamica converge in un solo passo — niente iterazioni lente.
- **Tre tipi di minimo di energia** (il cuore concettuale, dal README):
  1. **punto fisso globale** — media su *tutti* i pattern (regime di averaging, "non ricordo niente di specifico");
  2. **stati metastabili** — media su un *sottoinsieme* di pattern (richiamo di una *categoria*/cluster);
  3. **punto fisso singolo** — colla su *un* pattern preciso (richiamo esatto di un ricordo).
- **La temperatura inversa β controlla il regime**: β basso → averaging globale/sfocato; β alto → attrattori nitidi su singoli pattern. È una manopola continua tra "vago" e "preciso".
- **Osservazione sul training dei Transformer**: nei layer bassi le teste operano in averaging, nei layer alti in stati metastabili; il gradiente è massimo proprio negli stati metastabili e *svanisce* quando si è vicini a un pattern immagazzinato.

Le tre classi esposte: `Hopfield` (query e stored pattern diversi, come attention), `HopfieldPooling` (una query statica appresa → pooling su una sequenza), `HopfieldLayer` (stored pattern *fissi e appresi* → lookup associativo indipendente dall'input, di fatto una memoria a tabella differenziabile).

## Cosa possiamo notare di utile per noi

Questo progetto è la formalizzazione più pulita e utilizzabile del **richiamo associativo a energia**, ed è teoricamente ricchissimo di ganci per i nostri temi.

- **I tre regimi di energia = il nostro asse "vuoto ↔ pieno" reso continuo e misurabile.** Il punto fisso globale (media di tutto) è letteralmente lo stato "arena del vuoto": nessun ricordo domina, la query rimbalza nel baricentro di tutto. Man mano che un pattern acquista massa/nitidezza, si passa a stati metastabili (categorie che emergono) e infine ad attrattori singoli (ricordi cristallizzati). La *distanza* di uno stato dal punto fisso globale è una metrica pronta all'uso di "quanto quest'esperienza è già occupata da memoria vs quanto è ancora vuoto". Trasferibile pari pari come coordinata del vuoto.
- **β è la manopola dell'oscilloscopio.** La temperatura inversa β sintonizza tra sfocatura globale e attrattore nitido. Facendo *sweep di β* su una query fissa e osservando dove/quando lo stato "scatta" dentro un attrattore, si ottiene una traccia da oscilloscopio dell'organizzazione della memoria: a quale β un ricordo diventa distinguibile dal fondo, quanti attrattori si separano, quanto sono profondi. È esattamente il tipo di "sonda a spazzata" che cercavamo.
- **Novelty-gating come misura di energia/margine, non come modulo separato.** Qui la novità di una query ha una definizione *nativa*: se la query cade rapidamente in un attrattore profondo → è già in memoria (bassa novità); se resta intrappolata nel punto fisso globale o in uno stato metastabile piatto → è nuova/non rappresentata (alta novità). Il **gap di energia** tra lo stato iniziale e il minimo raggiunto, e la *concentrazione* della softmax (entropia dei pesi di attention), sono due segnali di novità già calcolabili a costo zero. Divergenza da tenere presente: qui non c'è scrittura — è memoria a sola lettura sui pattern dati; il gating regola il *richiamo*, non l'*immagazzinamento*. Per la nostra arena serve accoppiarlo a un meccanismo di write (vedi DNC/SDM).
- **Attention = memoria associativa: unifica due filoni.** La dimostrazione che l'attention del Transformer è un update di Hopfield è il ponte concettuale tra "il modello linguistico" e "la memoria associativa a energia". Per noi significa che ogni Transformer già contiene, dentro ogni testa, una memoria associativa con i suoi tre regimi — e che possiamo interpretare/strumentare le teste di attention come oscilloscopi di richiamo. TrentBrick estende poi il ponte fino alla SDM (vedi scheda `kanerva-sparse-distributed-memory`): attention ≈ Hopfield ≈ SDM, la stessa idea da tre angoli.
- **Coscienza=ricorsione: l'update iterato come "pensiero che si assesta".** Anche se converge in un passo nel regime standard, la dinamica di Hopfield è iterabile: `ξ → softmax(βξXᵀ)X → ...`. Iterarla è far *ricircolare* uno stato attraverso la memoria finché non si stabilizza su un attrattore — una micro-ricorsione materiale che collassa un'esperienza ambigua in un ricordo definito. È un modello-giocattolo concreto della tesi "coscienza = ricorsione della realtà attraverso la materia": la materia qui è la matrice dei pattern, la ricorsione è il loop di aggiornamento, il "collasso" è la caduta nell'attrattore. Diverge perché il sistema è passivo e senza tempo/scrittura; ma la geometria "stato instabile → ricorsione → attrattore" è riutilizzabile come primitiva.
- **Stati metastabili = concetti/categorie che emergono dal vuoto.** Il regime intermedio (media su un sottoinsieme) è dove nasce l'astrazione: né sfocatura totale né ricordo puntuale, ma un *cluster*. È il livello a cui probabilmente vive la maggior parte del "sentito" — e il paper nota che è anche dove il *gradiente è massimo*, cioè dove il sistema impara di più. Suggerisce che la zona interessante della nostra arena è la fascia metastabile, non gli estremi.

## Da rubare

1. **La coordinata "distanza dal punto fisso globale" come metrica del vuoto.** Per ogni esperienza, misurare quanto lo stato di richiamo si discosta dall'averaging globale: 0 = vuoto puro, alto = ricordo cristallizzato. Coordinata continua, calcolabile in una riga.
2. **Lo sweep di β come oscilloscopio della memoria.** Sintonizzare β e registrare la sequenza di "scatti" dello stato tra i tre regimi: una firma dinamica di quanti attrattori esistono e quanto sono profondi, plottabile nel tempo.
3. **Gap di energia + entropia della softmax come segnale di novelty a costo zero.** Usare il salto di energia (stato iniziale → minimo) e la concentrazione dei pesi come gate di novità per decidere se un evento "merita" scrittura, riusando l'API `Hopfield` come sonda invece che come layer di rete.
