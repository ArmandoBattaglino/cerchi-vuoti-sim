# RxInfer.jl

Link: https://github.com/ReactiveBayes/RxInfer.jl

Stelle: ~409 · Linguaggio: Julia (repo etichettato Jupyter per gli esempi) · Attivita: molto viva (push lug 2026) · Licenza: MIT

## Cosa fa
Pacchetto Julia per inferenza bayesiana automatica su factor graph tramite reactive message passing. Dato un modello probabilistico dichiarato, RxInfer usa la struttura del modello per generare un algoritmo fatto di una sequenza di calcoli locali sul grafo dei fattori, invece di un solutore centralizzato. E' l'engine che rende trattabile l'active inference in tempo reale (robotica, controllo, filtraggio di stato). Sfrutta le coppie coniugate likelihood-prior per posterior analitiche, battendo i sampler general-purpose (HMC/Turing) in velocita e accuratezza sui modelli congiunti.

## Come e fatto
Il modello viene rappresentato come factor graph: nodi-variabile e nodi-fattore collegati da edge. L'inferenza e' letteralmente passaggio di messaggi locali lungo gli edge (belief propagation / variational message passing): ogni nodo calcola il proprio messaggio in uscita solo da cio che riceve dai vicini, e i messaggi si propagano finche le credenze convergono. Il "reactive" viene da Rx (observable/stream): quando arriva un nuovo dato, il grafo ricalcola in modo incrementale solo cio che e' cambiato, quindi funziona su stream in tempo reale. Nessuna hyperparametrizzazione da tarare per l'inferenza esatta nei modelli coniugati.

## Perche riguarda te
E' l'anello mancante sul lato "coscienza-ricorsione" inteso come modello del mondo. Qui la mente non e' un calcolo centrale ma un grafo di credenze aggiornate per messaggi locali tra nodi in relazione - esattamente la forma "ricorsione/relazioni, non un computer centrale" che cerchi. Sotto c'e' l'active inference / free-energy: un agente mantiene un modello generativo e agisce per minimizzare la sorpresa. Nota il ponte con EM-LLM nella tua lista: la stessa "sorpresa bayesiana" che RxInfer minimizza e' cio che EM-LLM usa come confine di memoria - due usi opposti della stessa quantita. Divergenza onesta: RxInfer e' matematica pesante (Julia, coniugazione, message passing) e non e' un motore di simulazione visuale; non lo faresti girare dentro l'arena, ma e' il riferimento teorico su come modellare percezione/aggiornamento in modo puramente locale.

## Da rubare
1. Il principio "belief come messaggi locali su un grafo": se le tue particelle/agenti nell'arena devono avere un modello del mondo, dagli uno stato di credenza che si aggiorna solo dai vicini - niente stato globale condiviso. E' lo stesso pattern locale dei NCA, ma applicato alle credenze invece che alla materia.
2. La sorpresa bayesiana come segnale di controllo: usa la sorpresa (quanto un'osservazione devia dalla predizione) sia come trigger che come metrica di novelty - la stessa idea che ti serve per la memoria novelty-gated e per far reagire un oscilloscopio solo agli eventi inattesi, non a tutto il flusso.
