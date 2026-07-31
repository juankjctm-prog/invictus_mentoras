import re

with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject functions before the last </script>
js_code = """
// --- INYECTADO: GIMNASIA CEREBRAL, PPM, RECALL, SOS ---
let lecturaStartTime;
let lecturaInterval;

function iniciarLecturaPPM() {
    lecturaStartTime = Date.now();
    const content = document.getElementById('reader-content-premium');
    if(content) content.style.display = 'block';
    const btnIni = document.getElementById('btn-iniciar-lectura');
    if(btnIni) btnIni.style.display = 'none';
    const btnTer = document.getElementById('btn-terminar-lectura');
    if(btnTer) btnTer.style.display = 'block';
    
    lecturaInterval = setInterval(() => {
        let elapsed = Math.floor((Date.now() - lecturaStartTime) / 1000);
        const timerDisp = document.getElementById('ppm-timer-display');
        if(timerDisp) {
            let m = Math.floor(elapsed / 60);
            let s = elapsed % 60;
            timerDisp.innerText = m.toString().padStart(2, '0') + ':' + s.toString().padStart(2, '0');
        }
    }, 1000);
}

function terminarLecturaPPM() {
    clearInterval(lecturaInterval);
    let elapsedMs = Date.now() - lecturaStartTime;
    let elapsedMinutes = elapsedMs / 60000;
    
    let contentEl = document.getElementById('reader-content-premium');
    if(!contentEl) return;
    let text = contentEl.innerText || contentEl.textContent;
    let wordCount = text.trim().split(/\\s+/).length;
    
    if (elapsedMinutes < 0.1) elapsedMinutes = 0.1;
    
    let ppm = Math.round(wordCount / elapsedMinutes);
    if (ppm > 1200) ppm = 1200; 
    
    let key = 'mm_b_d' + currentDay + '_ppm';
    localStorage.setItem(key, ppm.toString());
    
    let resultEl = document.getElementById('ppm-result');
    if(resultEl) resultEl.innerText = ppm;
    
    let msg = "";
    if (ppm < 150) msg = "Velocidad base. Evita subvocalizar.";
    else if (ppm < 250) msg = "Velocidad promedio. Usa tu dedo o puntero.";
    else if (ppm < 400) msg = "¡Buena velocidad! Amplía tu visión periférica.";
    else if (ppm < 600) msg = "¡Nivel Ejecutivo! Excelente comprensión y velocidad.";
    else msg = "¡Nivel Élite! Velocidad de lectura biónica alcanzada.";
    
    let msgEl = document.getElementById('ppm-msg');
    if(msgEl) msgEl.innerText = msg;
    
    let modal = document.getElementById('ppm-modal');
    if(modal) modal.style.display = 'flex';
    
    const btnTer = document.getElementById('btn-terminar-lectura');
    if(btnTer) btnTer.style.display = 'none';
    const timerDisp = document.getElementById('ppm-timer-display');
    if(timerDisp) timerDisp.style.color = 'var(--success)';
}

function closePPMModal() {
    let modal = document.getElementById('ppm-modal');
    if(modal) modal.style.display = 'none';
}

function evaluarQuizReal(dayId) {
    let qData = [];
    if (window.activeTrackData) {
        const d = window.activeTrackData.find(x => x.dia === currentDay);
        if (d && d.preguntas) qData = d.preguntas;
    }
    if (!qData || qData.length === 0) return;

    let correctas = 0;
    let sinResponder = 0;
    qData.forEach((item, qIdx) => {
        const radios = document.getElementsByName('quiz-q' + (qIdx+1));
        let answered = false;
        for (let r of radios) {
            if (r.checked) {
                answered = true;
                let val = parseInt(r.value);
                let correctOpt = item.correct !== undefined ? item.correct : (item.answer !== undefined ? item.answer : 0);
                if (val === correctOpt) correctas++;
            }
        }
        if (!answered) sinResponder++;
    });

    const total = qData.length;
    const score = Math.round((correctas / total) * 100);

    const ppmKey = 'mm_b_d' + currentDay + '_ppm';
    const ppm = localStorage.getItem(ppmKey) || '—';

    localStorage.setItem('mm_b_d' + currentDay + '_score', score.toString());
    localStorage.setItem('mm_b_d' + currentDay, '1');

    const box = document.getElementById('quiz-result-' + currentDay);
    if (!box) return;
    box.style.display = 'block';

    let nivel = "";
    if (score >= 80) nivel = "Comprensión sólida";
    else if (score >= 60) nivel = "Comprensión parcial — repasa lo que falló";
    else nivel = "Fuga de comprensión — vuelve a leer antes de avanzar";

    const color = score >= 80 ? 'var(--success)' : (score >= 60 ? 'var(--accent-fire)' : '#FF4500');
    box.style.borderColor = color;
    box.style.background = 'rgba(255,255,255,0.03)';

    let detalle = sinResponder > 0
        ? `<p style="font-size:0.78rem; color: var(--text-tertiary); margin-top:6px;">${sinResponder} pregunta(s) sin responder — cuentan como incorrectas.</p>`
        : '';

    box.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <div>
                <div style="font-family:'Outfit'; font-size:1.8rem; color:${color}; font-weight:700;">${score}%</div>
                <div style="font-size:0.75rem; color:var(--text-secondary); text-transform:uppercase; letter-spacing:1px;">Comprensión (${correctas}/${total})</div>
            </div>
            <div style="text-align:right;">
                <div style="font-family:'Outfit'; font-size:1.8rem; color:var(--accent-water); font-weight:700;">${ppm}</div>
                <div style="font-size:0.75rem; color:var(--text-secondary); text-transform:uppercase; letter-spacing:1px;">PPM leídas</div>
            </div>
        </div>
        <p style="font-size:0.85rem; color:white; font-weight:500;">${nivel}</p>
        ${detalle}
    `;
    box.scrollIntoView({ behavior: 'smooth', block: 'center' });
    
    if(!completedDays.includes(currentDay)) {
        completedDays.push(currentDay);
        if(typeof saveProgress === 'function') saveProgress();
    }
}

let sosInterval;
const affirmations = [
    "Tus resultados hablan más fuerte que tu síndrome del impostor. Respira tu evidencia",
    "No tienes que saberlo todo, solo estar dispuesta a aprender el siguiente paso",
    "Tu valía no se mide por la validación externa, sino por tu congruencia interna",
    "Permítete ocupar espacio. Perteneces aquí"
];

window.openSOS = function() {
    let overlay = document.getElementById('sos-overlay');
    if(!overlay) return;
    overlay.classList.add('active');
    let currentAff = 0;
    const textEl = document.getElementById('sos-affirmation');
    textEl.textContent = affirmations[currentAff];
    textEl.classList.add('visible');
    sosInterval = setInterval(() => {
        textEl.classList.remove('visible');
        setTimeout(() => {
            currentAff = (currentAff + 1) % affirmations.length;
            textEl.textContent = affirmations[currentAff];
            textEl.classList.add('visible');
        }, 1000);
    }, 8000);
};

window.closeSOS = function() {
    let overlay = document.getElementById('sos-overlay');
    if(overlay) overlay.classList.remove('active');
    clearInterval(sosInterval);
};
"""

