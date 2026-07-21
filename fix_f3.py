import codecs
import re

with codecs.open('app.html', 'r', 'utf-8') as f:
    content = f.read()

# 1. Update HTML for F3
old_f3_html = """<!-- F3 -->
                    <div class="phase">
                        <div class="phase-node"></div>
                        <div class="phase-header"><h4>3. Síntesis Ejecutiva</h4><span class="phase-duration">1m</span></div>
                        <p class="phase-desc">Como mentora, debes destilar conocimiento complejo en principios simples.</p>
                        <input type="text" class="input-premium" placeholder="Resume la idea principal en 1 frase para tu mentoreada...">
                    </div>"""

new_f3_html = """<!-- F3 -->
                    <div class="phase">
                        <div class="phase-node"></div>
                        <div class="phase-header"><h4>3. Síntesis Ejecutiva</h4><span class="phase-duration">1m</span></div>
                        <div id="f3-vocab-container" style="margin-bottom: 12px; font-size: 0.85rem; color: #a1a1aa; background: rgba(0,0,0,0.2); padding: 8px; border-radius: 6px; display: none;"></div>
                        <p class="phase-desc">Como mentora, debes destilar conocimiento complejo en principios simples.</p>
                        <input type="text" id="f3-input" class="input-premium" placeholder="Resume la idea principal en 1 frase para tu mentoreada...">
                        <button class="btn-outline" id="f3-save-btn" style="width: 100%; margin-top: 8px;" onclick="window.markPhaseDone(this, 3); document.getElementById('f3-input').disabled = true;">💾 Guardar Síntesis</button>
                    </div>"""

if old_f3_html in content:
    content = content.replace(old_f3_html, new_f3_html)
else:
    print("WARNING: F3 HTML not found directly. Using regex.")
    content = re.sub(r'<!-- F3 -->.*?<input type="text" class="input-premium" placeholder="Resume la idea principal en 1 frase para tu mentoreada...">\s*</div>', new_f3_html, content, flags=re.DOTALL)


# 2. Update JS loadMujeresMentorasDay for F3
old_f3_js = """// F3: Vocabulario
    if (phases[2]) {
        const desc = phases[2].querySelector('.phase-desc');
        if (desc) {
            let html = `<strong>Vocabulario Activo:</strong><br>`;
            if(data.fase3_vocabulario) {
                data.fase3_vocabulario.forEach(v => {
                    html += `<span style="color:var(--accent-fire)">${v.palabra}</span>: ${v.definicion}<br>`;
                });
            }
            desc.innerHTML = html;
        }
    }"""

new_f3_js = """// F3: Vocabulario
    if (phases[2]) {
        const vocabContainer = document.getElementById('f3-vocab-container');
        const input = document.getElementById('f3-input');
        const saveBtn = document.getElementById('f3-save-btn');
        
        // Reset state
        if(input) { input.value = ''; input.disabled = false; }
        if(saveBtn) { 
            saveBtn.innerText = '💾 Guardar Síntesis'; 
            saveBtn.style.color = ''; 
            saveBtn.style.borderColor = ''; 
        }

        if (vocabContainer) {
            if(data.fase3_vocabulario && data.fase3_vocabulario.length > 0 && data.fase3_vocabulario[0].palabra !== "Concepto Clave") {
                let html = `<strong style="color:white;">Vocabulario Activo:</strong><br>`;
                data.fase3_vocabulario.forEach(v => {
                    html += `<span style="color:var(--accent-fire)">${v.palabra}</span>: ${v.definicion}<br>`;
                });
                vocabContainer.innerHTML = html;
                vocabContainer.style.display = 'block';
            } else {
                vocabContainer.style.display = 'none'; // Hide if it's the default placeholder
            }
        }
    }"""

if old_f3_js in content:
    content = content.replace(old_f3_js, new_f3_js)
else:
    print("WARNING: F3 JS not found directly. Using regex.")
    # The snippet is quite static, it should be found.

with codecs.open('app.html', 'w', 'utf-8') as f:
    f.write(content)

print("F3 UI and logic updated.")
