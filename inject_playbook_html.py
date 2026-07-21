import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_playbook = """<!-- LIBRETA (PLAYBOOK DIGITAL) -->
            <div id="view-libreta" class="view" style="padding-bottom:100px; padding-top:40px; height:100vh; overflow-y:auto;">
                <div class="session-hero stagger-1" style="padding: 0 20px;">
                    <h2 class="display-font" style="font-size: 1.8rem; margin-bottom: 8px;">Playbook Digital</h2>
                    <p style="color: var(--text-secondary); font-size: 0.85rem;">Tu bitácora de auto-maestría y reflexiones de impacto.</p>
                </div>
                
                <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); padding: 15px; border-radius: 12px; margin: 20px; display:flex; flex-direction:column; gap:10px;">
                    <span style="font-family:'Outfit'; font-weight:600; color:var(--text-secondary); font-size:0.9rem;">Seleccionar Día:</span>
                    <select id="playbook-day-selector" onchange="loadPlaybookContent(this.value)" style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); color: var(--text-primary); padding: 12px; border-radius: 8px; font-family: 'Inter'; font-size: 1rem; width:100%; outline:none;">
                        <!-- Options filled via JS -->
                    </select>
                </div>

                <div id="playbook-content-area" style="padding: 0 20px;">
                    <div style="text-align:center; padding: 40px 0; color: var(--text-tertiary);">Selecciona un día para ver o escribir tus apuntes...</div>
                </div>
            </div>
        </main>"""

pattern = r'<div id="view-libreta" class="view">.*?</main>'

if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, new_playbook, content, flags=re.DOTALL)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Playbook HTML replaced successfully.")
else:
    print("Pattern not found!")
