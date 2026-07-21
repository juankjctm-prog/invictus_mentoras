import codecs

with codecs.open('app.html', 'r', 'utf-8') as f:
    content = f.read()

start_marker = "// F3: Vocabulario"
end_marker = "// F4: Recall"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    old_js = content[start_idx:end_idx]
    
    new_js = """// F3: Vocabulario
    if (phases[2]) {
        const vocabContainer = document.getElementById('f3-vocab-container');
        const input = document.getElementById('f3-input');
        const saveBtn = document.getElementById('f3-save-btn');
        const desc = phases[2].querySelector('.phase-desc');
        
        // Reset state
        if(input) { input.value = ''; input.disabled = false; }
        if(saveBtn) { 
            saveBtn.innerText = '💾 Guardar Síntesis'; 
            saveBtn.style.color = ''; 
            saveBtn.style.borderColor = ''; 
        }
        if(desc) {
            desc.style.display = 'block'; // Make sure instructions are visible
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
    }

    """
    
    content = content[:start_idx] + new_js + content[end_idx:]
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(content)
    print("SUCCESS: F3 JS logic updated!")
else:
    print("FAILED to find markers")
