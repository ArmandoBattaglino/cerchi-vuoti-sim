# Interview Coder — ibttf/interview-coder

<https://github.com/ibttf/interview-coder>

**~4.440 stelle · (solo release, sorgente chiuso) · ultimo push set 2025 · nessuna licenza** · "An invisible desktop application to help you pass your technical interviews."

## Cosa fa

L'app che ha fatto partire l'intera ondata: un'applicazione desktop invisibile che, durante un colloquio tecnico di coding (LeetCode-style), cattura lo schermo con il problema, lo manda a un LLM, e mostra soluzione + spiegazione in un overlay che **non appare nella condivisione schermo né nelle registrazioni**. È il capostipite del meme "undetectable interview assistant" e l'origine diretta dei cloni open (cheating-daddy, poi Glass). Divenuto famoso anche per la vicenda del suo autore (Roy Lee / Columbia), che ha reso il progetto un caso mediatico oltre che tecnico. Prodotto commerciale a pagamento.

## Come è fatto

**Non ispezionabile dal repo**: questo repository GitHub contiene *solo i binari di release* — l'unico file è un README che rimanda alla pagina releases. Il codice sorgente è chiuso. Per struttura e comportamento è però lo stesso archetipo poi replicato open dai cloni: app Electron/desktop, overlay trasparente always-on-top, cattura schermo → LLM → risposta, con la stessa primitiva di invisibilità alla cattura (equivalente a `setContentProtection` su Electron / esclusione della finestra dal compositor). Hotkey per invocare/spostare/nascondere. In pratica: quello che cheating-daddy e Glass hanno poi reso leggibile in sorgente, qui è l'originale confezionato e distribuito solo come eseguibile.

## Cosa possiamo notare di utile per noi

Il valore per te è **storico e concettuale**, non di codice (non c'è codice da leggere). È il punto-zero del filone occultamento.

- **Il primato dell'idea, non dell'implementazione.** Interview Coder ha dimostrato commercialmente che "presente all'occhio, assente allo strumento di cattura" è un oggetto desiderabile e costruibile. È la prova d'esistenza dell'occultamento-nel-canale che poi i cloni hanno reso trasparente. Per il tuo dossier è la voce-radice a cui agganciare cheating-daddy e Glass: stessa primitiva, tre gradi di apertura (chiuso → clone leggibile → prodotto raffinato).
- **Sorgente chiuso = occultamento del meccanismo stesso.** C'è una ricorsione ironica utile: un'app il cui scopo è occultare, il cui *codice* è a sua volta occultato (solo binari). Due strati di invisibilità sovrapposti — l'artefatto nasconde l'utente all'osservatore, e l'autore nasconde l'artefatto all'analista. Nota da tenere quando ragioni su occultamento a più livelli / annidato.
- **Zero rilevanza sul resto del tuo lavoro.** Nessuna memoria, nessuna emergenza, nessun world-model, nessun anello su di sé. Come per tutta la famiglia ghost, l'unico transfer è la nozione di invisibilità relativa al canale di misura — qui in forma originaria ma non ispezionabile.

Dove diverge: è un prodotto commerciale chiuso; non offre né architettura da studiare né concetti oltre l'archetipo. Per il *come funziona davvero* devi guardare i cloni open (cheating-daddy, Glass), non questo repo.

## Da rubare

- **Niente codice** (non c'è). Da rubare c'è solo la **framing story**: la prova che "pieno per l'occhio, vuoto per la sonda" è un oggetto reale, costruibile e desiderato — da citare come radice del ramo occultamento e rimandare a cheating-daddy/Glass per il meccanismo.
- **L'idea dell'occultamento annidato** (app che nasconde + sorgente nascosto): spunto per pensare a occultamento a strati nell'arena, dove ciò che nasconde è a sua volta nascosto a un osservatore di livello superiore.
