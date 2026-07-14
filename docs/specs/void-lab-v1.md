# Void Lab v1 — spec (da deep-interview, 2026-07-14)

## Intent
Laboratorio-harness personale per validare in serie, riproducibilmente, le teorie
relazionali di Armando. Ipotesi v1: **una memoria relazionale novelty-gated dà a un
agente più potere gestionale con meno storage di una memoria che salva tutto.**
Nord lontano (fuori v1): teacher + linguaggio emergente sopra questa memoria.

## Principio di design
A e B differiscono in UNA cosa sola: *cosa entra in memoria*. Percezione, sorpresa,
metabolismo, movimento: identici. La vittoria (di chiunque) è attribuibile al gate.

- **Memoria A** — novelty-gated (attuale arena): scrive solo novità strutturata
  (sorpresa>0.13 E varianza>0.0045), cap 200.
- **Memoria B** — ingenua: scrive tutto ciò che percepisce, nessun gate.
- Sorpresa calcolata identica per entrambe (nearestDist/1.4 × structGate).

## Outcome v1
Banco dove si compone agente+mondo+memoria commutabile, si fa girare deterministico,
e si ottiene un verdetto numerico A-vs-B: catena ipotesi→esperimento→sweep→curva→verdetto.

## Modello dati (esperimento = JSON)
{ seed, world:{size,blobs,dynamic}, agent:{innateSeed,goal,memory:"A"|"B"},
  run:{maxSteps,noise}, sweep?:{param,from,to,steps} }

## Interfaccia memoria
makeMemory(kind) → { write(percept,surprise,variance,x,y), surprise(percept,variance),
size(), reset() }

## Metriche ("potere gestionale" = efficienza di navigazione, proxy onesto v1)
- passi-al-goal (A ≤ B?)   - |memoria| al goal (A ≪ B?)   - robustezza al rumore (A degrada meno?)

## Constraints
Vanilla JS + Canvas2D, self-contained, zero build, deterministico (mulberry32),
riuso motore arena-vuoto senza riscriverlo, doppio click e funziona.

## Non-goals v1
Patch-bay universale · teacher/linguaggio · integrazione LLM · gpu4/WebGPU ·
deploy/multiutente · framework/build.

## Acceptance criteria
1. Stesso seed → stessi numeri (headless-verificabile).
2. Switch A/B cambia solo la politica di memoria.
3. Report appaiato: passi-al-goal, |mem|, raggiunto — per A e B.
4. Sweep ≥10 punti → curva esportabile.
5. Verdetto a schermo, falsificabile (B può vincere).

## Decisioni default documentate
- Sweep di collaudo: rumore 0→0.12, 10 punti (curva di robustezza).
- Il file nuovo è void-lab.html; arena-vuoto.html resta intatto come riferimento.
