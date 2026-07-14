# Deep Image Steganography — Nascondere un'immagine dentro un'altra con CNN (arnoweng/PyTorch-Deep-Image-Steganography)

Link: https://github.com/arnoweng/PyTorch-Deep-Image-Steganography

140 stelle · Python (PyTorch) · fermo, ultimo push apr 2018 · nessuna licenza

## Cosa fa
Reimplementazione PyTorch del classico "Hiding Images in Plain Sight: Deep Steganography" (Baluja, NIPS 2017). Il sistema nasconde un'intera immagine a colori a piena risoluzione *dentro* un'altra immagine, con alterazioni visivamente impercettibili. Prende in input una cover image e una secret image (entrambe 256×256), produce una container image che a occhio e' indistinguibile dalla cover, e poi un secondo modello riesce a estrarre dalla container la secret quasi intatta. Non e' watermark a pochi bit: e' payload denso — un'immagine intera (centinaia di migliaia di valori) infilata nei bit meno significativi/nella texture di un'altra immagine, ma imparata end-to-end anziche' fissata a mano. Addestrato su 45.000 immagini ImageNet, ~24h su una GTX 1080 Ti.

## Come e' fatto
Due reti convoluzionali addestrate congiuntamente, con una terza rete di preparazione:
- **Prep network** — pre-elabora la secret image, distribuendone l'informazione su tutte le frequenze prima dell'iniezione (evita che stia solo nei bit bassi, dove sarebbe fragile).
- **Hiding network (H-net)** — prende cover + secret preparata e produce la container. E' l'encoder steganografico.
- **Reveal network (R-net)** — prende solo la container e ricostruisce la secret. E' il decoder.

Il training minimizza congiuntamente due loss: `||cover − container||` (l'occultamento deve essere invisibile) e `β·||secret − revealed||` (il payload deve essere recuperabile). Il trade-off tra i due termini e' regolato da β — identico in spirito al gamma/delta dei watermark testuali: piu peso al recupero = piu residuo visibile nella container. Il punto concettuale: l'informazione nascosta non sta in un canale designato a mano (LSB), ma in un pattern distribuito che le reti *scoprono* essere robusto e invisibile, sfruttando la ridondanza percettiva delle immagini naturali. Le "tiny deviations" nel README mostrano che il residuo cover→container e secret→revealed e' quasi rumore.

## Cosa possiamo notare di utile per noi
E' il caso puro di **steganografia a payload denso appreso end-to-end**, ed e' il piu vicino alla tua intuizione che l'occultamento debba emergere da una dinamica ottimizzata, non da una regola fissa (LSB). Tre trasferimenti concreti verso l'arena del vuoto / gli stati interni: (1) L'architettura encoder-carrier / decoder e' esattamente il pattern per **nascondere uno stato dentro un altro stato**. Se pensi al world-model-come-sogno, la H-net e' la prova che un sistema puo trasportare un contenuto latente (la secret) dentro una rappresentazione che sembra "innocua" (la cover) senza che un osservatore lo veda — un modello formale di contenuto occulto/subliminale dentro un portante percepibile. (2) La prep-network che *spalma l'informazione su tutte le frequenze* e' l'anti-LSB: dice che un occultamento robusto distribuisce il segnale, non lo concentra. Per una firma emergente nelle tue particelle, questo suggerisce di cercare la marcatura in correlazioni distribuite tra molti gradi di liberta', non in un singolo canale. (3) Le "deviation maps" (residuo cover−container) sono un **oscilloscopio dell'occultamento**: visualizzano *dove* la rete ha scelto di nascondere, rivelando la struttura del canale covert. Dove diverge dal tuo nucleo: qui l'occultamento e' supervisionato con un target esplicito (la secret data da fuori) e un decoder addestrato a coppia; nel tuo caso ideale la "secret" e' l'auto-modello ricorsivo del sistema e non c'e' un decoder esterno allineato — la firma dovrebbe essere leggibile *dal sistema stesso*, non da una R-net calata dall'alto. Nota anche il rischio: nessuna licenza -> non riusabile in codice, solo come architettura/idea.

## Da rubare
1. **Il pattern encoder-carrier + decoder con doppia loss (invisibilita × recuperabilita)** come scheletro per nascondere uno stato interno dentro un portante osservabile: applicalo per infilare un "marchio" o un contenuto latente nella dinamica dell'arena e verificarne il recupero.
2. **La prep-network che distribuisce il payload su tutte le frequenze**: principio di occultamento robusto = spalmare, non concentrare. Cerca la firma emergente in correlazioni multi-particella, non in un singolo canale.
3. **Le deviation/residual maps come oscilloscopio del canale covert**: visualizza il residuo tra stato-portante e stato-marchiato per *vedere dove* l'informazione si e' nascosta.
