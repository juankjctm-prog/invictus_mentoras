import os
import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure we don't inject twice
if "function loadMujeresMentorasDay" not in content:
    injection = """
<script src="mujeresMentorasData.js"></script>
<script>
function loadMujeresMentorasDay(dayIndex) {
    const data = window.mujeresMentorasData.find(d => d.dia === dayIndex);
    if (!data) return;

    // Update Header
    const badge = document.querySelector('.session-hero .badge-premium');
    if (badge) badge.innerText = `${data.bloque} • Día ${data.dia}`;
    const title = document.querySelector('.session-hero .display-font');
    if (title) title.innerText = data.titulo;

    const phases = document.querySelectorAll('.timeline .phase');
    
    // F1: Ancla
    if (phases[0]) {
        const desc = phases[0].querySelector('.phase-desc');
        if (desc) desc.innerHTML = `<strong>Respiración de Oxigenación:</strong> ${data.fase1_ancla}`;
    }

    // F2: Lectura
    if (phases[1]) {
        const reader = document.getElementById('reader-content');
        if (reader) {
            let html = `<h4 style="color: white; margin-bottom: 12px; font-family: 'Outfit'; text-transform: uppercase;">${data.titulo}</h4>`;
            data.fase2_lectura.texto.split('\\n\\n').forEach(p => {
                html += `<p class="reader-p">${p}</p>`;
            });
            reader.innerHTML = html;
        }
    }

    // F3: Vocabulario
    if (phases[2]) {
        const desc = phases[2].querySelector('.phase-desc');
        if (desc) {
            let html = `<strong>Vocabulario Activo:</strong><br>`;
            data.fase3_vocabulario.forEach(v => {
                html += `<span style="color:var(--accent-fire)">${v.palabra}</span>: ${v.definicion}<br>`;
            });
            desc.innerHTML = html;
        }
    }

    // F4: Recall
    if (phases[3]) {
        const testContent = document.getElementById('test-content');
        if (testContent) {
            let html = '';
            data.fase4_recall.forEach((r, idx) => {
                html += `
                <div style="margin-bottom: 20px;" class="recall-q" data-ans="${r.answer}">
                    <p style="font-size: 0.9rem; margin-bottom: 12px; color: white;"><strong>${idx+1}. ${r.q}</strong></p>
                `;
                r.options.forEach((opt, oIdx) => {
                    html += `<label style="display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-secondary);"><input type="radio" name="q${idx}" value="${oIdx}"> ${opt}</label>`;
                });
                html += `</div>`;
            });
            html += `<button class="btn-outline" style="width: 100%; margin-top: 8px;" onclick="evaluarRecall()">📊 Evaluar Comprensión Cruzada</button>`;
            testContent.innerHTML = html;
        }
    }

    // F5: Codificación Dual
    if (phases[4]) {
        const desc = phases[4].querySelectorAll('.phase-desc')[1]; // The second phase-desc has the text
        if (desc) desc.innerText = data.fase5_codificacion_dual;
    }

    // F6: Loci
    if (phases[5]) {
        const desc = phases[5].querySelector('.phase-desc');
        if (desc) desc.innerText = data.fase6_loci;
    }

    // F7: Analogía
    if (phases[6]) {
        const desc = phases[6].querySelector('.phase-desc');
        if (desc) desc.innerText = data.fase7_analogia;
    }

    // F8: Ejercicio
    if (phases[7]) {
        const desc = phases[7].querySelectorAll('.phase-desc')[1];
        if (desc) desc.innerText = data.fase8_ejercicio;
    }

    // F9: Feynman
    if (phases[8]) {
        const desc = phases[8].querySelector('.phase-desc');
        if (desc) desc.innerText = data.fase9_feynman ? "Aplica la Técnica Feynman hoy." : "Aplica cada 7 sesiones. Hoy descansa.";
    }

    // F10: Metacognición
    if (phases[9]) {
        const desc = phases[9].querySelectorAll('.phase-desc')[1];
        if (desc) desc.innerText = data.fase10_metacognicion;
    }

    // F11: Ensayo
    if (phases[10]) {
        const desc = phases[10].querySelector('.phase-desc');
        if (desc) desc.innerText = data.fase11_ensayo;
    }

    // F12: Sueño
    if (phases[11]) {
        // Here we could update affirmations variable if it exists in the global scope
        if (typeof window.affirmations !== 'undefined') {
            window.affirmations = [
                data.fase12_sueno.afirmacion1,
                data.fase12_sueno.afirmacion2,
                data.fase12_sueno.afirmacion3
            ];
        }
    }
}

// Llama a la función automáticamente cuando la página carga
document.addEventListener("DOMContentLoaded", () => {
    // Si la variable está lista
    if (window.mujeresMentorasData) {
        loadMujeresMentorasDay(1);
    }
});
</script>
</body>"""
    content = content.replace("</body>", injection)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully injected dynamic loading logic into {html_file}")
else:
    print(f"Injection already present in {html_file}")
