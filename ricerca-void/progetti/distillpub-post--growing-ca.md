# Growing Neural Cellular Automata — distillpub/post--growing-ca

Link: https://github.com/distillpub/post--growing-ca · articolo: https://distill.pub/2020/growing-ca/

104 stelle · HTML/JS + notebook · ultimo push 2022 · licenza CC-BY-4.0 · Mordvintsev, Randazzo, Niklasson, Levin (Distill 2020)

## Cosa fa
E' il codice e l'articolo interattivo di "Growing Neural Cellular Automata": un automa cellulare in cui **ogni cella e' identica** e gira la stessa piccola rete neurale, e queste celle imparano collettivamente a crescere da un singolo pixel-seme fino a formare un'immagine-target (una lucertola-emoji, ecc.) e — cosa notevole — a **rigenerarla** se viene danneggiata. Nessun controllo centrale: la forma globale emerge da regole locali identiche, iterate nel tempo. E' la dimostrazione fondativa di **morfogenesi differenziabile** — auto-organizzazione ottenuta per discesa del gradiente.

## Come e' fatto
Ogni cella ha un vettore di stato di 16 canali: i primi 4 sono RGBA (visibili), gli altri 12 sono **canali nascosti** — memoria interna che le celle usano per coordinarsi, senza significato imposto da fuori. Un passo di update e':
- **Percezione**: ogni cella guarda il proprio stato e quello dei vicini immediati tramite filtri di Sobel fissi (gradienti x/y) + identita — cioe percepisce solo localmente, un intorno 3x3.
- **Regola**: una piccola rete (un paio di layer, condivisa da tutte le celle) mappa il vettore percepito in un incremento di stato `Δstate`. La rete e' l'unica cosa allenata.
- **Stocasticita e vita**: gli update sono applicati in modo asincrono (ogni cella si aggiorna con probabilita casuale) e c'e' una maschera "alive" basata sul canale alpha — celle sotto soglia sono morte. Questo impedisce soluzioni fragili sincronizzate e forza robustezza.
Il training e' end-to-end: si srotolano ~64-96 step, si confronta l'immagine finale col target, si retropropaga attraverso tutti gli step. La rigenerazione emerge **gratis**: allenando anche su stati danneggiati, la rete impara a ricostruire — un attrattore stabile invece di un punto d'arrivo statico.

## Cosa possiamo notare di utile per noi
Questo e' forse il parente piu profondo del tuo lavoro sull'**arena del vuoto** e sulla ricorsione. Tre cose. Primo: i **12 canali nascosti** sono l'esatto analogo di uno stato interno non-visibile che il sistema usa per coordinarsi — sono la "materia oscura" della cella, invisibile dall'output ma indispensabile alla dinamica. Sono il posto naturale dove puntare un oscilloscopio: guardare come si organizzano i canali nascosti *mentre* la forma emerge e' esattamente "leggere lo stato interno" del tuo programma. Secondo: la **rigenerazione come attrattore** e' la versione concreta di "il sistema mantiene la propria forma" — non un target raggiunto e congelato, ma un equilibrio dinamico che resiste alla perturbazione. E' un modello pulito di identita-che-persiste, rilevante per coscienza-come-ricorsione (il sistema che continua a ri-costituirsi). Terzo: regole **puramente locali + identiche** che generano forma globale coerente e' la prova che non serve un controllore centrale — la forma e' un fatto emergente del campo, non un piano imposto: la stessa filosofia della tua particle-life.
Dove diverge: qui c'e' un target esplicito e differenziabile (l'immagine finale), quindi il sistema e' *addestrato a convergere*, non a esplorare open-ended; non c'e' novelty ne memoria episodica — l'unica "memoria" sono i canali nascosti entro un singolo rollout. Il tuo salto e' togliere il target fisso e sostituire la loss-verso-un'immagine con un gate di novelty che premia il nuovo invece del previsto. Ma il substrato — celle identiche, stato nascosto, update stocastico locale, attrattore auto-riparante — e' esattamente il tipo di motore su cui montare i tuoi strati.

## Da rubare
1. **I canali nascosti come stato interno ispezionabile**: adotta lo split "pochi canali visibili + molti canali nascosti" per le tue celle/particelle, e monta l'oscilloscopio proprio sui nascosti — visualizza come si strutturano nel tempo per leggere la "cognizione" interna del campo mentre emerge la forma.
2. **La rigenerazione-come-attrattore via training su stati danneggiati**: perturba lo stato a meta rollout e premia il ritorno alla configurazione — ottieni gratis identita che persiste e resiste al danno, un modello concreto di coscienza-come-ricorsione (il sistema che si ri-costituisce).
3. **Update asincrono + maschera "alive"**: applica gli aggiornamenti stocasticamente e uccidi le celle sotto soglia. E' il trucco che rende la dinamica robusta e non-fragile, e ti da nascita/morte di regioni come fenomeno emergente nell'arena — non hard-coded.
