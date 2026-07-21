import codecs
import re

file_path = 'app.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Fix renderComprensionLectora
old_comp = """function renderComprensionLectora(data, container) {
    if(!data.fase2_lectura.comprension) return;
    const comp = data.fase2_lectura.comprension;
    
    let html = `
    <div style="margin-top: 24px; padding: 16px; background: rgba(0, 198, 255, 0.05); border: 1px solid rgba(0, 198, 255, 0.2); border-radius: 12px;">
        <h5 style="color: var(--accent-water); font-family: 'Outfit'; margin-bottom: 8px;">EXTRA: COMPRENSIÓN LECTORA</h5>
        <p style="font-size: 0.9rem; color: white; margin-bottom: 12px;">${comp.q}</p>
    `;
    
    comp.options.forEach((opt, idx) => {
        html += `
        <label style="display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-secondary); cursor:pointer;">
            <input type="radio" name="comprension" value="${idx}" onchange="checkComprension(${comp.answer}, this)"> ${opt}
        </label>`;
    });
    
    html += `<div id="comp-feedback" style="margin-top: 10px; font-weight:bold; font-size: 0.85rem;"></div></div>`;
    
    const div = document.createElement('div');
    div.innerHTML = html;
    container.appendChild(div);
}

window.checkComprension = function(correctIdx, el) {
    const feedback = document.getElementById('comp-feedback');
    if(parseInt(el.value) === correctIdx) {
        feedback.innerText = "✓ Respuesta correcta. Excelente comprensión táctica.";
        feedback.style.color = "var(--success)";
        completePhase(2); // Auto-complete phase 2
    } else {
        feedback.innerText = "✗ Incorrecto. Revisa el texto e intenta de nuevo.";
        feedback.style.color = "var(--accent-fire)";
    }
}"""

new_comp = """window.checkComprension = function(qIdx, correctIdx, btnIdx, btnElement) {
    if(btnIdx === correctIdx) {
        btnElement.style.background = "linear-gradient(45deg, #10b981, #059669)";
        btnElement.style.color = "white";
        btnElement.style.borderColor = "var(--success)";
        btnElement.innerText += " ✓ Correcto";
        
        let allCorrect = true;
        document.querySelectorAll('.comp-question').forEach(q => {
            if(!q.querySelector('button[style*="#10b981"]')) allCorrect = false;
        });
        if(allCorrect) {
            completePhase(2);
            showMotivationToast("¡Comprensión táctica perfecta! Fase 2 completada.");
        }
    } else {
        btnElement.style.background = "rgba(239, 68, 68, 0.2)";
        btnElement.style.borderColor = "var(--accent-fire)";
        btnElement.innerText += " ✗ Incorrecto";
    }
    
    // Disable siblings
    const siblings = btnElement.parentElement.querySelectorAll('button');
    siblings.forEach(s => s.disabled = true);
};

function renderComprensionLectora(data, container) {
    if(!data.fase2_lectura.comprension) return;
    
    let compData = Array.isArray(data.fase2_lectura.comprension) ? data.fase2_lectura.comprension : [data.fase2_lectura.comprension];
    
    let html = `
    <div id="comprension-block" style="display: none; margin-top: 24px; padding: 16px; background: rgba(0, 198, 255, 0.05); border: 1px solid rgba(0, 198, 255, 0.2); border-radius: 12px;">
        <h5 style="color: var(--accent-water); font-family: 'Outfit'; margin-bottom: 12px;">EVALUACIÓN DE COMPRENSIÓN</h5>
    `;
    
    compData.forEach((comp, qIdx) => {
        html += `<div class="comp-question" style="margin-bottom: 20px;">
            <p style="font-size: 0.95rem; color: white; margin-bottom: 12px;"><strong>Pregunta ${qIdx + 1}:</strong> ${comp.q}</p>
            <div style="display: flex; flex-direction: column; gap: 8px;">`;
            
        comp.options.forEach((opt, optIdx) => {
            html += `<button class="btn-outline" style="text-align: left; font-size: 0.85rem; padding: 10px;" onclick="checkComprension(${qIdx}, ${comp.answer}, ${optIdx}, this)">${opt}</button>`;
        });
        
        html += `</div></div>`;
    });
    
    html += `</div>`;
    
    const div = document.createElement('div');
    div.innerHTML = html;
    container.appendChild(div);
}"""

if old_comp in content:
    content = content.replace(old_comp, new_comp)
else:
    print("WARNING: Could not find old_comp in app.html")
    # regex fallback
    content = re.sub(r'function renderComprensionLectora.*?\}\n\n\}', new_comp, content, flags=re.DOTALL)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Comprension HTML/JS updated in app.html")
