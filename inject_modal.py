import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the button to trigger a modal instead of going to app.html
old_button = r'<a href="app\.html" class="cta-btn" style="display:inline-block; width:100%; margin-top:10px;">Adquirir Programa</a>'
new_button = '<button onclick="openLeadModal()" class="cta-btn" style="display:inline-block; width:100%; margin-top:10px;">Adquirir Programa</button>'
content = re.sub(old_button, new_button, content)

# 2. Add Modal CSS
modal_css = """
        /* MODAL STYLES */
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8); backdrop-filter: blur(5px);
            display: none; justify-content: center; align-items: center; z-index: 2000;
            opacity: 0; transition: opacity 0.3s;
        }
        .modal-box {
            background: rgba(20,20,20,0.9);
            border: 1px solid rgba(0, 229, 255, 0.3);
            padding: 40px; border-radius: 20px; width: 90%; max-width: 400px;
            text-align: center; box-shadow: 0 0 30px rgba(0, 229, 255, 0.2);
            transform: translateY(20px); transition: transform 0.3s;
        }
        .modal-input {
            width: 100%; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
            padding: 15px; border-radius: 10px; color: white; font-family: 'Inter'; margin-bottom: 15px;
            outline: none;
        }
        .modal-input:focus { border-color: var(--accent-water); }
        .close-btn { position: absolute; top: 15px; right: 20px; background: none; border: none; color: #888; font-size: 1.5rem; cursor: pointer; }
</style>
"""
content = content.replace('</style>', modal_css)

# 3. Add Modal HTML and JS before </body>
modal_html = """
    <!-- LEADS MODAL -->
    <div id="lead-modal" class="modal-overlay">
        <div class="modal-box" id="lead-box">
            <button class="close-btn" onclick="closeLeadModal()">×</button>
            <h3 style="color:var(--accent-water); font-size:1.8rem; margin-bottom:10px;">Postula a Invictus</h3>
            <p style="color:var(--text-dim); font-size:0.9rem; margin-bottom:25px;">Déjanos tus datos para enviarte los detalles de pago y acceso al Master Track.</p>
            
            <input type="text" id="lead-name" class="modal-input" placeholder="Tu Nombre Completo">
            <input type="email" id="lead-email" class="modal-input" placeholder="Tu Correo Electrónico">
            
            <button onclick="submitLead()" class="cta-btn" style="width:100%; margin-top:10px;">Enviar Solicitud</button>
        </div>
    </div>

    <script>
        function openLeadModal() {
            const modal = document.getElementById('lead-modal');
            const box = document.getElementById('lead-box');
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.style.opacity = '1';
                box.style.transform = 'translateY(0)';
            }, 10);
        }

        function closeLeadModal() {
            const modal = document.getElementById('lead-modal');
            const box = document.getElementById('lead-box');
            modal.style.opacity = '0';
            box.style.transform = 'translateY(20px)';
            setTimeout(() => { modal.style.display = 'none'; }, 300);
        }

        function submitLead() {
            const name = document.getElementById('lead-name').value.trim();
            const email = document.getElementById('lead-email').value.trim();
            
            if(!name || !email) {
                alert('Por favor completa todos los campos.');
                return;
            }

            const box = document.getElementById('lead-box');
            box.innerHTML = `
                <div style="font-size:4rem; margin-bottom:10px;">✨</div>
                <h3 style="color:var(--accent-earth); font-size:1.8rem; margin-bottom:10px;">¡Gracias, ${name.split(' ')[0]}!</h3>
                <p style="color:var(--text-main); font-size:1rem; margin-bottom:25px;">Hemos recibido tus datos correctamente.</p>
                <p style="color:var(--text-dim); font-size:0.9rem; border-top:1px solid rgba(255,255,255,0.1); padding-top:20px;"><strong>Pronto nos pondremos en contacto contigo</strong> al correo ${email} con los siguientes pasos.</p>
                <button onclick="closeLeadModal()" class="btn-login" style="margin-top:20px; width:100%;">Cerrar</button>
            `;
        }
    </script>
</body>
"""
content = content.replace('</body>', modal_html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal added.")
