import codecs
import re
import json

file_path = 'app.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Update Phase 1 UI (Breathing)
old_f1 = '<p class="phase-desc"><strong>Respiración de Oxigenación (4 Ciclos):</strong> Inhala en 4s, retén en 8s, exhala en 16s. Máxima oxigenación linfática.</p>'
new_f1 = """
<div id="breathing-ui" style="text-align:center; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 8px; margin-top: 15px; border: 1px solid var(--border-subtle);">
    <div id="b-circle" style="width: 100px; height: 100px; border-radius: 50%; background: var(--accent-water); margin: 0 auto; transition: all 1s linear; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: #fff; font-weight: bold; opacity: 0.8;"></div>
    <p id="b-text" style="margin-top: 15px; font-weight: bold; color: white;">Ciclo 4-8-16. Oxigena tu cerebro.</p>
    <button id="b-start-btn" class="btn-outline" style="margin-top: 15px; font-size: 0.8rem;" onclick="startBreathing()">Iniciar 2 Ciclos</button>
</div>
"""
content = content.replace(old_f1, new_f1)

# Inject startBreathing() js function
breathing_js = """
function startBreathing() {
    let circle = document.getElementById('b-circle');
    let text = document.getElementById('b-text');
    let btn = document.getElementById('b-start-btn');
    btn.style.display = 'none';
    let cycles = 2;
    let currentCycle = 0;
    
    function runCycle() {
        if(currentCycle >= cycles) {
            text.innerText = "¡Oxigenación completa! Estás lista.";
            circle.style.transform = "scale(1)";
            circle.innerText = "✓";
            btn.style.display = 'inline-block';
            btn.innerText = "Rehacer Respiración";
            
            // Mark phase completed if not already done
            window.markPhaseDone(null, 1);
            showMotivationToast("¡Excelente preparación! Tu cerebro está oxigenado.");
            return;
        }
        
        currentCycle++;
        // Inhale 4s
        text.innerText = `Ciclo ${currentCycle}/2: INHALA (4s)`;
        circle.style.transition = "transform 4s linear, opacity 4s linear";
        circle.style.transform = "scale(1.5)";
        circle.style.opacity = "1";
        
        setTimeout(() => {
            // Hold 8s
            text.innerText = `Ciclo ${currentCycle}/2: RETÉN (8s)`;
            circle.style.transition = "transform 8s linear";
            circle.style.transform = "scale(1.6)";
            
            setTimeout(() => {
                // Exhale 16s
                text.innerText = `Ciclo ${currentCycle}/2: EXHALA (16s)`;
                circle.style.transition = "transform 16s linear, opacity 16s linear";
                circle.style.transform = "scale(0.8)";
                circle.style.opacity = "0.5";
                
                setTimeout(() => {
                    runCycle();
                }, 16000);
            }, 8000);
        }, 4000);
    }
    
    runCycle();
}
"""
content = content.replace('let timer, secs = 0, isRunning = false;', breathing_js + '\nlet timer, secs = 0, isRunning = false;')

# 2. Phase 2 Sticky Timer & Reread Prompt
# Wrap timer in sticky div
old_timer = '<button class="btn-premium fire" id="btn-timer" style="margin-top: 16px;" onclick="toggleTimer()">Iniciar Cronómetro (Obligatorio)</button>'
if old_timer not in content:
    old_timer = '<button class="btn-premium fire" id="btn-timer" style="margin-top: 16px;" onclick="toggleTimer()">Iniciar Cronómetro</button>'

new_timer = """
<div id="sticky-timer-wrapper" style="position: sticky; top: 10px; z-index: 1000; background: rgba(0,0,0,0.8); padding: 10px; border-radius: 8px; text-align: center; border: 1px solid var(--accent-fire); margin-bottom: 10px;">
    <button class="btn-premium fire" id="btn-timer" style="width: 100%;" onclick="toggleTimer()">Iniciar Cronómetro</button>
    <div id="re-read-prompt" style="display: none; margin-top: 10px; font-size: 0.9rem;">
        <p style="color: white; margin-bottom: 8px;">¿Hay algo que no entendiste?</p>
        <div style="display: flex; gap: 10px;">
            <button class="btn-outline" style="flex:1; font-size:0.7rem;" onclick="resetTimer()">🔁 Repetir Lectura</button>
            <button class="btn-primary" style="flex:1; font-size:0.7rem;" onclick="continueToComprension()">✅ Continuar a Comprensión</button>
        </div>
    </div>
</div>
"""
content = content.replace(old_timer, new_timer)