idx = content.rfind("</script>")
if idx != -1:
    content = content[:idx] + js_code + "\\n" + content[idx:]

# 2. Modify renderMentoraSession for the new Phase 2 and 4 HTML
old_phase2 = """        <!-- F2 -->
        <div class="phase active">
            <div class="phase-node"></div>
            <div class="phase-header"><h4 style="color: var(--accent-fire);">2. Lectura Táctica</h4><span class="phase-duration" style="color:var(--accent-fire);">12m</span></div>
            <button class="btn-outline" id="btn-bionic" onclick="toggleBionic()" style="margin-top: 10px;">⚡ Lectura Biónica <span style="font-size:0.6rem;opacity:0.7;display:block;">(Entrena tu salto visual)</span></button>
            <div class="reader-premium" id="reader-content">
                <h4 style="color: white; margin-bottom: 12px; font-family: 'Outfit'; text-transform: uppercase;">${titulo}</h4>
                ${texto}
            </div>
            
            <div id="ppm-box" style="display: none; margin-top: 16px; padding: 12px; border-radius: 12px; background: rgba(255,255,255,0.05); color: white; font-size: 0.85rem;"></div>
            
            <div id="sticky-timer-wrapper" style="position: sticky; top: 10px; z-index: 1000; background: rgba(0,0,0,0.8); padding: 10px; border-radius: 8px; text-align: center; border: 1px solid var(--accent-fire); margin-bottom: 10px;">
                <button class="btn-premium fire" id="btn-timer" style="width: 100%;" onclick="toggleTimer()">Iniciar Cronómetro</button>
                <div id="visual-timer" style="font-family: 'Outfit'; font-size: 2rem; color: white; display: none; margin-top: 10px;">00:00</div>
            </div>
        </div>"""

