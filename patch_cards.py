import os
import re

dir_path = r"d:\Documents\Negocios\ASSINT\app\Invictus\invictus-web\Mapa espiritual\Mujeres mentoras"

files_to_patch = [f for f in os.listdir(dir_path) if f.endswith('.html') and not f.endswith('_fixed.html')]

card_sesion = r'''
<div class="card" style="background:linear-gradient(135deg, rgba(0,229,255,0.05), rgba(0,0,0,0.4)); border:1px solid var(--accent-water); border-radius:16px; padding:20px; margin-bottom:24px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
        <div style="background:rgba(0,198,255,0.15); color:var(--accent-water); padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:bold;"> ENTRENAMIENTO COGNITIVO & LECTURA BIÓNICA</div>
    </div>
    <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:6px; color:#fff;">Tu Espacio de Preparación Neuro-Lectora</h3>
    <p style="font-size:0.82rem; color:var(--text-secondary); line-height:1.5; margin-bottom:10px;">
        Antes de guiar a tu mentoreada, ejercita tu cerebro con la lectura del día, evalúa tu velocidad (PPM) con comprensión profunda y completa la rutina neuropedagógica.
    </p>
    <ul style="font-size:0.78rem; color:var(--text-secondary); padding-left:16px; line-height:1.6;">
        <li><strong style="color:var(--accent-water);">Modo Biónico:</strong> Usa el resaltado de fijación para apagar la subvocalización.</li>
        <li><strong style="color:#FFD700;">Recall Activo:</strong> Responde el quiz sin volver al texto para fortalecer tu memoria de trabajo.</li>
    </ul>
</div>
'''

card_playbook = r'''
<div class="card" style="background:linear-gradient(135deg, rgba(255,94,0,0.05), rgba(0,0,0,0.4)); border:1px solid var(--accent-fire); border-radius:16px; padding:20px; margin-bottom:24px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
        <div style="background:rgba(255,94,0,0.15); color:var(--accent-fire); padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:bold;"> GUÍA DE FACILITACIÓN 1-A-1</div>
    </div>
    <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:6px; color:#fff;">Tu Hoja de Ruta para la Sesión con tu Mentada</h3>
    <p style="font-size:0.82rem; color:var(--text-secondary); line-height:1.5; margin-bottom:10px;">
        Estructura la transformación de tu mentoreada en 2 momentos clave:
    </p>
    <ul style="font-size:0.78rem; color:var(--text-secondary); padding-left:16px; line-height:1.6;">
        <li><strong style="color:var(--accent-fire);">Paso 1 (Auto-Maestría):</strong> Completa tus 3 ejercicios de preparación antes de la reunión.</li>
        <li><strong style="color:var(--accent-water);">Paso 2 (Sesión 1-a-1):</strong> Envía el ancla de WhatsApp 24h antes, lanza la pregunta de coaching socrático y ejecuta el ejercicio de valor en vivo durante la reunión.</li>
    </ul>
</div>
'''

card_kit = r'''
<div class="card" style="background:linear-gradient(135deg, rgba(16,185,129,0.05), rgba(0,0,0,0.4)); border:1px solid var(--success); border-radius:16px; padding:20px; margin-bottom:24px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
        <div style="background:rgba(16,185,129,0.15); color:var(--success); padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:bold;"> CENTRO DE APOYO & CONTINGENCIAS</div>
    </div>
    <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:6px; color:#fff;">Tu Caja de Herramientas de Mentoría</h3>
    <p style="font-size:0.82rem; color:var(--text-secondary); line-height:1.5; margin-bottom:10px;">
        Respuestas tácticas para desatascar sesiones y calibrar tu criterio de liderazgo:
    </p>
    <ul style="font-size:0.78rem; color:var(--text-secondary); padding-left:16px; line-height:1.6;">
        <li><strong style="color:var(--success);">Coach de Crisis:</strong> Toca cualquier tarjeta cuando tu mentada llore, no avance, se muestre defensiva o se estanque la sesión.</li>
        <li><strong style="color:var(--accent-water);">Sala de Casos:</strong> Resuelve escenarios reales y recibe retroalimentación metodológica (Candor Radical, Escucha U, Humble Inquiry).</li>
    </ul>
</div>
'''

for f in files_to_patch:
    file_path = os.path.join(dir_path, f)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # 1. Remove the global card
    global_card_pattern = re.compile(r'<!-- NEURO-READING MANIFESTO -->.*?</div>\s*(?:<!-- DASHBOARD -->)?\s*<div id="view-dashboard"', re.DOTALL)
    if global_card_pattern.search(content):
        content = global_card_pattern.sub('<!-- DASHBOARD -->\n            <div id="view-dashboard"', content)
        modified = True
    else:
        # fallback regex if <!-- NEURO-READING MANIFESTO --> is not present
        alt_pattern = re.compile(r'<div class="card"[^>]*>\s*<div[^>]*>\s*<div[^>]*>.*?TU ENTRENAMIENTO COGNITIVO.*?</ul>\s*</div>\s*(?:<!-- DASHBOARD -->)?\s*<div id="view-dashboard"', re.DOTALL)
        if alt_pattern.search(content):
            content = alt_pattern.sub('<!-- DASHBOARD -->\n            <div id="view-dashboard"', content)
            modified = True
            
    # 2. Add to Session
    session_pattern = re.compile(r'(<div id="view-session"[^>]*>\s*)')
    if session_pattern.search(content) and "ENTRENAMIENTO COGNITIVO & LECTURA BIÓNICA" not in content:
        content = session_pattern.sub(r'\1' + card_sesion + '\n', content, count=1)
        modified = True

    # 3. Add to Playbook
    libreta_pattern = re.compile(r'(<div id="view-libreta"[^>]*>\s*)')
    if libreta_pattern.search(content) and "GUÍA DE FACILITACIÓN 1-A-1" not in content:
        content = libreta_pattern.sub(r'\1' + card_playbook + '\n', content, count=1)
        modified = True
        
    # 4. Add to Kit
    kit_pattern = re.compile(r'(<div id="view-kit"[^>]*>\s*<div class="kit-scroll">\s*(?:<div[^>]*>.*?</div>\s*)?)', re.DOTALL)
    if kit_pattern.search(content) and "CENTRO DE APOYO & CONTINGENCIAS" not in content:
        content = kit_pattern.sub(r'\1' + card_kit + '\n', content, count=1)
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
