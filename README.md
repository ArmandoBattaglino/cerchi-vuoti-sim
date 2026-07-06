# Sistema · complemento · analisi dei vuoti

Simulazione visiva a 4 quadrati:

- **S1 · obiettivi** — ogni pallina conosce la sua posizione-meta e si muove *solo spingendo gli altri* (rincula, come remare). Genera un **battito** (frequenza degli scambi).
- **S2 · frequenza** — nessun obiettivo: conosce solo il battito di S1, gira la fase a quel ritmo e si **sincronizza** (modello di Kuramoto).
- **S3 · vuoti di S2** — il negativo di S2 (campo di distanza): le zone lontane da ogni pallina si illuminano.
- **S4 · vuoti di S1** — lo stesso, per S1.

Metriche live: distanza media dall'obiettivo, sincronizzazione (0→1), sovrapposizione S1↔vuoti S2, vuoto medio (concentrazione).

## Come si usa

Apri **`index.html`** con un browser (doppio click). Niente da installare — è un singolo file HTML autonomo.

- Slider: numero palline, forza, attrito, raggio d'interazione, accoppiamento (sync S2), intensità/risoluzione vuoti.
- **Clicca** in S1 o S2 per iniettare una pallina in *entrambi*.
- Pausa / Aggiungi 25 / Rigenera.

## Regimi da provare
- Attrito basso → il sistema *churna* (vivo); attrito alto → si *congela* (raggiunge gli obiettivi ma si ferma).
- Accoppiamento alto → S2 si sincronizza (r→1) e i vuoti diventano grandi e connessi.
- Raggio corto + densità media → emergono strutture e veri vuoti (a saturazione l'analisi si appiattisce).
