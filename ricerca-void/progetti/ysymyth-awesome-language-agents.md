# CoALA — Cognitive Architectures for Language Agents (ysymyth/awesome-language-agents)

Link: https://github.com/ysymyth/awesome-language-agents · Paper: https://arxiv.org/abs/2309.02427

1244 stelle · TeX / lista curata · ultimo push 2025 · paper Sumers, Yao, Narasimhan, Griffiths (2023)

## Cosa fa
CoALA e' un paper-quadro che rilegge gli agenti LLM come **architetture cognitive** nel senso classico (Soar, ACT-R), invece che come prompt ad hoc. Propone un vocabolario unico per descrivere qualsiasi agente linguistico lungo tre assi: lo spazio delle memorie, lo spazio delle azioni, e il ciclo di decisione. La repo e' la lista curata che classifica centinaia di lavori sugli agenti dentro questo schema, piu il file BibTeX con 300+ citazioni. Serve sia da mappa concettuale del filone sia da indice navigabile per trovare quale lavoro copre quale pezzo dell'architettura.

## Come e' fatto
L'idea chiave e' fattorizzare un agente in componenti ortogonali e nominarli con precisione:
- **Memorie**: una working memory a breve termine + memorie a lungo termine opzionali — **episodica** (esperienze passate), **semantica** (conoscenza sul mondo), **procedurale** (codice / i pesi stessi dell'LLM).
- **Spazio delle azioni** diviso in due meta-tipi: **azioni esterne** (grounding — agire sul mondo) e **azioni interne** che manipolano le memorie: **reasoning** (aggiorna la working memory con l'LLM), **retrieval** (legge dalla memoria a lungo termine), **learning** (scrive nella memoria a lungo termine).
- **Ciclo decisionale** in due fasi: **planning** (usa reasoning/retrieval per proporre e valutare azioni candidate) ed **execution** (esegue l'azione scelta, learning o grounding). Il loop si ripete.
La forza e' che retrieval e learning diventano azioni di *prima classe*, non effetti collaterali: leggere e scrivere la memoria sono mosse che l'agente decide, non magia implicita.

## Cosa possiamo notare di utile per noi
CoALA e' la **spina dorsale concettuale** per formalizzare quello che stai gia facendo in modo intuitivo. La tua memoria novelty-gated corrisponde esattamente all'azione di **learning** (scrittura in memoria a lungo termine) resa condizionale: nel loro schema il "quando scrivere" e' lasciato aperto: il tuo contributo e' *gatarlo sulla novelty*. I tuoi oscilloscopi sugli stati interni sono, nel loro linguaggio, strumenti che ispezionano la **working memory** e la memoria episodica — CoALA ti da il posto preciso dove agganciarli. La distinzione episodica/semantica/procedurale e' preziosa per la tua arena: la traiettoria delle particelle e' episodica, i pattern ricorrenti che estrai sono semantici, e le regole di aggiornamento del campo sono procedurali — separarle chiarisce cosa il sistema sta imparando e a che livello. Il ciclo planning/execution mappa bene sul tuo world-model-come-sogno: la fase di "planning dentro il modello" (proporre e valutare azioni simulandole) e' letteralmente sognare prima di agire.
Dove diverge (fortemente): CoALA e' tutto simbolico-linguistico e centrato sull'LLM; le sue memorie sono testo recuperato per similarita, non stati fisici di un campo. Non ha nessuna nozione di substrato materiale, di ricorsione realta-attraverso-la-materia, ne di emergenza dal basso — l'agente e' un pianificatore sopra un mondo, non un mondo che si osserva. Prendi l'ontologia (i nomi, gli assi, la fattorizzazione), non l'implementazione.

## Da rubare
1. **La tripartizione della memoria** episodica / semantica / procedurale come schema per organizzare cio che la tua arena conserva: traiettorie grezze (episodica), pattern/attrattori estratti (semantica), regole di update (procedurale). Chiarisce a che livello sta avvenendo l'apprendimento.
2. **Learning come azione condizionale esplicita**: modella la scrittura in memoria come una mossa decisa dal sistema (gatata da novelty), non come logging automatico. E' la formalizzazione pulita della tua memoria novelty-gated.
3. **Il ciclo planning-dentro-il-modello / execution-nel-mondo** come struttura per il tuo world-model-come-sogno: separa nettamente la fase in cui il sistema simula e valuta futuri dentro il proprio modello dalla fase in cui agisce sul substrato reale, e misura la divergenza tra le due come segnale.
