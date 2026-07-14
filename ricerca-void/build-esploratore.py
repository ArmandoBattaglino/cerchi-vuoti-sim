# -*- coding: utf-8 -*-
"""Genera esploratore.html self-contained: 225 progetti + 125 schede incastonati.
Rigenerabile: aggiorna _data.json / progetti/*.md e rilancia `python build-esploratore.py`."""
import json, os, io

BASE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(BASE, "_data.json"), encoding="utf-8"))

# carica le schede reali presenti su disco (fonte di verita per 'analizzato')
sheets = {}
pdir = os.path.join(BASE, "progetti")
for fn in os.listdir(pdir):
    if fn.endswith(".md"):
        sheets[fn[:-3]] = open(os.path.join(pdir, fn), encoding="utf-8").read()

# fondo stream -> cluster leggibili, in ordine di vicinanza ai temi del vuoto
CLUSTERS = [
    ("vuoto",        "Vuoto - nicchie: campi, oscilloscopi, novelty",      ["vuoto-niche"]),
    ("alife",        "Artificial Life & emergenza",                        ["alife-emergenza"]),
    ("memoria",      "Memoria degli agenti (+ radici)",                    ["memoria-agenti"]),
    ("coscienza",    "Coscienza artificiale",                              ["coscienza-frameworks"]),
    ("world",        "World models - mondi interni & sogno",               ["world-models"]),
    ("inferenza",    "Inferenza attiva / predictive coding",               ["inferenza-attiva"]),
    ("cognitive",    "Architetture cognitive",                             ["architetture-cognitive"]),
    ("spaziale",     "Intelligenza spaziale / robotica",                   ["spaziale-robotica"]),
    ("teoria",       "Teoria di frontiera",                                ["teoria-frontiera"]),
    ("indie",        "Scena indie / fringe",                               ["scena-indie"]),
    ("stego",        "Steganografia / occultamento",                       ["steganografia", "steganografia-occultamento"]),
    ("ghost",        "GhostCode & AI-invisibili",                          ["ghostcode", "ghostcode-simili"]),
]
stream2cluster = {}
for cid, label, streams in CLUSTERS:
    for s in streams:
        stream2cluster[s] = cid

projects = []
for r in data:
    slug = r.get("slug") or ""
    cid = stream2cluster.get(r.get("stream", ""), "teoria")
    projects.append({
        "name": r.get("name", ""), "url": r.get("url", ""), "kind": r.get("kind", ""),
        "category": r.get("category", ""), "cluster": cid,
        "stars": r.get("stars") or 0, "rel": r.get("relevanza") or 0,
        "summary": r.get("summary", ""), "slug": slug,
        "hasSheet": slug in sheets,
    })

DATA = {
    "clusters": [{"id": c, "label": l} for c, l, _ in CLUSTERS],
    "projects": projects,
    "sheets": {s: sheets[s] for s in sheets},
    "counts": {"projects": len(projects), "sheets": len(sheets)},
}
blob = json.dumps(DATA, ensure_ascii=False)
# proteggi da chiusura anticipata dello <script>
blob = blob.replace("</", "<\\/")

