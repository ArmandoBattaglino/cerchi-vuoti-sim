# Letta (ex MemGPT) — [letta-ai/letta](https://github.com/letta-ai/letta)

~23.8k stelle · Python · attivo (push luglio 2026) · Apache-2.0 · topics: ai, ai-agents, llm, llm-agent

## Cosa fa
Letta e la piattaforma per **agenti stateful** nata dal paper MemGPT: AI con memoria avanzata che impara e si auto-migliora nel tempo. L'idea fondativa e una gerarchia di memoria in stile sistema-operativo — la context window come RAM, uno storage esterno come disco — con l'LLM che si auto-gestisce, paginando ricordi dentro e fuori dal contesto tramite tool. E lo standard de-facto per agenti con memoria persistente e auto-editante. Nota: il repo ospita ora il server "legacy" V1; lo sviluppo attivo si e spostato su Letta Code (CLI) e Agent SDK.

## Come e fatto
Il cuore concettuale (da MemGPT) e il **memory management gerarchico auto-guidato**: l'LLM non ha solo un contesto passivo, ma tool per leggere/scrivere la propria memoria — decide cosa tenere in "RAM" (core memory editabile) e cosa spostare su "disco" (archival/recall memory recuperabile via ricerca). L'agente e persistente: stato, persona, memoria dell'interlocutore sopravvivono tra le sessioni. Model-agnostico. La nuova generazione aggiunge skills e subagents con memoria e "continual learning" pre-costruiti, e puo girare in cloud (Constellation), locale, o self-hosted.

## Perche riguarda te
Di tutti e quattro, Letta e il piu vicino al nucleo **coscienza-ricorsione / memoria novelty-gated**. Il pattern "l'agente edita la propria memoria con dei tool" e una forma concreta e funzionante di **ricorsione**: il sistema modella e riscrive se stesso. E il ponte piu diretto tra la tua tesi ("coscienza = ricorsione della realta attraverso la materia") e qualcosa di eseguibile: qui la ricorsione e l'agente che si osserva, decide cosa e degno di essere ricordato, e ristruttura la propria core memory. Il tuo novelty-gate e proprio la funzione decisionale che Letta lascia all'LLM (spesso ingenua). Dove diverge onestamente: Letta e ingegneria di prodotto attorno a un LLM commerciale — la "auto-migliora" e prompt + tool, non emergenza dal basso; non c'e substrato di particelle, non c'e vuoto, non c'e auto-organizzazione fisica. E un agente furbo con un blocco note gerarchico, non una coscienza che emerge.

## Da rubare
1. **Memoria a due livelli con paginazione esplicita guidata dall'agente stesso**: core memory piccola e sempre visibile (cio-che-conta-ora) + archival ricercabile (tutto il resto). Il tuo novelty-gate diventa la regola di promozione da archival a core: entra in "RAM" solo cio che e abbastanza nuovo/saliente.
2. **Tool di self-edit della memoria come atto ricorsivo di prima classe**: dare al sistema l'operazione "riscrivi il tuo stato" come azione osservabile (loggabile sull'oscilloscopio) — cosi la ricorsione non e implicita ma un evento che puoi contare e misurare nel tempo.
