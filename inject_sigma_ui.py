import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

sigma_html = """
    <!-- SIGMA COACH FAB & MODAL -->
    <div id="sigma-fab" onclick="toggleSigmaChat()" style="position:fixed; bottom:110px; right:20px; width:60px; height:60px; border-radius:50%; background:linear-gradient(135deg, #111, #222); border:2px solid var(--accent-water); display:flex; justify-content:center; align-items:center; cursor:pointer; z-index:9000; box-shadow:0 0 20px rgba(0, 229, 255, 0.4); transition:transform 0.3s;">
        <span style="font-size:2rem;">🧠</span>
    </div>

    <div id="sigma-modal" style="position:fixed; bottom:180px; right:20px; width:350px; max-width:calc(100vw - 40px); height:500px; max-height:60vh; background:rgba(10,10,12,0.95); backdrop-filter:blur(20px); border:1px solid var(--accent-water); border-radius:16px; display:flex; flex-direction:column; z-index:9000; opacity:0; pointer-events:none; transform:translateY(20px); transition:all 0.3s ease; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.8);">
        <div style="padding:15px 20px; border-bottom:1px solid rgba(0, 229, 255, 0.2); display:flex; justify-content:space-between; align-items:center; background:linear-gradient(90deg, rgba(0,229,255,0.1), transparent);">
            <div style="display:flex; align-items:center; gap:10px;">
                <span style="font-size:1.5rem;">🧠</span>
                <div>
                    <h3 style="font-family:'Outfit'; color:white; font-size:1.1rem; margin:0;">Sigma Coach</h3>
                    <span style="font-size:0.7rem; color:var(--accent-water);">Asistente IA de Invictus</span>
                </div>
            </div>
            <button onclick="toggleSigmaChat()" style="background:transparent; border:none; color:white; font-size:1.5rem; cursor:pointer;">×</button>
        </div>
        
        <div id="sigma-chat-history" style="flex:1; padding:20px; overflow-y:auto; display:flex; flex-direction:column; gap:15px;">
            <div class="sigma-msg received">
                Hola, soy Sigma. Estoy aquí para acompañarte en tu transformación hacia el liderazgo. ¿En qué bloque o fase tienes dudas hoy?
            </div>
        </div>
        
        <div style="padding:15px; border-top:1px solid rgba(255,255,255,0.1); display:flex; gap:10px;">
            <input type="text" id="sigma-input" placeholder="Pregúntale a Sigma..." onkeypress="if(event.key === 'Enter') sendSigmaMessage()" style="flex:1; background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.2); border-radius:20px; padding:10px 15px; color:white; font-family:'Inter'; outline:none;">
            <button onclick="sendSigmaMessage()" style="background:var(--accent-water); color:black; border:none; width:40px; height:40px; border-radius:50%; cursor:pointer; display:flex; justify-content:center; align-items:center; font-size:1.2rem;">➤</button>
        </div>
    </div>
    <style>
        .sigma-msg { max-width:85%; padding:12px 16px; border-radius:12px; font-size:0.9rem; line-height:1.4; word-wrap:break-word; font-family:'Inter'; }
        .sigma-msg.sent { align-self:flex-end; background:rgba(255,255,255,0.1); color:white; border-bottom-right-radius:2px; }
        .sigma-msg.received { align-self:flex-start; background:rgba(0,229,255,0.1); color:white; border:1px solid rgba(0,229,255,0.3); border-bottom-left-radius:2px; box-shadow:0 0 10px rgba(0,229,255,0.1); }
        .sigma-thinking { align-self:flex-start; color:var(--accent-water); font-size:0.8rem; font-style:italic; display:none; margin-left:10px; }
    </style>
"""

# Insert right before </main>
pattern = r'</main>'
if r'<!-- SIGMA COACH FAB & MODAL -->' not in content:
    content = re.sub(pattern, sigma_html + '\n</main>', content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Sigma HTML added.")
else:
    print("Sigma HTML already exists.")
