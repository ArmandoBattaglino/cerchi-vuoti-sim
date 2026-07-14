# ngc-learn — [NACLab/ngc-learn](https://github.com/NACLab/ngc-learn)

197 stelle · Python (JAX) · attivo (push lug 2026) · licenza BSD-3-Clause

## Cosa fa
Libreria di neuroscienza computazionale / NeuroAI del Neural Adaptive Computing (NAC) Lab per costruire, simulare e analizzare reti neurali biologicamente plausibili: predictive coding, spiking neural network, circuiti Hebbiani, plasticita STDP. Nasce dal paper Nature Communications 2022 "The neural coding framework for learning generative models" (Ororbia & Kifer). L'idea centrale e l'apprendimento *locale* (credit assignment senza backprop globale) minimizzando energia libera / errore di predizione a ogni livello.

## Come e fatto
Costruita su JAX, con la libreria di simulazione companion `ngcsimlib` (grafi di componenti a tempo discreto) e un "model museum" (`ngc-museum`) che re-implementa modelli storici. Un modello e un grafo di componenti (neuroni, sinapsi, nodi di errore) che si aggiornano per passi temporali: ogni nodo espone il suo stato di membrana, lo spike, e soprattutto il *segnale di errore di predizione* locale. L'apprendimento e una regola locale (Hebbian / delta) che consuma quegli errori, non una catena di gradiente globale.

## Perche riguarda te
E il candidato piu solido come "oscilloscopio su stati interni". A differenza di una rete black-box, qui ogni livello ha uno stato latente e un errore di predizione *ispezionabili a ogni tick* — esattamente il tipo di segnale che vuoi sondare in un'arena dove la coscienza e trattata come dinamica ricorsiva di errore/correzione. Il predictive coding e anche la formalizzazione piu vicina alla tua intuizione "coscienza = ricorsione della realta attraverso la materia": lo stato interno predice il proprio input e si corregge in loop. Diverge dalla tua arena su un punto onesto: qui non ci sono particelle/campi spaziali emergenti, e la dinamica e ingegnerizzata per fare ML (MNIST, generazione), non per far emergere struttura dal vuoto. E un banco di misura, non un mondo.

## Da rubare
1. Il pattern "nodo di errore locale ispezionabile per tick": ogni tua particella/campo espone un residuo predizione-vs-realta leggibile in tempo reale, cosi l'oscilloscopio non guarda solo posizioni ma il *disaccordo interno* del sistema.
2. La regola di aggiornamento locale (Hebbian/delta) come alternativa alla backprop: per far apprendere l'arena senza un obiettivo globale, usa solo informazione disponibile localmente a ciascun elemento — piu coerente con "emergenza dal basso".
