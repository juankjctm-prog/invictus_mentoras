import codecs
import re

with codecs.open('prototype_scripts.txt', 'r', 'utf-8', errors='ignore') as f:
    proto_js = f.read()

# Extract CRISIS_DATA
crisis_data_match = re.search(r'const CRISIS_DATA.*?;', proto_js, re.IGNORECASE | re.DOTALL)
if crisis_data_match:
    crisis_data = crisis_data_match.group(0)
else:
    crisis_data = ""
    print("Warning: CRISIS_DATA not found")

# Extract abrirCrisisMM and cerrarCrisisMM
abrir_match = re.search(r'window\.abrirCrisisMM\s*=\s*function\(id\)\s*\{.*?\n\};', proto_js, re.IGNORECASE | re.DOTALL)
if abrir_match:
    abrir_crisis = abrir_match.group(0)
else:
    abrir_crisis = ""
    print("Warning: abrirCrisisMM not found")

cerrar_match = re.search(r'window\.cerrarCrisisMM\s*=\s*function\(\)\s*\{.*?\n\};', proto_js, re.IGNORECASE | re.DOTALL)
if cerrar_match:
    cerrar_crisis = cerrar_match.group(0)
else:
    cerrar_crisis = ""
    print("Warning: cerrarCrisisMM not found")

# We will create an updateKitStats function that uses local variables to update the kit UI
update_kit_func = """
window.updateKitStats = function() {
    let diasActivos = 0;
    let maxStreak = 0;
    let currentStreak = 0;
    let bestPpm = 0;
    let scoreSum = 0;
    let scoreCount = 0;

    const dataArr = window.mujeresMentorasData || [];
    const total = dataArr.length > 0 ? dataArr.length : 1;

    for (let d of dataArr) {
        if (progresoLocal[d.dia] && progresoLocal[d.dia].completado) {
            diasActivos++;
            currentStreak++;
            if (currentStreak > maxStreak) maxStreak = currentStreak;
            
            if (progresoLocal[d.dia].ppm && progresoLocal[d.dia].ppm > bestPpm) {
                bestPpm = progresoLocal[d.dia].ppm;
            }
            if (progresoLocal[d.dia].comprension) {
                scoreSum += progresoLocal[d.dia].comprension;
                scoreCount++;
            }
        } else {
            currentStreak = 0;
        }
    }

    const pct = Math.round((diasActivos / total) * 100);
    const avgComp = scoreCount > 0 ? Math.round(scoreSum / scoreCount) : null;

    const el = id => document.getElementById(id);
    if (el('km-dias')) el('km-dias').textContent = diasActivos;
    if (el('km-streak')) el('km-streak').textContent = maxStreak;
    if (el('km-ppm')) el('km-ppm').textContent = bestPpm || '0';
    if (el('km-comp')) el('km-comp').textContent = avgComp !== null ? (avgComp + '%') : '0%';
    if (el('km-pct')) el('km-pct').textContent = pct + '%';
    if (el('km-bar')) el('km-bar').style.width = pct + '%';

    // Profile
    if (diasActivos >= 5) {
        const profiles = [
            {n:'Mentora Socrática', d:'Preguntas poderosas sobre consejos. Genera autonomía profunda en sus mentoreadas.'},
            {n:'Mentora Catalizadora', d:'Activa el potencial dormido. Transforma la ambivalencia en movimiento.'},
            {n:'Mentora Espejo', d:'Refleja verdades difíciles con gracia. Sus mentoreadas se ven a sí mismas con claridad brutal.'},
            {n:'Mentora Estratega', d:'Conecta el desarrollo personal con la visión organizacional. Piensa en sistemas.'},
        ];
        const p = profiles[diasActivos % profiles.length];
        const wrap = el('km-mirror-profile');
        if (wrap) { wrap.style.display = 'block'; }
        if (el('km-profile-name')) el('km-profile-name').textContent = p.n;
        if (el('km-profile-desc')) el('km-profile-desc').textContent = p.d;
    }
};
"""

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    app_html = f.read()

# Only inject if not already present
if 'CRISIS_DATA' not in app_html:
    injection = f"\n\n// --- INJECTED KIT PROTOCOL LOGIC ---\n{crisis_data}\n\n{abrir_crisis}\n\n{cerrar_crisis}\n\n{update_kit_func}\n// -----------------------------------\n\n</script>"
    app_html = app_html.replace('</script>\n</body>', injection + '\n</body>')
    app_html = app_html.replace('</script></body>', injection + '</body>')
    
    # Also hook updateKitStats into renderDashboard
    # we can just find 'renderDashboard() {' and append to it, but safer to replace `function switchTab(viewId, elm)` to also call it if viewId === 'view-kit'
    switch_tab_logic = """
        if (viewId === 'view-kit' && typeof window.updateKitStats === 'function') {
            window.updateKitStats();
        }
    """
    app_html = re.sub(r'(function switchTab\([^)]+\)\s*\{)', r'\1\n' + switch_tab_logic, app_html)
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(app_html)
    print("Injected Kit Protocol Logic!")
else:
    print("Kit Protocol Logic already injected!")
