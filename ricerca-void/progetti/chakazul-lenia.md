# Chakazul/Lenia — [Chakazul/Lenia](https://github.com/Chakazul/Lenia)

Stelle: ~3.8k · Linguaggio: Python (+ JS, Matlab, Jupyter) · Ultima attivita: lug 2024 · Licenza: MIT

## Cosa fa
Repo canonico di Bert Wang-Chak Chan: Lenia e' la generalizzazione continua del Game of Life. Invece di celle 0/1 su griglia con vicinato discreto e tempo a scatti, tutto e' continuo — stato (valori reali in [0,1]), spazio (kernel largo e liscio) e tempo (incrementi infinitesimi). Da questo emergono centinaia di "creature" auto-mantenute (l'orbium che scivola, forme che ruotano, si dividono, reagiscono agli urti) che il repo cataloga in uno zoo di specie (`animals.json`, `animals3D.json`, `animals4D.json`, cartella `found/`). E' il paradigma-padre di Flow-Lenia e Particle Lenia.

## Come e fatto
L'idea chiave sta in poche righe di update. Lo stato `A` evolve cosi: si convolve `A` con un **kernel radiale** `K` (un anello, spesso a picchi multipli/convessita multiple, normalizzato a somma 1), ottenendo un "potenziale" `U = K * A`. Si applica una **funzione di crescita** `G` — tipicamente una gaussiana centrata su un valore-bersaglio `mu` con larghezza `sigma` — che mappa il potenziale in una crescita in [-1, +1]. Si integra: `A <- clip(A + dt * G(U), 0, 1)`. Tutto qui: la vita e' interamente nel triplice `(kernel, mu, sigma, dt)`. Il codice Python scala in N dimensioni (`LeniaND.py`), con varianti multi-kernel (`LeniaNDK.py`) e multi-canale/colore (`LeniaNDKC.py`). Le creature non sono programmate: sono soluzioni stabili (solitoni) di quella singola equazione, trovate esplorando i parametri.

## Perche riguarda te
Lenia e' probabilmente il cuore matematico piu pulito della tua "arena del vuoto" e delle "particelle-emergenza":
- **Emergenza da substrato quasi-vuoto.** Una griglia inizializzata a rumore piu' la giusta regola locale produce entita persistenti e mobili. E' l'esempio piu' nitido di "forma che si auto-mantiene dentro un campo continuo" — esattamente il tipo di oggetto che un'arena del vuoto dovrebbe far nascere.
- **Continuo, non discreto.** Se la tua intuizione e' che la coscienza/ricorsione vive in campi continui piu' che in bit, Lenia e' la palestra: mostra che tutta la ricchezza del Game of Life sopravvive e si amplifica quando togli la griglia rigida.
- **Solitoni come "identita".** Un orbium mantiene la sua identita' pur essendo solo un pattern nel campo — nessuna materia lo compone stabilmente, e' pura ricorsione di forma nel tempo. E' un modello giocattolo fortissimo per la tua tesi "identita = ricorsione della realta attraverso la materia": qui la materia e' liquida e l'identita persiste comunque.
- **Dove diverge:** Lenia e' un campo denso (ogni cella ha uno stato), non particelle discrete. Se vuoi l'oscilloscopio come osservatore locale o particelle vere, guarda le derivate (Particle Lenia). Inoltre Lenia non ha "novelty gate" ne memoria: e' pura dinamica senza traccia storica. Il vuoto qui e' rumore iniziale, non un vuoto attivo che seleziona.

## Da rubare
1. **Il triplet update `(kernel-anello, growth-gaussiana, clip)`** come motore minimo dell'arena: e' 20 righe e ti da subito solitoni auto-mantenuti. Parti da `LeniaND.py`, e' scritto per essere riletto.
2. **Lo zoo come metodo, non solo come dato:** salvare ogni pattern stabile trovato in un JSON con i suoi parametri (`found/`) e' un archivio di "novita' scoperte" esplorando lo spazio dei parametri. E' l'ossatura di una memoria novelty-gated per un'arena: non registri gli stati, registri le *scoperte* (i regimi che producono qualcosa di nuovo e persistente).
