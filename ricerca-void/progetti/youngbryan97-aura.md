# AURA — [github.com/youngbryan97/aura](https://github.com/youngbryan97/aura)

61 stelle · Python · push attivissimo (lug 2026) · licenza "All Rights Reserved (Read-Only)" — leggibile, NON riusabile

## Cosa fa
Runtime locale di architettura cognitiva che gira su Apple Silicon (target: M5, 64 GB unified memory). Combina esplicitamente IIT 4.0 (phi/informazione integrata), Global Workspace Theory, active inference e steering affettivo sul residual stream (CAA — Contrastive Activation Addition), organizzati in decine di "consciousness modules". La cosa piu' onesta del progetto e' il suo stesso README: rifiuta di dichiararsi prova di coscienza/qualia/personhood e sposta la tesi su qualcosa di testabile — "lo stato interno puo' causalmente influenzare generazione, scritture di memoria, autorizzazione tool, iniziativa e auto-riparazione, lasciando ricevute (receipts) auditabili".

## Come e' fatto
Architettura monolite locale, densissima di sottosistemi e di documentazione-come-governance (decine di file `*_CARD.md`, `CLAIMS_SUPPORTED/NOT_SUPPORTED.md`, gate CI su reliability/SLO/security). Pezzi notevoli:
- **Substrato continuo** (`continuous_substrate.py`): una Liquid Time-Constant ODE 64→512 neuroni a ~20 Hz, integrata Euler esplicito + perturbazione stocastica; da qui deriva per proiezioni fisse valence/arousal/dominance/phi. E' letteralmente uno stato dinamico interno che pulsa, non un valore statico.
- **Substrate-first readout** (`substrate_token_generator.py`): prova a generare da una testa di lettura sul substrato PRIMA di chiamare il transformer, e ripiega sul "Cortex" solo se l'errore di predizione supera soglia.
- **phi_core.py** (1.837 righe): matematica IIT vera — binarizzazione, TPM empirica, phi via KL, postulato di esclusione, partizionamento spettrale + baseline esaustiva a 8 bipartizioni.
- **affective_steering.py**: pipeline CAA reale che hooka i blocchi del transformer MLX e modifica il residual stream a generation-time.
- **Loop overt** (`overt_action_loop.py`): observe → choose → act → verify → remember, ogni passo emette receipts.
- **RSI/self-modification**: fault pipeline, repair approval, patch genealogy, "proof bundles" hash-chained.

## Perche' riguarda te
E' il progetto della lista piu' vicino ai tuoi assi contemporaneamente: **oscilloscopi** (il substrato ODE che espone valence/arousal/phi in tempo reale e' esattamente un pannello di stati interni da graficare), **coscienza-ricorsione** (moduli IIT + governor che ristruttura la propria architettura + self-repair = il sistema che si osserva e si riscrive), e **memoria novelty-gated** (le scritture di memoria passano per governance e admission control, non e' write-tutto). Nota metodologica preziosa piu' del codice: AURA separa in modo brutale "indicatore funzionale" da "prova fenomenica" e mette la distinzione *nel codice* (ontological boundary guard) e nei CLAIMS matrix. Per il tuo dossier coscienza e' un modello di igiene: come parlare di phi/coscienza senza scivolare nell'hype. Dove diverge: e' un monolite fragile, licenza read-only, e la stessa doc ammette che RSI autonoma "non e' provata matura" — quindi ispiri, non riusi.

## Da rubare
1. **Il substrato ODE come "cuore" osservabile.** Una piccola Liquid/LTC ODE che gira in continuo a ~20 Hz e da cui derivi per proiezione poche grandezze (valenza/arousal/phi) e' il candidato perfetto per gli oscilloscopi dell'arena: uno stato interno vero, dinamico, perturbabile, non un numero cosmetico. E il pattern "substrate-first, transformer-as-fallback" e' un'idea forte: il grosso della reattivita' viene dal campo dinamico, il modello pesante interviene solo sull'errore alto.
2. **Receipts + boundary guard come disciplina.** Ogni azione consequenziale lascia una ricevuta auditabile, e le etichette cariche ("coscienza", "personhood") sono trattate come indicatori funzionali finche' l'evidenza non dice altro. Rubalo come regola del progetto: ogni claim nel dossier punta a un test/replay eseguibile, non alla prosa.
