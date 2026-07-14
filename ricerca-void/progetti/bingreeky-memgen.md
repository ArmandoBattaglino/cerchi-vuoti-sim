# MemGen — Generative Latent Memory

Link: https://github.com/bingreeky/MemGen

Stelle: ~405 · Linguaggio: Python (PyTorch, framework stile LAVIS) · Attivita: viva (push giu 2026) · Licenza: nessuna dichiarata (attenzione: no LICENSE = niente permessi d'uso espliciti)

## Cosa fa
Implementazione ufficiale del paper ICLR 2026 (arXiv 2509.24704, Zhang/Fu/Yan). MemGen da' a un agente LLM una memoria che vive dentro il flusso di ragionamento invece che in un DB esterno o nei pesi congelati. Due moduli: un Memory Trigger che monitora lo stato di ragionamento e decide QUANDO invocare la memoria, e un Memory Weaver che genera token latenti (non testo leggibile) che incapsulano esperienza passata e vengono intrecciati nella catena di reasoning corrente. La tesi forte: senza supervisione esplicita, sotto training emergono spontaneamente facolta di memoria "umane" (planning, memoria procedurale, working memory).

## Come e fatto
Training in due stadi, un modulo per volta. Il Weaver e' allenato (SFT poi GRPO, reinforcement) a produrre una sequenza latente compatta condizionata sul contesto; questi vettori vengono iniettati nello stream come se fossero token, arricchendo il ragionamento senza espandere il prompt testuale. Il Trigger e' un classificatore leggero sullo stato interno che apre/chiude il rubinetto della memoria - cosi non paghi il costo del richiamo ad ogni passo, solo quando serve. Nel codice il cuore e' `memgen/model/modeling_memgen.py` con una `generate` custom (la vanilla si ottiene sostituendola con l'implementazione commentata). Nota di riproducibilita' dai loro FAQ: FSDP non supportato (solo DDP), e dettagli minuti del template (ChatML, `.` vs `\n` dopo `\boxed{}`) spostano molto le performance - segnale che i gain sono reali ma fragili al setup.

## Perche riguarda te
E' il progetto piu vicino alla tua "memoria latente nei pesi" e soprattutto alla memoria novelty-gated. Il Trigger e' letteralmente un gate: decide quando ricordare guardando lo stato interno, non un timer o una regola fissa. E' l'analogo, sul lato agente-LLM, di cio che nell'arena del vuoto sarebbe "scrivi in memoria solo se l'evento e' abbastanza saliente". Il Weaver invece incarna un'idea forte per la coscienza-ricorsione: la memoria non e' un archivio da rileggere ma un segnale generato al volo che ri-entra nel ragionamento - ricorsione dello stato su se stesso. Divergenza onesta: e' pesante (training RL su LLM, GPU), i checkpoint sono rilasciati solo in parte, e manca la licenza; non e' codice che adotti direttamente, ma l'architettura Trigger+Weaver e' un pattern trasferibile. Diverge anche da EM-LLM: qui la memoria e' generata (token latenti sintetici), la' e' recuperata (segmenti reali del passato) - due filosofie opposte da tenere entrambe in mente.

## Da rubare
1. La separazione Trigger/Weaver: tieni distinti "quando ricordare" (un gate cheap sullo stato interno) da "cosa/come ricordare" (il contenuto). Nella memoria novelty-gated dell'arena questo significa un rilevatore di salienza economico separato dal meccanismo di scrittura/lettura - puoi tararli in modo indipendente.
2. Memoria come segnale generato che rientra nel loop, non come lettura da store: invece di riesumare uno stato passato tale e quale, produci un riassunto latente che si fonde nello stato corrente. Piu vicino alla ricorsione della materia su se stessa che a un log riletto.
