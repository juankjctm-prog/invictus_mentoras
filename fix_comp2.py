import codecs
import re

with codecs.open('app.html', 'r', 'utf-8') as f:
    content = f.read()

start_idx = content.find('function renderComprensionLectora')
end_idx = content.find('// Global func to mark manual phases done')

if start_idx != -1 and end_idx != -1:
    old_comp = content[start_idx:end_idx]
    
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
}

"""
    content = content[:start_idx] + new_comp + content[end_idx:]
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(content)
    print('SUCCESS: Injected checkComprension and renderComprensionLectora')
else:
    print('FAILED to find markers')
