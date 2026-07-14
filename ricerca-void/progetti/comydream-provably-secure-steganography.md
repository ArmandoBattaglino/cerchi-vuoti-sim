# Provably Secure Steganography — Must-read Papers (mappa curata)

Link: https://github.com/comydream/provably-secure-steganography

Stelle: ~22 · Linguaggio: n/a (repo di curation, Markdown) · Attivita: manutenuto attivamente (push set 2025) · Licenza: non dichiarata

## Cosa fa
Non e' codice: e' la **mappa unificata** del campo della steganografia generativa provably-secure, curata da uno degli autori di Discop (comydream/Jinyang Ding). Raccoglie e classifica in una tabella ragionata i lavori che contano — dalle basi teoriche (Shannon 1949, Cachin 1998, Fridrich 2009) fino agli schemi moderni — indicando per ciascuno l'abbreviazione, il **dominio di embedding** (dove viene nascosta l'informazione) e soprattutto i **drawback** (il difetto chiave). E' la bussola per capire dove sta ogni metodo sulla frontiera sicurezza/efficienza/velocita', con link a paper, citazioni e repo di codice.

## Come e fatto
Il valore e' nella tassonomia. Ordina i metodi in famiglie per "come" nascondono:
- **Basic Theories**: Shannon (secrecy systems), Cachin (modello teorico-informazionale della steganografia, definisce la sicurezza come distanza KL nulla tra cover e stego), Fridrich (sicurezza steganografica).
- **Rejection sampling-based** (Hopper/von Ahn/Backes-Cachin, CRYPTO'02 in poi): i primi provably-secure, dominio = f(stego); drawback: lenti e inefficienti.
- **Arithmetic coding-based** (Le'03, Yang'18, **Ziegler EMNLP'19 = STEGASURAS**, Chen TDSC'21): nascondono negli indici dei token; drawback: "not secure" (perturbano la distribuzione).
- **Meteor** (Kaptchuk CCS'21): token indexes; drawback: lento (con sort) o inefficiente (senza).
- **Grouping-based / ADG** (Zhang ACL'21): group indexes; drawback: not secure.
- **Coupling-based / iMEC** (Schroeder de Witt et al., ICLR'23): token indexes; drawback: lento — ma perfetto.
- **Distribution copies-based / Discop** (Ding S&P'23): copy indexes; sicuro e ad alta capacita'.

La colonna "Drawbacks" e' la parte piu' preziosa: e' un giudizio onesto e sintetico sul tallone d'Achille di ogni approccio, cosi vedi subito il trade-off (sicurezza dimostrabile <-> velocita' <-> capacita').

## Cosa possiamo notare di utile per noi
Per il tuo lavoro questo repo vale come **cartografia gia' fatta del territorio occultamento** — esattamente il tipo di sintesi che eviti di rifare da zero. Ti da' in un colpo la traiettoria storica: si parte dal rejection sampling (sicuro ma lento), si passa all'arithmetic coding (veloce ma NON sicuro, perche' deforma la distribuzione — e' il difetto di STEGASURAS), e si arriva a due modi diversi di ottenere la sicurezza vera preservando il marginale: coupling a entropia minima (iMEC, perfetto ma lento) e copie di distribuzione (Discop, veloce e capiente). Questa progressione e' una lezione metodologica trasferibile ben oltre la steganografia: ogni volta che vuoi far convivere una superficie-innocente con un canale-nascosto, il campo ti dice che il criterio d'oro e' **preservare esattamente il marginale osservabile** (la definizione di Cachin: KL(cover||stego)=0), e che il gioco vero e' quanto puoi avvicinarti al limite di capacita' senza rompere quel vincolo. E' la stessa tensione che hai tra "l'arena deve continuare a sembrare se stessa" e "voglio in-scriverci dentro memoria/stato/messaggio". Il modello di sicurezza di Cachin (indistinguibilita' come distanza tra distribuzioni) e' anche un candidato diretto come definizione formale per i tuoi oscilloscopi: un osservabile "non rivela nulla" se e solo se la sua distribuzione con e senza il contenuto nascosto e' la stessa. Divergenza onesta: e' una reading list, non uno strumento; il valore e' orientativo, non eseguibile. Ma e' la porta d'ingresso corretta al cluster e ti dice quali due repo clonare davvero (Discop e iMEC).

## Da rubare
1. **La tabella famiglia -> dominio-di-embedding -> drawback** come template mentale: quando valuti un tuo meccanismo di occultamento, chiediti sempre quelle tre cose (in che spazio nascondo? qual e' il difetto strutturale? preserva il marginale?). Riduce mesi di reinvenzione.
2. **Il criterio di Cachin (KL cover||stego = 0) come definizione operativa di "invisibile"**: adottalo come specifica formale per l'oscilloscopio — un canale e' nascosto sse le due distribuzioni dell'osservabile coincidono. Ti da' un test statistico concreto invece di un giudizio a occhio.
3. **La shortlist implicita**: il repo dice, senza dirlo, che i due punti non-dominati della frontiera sono iMEC (sicurezza perfetta) e Discop (capacita'+velocita'). Se devi implementare, parti da quei due e salta i metodi "not secure" o "slow" gia' etichettati come tali.
