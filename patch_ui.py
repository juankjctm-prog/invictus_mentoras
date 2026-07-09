import glob

for filename in glob.glob("Bloque*_Premium.html"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix undefined description in Dashboard
    content = content.replace('${day.desc}', '${day.desc || "Estrategia Avanzada"}')
    
    # Fix crash in Session View when recall array is missing
    target = "data.recall.forEach((r, idx) => {"
    if target in content and "if (data.recall)" not in content:
        # We need to wrap the loop in an if statement
        old_chunk = """            data.recall.forEach((r, idx) => {
                recallHTML += `
                    <div style="margin-bottom: 16px; background: rgba(255,94,0,0.05); border: 1px dashed rgba(255,94,0,0.3); padding: 16px; border-radius: 12px;">
                        <span style="font-size: 0.75rem; color: var(--accent-fire); text-transform: uppercase;">${r.type}</span>
                        <p style="font-size: 0.9rem; margin: 8px 0; color: white;">${r.q}</p>
                        <textarea class="input-premium" placeholder="Escribe tu respuesta analítica..."></textarea>
                    </div>
                `;
            });"""
            
        new_chunk = """            if (data.recall) {
                data.recall.forEach((r, idx) => {
                    recallHTML += `
                        <div style="margin-bottom: 16px; background: rgba(255,94,0,0.05); border: 1px dashed rgba(255,94,0,0.3); padding: 16px; border-radius: 12px;">
                            <span style="font-size: 0.75rem; color: var(--accent-fire); text-transform: uppercase;">${r.type}</span>
                            <p style="font-size: 0.9rem; margin: 8px 0; color: white;">${r.q}</p>
                            <textarea class="input-premium" placeholder="Escribe tu respuesta analítica..."></textarea>
                        </div>
                    `;
                });
            }"""
        content = content.replace(old_chunk, new_chunk)
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Patched all Premium HTML files.")