HTML = r"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Esploratore Void - __NP__ progetti</title>
<style>
:root{--bg:#0a0c0a;--panel:#0f140f;--line:#1b241b;--dim:#6a7a6a;--ph:#39ff6e;--ph2:#5ee0c0;--org:#ffb14e;--txt:#cfe8cf}
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:var(--bg);color:var(--txt);font:13px/1.5 "Cascadia Mono","Consolas",monospace}
a{color:var(--ph2);text-decoration:none}a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:5;background:linear-gradient(#0a0c0a,#0a0c0aee);border-bottom:1px solid var(--line);padding:12px 16px}
h1{margin:0;font-size:15px;color:var(--ph);letter-spacing:2px;text-shadow:0 0 10px #39ff6e66}
.sub{color:var(--dim);font-size:12px;margin-top:2px}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:10px}
input,select{background:#0b110b;color:var(--txt);border:1px solid #223022;border-radius:6px;padding:7px 9px;font:12px "Cascadia Mono",monospace}
input#q{flex:1;min-width:180px}
.chip{cursor:pointer;border:1px solid #223022;border-radius:14px;padding:4px 10px;color:var(--dim);font-size:11px;user-select:none}
.chip.on{background:var(--ph);color:#04140a;border-color:var(--ph);font-weight:700}
.wrap{display:flex;gap:0;min-height:calc(100vh - 92px)}
.side{width:240px;flex:none;border-right:1px solid var(--line);padding:12px;overflow:auto;max-height:calc(100vh - 92px);position:sticky;top:92px}
.side h3{color:var(--dim);font-size:11px;text-transform:uppercase;letter-spacing:1px;margin:12px 0 6px}
.cl{display:flex;justify-content:space-between;cursor:pointer;padding:4px 6px;border-radius:5px;color:#9fbf9f}
.cl:hover{background:#12200f}.cl.on{background:#132013;color:var(--ph)}
.cl .n{color:var(--dim)}
.main{flex:1;padding:14px 16px;overflow:auto}
.cluster-h{color:var(--ph);font-size:13px;letter-spacing:1px;margin:18px 0 8px;border-bottom:1px solid var(--line);padding-bottom:4px}
.cluster-h .c{color:var(--dim);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:10px;cursor:pointer;transition:border-color .1s}
.card:hover{border-color:var(--ph2)}
.card .nm{color:var(--txt);font-weight:700;font-size:12.5px;display:flex;justify-content:space-between;gap:6px}
.card .meta{color:var(--dim);font-size:11px;margin:3px 0}
.card .sm{color:#a9c4a9;font-size:11.5px;margin-top:4px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.rel{color:var(--ph);letter-spacing:1px;font-size:11px}
.badge{font-size:10px;border:1px solid #274027;border-radius:4px;padding:1px 5px;color:var(--ph2)}
.star{color:var(--org)}
.empty{color:var(--dim);padding:30px;text-align:center}
/* detail overlay */
.ov{position:fixed;inset:0;background:#000a;z-index:20;display:none;padding:20px;overflow:auto}
.ov.on{display:block}
.doc{max-width:820px;margin:20px auto;background:#0c110c;border:1px solid #26402a;border-radius:12px;padding:22px 26px;box-shadow:0 0 40px #000}
.doc h2{color:var(--ph);font-size:17px;margin:.2em 0}.doc h3{color:var(--ph2);font-size:14px;margin:1.2em 0 .3em;border-bottom:1px solid var(--line);padding-bottom:3px}
.doc h4{color:var(--ph2);font-size:12.5px;margin:1em 0 .2em}
.doc p{margin:.5em 0}.doc ul{margin:.4em 0 .6em 1.1em}.doc li{margin:.2em 0}
.doc code{background:#0b1f0b;color:var(--ph2);padding:1px 4px;border-radius:4px}
.doc hr{border:0;border-top:1px solid var(--line);margin:1em 0}
.close{position:sticky;top:0;float:right;background:#132013;border:1px solid #274027;color:var(--txt);border-radius:7px;padding:6px 12px;cursor:pointer}
.dhead{color:var(--dim);font-size:12px;margin-bottom:8px}
.noan{color:var(--dim);font-style:italic;margin-top:10px}
</style></head><body>
<header>
  <h1>ESPLORATORE VOID</h1>
  <div class="sub">La mappa navigabile della ricerca - <b id="np"></b> progetti in <b id="nc"></b> cluster - <b id="ns"></b> con scheda di analisi. Clicca un progetto per leggerla.</div>
  <div class="bar">
    <input id="q" placeholder="cerca nome / descrizione / categoria...">
    <span class="chip rel-chip" data-r="0">tutti</span>
    <span class="chip rel-chip" data-r="4">rilevanza 4+</span>
    <span class="chip rel-chip on" data-r="0" style="display:none"></span>
    <span class="chip rel-chip" data-r="5">solo 5 (on-theme)</span>
    <span class="chip" id="onlyAn">solo analizzati</span>
    <select id="sort"><option value="rel">ordina: rilevanza</option><option value="stars">ordina: stelle</option><option value="name">ordina: nome</option></select>
  </div>
</header>
<div class="wrap">
  <div class="side">
    <h3>Cluster</h3>
    <div class="cl on" data-c="all"><span>Tutti</span><span class="n" id="cnt-all"></span></div>
    <div id="clusterList"></div>
  </div>
  <div class="main" id="main"></div>
</div>
<div class="ov" id="ov"><div class="doc"><button class="close" onclick="closeDoc()">chiudi &times;</button><div id="docBody"></div></div></div>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const CL = {}; DATA.clusters.forEach(c=>CL[c.id]=c.label);
const S = { q:'', rel:0, onlyAn:false, sort:'rel', cluster:'all' };
const $ = id=>document.getElementById(id);
$('np').textContent = DATA.counts.projects; $('nc').textContent = DATA.clusters.length; $('ns').textContent = DATA.counts.sheets;

function dots(n){ return '●'.repeat(n)+'○'.repeat(5-n); }
function starFmt(n){ if(!n) return ''; return n>=1000 ? (n/1000).toFixed(1).replace('.0','')+'k' : ''+n; }

// mini markdown -> html
function inl(s){ return s
  .replace(/&lt;(https?:\/\/[^ >]+)&gt;/g,'<a href="$1" target="_blank" rel="noopener">$1</a>')
  .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
  .replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>')
  .replace(/`([^`]+)`/g,'<code>$1</code>'); }
function md(src){ if(!src) return '';
  let s = src.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const out=[]; let inList=false;
  for(const raw of s.split('\n')){
    const l=raw;
    const h=l.match(/^(#{1,4})\s+(.*)$/);
    if(h){ if(inList){out.push('</ul>');inList=false;} const lv=Math.min(4,h[1].length+1); out.push('<h'+lv+'>'+inl(h[2])+'</h'+lv+'>'); continue; }
    const li=l.match(/^\s*[-*]\s+(.*)$/);
    if(li){ if(!inList){out.push('<ul>');inList=true;} out.push('<li>'+inl(li[1])+'</li>'); continue; }
    if(inList){out.push('</ul>');inList=false;}
    if(l.trim()===''){ continue; }
    if(/^-{3,}$/.test(l.trim())){ out.push('<hr>'); continue; }
    out.push('<p>'+inl(l)+'</p>');
  }
  if(inList)out.push('</ul>');
  return out.join('\n');
}

function match(p){
  if(S.rel && p.rel < S.rel) return false;
  if(S.onlyAn && !p.hasSheet) return false;
  if(S.cluster!=='all' && p.cluster!==S.cluster) return false;
  if(S.q){ const q=S.q.toLowerCase(); if(!((p.name+' '+p.summary+' '+p.category).toLowerCase().includes(q))) return false; }
  return true;
}
function sortF(a,b){ if(S.sort==='stars') return (b.stars-a.stars)||(b.rel-a.rel);
  if(S.sort==='name') return a.name.localeCompare(b.name); return (b.rel-a.rel)||(b.stars-a.stars); }

function render(){
  const vis = DATA.projects.filter(match);
  const main=$('main'); main.innerHTML='';
  const order = DATA.clusters.map(c=>c.id);
  let shown=0;
  for(const cid of order){
    const list = vis.filter(p=>p.cluster===cid).sort(sortF);
    if(!list.length) continue;
    const anz = list.filter(p=>p.hasSheet).length;
    const h=document.createElement('div'); h.className='cluster-h';
    h.innerHTML = CL[cid]+' <span class="c">- '+list.length+' progetti - '+anz+' con scheda</span>';
    main.appendChild(h);
    const g=document.createElement('div'); g.className='grid';
    for(const p of list){ shown++;
      const c=document.createElement('div'); c.className='card'; c.onclick=()=>openDoc(p);
      const st = p.stars? '<span class="star">★'+starFmt(p.stars)+'</span>' : '';
      c.innerHTML = '<div class="nm"><span>'+esc(p.name)+'</span><span class="rel">'+dots(p.rel)+'</span></div>'
        + '<div class="meta">'+st+(st&&p.category?' - ':'')+esc(p.category||'')+(p.hasSheet?' - <span class="badge">analisi</span>':'')+'</div>'
        + '<div class="sm">'+esc(p.summary||'')+'</div>';
      g.appendChild(c);
    }
    main.appendChild(g);
  }
  if(!shown) main.innerHTML='<div class="empty">Nessun progetto con questi filtri.</div>';
  // sidebar counts
  $('cnt-all').textContent = vis.length;
  buildSidebar(vis);
}
function esc(s){ return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

function buildSidebar(vis){
  const box=$('clusterList'); box.innerHTML='';
  for(const c of DATA.clusters){
    const n=vis.filter(p=>p.cluster===c.id).length;
    const total=DATA.projects.filter(p=>p.cluster===c.id).length;
    const d=document.createElement('div'); d.className='cl'+(S.cluster===c.id?' on':''); d.dataset.c=c.id;
    d.innerHTML='<span>'+c.label+'</span><span class="n">'+n+'/'+total+'</span>';
    d.onclick=()=>{ S.cluster = (S.cluster===c.id?'all':c.id); syncCl(); render(); };
    box.appendChild(d);
  }
  document.querySelectorAll('.side .cl[data-c="all"]')[0].classList.toggle('on',S.cluster==='all');
}
function syncCl(){ document.querySelectorAll('.side .cl').forEach(e=>e.classList.toggle('on', e.dataset.c===S.cluster || (e.dataset.c==='all'&&S.cluster==='all'))); }

function openDoc(p){
  const body=$('docBody');
  const head = '<div class="dhead">'+esc(CL[p.cluster])+' - '+dots(p.rel)+(p.stars?' - ★'+starFmt(p.stars):'')+' - <a href="'+p.url+'" target="_blank" rel="noopener">apri su web ↗</a></div>';
  if(p.hasSheet){ body.innerHTML = head + md(DATA.sheets[p.slug]); }
  else { body.innerHTML = head + '<h2>'+esc(p.name)+'</h2><p>'+esc(p.summary)+'</p><p class="noan">Scheda di analisi profonda non ancora scritta per questo progetto (e nella mappa, non tra le 125 analizzate). <a href="'+p.url+'" target="_blank" rel="noopener">Vai al progetto</a>.</p>'; }
  $('ov').classList.add('on'); $('ov').scrollTop=0; document.querySelector('.doc').scrollTop=0;
}
function closeDoc(){ $('ov').classList.remove('on'); }
$('ov').addEventListener('click',e=>{ if(e.target.id==='ov') closeDoc(); });
document.addEventListener('keydown',e=>{ if(e.key==='Escape') closeDoc(); });

// controls
$('q').addEventListener('input',e=>{ S.q=e.target.value; render(); });
$('sort').addEventListener('change',e=>{ S.sort=e.target.value; render(); });
document.querySelectorAll('.rel-chip').forEach(ch=>ch.addEventListener('click',()=>{
  document.querySelectorAll('.rel-chip').forEach(x=>x.classList.remove('on')); ch.classList.add('on'); S.rel=+ch.dataset.r; render();
}));
$('onlyAn').addEventListener('click',()=>{ S.onlyAn=!S.onlyAn; $('onlyAn').classList.toggle('on',S.onlyAn); render(); });

render();
</script></body></html>"""

HTML = HTML.replace("__DATA__", blob).replace("__NP__", str(len(projects)))
open(os.path.join(BASE, "esploratore.html"), "w", encoding="utf-8").write(HTML)
print("scritto esploratore.html:", len(HTML), "byte -", len(projects), "progetti,", len(sheets), "schede")
