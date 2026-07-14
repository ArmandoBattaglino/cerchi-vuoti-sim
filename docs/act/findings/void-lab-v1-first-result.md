# Void Lab v1 — primo risultato (e prima falsificazione)

Data: 2026-07-14 · seed canonico 1337 · deterministico, riproducibile.

## L'ipotesi (dallo spec)
Una memoria relazionale novelty-gated (A) dà a un agente **più potere gestionale
con meno storage** di una memoria che salva tutto (B).

## Cosa dice il banco

### Regime goal-dominato (goalPull 0.95, il default)
| metrica | A (novelty-gated) | B (store-all) |
|---|---|---|
| passi al goal | 88 | 87 |
| \|memoria\| | 35 | 87 |
| raggiunto | sì | sì |

A usa il **40% della memoria** di B ma arriva **allo stesso tempo** (anzi B −1 passo).
In questo regime la memoria conta **solo per lo storage**, non per la navigazione —
verdetto quasi tautologico (A gated stora meno per costruzione).

### Sweep del goalPull (0.9 → 0.1) — il test vero
Abbassando il tiro al goal, la navigazione deve reggersi sulla memoria.
| goalPull | A arriva? | B arriva? |
|---|---|---|
| 0.95–0.56 | sì | sì (B leggermente più veloce) |
| **0.44 e sotto** | **NO (maxSteps)** | **sì** |

**A vince su 0/10 punti.** Sotto goalPull ~0.5 **A fallisce** (non raggiunge il goal),
mentre **B ci arriva sempre** (più lento, più memoria, ma arriva).

## Il perché (la scoperta)
Il gate di A è così severo che in esplorazione libera **immagazzina troppo poco**
(mem 5–7): resta senza mappa interna e vaga. B, salvando tutto, **accumula abbastanza
struttura** da orientarsi e raggiungere il goal.

**Conclusione onesta:** l'ipotesi forte è FALSA in questo modello. Il novelty-gate
scambia storage per navigabilità: ottimo quando c'è una guida esterna (goalPull alto),
**controproducente quando l'agente deve auto-orientarsi**. Il risparmio di memoria non
si traduce in potere gestionale — al contrario, lo toglie sotto una certa soglia.

## Perché è un buon risultato
È esattamente ciò per cui il lab esiste: **riproducibile, falsificabile, controintuitivo,
con un meccanismo spiegato.** Il lab non ha confermato la tesi: l'ha contraddetta e ha
detto *perché*. È il primo mattone della suite di test canonici (v2).

## Piste per la v2 (fuori scope v1)
- Un gate **adattivo** (severo quando c'è guida, permissivo quando serve auto-mappa).
- Metrica di gestione oltre la navigazione (compiti dove la memoria è davvero il collo).
- Il "valore = quanto un ricordo riduce la sorpresa futura" come politica di *oblio*
  (non solo di ammissione) — potrebbe dare ad A la mappa che gli manca senza gonfiarsi.
