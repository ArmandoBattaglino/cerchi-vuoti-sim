# realtime-flowlenia — Flow-Lenia GPU in tempo reale ([repo](https://github.com/ochyai/realtime-flowlenia))

Stelle: 16 · Linguaggio: Python (PyTorch) · Ultima attività: febbraio 2026 · Licenza: MIT

## Cosa fa
È un'implementazione real-time e GPU-accelerata di **Flow-Lenia**, la variante di Lenia (automa cellulare continuo) che aggiunge la **conservazione della massa**: la materia non appare/scompare, viene *trasportata* (advection) attraverso il campo, così le "creature" che emergono si comportano come blob di sostanza fluida invece che come pattern di intensità arbitraria. Gira a 512x512 a 30+ FPS su Apple Silicon (MPS) e più veloce su CUDA, con upscale a 1024 per il display. La caratteristica distintiva rispetto ad altre demo di Lenia è il livello di **rendering "liquid shader"**: distorsione fluida, interferenza a film sottile (i colori iridescenti tipo bolla di sapone), glow/bloom. E soprattutto è **interattivo**: col mouse perturbi il campo e le creature si riorganizzano dal vivo, in diretta.

## Come è fatto
Il cuore è il ciclo Lenia standard — convoluzione con un kernel (di solito a anelli gaussiani) → funzione di crescita → aggiornamento del campo — ma con due aggiunte cruciali di Flow-Lenia:
1. **Campo di flusso**: dal gradiente del potenziale si deriva un campo di velocità, e la massa viene trasportata lungo quel campo tramite advection. Nel repo questo è implementato con `grid_sample` di PyTorch (sampling bilineare del campo alle posizioni advette) nella versione GPU, e con "reintegration tracking" (schema di trasporto conservativo più accurato) nella versione engine. È qui che la conservazione della massa diventa esatta.
2. **Modulazione multi-armonica dei parametri nel tempo**: i parametri (μ, σ della growth, ecc.) "respirano" con oscillazioni a più frequenze, il che impedisce alle configurazioni di collassare in punti fissi morti e le tiene perennemente vive/metastabili.
La versione CoreML fa mixed-precision chirurgica (fp16 per la growth, fp32 per le coordinate — le coordinate non tollerano la perdita di precisione), `torch.compile` per fondere i kernel, e offload opzionale del rendering su ANE. C'è anche l'auto-evoluzione: ogni ~20s interpola dolcemente verso un nuovo set di parametri casuali, esplorando lo spazio delle dinamiche da solo. Quattro file = quattro entry point (gpu, coreml, engine con reintegration, cpu viewer).

## Cosa possiamo notare di utile per noi
Questo è, letteralmente, un prototipo funzionante della tua **arena del vuoto/particelle** con **oscilloscopio visivo integrato**. Le corrispondenze sono quasi uno-a-uno:
- **Arena di materia-flusso**: Flow-Lenia *è* un vuoto continuo in cui la materia si auto-organizza in enti localizzati e persistenti, con conservazione della massa — esattamente il substrato fisico che cerchi, non particelle discrete ma un campo continuo dove il "qualcosa" emerge dal "quasi-niente". La conservazione della massa è il vincolo che rende gli enti *reali* (hanno una quantità, non solo una forma), ed è ciò che distingue un'arena con ontologia da un semplice pattern grafico.
- **Perturbazione live = interrogazione dell'arena**: il mouse che perturba e le creature che si riorganizzano è la forma più diretta di "oscilloscopio attivo" — non solo osservi lo stato, lo *stimoli* e guardi la risposta. Per il tuo lavoro sulla ricorsione/coscienza questo è oro: la firma di un sistema con struttura interna è *come reagisce a una perturbazione*, non come appare a riposo.
- **Modulazione multi-armonica contro la morte**: il trucco del "respiro" dei parametri risolve un problema che avrai anche tu — le arene tendono o a esplodere o a congelarsi. Tenere i parametri in oscillazione dolce li mantiene sul bordo del caos, dove vive la novelty. Questo si lega direttamente al **novelty-gating**: la memoria dovrebbe ingaggiarsi proprio quando l'arena produce configurazioni fuori dal repertorio periodico atteso.

Dove diverge: Flow-Lenia non ha memoria, né un world-model, né ricorsione — è puramente reattivo, markoviano, senza stato oltre il campo corrente. È il *substrato* del tuo progetto, non il progetto. Il rendering liquid-shader è spettacolare ma è cosmesi: per un oscilloscopio *scientifico* sugli stati interni ti serve il contrario, visualizzazioni fedeli e misurabili (mappe di massa, di velocità, di novelty), non iridescenze che mascherano la struttura. Prendi il motore, ignora lo shader.

Collegamento al **world-model-come-sogno**: un'arena Flow-Lenia differenziabile e veloce può fare da *ambiente sognato* dentro cui un agente predice/pianifica. Gira a 30+ FPS: abbastanza da usarla come rollout immaginativo in tempo reale.

## Da rubare
1. **Il motore Flow-Lenia con advection via `grid_sample` + reintegration tracking** come substrato dell'arena del vuoto: dà gratis la conservazione della massa (enti con quantità reale) e gira real-time su GPU consumer/Apple Silicon.
2. **Modulazione multi-armonica dei parametri** per tenere l'arena eternamente metastabile sul bordo del caos — antidoto diretto al collasso in punto fisso o all'esplosione, e generatore naturale di novelty per la memoria.
3. **Perturbazione interattiva come primitiva di oscilloscopio**: implementa "clicca e stimola, poi misura la risposta transitoria" come strumento base per sondare la struttura interna dell'arena, non solo osservarla passivamente.
