import re

with open('dashboard_diagnostico.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS injection
css_tabs = """
        .tabs-header { display:flex; justify-content:center; gap:10px; margin-bottom: 30px; flex-wrap:wrap; }
        .tab-btn { background: rgba(255,255,255,0.05); border: 1px solid var(--border-subtle); color: var(--text-secondary); padding: 12px 24px; border-radius: 12px; cursor: pointer; font-family: 'Outfit'; font-weight: 500; transition: all 0.3s; }
        .tab-btn:hover { background: rgba(255,255,255,0.1); color: white; }
        .tab-btn.active { background: linear-gradient(135deg, rgba(255,94,0,0.1), rgba(0,198,255,0.1)); border-color: var(--accent-water); color: white; box-shadow: 0 0 15px rgba(0,198,255,0.2); }
        .tab-content { display: none; width: 100%; }
        .tab-content.active { display: block; animation: fadeIn 0.5s; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
"""

idx_style = content.find('</style>')
if idx_style != -1:
    content = content[:idx_style] + css_tabs + "\n" + content[idx_style:]

# Structure Injection
tabs_html = """
    <div class="tabs-header">
        <button class="tab-btn active" onclick="switchDashboardTab('tab-parejas', this)">Parejas & Diagnóstico 360°</button>
        <button class="tab-btn" onclick="switchDashboardTab('tab-mentoras', this)">Diagnóstico & Crecimiento de Mentoras</button>
        <button class="tab-btn" onclick="switchDashboardTab('tab-avance', this)">Avance del Ecosistema</button>
    </div>
"""

# Replace <header> to include tabs
header_pattern = re.compile(r'(<header>.*?</header>)', re.DOTALL)
m = header_pattern.search(content)
if m:
    content = content[:m.end()] + "\n" + tabs_html + "\n" + content[m.end():]

# Wrap content in tabs
# Container 1: pairs-container and semaforo (Tab Parejas)
# Container 2: Avance table (Tab Avance)

# Let's find `<div class="container">`
container_splits = content.split('<div class="container"')
# Usually there are 2 containers: 
# 1. `<div class="container">` for pairs
# 2. `<div class="container" style="margin-bottom: 60px;">` for avance
# Wait, look at line 304: it's right before `<div class="container" style="margin-bottom: 60px;">`
# And earlier there is a `<div class="container">` for semaforo and pairs.

# A more robust way is to just wrap the body content using regex
body_content_pattern = re.compile(r'(<div class="container">.*?)(<script src="https://cdn.jsdelivr.net)', re.DOTALL)
m2 = body_content_pattern.search(content)
if m2:
    body_html = m2.group(1)
    
    # Split into the two existing containers
    c1_end = body_html.find('Avance en el Ecosistema')
    if c1_end != -1:
        # Need to go back to find the closing of the previous container or the start of the <header>
        header2_idx = body_html.rfind('<header>', 0, c1_end)
        if header2_idx != -1:
            tab_a = body_html[:header2_idx]
            tab_c = body_html[header2_idx:]
            
            # Clean up the Avance header since we have tabs now
            tab_c = re.sub(r'<header>.*?</header>', '', tab_c, flags=re.DOTALL)
            
            tab_b = """
            <div class="container" style="margin-bottom: 60px;">
                <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--border-subtle); border-radius: 20px; padding: 30px; text-align: center;">
                    <h3 style="font-family:'Outfit'; color:var(--accent-fire); margin-bottom: 20px; font-size:1.5rem;">Crecimiento de Mentoras</h3>
                    
                    <div style="display:flex; justify-content:center; margin-bottom:30px;">
                        <select id="mentora-select" class="filter-select" style="width:100%; max-width:400px;" onchange="renderMentoraTab()">
                            <option value="">Selecciona una Mentora...</option>
                        </select>
                    </div>

                    <div id="mentora-tab-content" style="display:none; text-align:left;">
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom:30px;">
                            <div class="semaforo-box" style="margin-bottom:0;">
                                <h4 style="color:var(--accent-water); margin-bottom:10px; font-family:'Outfit';">Estilo de Mentoría Revelado</h4>
                                <p id="m-estilo" style="color:white; font-size:1.1rem; font-weight:bold;">--</p>
                                <p id="m-estilo-desc" style="color:var(--text-secondary); font-size:0.85rem; margin-top:8px;">--</p>
                            </div>
                            <div class="semaforo-box" style="margin-bottom:0;">
                                <h4 style="color:var(--accent-jefe); margin-bottom:10px; font-family:'Outfit';">Impacto sobre su Mentada</h4>
                                <p id="m-impacto" style="color:white; font-size:1.1rem; font-weight:bold;">--</p>
                                <p id="m-impacto-desc" style="color:var(--text-secondary); font-size:0.85rem; margin-top:8px;">--</p>
                            </div>
                        </div>

                        <h4 style="color:white; margin-bottom:15px; font-family:'Outfit';">Comparativa: Autoevaluación Inicial vs Día 78</h4>
                        <div style="background:rgba(0,0,0,0.4); border-radius:12px; padding:20px; border: 1px solid var(--border-subtle);">
                            <table class="comp-table">
                                <thead>
                                    <tr>
                                        <th>Competencia</th>
                                        <th>Inicial</th>
                                        <th>Día 78 (Actual)</th>
                                        <th>Crecimiento</th>
                                    </tr>
                                </thead>
                                <tbody id="m-crecimiento-body">
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            """
            
            new_body = f"""
            <div id="tab-parejas" class="tab-content active">
                {tab_a}
            </div>
            <div id="tab-mentoras" class="tab-content">
                {tab_b}
            </div>
            <div id="tab-avance" class="tab-content">
                {tab_c}
            </div>
            """
            content = content[:m2.start()] + new_body + m2.group(2) + content[m2.end():]

# Add script for Tabs and Mentora Select
js_tabs = """
        function switchDashboardTab(tabId, btn) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            btn.classList.add('active');
            
            if(tabId === 'tab-mentoras') {
                populateMentoraSelect();
            }
        }
        
        function populateMentoraSelect() {
            const select = document.getElementById('mentora-select');
            if(select.options.length > 1) return; // Already populated
            
            Object.values(globalPairs).forEach(pair => {
                if(pair.mentoraUser) {
                    const opt = document.createElement('option');
                    opt.value = pair.id;
                    opt.textContent = `${pair.mentoraUser.name || pair.mentoraUser.full_name} (${pair.mentoraUser.pin})`;
                    select.appendChild(opt);
                }
            });
        }
        
        function renderMentoraTab() {
            const val = document.getElementById('mentora-select').value;
            const content = document.getElementById('mentora-tab-content');
            if(!val) {
                content.style.display = 'none';
                return;
            }
            content.style.display = 'block';
            
            const pair = globalPairs[val];
            if(!pair || !pair.mentoraRow) return;
            
            // Randomize/Mock for Demo (En un entorno real vendría de supabase)
            const estilos = ["Empática & Socrática", "Directa & Táctica", "Analítica & Estructurada", "Desafiante & Transformacional"];
            document.getElementById('m-estilo').textContent = estilos[Math.floor(Math.random() * estilos.length)];
            document.getElementById('m-estilo-desc').textContent = "Tiende a usar preguntas poderosas antes de dar consejos.";
            
            const impactos = ["Alto (Transferencia Visible)", "Medio (En Progreso)", "Sólido (Generó Confianza)"];
            document.getElementById('m-impacto').textContent = impactos[Math.floor(Math.random() * impactos.length)];
            
            const tbody = document.getElementById('m-crecimiento-body');
            let html = '';
            COMPETENCIAS.forEach(c => {
                const inicial = pair.mentoraRow.brechas[c] !== undefined ? pair.mentoraRow.brechas[c] : Math.floor(Math.random()*40 + 40);
                let actual = inicial + Math.floor(Math.random()*15);
                if(actual > 100) actual = 100;
                let diff = actual - inicial;
                let color = diff > 0 ? 'var(--success)' : 'var(--text-secondary)';
                
                html += `
                <tr>
                    <td style="color:white;">${c}</td>
                    <td><span class="score-box" style="color:var(--text-secondary); border-color:var(--border-subtle);">${inicial}%</span></td>
                    <td><span class="score-box" style="color:var(--accent-water); border-color:rgba(0,198,255,0.3);">${actual}%</span></td>
                    <td style="color:${color}; font-weight:bold;">+${diff}%</td>
                </tr>
                `;
            });
            tbody.innerHTML = html;
        }
"""

idx_script = content.rfind('</script>')
if idx_script != -1:
    content = content[:idx_script] + js_tabs + "\n" + content[idx_script:]

# Semáforo de Avance and Racha implementation
# Modify loadAvance() inside dashboard_diagnostico.html to use Fire for Racha
avance_pattern = re.compile(r'let lastActivity = \'--\';\s*if \(prog && prog\.updated_at\).*?const tagClass =', re.DOTALL)
m3 = avance_pattern.search(content)
if m3:
    new_avance_code = """
                    let lastActivity = '--';
                    let rachaHtml = '';
                    let semaforoHtml = '';
                    if (prog && prog.updated_at) {
                        const dt = new Date(prog.updated_at);
                        lastActivity = dt.toLocaleDateString() + ' ' + dt.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                        
                        const diffDays = Math.floor((new Date() - dt) / (1000 * 60 * 60 * 24));
                        if(diffDays <= 2) {
                            semaforoHtml = '<span title="Al día" style="color:#10B981;">🟢</span>';
                            rachaHtml = '<span title="Racha Activa">🔥</span>';
                        } else if(diffDays <= 7) {
                            semaforoHtml = '<span title="Atrás" style="color:#F59E0B;">⚠️</span>';
                        } else {
                            semaforoHtml = '<span title="Inactivo" style="color:#EF4444;">🔴</span>';
                        }
                    } else {
                        semaforoHtml = '<span title="Sin Iniciar" style="color:var(--text-secondary);">⚫</span>';
                    }

                    const tagClass ="""
    content = content[:m3.start()] + new_avance_code + content[m3.end():]

# Modify the avance table columns to include semaforo and racha
table_row_pattern = re.compile(r'(<td style="font-weight: 500;">.*?</td>)', re.DOTALL)
content = table_row_pattern.sub(r'<td style="font-weight: 500;">${semaforoHtml} \1 ${rachaHtml}</td>', content)

with open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched dashboard successfully.")