# Inject JS for reread logic
timer_js_replacement = """
function toggleTimer() {
    const btn = document.getElementById('btn-timer');
    if(!isRunning) {
        isRunning = true;
        btn.innerText = "Detener Cronómetro";
        btn.style.background = "linear-gradient(45deg, #10b981, #059669)";
        
        // Hide reader if not already visible (just in case)
        if(document.getElementById('reader-content').innerText.includes('Activa el cronómetro') === false) {
           document.getElementById('reader-content').style.filter = "none";
           document.getElementById('reader-content').style.userSelect = "auto";
        }

        timer = setInterval(() => {
            secs++;
            const m = Math.floor(secs/60).toString().padStart(2,'0');
            const s = (secs%60).toString().padStart(2,'0');
            btn.innerText = `Detener (${m}:${s})`;
        }, 1000);
    } else {
        clearInterval(timer); isRunning = false;
        const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / secs * 60);
        btn.innerText = `PPM: ${basePPM} (Velocidad Registrada)`;
        btn.disabled = true;
        
        // Show reread prompt
        document.getElementById('re-read-prompt').style.display = 'block';
    }
}

function resetTimer() {
    secs = 0;
    isRunning = false;
    const btn = document.getElementById('btn-timer');
    btn.disabled = false;
    btn.innerText = "Iniciar Cronómetro";
    btn.style.background = "";
    document.getElementById('re-read-prompt').style.display = 'none';
}

function continueToComprension() {
    document.getElementById('re-read-prompt').style.display = 'none';
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / secs * 60);
    document.getElementById('comprension-block').style.display = 'block';
    showMotivationToast("Velocidad registrada. Ahora, pongamos a prueba tu retención.");
}
"""

content = re.sub(r'function toggleTimer\(\) \{.*?(?=window\.showCompFeedback)', timer_js_replacement + '\n\n', content, flags=re.DOTALL)

