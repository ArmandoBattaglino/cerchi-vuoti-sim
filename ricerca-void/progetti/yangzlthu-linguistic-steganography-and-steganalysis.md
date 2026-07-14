# YangzlTHU/Linguistic-Steganography-and-Steganalysis

<https://github.com/YangzlTHU/Linguistic-Steganography-and-Steganalysis>

Stelle: ~35 · Linguaggio: Python · Ultimo push: nov 2022 (fermo) · Licenza: nessuna dichiarata

## Cosa fa

È una collezione-vetrina del NGN-lab di Tsinghua che raccoglie in un unico repo il loro filone di lavoro su due lati speculari: la **steganografia linguistica** (nascondere un messaggio segreto DENTRO testo generato che sembra normale) e la **steganalisi** (il lato difensivo: distinguere un covertext benigno da uno che porta un carico nascosto). Sul lato generativo include RNN-Stega, VAE-Stega, KC-Stega (generazione vincolata a keyword), ADG-steganography (Adaptive Dynamic Grouping, "provably secure") e lavori sullo spostamento dallo spazio simbolico allo spazio semantico. Sul lato detection include TS-RNN, TS-CNN, SeSy e varianti attention/graph-based. C'è anche una cartella `Dataset` che prova a simulare corpus reali. Non è una libreria unificata ma un archivio di sotto-progetti, ognuno con proprio README, codice e tabelle di risultati.

## Come è fatto

L'idea chiave della steganografia generativa qui è che il messaggio segreto **controlla il campionamento del linguaggio**: invece di scegliere il prossimo token per massimizzare la probabilità, si partiziona la distribuzione di probabilità in gruppi e la scelta del gruppo è dettata dai bit segreti. RNN-Stega usa Huffman/arithmetic coding sui token; ADG (Adaptive Dynamic Grouping) raggruppa dinamicamente i token in modo che la distribuzione risultante resti il più vicino possibile a quella naturale del modello — da qui la "provable security" (l'entropia del testo stego è indistinguibile da quella del covertext). VAE-Stega interviene sullo spazio latente per migliorare l'impercettibilità statistica. Il lato steganalisi (TS-RNN/TS-CNN/SeSy) sono classificatori addestrati a fiutare la **firma statistica** che l'incorporamento lascia: anche quando il testo è fluente a occhio umano, la distribuzione dei token si sposta rispetto al baseline naturale, e una rete impara a leggere quello spostamento.

## Cosa possiamo notare di utile per noi

Questo repo è il gemello "linguistico" esatto della tua tensione tra **occultamento** e **oscilloscopio**, e vale come mappa concettuale più che come codice riusabile (è vecchio, TF1/PyTorch datato, senza licenza).

- **Il vuoto come budget di entropia.** La lezione trasferibile più forte: nascondere informazione = spendere l'entropia libera della distribuzione. ADG dice esplicitamente che puoi occultare in modo "provabilmente sicuro" solo fino a quanta incertezza il generatore ha già. Nella tua arena del vuoto, questo è un principio fisico: un segnale nascosto in uno stato interno è impercettibile solo se sta dentro il "gioco" (variance/entropia) che quello stato aveva comunque — appena eccedi, emergi come anomalia. È un tetto teorico al canale nascosto, misurabile.
- **Steganalisi = oscilloscopio addestrato.** TS-RNN/SeSy sono letteralmente sonde che leggono uno stato (sequenza di token) e dicono "qui c'è qualcosa di nascosto". Traslato ai tuoi oscilloscopi su stati interni: invece di sonde disegnate a mano, addestri una piccola rete a distinguere "traiettoria interna spontanea" vs "traiettoria che porta un carico/una struttura iniettata". La firma non è nel contenuto ma nello *scostamento dal baseline naturale* — è la stessa cosa che fai quando cerchi novità novelty-gated: novità = deviazione statistica dal previsto.
- **Simmetria generatore↔rilevatore come loop di coscienza.** Il co-design stego/steganalisi è un mini-modello del tuo "coscienza = ricorsione": il sistema che genera e il sistema che si auto-ispeziona sono lo stesso spazio letto da due direzioni. Un'arena dove le particelle sia occultano che rilevano occultamento chiude un anello di auto-osservazione senza scomodare linguaggio.
- **Dove diverge:** è tutto supervisionato, task-specifico, su testo — nessuna nozione di world-model, sogno o memoria episodica. Non ti serve il codice; ti serve la *coppia di concetti* (canale = entropia disponibile; rilevatore = classificatore di scostamento).

## Da rubare

1. **Metrica "budget di occultamento" per l'arena:** per ogni stato interno calcola l'entropia/variance locale spontanea; definisci la capacità di canale nascosto come frazione di quell'entropia. Un segnale iniettato oltre soglia diventa rilevabile — usalo come legge quantitativa di steganografia nel tuo simulatore.
2. **Sonda-oscilloscopio appresa (TS-style):** addestra un classificatore leggero a separare traiettorie "vergini" da traiettorie con struttura iniettata, e usa la sua confidence come lettura continua dell'oscilloscopio, non solo un allarme binario.
3. **Loop stego↔steganalisi come test di ricorsione:** fai coevolvere nella stessa arena chi nasconde e chi rileva; l'equilibrio (o l'oscillazione) tra i due è un osservabile emergente dell'auto-osservazione ricorsiva.
