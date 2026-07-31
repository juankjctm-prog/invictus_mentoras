import re

with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Add 'Despertador Neuronal' and update 'Centro de Apoyo' in view-kit
kit_header_pattern = re.compile(r'(<div id="view-kit" class="view kit-view">.*?<div class="kit-sec-title">📊 Mi Impacto</div>)', re.DOTALL)
m2 = kit_header_pattern.search(content)
if m2:
    new_kit = """<div id="view-kit" class="view kit-view">
  <div class="kit-scroll">
    <div style="padding:20px 0 10px">
      <h2 style="font-family:'Outfit';font-size:1.4rem;font-weight:700">Kit de Mentoría</h2>
      <p style="color:#8A8F98;font-size:.82rem;margin-top:4px">Tus herramientas como mentora</p>
    </div>
    
<div class="card" style="background:linear-gradient(135deg, rgba(16,185,129,0.05), rgba(0,0,0,0.4)); border:1px solid var(--success); border-radius:16px; padding:20px; margin-bottom:24px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
        <div style="background:rgba(16,185,129,0.15); color:var(--success); padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:bold;"> CENTRO DE APOYO & CONTINGENCIAS</div>
    </div>
    <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:6px; color:#fff;">Tu Caja de Herramientas de Mentoría</h3>
    <p style="font-size:0.82rem; color:var(--text-secondary); line-height:1.5; margin-bottom:10px;">
        Respuestas tácticas para desatascar sesiones y calibrar tu criterio de liderazgo:
    </p>
    <ul style="font-size:0.78rem; color:var(--text-secondary); padding-left:16px; line-height:1.6; margin-bottom:15px;">
        <li><strong style="color:var(--success);">Coach de Crisis:</strong> Úsalo cuando tu mentada llore, no avance o se muestre defensiva.</li>
        <li><strong style="color:var(--accent-water);">Gimnasia Cerebral:</strong> Despierta tu agilidad visual antes de liderar la sesión.</li>
    </ul>
    <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <button class="btn-outline" style="border-color:var(--success); color:var(--success); flex:1;" onclick="openCrisisModal()">🚨 Coach de Crisis</button>
        <button class="btn-outline" style="border-color:var(--accent-water); color:var(--accent-water); flex:1;" onclick="iniciarDespertadorNeuronal()">🧠 Despertador Neuronal</button>
    </div>
</div>

<!-- Modal Despertador Neuronal -->
<div id="despertador-modal" style="display:none;position:fixed;inset:0;z-index:9000;background:rgba(6,6,13,.98);justify-content:center;align-items:center;padding:20px;">
    <div style="background:var(--bg-surface);border:1px solid var(--accent-water);padding:30px;border-radius:24px;text-align:center;max-width:400px;width:100%;">
        <div style="font-size:2.5rem;margin-bottom:10px;">🧠</div>
        <h3 style="font-family:'Outfit';font-size:1.3rem;color:white;margin-bottom:5px;">El Despertador Neuronal</h3>
        <p style="font-size:0.85rem;color:var(--text-secondary);line-height:1.4;margin-bottom:20px;">Decodifica la siguiente frase ejecutiva encriptada (A→4, E→3, I→1, O→0, S→5, B→8, T→7). Tienes 15 segundos.</p>
        
        <div id="dn-frase-box" style="background:rgba(0,198,255,0.05); border:1px solid rgba(0,198,255,0.2); padding:20px; border-radius:12px; margin-bottom:20px;">
            <p id="dn-frase" style="font-family:'Courier New', monospace; font-size:1.1rem; color:var(--accent-water); font-weight:bold; letter-spacing:1px; line-height:1.4; word-break:break-word;">
                C4RG4ND0...
            </p>
        </div>
        
        <div id="dn-timer" style="font-family:'Outfit';font-size:3rem;font-weight:bold;color:white;margin-bottom:20px;">15</div>
        
        <button id="btn-dn-revelar" class="btn-premium" style="width:100%; margin-bottom:10px;" onclick="revelarDespertador()">Revelar Texto Original</button>
        <button class="btn-outline" style="width:100%; border-color:var(--text-secondary); color:var(--text-secondary);" onclick="document.getElementById('despertador-modal').style.display='none'">Cerrar</button>
    </div>
</div>

<script>
const dnFrases = [
    { enc: "3L L1D3R4ZG0 N0 35 UN 717UL0, 35 UN4 R35P0N5481L1D4D.", orig: "EL LIDERAZGO NO ES UN TITULO, ES UNA RESPONSABILIDAD." },
    { enc: "L4 R351L13NC14 53 C0N57RUY3 3N L4 4DV3R51D4D, N0 3N L4 C0M0D1D4D.", orig: "LA RESILIENCIA SE CONSTRUYE EN LA ADVERSIDAD, NO EN LA COMODIDAD." },
    { enc: "L4 M3J0R 1NV3R510N QU3 PU3D35 H4C3R 35 3N 7U PR0P10 CR3C1M13N70.", orig: "LA MEJOR INVERSION QUE PUEDES HACER ES EN TU PROPIO CRECIMIENTO." },
    { enc: "N0 8U5QU35 3XC0545, 8U5C4 R35UL74D05 Y 50LU010N35.", orig: "NO BUSQUES EXCUSAS, BUSCA RESULTADOS Y SOLUCIONES." }
];
let dnInterval;
let dnCurrentFrase;

function iniciarDespertadorNeuronal() {
    const modal = document.getElementById('despertador-modal');
    modal.style.display = 'flex';
    
    dnCurrentFrase = dnFrases[Math.floor(Math.random() * dnFrases.length)];
    document.getElementById('dn-frase').textContent = dnCurrentFrase.enc;
    document.getElementById('dn-frase').style.color = 'var(--accent-water)';
    document.getElementById('dn-timer').textContent = '15';
    document.getElementById('btn-dn-revelar').disabled = false;
    
    let left = 15;
    clearInterval(dnInterval);
    dnInterval = setInterval(() => {
        left--;
        document.getElementById('dn-timer').textContent = left;
        if(left <= 0) {
            clearInterval(dnInterval);
            revelarDespertador();
        }
    }, 1000);
}

function revelarDespertador() {
    clearInterval(dnInterval);
    document.getElementById('dn-frase').textContent = dnCurrentFrase.orig;
    document.getElementById('dn-frase').style.color = 'var(--success)';
    document.getElementById('btn-dn-revelar').disabled = true;
}
</script>

<div class="kit-sec-title">📊 Mi Impacto</div>"""
    content = content[:m2.start()] + new_kit + content[m2.end():]
    with open('app.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched tools successfully.")
else:
    print("m2 not found, regex failed")