new_phase2 = """        <!-- F2 -->
        <div class="phase active">
            <div class="phase-node"></div>
            <div class="phase-header"><h4 style="color: var(--accent-fire);">2. Lectura Táctica</h4><span class="phase-duration" style="color:var(--accent-fire);">12m</span></div>
            
            <div id="sticky-timer-wrapper" style="position: sticky; top: 10px; z-index: 1000; background: rgba(0,0,0,0.8); padding: 16px; border-radius: 12px; text-align: center; border: 1px solid rgba(255,94,0,0.3); margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="font-size: 0.8rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">Tiempo PPM</span>
                    <div id="ppm-timer-display" style="font-family: 'Outfit'; font-size: 1.8rem; color: white; font-weight: bold; text-shadow: 0 0 10px rgba(255,94,0,0.5);">00:00</div>
                </div>
                <button id="btn-iniciar-lectura" class="btn-outline" style="width: 100%; border-color: var(--accent-fire); color: white; background: rgba(255,94,0,0.1);" onclick="iniciarLecturaPPM()">▶ Iniciar Lectura Biónica</button>
                <button id="btn-terminar-lectura" class="btn-premium fire" style="width: 100%; display: none;" onclick="terminarLecturaPPM()">⏹ Terminé de Leer</button>
            </div>
            
            <div class="reader-premium" id="reader-content-premium" style="display: none;">
                <h4 style="color: white; margin-bottom: 12px; font-family: 'Outfit'; text-transform: uppercase;">${titulo}</h4>
                ${texto}
            </div>
        </div>"""

content = content.replace(old_phase2, new_phase2)

# Modifying phase 4 for Quiz
old_phase4 = """        <!-- F4 -->
        <div class="phase" id="comprension-block" style="display:none;">
            <div class="phase-node"></div>
            <div class="phase-header"><h4>4. Recall Activo y Evaluación</h4><span class="phase-duration">4m</span></div>
            <p class="phase-desc">La extracción forzada es la base de la retención a largo plazo. Al iniciar el test, el texto desaparecerá permanentemente.</p>
            <div id="test-intro">
                <button class="btn-outline" style="width: 100%; margin-top: 8px; border-color: var(--accent-fire); color: var(--accent-fire);" onclick="iniciarTest()">🧠 Iniciar Recall (Ocultar Lectura)</button>
            </div>
            <div id="test-content" style="display: none; margin-top: 16px;">
                ${preguntasHTML}
                <button class="btn-outline" style="width: 100%; margin-top: 8px;" onclick="evaluarRecall()">📊 Evaluar Comprensión Cruzada</button>
            </div>
            <div id="quiz-result-${dayIndex}" style="display:none; margin-top:20px; padding:20px; border-radius:12px; border:1px solid;"></div>
        </div>"""

new_phase4 = """        <!-- F4 -->
        <div class="phase active" id="comprension-block">
            <div class="phase-node"></div>
            <div class="phase-header"><h4>4. Recall Activo y Evaluación</h4><span class="phase-duration">4m</span></div>
            <p class="phase-desc">La extracción forzada es la base de la retención a largo plazo.</p>
            <div id="test-content" style="margin-top: 16px;">
                ${preguntasHTML}
                <button class="btn-premium fire" style="width: 100%; margin-top: 8px;" onclick="evaluarQuizReal(${dayIndex})">📊 Evaluar Comprensión</button>
            </div>
            <div id="quiz-result-${dayIndex}" style="display:none; margin-top:20px; padding:20px; border-radius:12px; border:1px solid;"></div>
        </div>"""

content = content.replace(old_phase4, new_phase4)

# 3. Modify `preguntasHTML` generation to use `quiz-q${i+1}`
old_preg_html = """        preguntasHTML = d.preguntas.map((q, i) => `
            <div style="margin-bottom: 20px;">
                <p style="font-size: 0.9rem; margin-bottom: 12px; color: white;"><strong>${i+1}. ${q.q || q.pregunta}</strong></p>
                ${(q.options || q.opciones).map((opt, j) => `
                    <label style="display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-secondary);"><input type="radio" name="q${i+1}" value="${j}"> ${opt}</label>
                `).join('')}
            </div>
        `).join('');"""

