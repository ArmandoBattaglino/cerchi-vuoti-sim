# EM-LLM — Human-inspired Episodic Memory

Link: https://github.com/em-llm/EM-LLM-model

Stelle: ~279 · Linguaggio: Python (PyTorch, HuggingFace) · Attivita: stabile/matura (push mar 2025, repo consultato lug 2026) · Licenza: MIT

## Cosa fa
Codice del paper ICLR 2025 (Fountas et al., Huawei Noah's Ark + UCL). EM-LLM da' a un LLM una memoria episodica in stile umano senza alcun fine-tuning: segmenta il flusso di token in "eventi" e li recupera all'occorrenza, permettendo contesti praticamente infiniti (retrieval dimostrato su 10M token) a costo computazionale sostenibile. Batte InfLLM (SOTA retrieval) e supera RAG su LongBench e infinity-Bench, arrivando in molti task sopra i modelli full-context.

## Come e fatto
Due fasi, per ogni layer del modello. Formazione: il flusso di token viene tagliato in eventi ai punti di alta sorpresa bayesiana (surprise-gated: dove il modello e' piu sorpreso dal token successivo cade un confine), poi i confini vengono raffinati con metriche di teoria dei grafi (modularity/conductance sulla matrice di adiacenza tra token) per rendere gli eventi coesi. Recupero a due stadi: k-NN sui token rappresentativi di ogni evento (similarita) PIU un buffer di contiguita' temporale che tira dentro anche gli eventi adiacenti nel tempo - proprio come il ricordo umano, che dall'evento saltato ripesca cio che gli sta accanto. Parametri chiave nel YAML: `surprisal_threshold_gamma` (soglia in deviazioni standard), `min/max_block_size`, `n_mem`, `contiguity_buffer_size`. Tutto online, con offload su CPU/disco per sequenze enormi.

## Perche riguarda te
E' il riferimento piu diretto e pulito per la memoria novelty-gated: il confine di un ricordo cade dove c'e' sorpresa, non a intervalli fissi. E' la stessa quantita' (sorpresa bayesiana) che RxInfer minimizza nella tua lista - qui viene invece usata costruttivamente come segnale di segmentazione. Sul lato coscienza-ricorsione, il recupero similarita'+contiguita' e' un modello concreto di come un'esperienza richiami sia cio che le somiglia sia cio che le stava vicino nel tempo, ricostruendo il flusso. Per l'arena del vuoto e gli oscilloscopi: la sorpresa e' esattamente la lettura che vorresti da un oscilloscopio - un tracciato che si accende solo quando l'evento devia dalla predizione, e quel picco definisce automaticamente l'inizio di un nuovo "capitolo" da memorizzare. Divergenza onesta: e' un sistema per LLM di lungo contesto, non un motore di simulazione; ma i suoi due meccanismi (segmentazione per sorpresa, retrieval bimodale) sono algoritmi generali che trasporti fuori dal contesto LLM.

## Da rubare
1. Segmentazione per sorpresa con soglia in deviazioni standard (`gamma`): invece di decidere a priori quando un evento inizia/finisce, misura la sorpresa istante per istante e apri un nuovo segmento quando supera media+gamma*std. E' la ricetta pronta per la memoria novelty-gated dell'arena e per far scattare gli oscilloscopi.
2. Retrieval a due canali similarita'+contiguita': quando richiami un ricordo non prendere solo il piu simile, ma trascina anche i vicini temporali. Per un'arena di particelle significa che riattivare uno stato passato riporta in scena anche cio che gli era adiacente - ricostruzione di scena, non fotogramma isolato.
