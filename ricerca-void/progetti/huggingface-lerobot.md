# LeRobot — [huggingface/lerobot](https://github.com/huggingface/lerobot)

~25.8k stelle · Python · molto attivo (push luglio 2026) · Apache-2.0

## Cosa fa
LeRobot e lo stack open end-to-end di Hugging Face per la robotica reale in PyTorch. Punta ad abbassare la barriera d'ingresso: modelli, dataset e tool condivisi cosi che chiunque possa contribuire e beneficiare. Fornisce policy state-of-the-art gia allenate (ACT, Diffusion Policy, VQ-BeT, VLA), un formato dataset standardizzato, supporto per hardware low-cost (bracci SO-100) fino a umanoidi. E l'hub de-facto della community embodied.

## Come e fatto
Tre pilastri. **Interfaccia Robot hardware-agnostica**: una classe `Robot` unica che disaccoppia la logica di controllo dall'hardware — il loop e sempre `get_observation()` → `select_action()` → `send_action()`, identico dal braccetto da 100$ all'umanoide Unitree G1. **LeRobotDataset**: video MP4 sincronizzati (visione) + Parquet (stato/azione), hostati sull'HF Hub, con streaming e visualizzazione di dataset enormi e tool per split/merge/edit degli episodi. **Policy SoTA in puro PyTorch**: imitation learning, RL, VLA, world models, reward models — training con un solo comando `lerobot-train --policy.type=act --dataset.repo_id=...`.

## Perche riguarda te
LeRobot e il punto d'ingresso pratico del filone embodied, ma per i tuoi temi e il piu tangenziale dei quattro. Il legame onesto e nel *formato dati* e nel *loop osservazione-azione*, non nella coscienza. Se la tua arena del vuoto produce traiettorie di particelle che vuoi registrare, ispezionare e ri-processare, il pattern LeRobotDataset (stream sincronizzato + tool di editing per episodio) e un modello maturo di come si serializza e si visualizza il comportamento emergente nel tempo — il tuo "oscilloscopio" come dataset navigabile. Dove diverge: qui non c'e nessuna nozione di memoria auto-editante, novelty o ricorsione; e ingegneria di robot learning supervisionato/imitativo. Nessuna auto-organizzazione dal vuoto — le policy imparano da dimostrazioni umane.

## Da rubare
1. **Formato episodio = video/stream sincronizzato + tabella stato-azione, con tool di split/merge/delete**: adotta questa separazione per registrare le run della tua sim. Rende il comportamento emergente riproducibile, tagliabile e confrontabile senza riavviare il mondo.
2. **Interfaccia astratta a 3 verbi (`observe / decide / act`) indipendente dal substrato**: lo stesso disaccoppiamento ti permette di scambiare la "fisica" della particella sotto senza toccare l'agente che la osserva — utile per confrontare regole di emergenza diverse a parita di osservatore.