new_preg_html = """        preguntasHTML = d.preguntas.map((q, i) => `
            <div style="margin-bottom: 20px;">
                <p style="font-size: 0.9rem; margin-bottom: 12px; color: white;"><strong>${i+1}. ${q.q || q.pregunta}</strong></p>
                ${(q.options || q.opciones).map((opt, j) => `
                    <label style="display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-secondary);"><input type="radio" name="quiz-q${i+1}" value="${j}"> ${opt}</label>
                `).join('')}
            </div>
        `).join('');"""
        
content = content.replace(old_preg_html, new_preg_html)

# Add SOS modal and PPM modal to the HTML body
modals_html = """
    <!-- PPM Result Modal -->
    <div id="ppm-modal" style="display:none;position:fixed;inset:0;z-index:9000;background:rgba(6,6,13,.98);justify-content:center;align-items:center;padding:20px;">
        <div style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);padding:30px;border-radius:24px;text-align:center;max-width:320px;width:100%;">
            <div style="font-size:3rem;margin-bottom:10px;">⚡</div>
            <h3 style="font-family:'Outfit';font-size:1.5rem;color:white;margin-bottom:5px;">Lectura Completada</h3>
            <div style="font-family:'Outfit';font-size:3.5rem;font-weight:bold;color:var(--accent-fire);line-height:1;" id="ppm-result">--</div>
            <div style="font-size:0.8rem;color:var(--text-secondary);text-transform:uppercase;letter-spacing:1px;margin-bottom:20px;">Palabras por Minuto</div>
            <p style="font-size:0.9rem;color:var(--text-tertiary);line-height:1.5;margin-bottom:24px;" id="ppm-msg">--</p>
            <button class="btn-premium" style="width:100%;" onclick="closePPMModal()">Continuar al Recall Activo</button>
        </div>
    </div>

    <!-- SOS Overlay Protocol -->
    <div id="sos-overlay" class="sos-overlay">
        <button class="close-sos" onclick="closeSOS()">Mi frecuencia se ha elevado ⏹</button>
        <div class="sos-content">
            <h2 class="display-font" style="font-size:2rem;color:white;margin-bottom:10px;">Protocolo SOS</h2>
            <p style="color:var(--text-secondary);margin-bottom:40px;">Regulación de Cortisol</p>
            
            <div class="breathing-circle-container">
                <div class="b-circle outer"></div>
                <div class="b-circle inner"></div>
                <div class="b-text">Inhala</div>
            </div>
            
            <div class="affirmation-container" id="sos-affirmation">
                Tus resultados hablan más fuerte que tu síndrome del impostor. Respira tu evidencia
            </div>
        </div>
    </div>
    
    <style>
    /* SOS CSS */
    .sos-overlay { position:fixed; inset:0; z-index:9999; background:rgba(6,6,13,0.98); display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; pointer-events:none; transition:opacity 0.5s; }
    .sos-overlay.active { opacity:1; pointer-events:all; }
    .close-sos { position:absolute; top:30px; right:30px; background:transparent; border:1px solid rgba(255,255,255,0.2); color:white; padding:10px 20px; border-radius:20px; cursor:pointer; font-size:0.8rem; }
    .breathing-circle-container { position:relative; width:200px; height:200px; margin:0 auto 40px; display:flex; align-items:center; justify-content:center; }
    .b-circle { position:absolute; border-radius:50%; }
    .b-circle.outer { width:200px; height:200px; background:rgba(0,198,255,0.1); animation: breath 8s infinite ease-in-out; }
    .b-circle.inner { width:100px; height:100px; background:var(--accent-water); box-shadow:0 0 30px rgba(0,198,255,0.4); }
    .b-text { position:relative; color:white; font-family:'Outfit'; font-weight:bold; font-size:1.2rem; }
    .affirmation-container { font-size:1.1rem; color:white; text-align:center; max-width:400px; line-height:1.6; opacity:0; transition:opacity 1s; padding:0 20px; }
    .affirmation-container.visible { opacity:1; }
    @keyframes breath {
        0% { transform:scale(0.5); opacity:0.5; }
        40% { transform:scale(1.2); opacity:1; }
        50% { transform:scale(1.2); opacity:1; }
        90% { transform:scale(0.5); opacity:0.5; }
        100% { transform:scale(0.5); opacity:0.5; }
    }
    </style>
"""

idx = content.rfind("</body>")
if idx != -1:
    content = content[:idx] + modals_html + "\\n" + content[idx:]

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched app.html successfully.")