# Phase 2 Comprension JS overhaul (handling multiple questions)
comprension_js = """
window.showCompFeedback = function(btn, isCorrect, ansText, qIndex, totalQs) {
    if(!window.compScores) window.compScores = 0;
    const parent = btn.parentElement.parentElement; // the options container
    const btns = parent.querySelectorAll('button');
    btns.forEach(b => {
        b.disabled = true;
        b.style.opacity = "0.5";
    });
    
    btn.style.opacity = "1";
    
    // Only append feedback message div once per question
    let fbDiv = document.createElement('div');
    fbDiv.style.marginTop = "10px";
    fbDiv.style.padding = "10px";
    fbDiv.style.borderRadius = "4px";
    fbDiv.style.fontSize = "0.85rem";
    
    if(isCorrect) {
        window.compScores++;
        btn.style.borderColor = "var(--success)";
        btn.style.background = "rgba(16, 185, 129, 0.1)";
        fbDiv.style.background = "rgba(16, 185, 129, 0.1)";
        fbDiv.style.color = "var(--success)";
        fbDiv.innerHTML = `<strong>¡Correcto!</strong> Respuesta acertada.`;
    } else {
        btn.style.borderColor = "var(--accent-fire)";
        btn.style.background = "rgba(255, 107, 0, 0.1)";
        fbDiv.style.background = "rgba(255, 107, 0, 0.1)";
        fbDiv.style.color = "var(--accent-fire)";
        fbDiv.innerHTML = `<strong>Incorrecto.</strong> La respuesta correcta es: ${ansText}`;
    }
    
    parent.appendChild(fbDiv);
    
    // Increment answered count
    if(!window.compAnswered) window.compAnswered = 0;
    window.compAnswered++;
    
    if(window.compAnswered >= totalQs) {
        // All answered!
        let scorePct = Math.round((window.compScores / totalQs) * 100);
        let finalFeedback = document.createElement('div');
        finalFeedback.style.marginTop = "20px";
        finalFeedback.style.padding = "15px";
        finalFeedback.style.borderRadius = "8px";
        finalFeedback.style.background = "rgba(0,0,0,0.5)";
        finalFeedback.style.textAlign = "center";
        finalFeedback.innerHTML = `
            <h4 style="color: var(--accent-water); margin-bottom:10px;">Comprensión Finalizada</h4>
            <p style="color:white; font-size:1.5rem; font-weight:bold;">Score: ${scorePct}% (${window.compScores}/${totalQs})</p>
            <button class="btn-outline" style="margin-top: 15px;" onclick="saveComprensionAndAdvance(${scorePct})">Guardar y Avanzar</button>
        `;
        parent.parentElement.appendChild(finalFeedback);
    }
}

window.saveComprensionAndAdvance = function(scorePct) {
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / secs * 60);
    localStorage.setItem('invictus_recall_score', scorePct);
    localStorage.setItem('invictus_recall_ppm', basePPM);
    window.markPhaseDone(null, 2);
    showMotivationToast(`Resultados guardados: ${basePPM} PPM | ${scorePct}% Comprensión`);
}

function renderComprensionLectora(data, container) {
    window.compScores = 0;
    window.compAnswered = 0;
    
    // Check if comprension is array or single object
    let compData = Array.isArray(data.fase2_lectura.comprension) ? data.fase2_lectura.comprension : [data.fase2_lectura.comprension];
    const totalQs = compData.length;
    
    let html = `<div id="comprension-block" style="display:none; margin-top: 24px; padding: 16px; border: 1px solid var(--border-subtle); border-radius: 8px; background: rgba(0,0,0,0.2);">`;
    html += `<h4 style="color:var(--accent-water); margin-bottom: 16px;">Prueba de Comprensión Lector (Dashboard)</h4>`;
    
    compData.forEach((comp, qIndex) => {
        html += `<div class="comp-question" style="margin-bottom: 24px;">`;
        html += `<p style="font-size: 0.9rem; color: white; margin-bottom: 12px;"><strong>Q${qIndex+1}: ${comp.q}</strong></p>`;
        html += `<div style="display: flex; flex-direction: column; gap: 8px;">`;
        
        comp.options.forEach((opt, idx) => {
            const isCorrect = (idx === comp.answer);
            const ansText = comp.options[comp.answer].replace(/'/g, "\\\\'");
            html += `<button class="btn-outline" style="text-align: left; padding: 12px; font-size: 0.85rem;" onclick="window.showCompFeedback(this, ${isCorrect}, '${ansText}', ${qIndex}, ${totalQs})">${opt}</button>`;
        });
        html += `</div></div>`;
    });
    
    html += `</div>`;
    container.innerHTML += html;
}
"""
content = re.sub(r'window\.showCompFeedback = function.*?function renderComprensionLectora[^\}]+\}', comprension_js, content, flags=re.DOTALL)

# Ensure showMotivationToast exists
toast_js = """
function showMotivationToast(msg) {
    let t = document.createElement('div');
    t.innerText = msg;
    t.style = "position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%); background: var(--accent-water); color: white; padding: 12px 20px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); z-index: 10000; font-size: 0.85rem; font-weight: 500; opacity: 0; transition: opacity 0.3s; pointer-events: none;";
    document.body.appendChild(t);
    setTimeout(() => t.style.opacity = "1", 100);
    setTimeout(() => {
        t.style.opacity = "0";
        setTimeout(() => t.remove(), 300);
    }, 4000);
}
"""
if "showMotivationToast" not in content:
    content = content.replace('function showRealtimeNotification(msg) {', toast_js + '\nfunction showRealtimeNotification(msg) {')


# Phase 11 modification (En la mente)
content = content.replace('Escribe a mano en tu Libreta Invictus Mind:', 'Realiza este ensayo mentalmente (visualización profunda) y luego escríbelo en tu Libreta MindJump:')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print('app.html updated successfully.')
