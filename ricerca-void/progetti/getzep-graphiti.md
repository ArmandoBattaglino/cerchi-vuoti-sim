# Graphiti (Zep) — [getzep/graphiti](https://github.com/getzep/graphiti)

~28.7k stelle · Python · attivo (push luglio 2026) · Apache-2.0 · topics: agents, graph, llms, rag

## Cosa fa
Graphiti costruisce e interroga **context graph temporali** per agenti AI. A differenza dei knowledge graph statici, ogni fatto ha una finestra di validita temporale (quando e diventato vero, quando e stato superato), mantiene la provenienza fino al dato grezzo, e supporta ontologie sia prescritte sia apprese. E il motore open-source dietro Zep, che il team rivendica come state-of-the-art nella agent memory (paper arXiv 2501.13956).

## Come e fatto
Quattro componenti: **Entities** (nodi: persone, prodotti, concetti — con summary che evolvono nel tempo), **Facts/Relationships** (archi: triple Entita→Relazione→Entita con finestra di validita), **Episodes** (la provenienza: il dato grezzo ingerito da cui ogni fatto deriva), **Custom Types** (ontologia definita via modelli Pydantic). L'idea chiave e il modello **bi-temporale**: quando l'informazione cambia, il vecchio fatto NON viene cancellato ma **invalidato** — resta interrogabile "cosa era vero a marzo". Aggiornamenti incrementali senza ricalcolo dell'intero grafo, retrieval ibrido (semantico + keyword + traversal del grafo).

## Perche riguarda te
Questo e il pezzo piu direttamente saccheggiabile per la tua **memoria novelty-gated**. Graphiti risolve, in produzione e con un paper dietro, il problema che ti interessa: come una memoria puo modellare il *tempo* e la *revisione delle credenze* invece di essere un blob append-only. Il concetto "invalida, non cancellare" e esattamente cio che serve a una memoria che deve distinguere cio-che-era-nuovo da cio-che-e-diventato-obsoleto senza perdere la storia. Dove diverge onestamente: Graphiti NON ha un gate di novelty — ingerisce tutto e lascia che l'ontologia emerga; il filtro "questo merita di entrare?" lo devi mettere tu a monte. E anche pesante (richiede un graph DB, LLM per l'estrazione entita): per una sim di particelle-emergenza e sovradimensionato, ti serve l'idea non l'implementazione.

## Da rubare
1. **Fatto = tripla + finestra di validita + puntatore all'episodio grezzo**: adotta questo schema minimo per la tua memoria. Ogni ricordo porta con se `valid_from / valid_until / source`. Il novelty-gate diventa allora "apri una nuova finestra solo se il fatto contraddice o estende quelle esistenti".
2. **Episodes come ground-truth immutabile sotto i fatti derivati**: separare lo stream grezzo osservato (l'oscilloscopio) dai fatti sintetizzati sopra — cosi puoi ri-derivare la memoria con un gate diverso senza aver distrutto l'osservazione originale.
