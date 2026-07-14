# JEPA-WMs — What drives success in physical planning with Joint-Embedding Predictive World Models? (facebookresearch/jepa-wms)

Link: https://github.com/facebookresearch/jepa-wms

429 stelle · Python (PyTorch) · attivo, rilascio recente (repo creato dic 2025) · licenza custom FAIR (NOASSERTION, research-only)

## Cosa fa
E' il codice, i dati e i pesi ufficiali FAIR del paper omonimo (Terver, Yang, Ponce, Bardes, LeCun). Studia sistematicamente *cosa* rende efficace un world model usato per pianificare azioni fisiche — manipolazione robotica e task di controllo (DROID, RoboCasa, Metaworld, Push-T, PointMaze, Wall). Incarna la tesi di LeCun: un world model utile predice **rappresentazioni latenti future**, non pixel ne token. Fornisce JEPA-WM addestrati e due baseline riprodotte (DINO-WM, V-JEPA-2-AC) per confronto diretto.

## Come e' fatto
L'ossatura JEPA (Joint-Embedding Predictive Architecture):
- Un **encoder congelato pre-addestrato** (DINOv2 ViT-S/14 o DINOv3 ViT-L/16) mappa l'osservazione visiva in un embedding. Non si ricostruiscono i pixel: si lavora sempre nello spazio delle rappresentazioni.
- Un **predittore** (transformer di profondita 6-24) prende l'embedding corrente + l'azione e predice l'embedding al passo successivo. Questo e' il "world model" vero e proprio: dinamica in latent-space.
- La **pianificazione** avviene srotolando il predittore per piu passi immaginati e cercando (via MPC / ottimizzazione, es. CEM) la sequenza di azioni che porta l'embedding finale piu vicino all'embedding-goal. Il modello sogna traiettorie in rappresentazione, non in immagine.
- Head decoder VM2M **opzionali** permettono di ri-visualizzare gli embedding in pixel, ma non servono ne per addestrare ne per pianificare — la visione e' un lusso per l'umano che guarda, non un requisito del sistema.

L'idea-chiave (e il punto del paper): la ricostruzione pixel-perfetta e' uno spreco e spesso danneggia il planning; cio che conta e' che lo spazio latente predetto sia *sufficiente* per distinguere gli stati rilevanti al compito. Il paper isola quali scelte (encoder, profondita del predittore, come si costruisce il target di training) muovono davvero il successo.

## Perche riguarda te
E' il polo "scientifico/robotico" del dibattito world-model-vs-LLM e il contrappunto rigoroso al World Models di hardmaru: stessa idea di sognare traiettorie, ma con la tesi forte che il sogno va fatto **in spazio di rappresentazione astratta**, non ricostruendo l'apparenza. Per la tua tesi coscienza-ricorsione e' rilevante perche mette al centro una domanda che ti riguarda: qual e' il *livello giusto* a cui un sistema deve modellare se stesso e il mondo? Non i pixel (troppo, rumore irrilevante), non i simboli/token (troppo poco, gia digeriti dall'umano), ma una rappresentazione intermedia auto-appresa. Il fatto che il decoder-in-pixel sia opzionale e' filosoficamente vicino al tuo oscilloscopio: la lettura visiva e' uno strumento esterno che possiamo attaccare o staccare, mentre la "vita" del sistema sta tutta nello spazio latente. Dove diverge: qui non c'e' emergenza aperta ne novelty — il world model e' un mezzo per raggiungere un goal esterno fissato (MPC verso un embedding-target), congelato dopo il training. Zero auto-organizzazione, zero ricorsione del sistema su se stesso: e' ingegneria del planning, non modello di coscienza.

## Da rubare
1. **Predire nello spazio di rappresentazione, non nei pixel**: se costruisci un modello predittivo dell'arena, non fargli allucinare i frame — fagli predire embedding (DINO o un encoder che addestri tu). E' piu robusto, piu economico, e la "distanza fra stati" diventa naturalmente una distanza in latent-space (riutilizzabile come metrica di novelty, vedi ASAL).
2. **Decoder-in-pixel come strumento staccabile**: tieni la dinamica del tuo sistema puramente in latent-space e aggiungi un decoder solo come "oscilloscopio" on-demand per visualizzare cosa sta immaginando. Separare nettamente il substrato-che-vive (latente) dallo strumento-che-guarda (decoder) e' un pattern architetturale pulito da imitare nell'arena del vuoto.
