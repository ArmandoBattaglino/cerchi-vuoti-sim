# erwanplantec/FlowLenia

Link: https://github.com/erwanplantec/FlowLenia

Stelle: ~26 · Linguaggio: Python (JAX) · Attivita: ultimo push feb 2024 (poco mantenuto ma stabile) · Licenza: nessuna dichiarata (no LICENSE file — attenzione se vuoi riusare codice)

## Cosa fa
Implementazione in JAX di Flow-Lenia, la variante di Lenia (automa cellulare continuo) firmata dall'autore stesso del paper originale (arXiv 2212.07906). La novita rispetto a Lenia classico e la conservazione della massa: invece di sommare un incremento all'attivazione, il sistema calcola un campo di flusso (advection) e sposta la massa esistente, cosi la quantita totale nel campo si conserva. Questo permette la localizzazione dei parametri (ogni pezzo di materia porta il suo "genoma" locale) e quindi evoluzione open-ended: creature con regole diverse coesistono e competono nello stesso spazio senza confini imposti.

## Come e fatto
Repo piccolo e leggibile: `flowlenia/flowlenia.py` ha i componenti base (Config dataclass, State = attivazioni A, classe FlowLenia che impacchetta step function, calcolo dei kernel, spazio delle regole). Il pezzo chiave e `reintegration_tracking.py`: implementa l'"advection/reintegration tracking", l'algoritmo che sposta la massa lungo il campo di flusso e la reintegra nelle celle di destinazione garantendo la conservazione. `flowlenia_params.py` aggiunge il parameter embedding: lo State diventa attivazioni A + mappa di parametri P, cosi i parametri sono un campo spaziale localizzato e non piu globali — e questo che abilita genomi locali e competizione. Tutto e JAX (jittabile, GPU, vettorizzabile). Gli esempi mostrano configurazioni 1-canale e 2-canali multi-kernel piu la demo del parameter embedding.

## Perche riguarda te
Questo e centrale per la tua arena del vuoto e per il tema particelle-emergenza. La conservazione della massa e proprio l'ingrediente che rende un automa continuo un mondo fisico credibile: la materia non appare/scompare, si sposta — e da questo vincolo emergono creature localizzate stabili. Se la tua arena vuole "particelle" che si aggregano in strutture persistenti dentro un campo, il reintegration tracking e la ricetta matematica pulita per farlo senza hack. Il parameter embedding e ancora piu vicino alla tua tesi: e l'idea che ogni frammento di materia porti localmente la propria regola/identita, competendo nello stesso spazio condiviso — una lettura molto concreta di "ricorsione della realta attraverso la materia" e di arena come spazio conteso. Dove diverge: Flow-Lenia e puramente fisico-morfogenetico, non ha nessuna nozione di memoria, novelty o coscienza; le "creature" non ricordano nulla e non c'e broadcast/relazione tra loro oltre la collisione fisica. E' il substrato del mondo, non la mente che ci vive dentro. Inoltre manca licenza, quindi trattalo come riferimento concettuale piu che come dipendenza.

## Da rubare
1. L'algoritmo di reintegration tracking come motore della tua arena: campo di flusso + spostamento di massa conservativa ti da particelle-emergenza stabili "gratis", senza dover inseguire manualmente la conservazione. Anche solo la struttura Config/State/step-function in JAX e un ottimo scheletro.
2. Il parameter embedding (mappa spaziale di parametri P che viaggia con la massa): usalo per dare ai tuoi agenti/particelle un "genoma locale" che si muove con loro nel vuoto, cosi regioni diverse dell'arena evolvono regole diverse e possono competere — molto piu ricco di parametri globali uniformi.
