# Genesis World — [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world)

~29.6k stelle · Python · attivo (push luglio 2026) · Apache-2.0

## Cosa fa
Genesis World e una piattaforma di simulazione per "physical AI": robotica ed embodied AI. Mette insieme un motore multi-fisica unificato, un renderer foto-realistico (Nyx) e un compilatore cross-platform (Quadrants) dietro un'unica API Python. L'ambizione dichiarata e scalare dallo stesso codice che gira sul laptop fino a GPU da datacenter, restando leggibile ed embeddabile nel codice di ricerca. E il progetto piu stellato dell'area embodied.

## Come e fatto
Quattro layer sotto la tua applicazione: **Simulation Interface** (parsing asset URDF/MJCF/OBJ/GLB/USD, controller, sensori, ambienti paralleli ed eterogenei, GUI), **Physics** (un solo motore che integra Rigid, FEM, MPM, Particle via PBD/SPH, IPC, un coupler esplicito e SAP — tutti che condividono UNA scena e UNO stato), **Render** (tre percorsi collegabili come camera-sensor: Nyx, Luisa ray-tracer, Pyrender rasterizer) e **Compiler** (Quadrants abbassa il kernel Python a CUDA/ROCm/Metal/Vulkan/x86/ARM64, portandosi dietro autodiff, GPU-graph e caching). L'idea chiave architetturale: solver fisici eterogenei che coabitano in un unico stato di scena, differenziabile.

## Perche riguarda te
E la referenza pesante della categoria "simulatore come arena". La tua arena del vuoto e concettualmente lo stesso pattern — un mondo con regole in cui lasci auto-organizzare qualcosa — ma Genesis lavora su fisica reale continua (particelle SPH/MPM, cloth, fluidi) mentre tu lavori su emergenza astratta/simbolica. Il valore per te non e clonare la fisica: e vedere come tengono UN unico stato condiviso tra piu solver eterogenei senza che si pestino i piedi, e come espongono tutto dietro un'API Python minima. Dove diverge onestamente: Genesis e pensato per generare dati di training per policy robotiche, non per esplorare coscienza-ricorsione o novelty; non troverai qui nulla su memoria o auto-modellazione. E un motore, non una tesi.

## Da rubare
1. **Stato unico condiviso tra sotto-sistemi eterogenei**: invece di far dialogare N moduli con N stati, un solo `Scene`/`state` in cui rigidi, particelle e fluidi coesistono — utile se la tua arena mescola tipi diversi di "particelle-emergenza" che devono interagire in un unico campo.
2. **Camera-sensor come plugin intercambiabile**: il rendering (il tuo "oscilloscopio") e un sensore collegabile alla scena, non parte del loop di simulazione — puoi avere piu viste/strumenti di osservazione sullo stesso stato senza toccare la dinamica.
