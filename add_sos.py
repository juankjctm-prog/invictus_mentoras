import os
import re

css_snippet = """
        /* SOS Modal */
        .sos-overlay { position: fixed; inset: 0; background: var(--bg-absolute); z-index: 2000; display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.8s ease; backdrop-filter: blur(20px); }
        .sos-overlay.active { opacity: 1; pointer-events: auto; }
        .sos-circle { width: 150px; height: 150px; border-radius: 50%; background: radial-gradient(circle, var(--accent-water-glow) 0%, transparent 70%); box-shadow: 0 0 60px var(--accent-water-glow); animation: breathe 8s ease-in-out infinite; }
        @keyframes breathe { 0% { transform: scale(1); opacity: 0.5; } 50% { transform: scale(1.8); opacity: 1; } 100% { transform: scale(1); opacity: 0.5; } }
        .sos-text { margin-top: 80px; font-family: 'Outfit'; font-size: 1.3rem; font-weight: 300; text-align: center; max-width: 85%; line-height: 1.6; color: white; opacity: 0; transition: opacity 1s ease; }
        .sos-text.visible { opacity: 1; }
    </style>
"""

html_snippet = """
        <!-- PANTALLA SOS (Síndrome del Impostor) -->
        <div id="sos-overlay" class="sos-overlay">
            <h3 style="font-family: 'Outfit'; font-weight: 300; color: var(--accent-water); margin-bottom: 60px; letter-spacing: 4px; font-size: 0.9rem;">INHALA...</h3>
            <div class="sos-circle"></div>
            <p id="sos-affirmation" class="sos-text">No estás aquí por suerte. Estás aquí por tu luz, tu capacidad y tu resiliencia.</p>
            <button class="btn-outline" style="margin-top: 80px; border-color: rgba(255,255,255,0.2); color: white; padding: 12px 24px;" onclick="closeSOS()">Mi frecuencia se ha elevado</button>
        </div>

    <script>
        // LÓGICA SOS (Síndrome del Impostor - Regulación y Elevación de Frecuencia)
        const affirmations = [
            "No estás aquí por suerte. Estás aquí por tu inteligencia táctica y tu resiliencia.",
            "Tus resultados hablan más fuerte que tu síndrome del impostor. Respira tu evidencia.",
            "La incomodidad que sientes es neuroplasticidad en acción. Tu cerebro está expandiendo su capacidad. Sostenlo.",
            "No necesitas saberlo todo ahora. Eres una estratega, tu trabajo es descubrir la respuesta, no tenerla memorizada.",
            "Esa voz crítica no es la verdad, es solo el ego asustado. Tú eres la consciencia que observa al ego.",
            "El espacio que ocupas te pertenece. Lo ganaste. Respira en él y expándete."
        ];
        let sosInterval;

        function openSOS() {
            document.getElementById('sos-overlay').classList.add('active');
            let currentAff = 0;
            const textEl = document.getElementById('sos-affirmation');
            textEl.textContent = affirmations[currentAff];
            textEl.classList.add('visible');
            
            sosInterval = setInterval(() => {
                textEl.classList.remove('visible');
                setTimeout(() => {
                    currentAff = (currentAff + 1) % affirmations.length;
                    textEl.textContent = affirmations[currentAff];
                    textEl.classList.add('visible');
                }, 1000);
            }, 8000);
        }

        function closeSOS() {
            document.getElementById('sos-overlay').classList.remove('active');
            clearInterval(sosInterval);
            document.getElementById('sos-affirmation').classList.remove('visible');
        }
"""

def process(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if '.sos-overlay' not in content:
        content = content.replace('    </style>', css_snippet)
        modified = True
        
    if 'id="sos-overlay"' not in content:
        content = content.replace('    <script>', html_snippet)
        modified = True
        
    # fix button specifically for Protocolo SOS
    if 'onclick="openSOS()"' not in content:
        content = re.sub(r'(<button class="btn-outline"[^>]*?justify-content: center; background: var\(--bg-surface-elevated\);)(">)(\s*<span>🆘</span> Protocolo SOS)', r'\1" onclick="openSOS()">\3', content)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

folder = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras"
for file in os.listdir(folder):
    if file.endswith('_Premium.html'):
        process(os.path.join(folder, file))
