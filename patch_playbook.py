import re

with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Modify <div id="view-libreta" class="view">
old_libreta_start = content.find('<div id="view-libreta" class="view">')
old_libreta_end = content.find('<div id="view-kit" class="view">')

if old_libreta_start != -1 and old_libreta_end != -1:
    new_libreta = """<div id="view-libreta" class="view">
        <div class="card" style="background:linear-gradient(135deg, rgba(255,94,0,0.05), rgba(0,0,0,0.4)); border:1px solid var(--accent-fire); border-radius:16px; padding:20px; margin-bottom:24px;">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                <div style="background:rgba(255,94,0,0.15); color:var(--accent-fire); padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:bold;"> GUÍA DE FACILITACIÓN 1-A-1</div>
            </div>
            <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:6px; color:#fff;">Tu Hoja de Ruta para la Sesión con tu Mentada</h3>
            <p style="font-size:0.82rem; color:var(--text-secondary); line-height:1.5; margin-bottom:10px;">
                Estructura la transformación de tu mentoreada en 2 momentos clave:
            </p>
        </div>

        <!-- PASO 1 -->
        <div class="phase active">
            <div class="phase-node"></div>
            <div class="phase-header"><h4 style="color: var(--accent-water);">PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)</h4></div>
            <p class="phase-desc" style="margin-bottom:12px;">3 ejercicios de introspección para la mentora antes de la cita.</p>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">1. Purga de Prejuicios</p>
                <p style="color:var(--text-secondary); font-size:0.85rem;">¿Qué sesgos tengo sobre esta persona basados en su rol, edad o interacción previa?</p>
            </div>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">2. Definición del 'Por Qué'</p>
                <p style="color:var(--text-secondary); font-size:0.85rem;">¿Qué transformación específica busco catalizar en ella hoy?</p>
            </div>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">3. Anclaje de Presencia</p>
                <p style="color:var(--text-secondary); font-size:0.85rem;">(Realiza 2 ciclos de respiración táctica 4-8-16 antes de iniciar la videollamada).</p>
            </div>
        </div>

        <!-- PASO 2 -->
        <div class="phase active" style="margin-top:40px;">
            <div class="phase-node"></div>
            <div class="phase-header"><h4 style="color: var(--accent-fire);">PASO 2: GUÍA DE LA SESIÓN 1-A-1</h4></div>
            <p class="phase-desc" style="margin-bottom:12px;">Ejecución interactiva durante la sesión.</p>
            <div style="background:rgba(255,94,0,0.05); padding:16px; border-radius:12px; border:1px solid rgba(255,94,0,0.2); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">A. Mensaje Ancla (24h antes)</p>
                <p style="color:var(--text-secondary); font-size:0.85rem; font-style:italic;">"Hola [Nombre], nos vemos mañana. Por favor piensa en [Tema específico] para discutirlo a profundidad."</p>
            </div>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">B. Pregunta de Coaching Socrático</p>
                <p style="color:var(--text-secondary); font-size:0.85rem; margin-bottom:8px;">En lugar de darle la respuesta, pregúntale para que ella misma descubra el camino.</p>
                <button class="btn-outline" style="width:100%; border-color:var(--accent-water); color:var(--accent-water);" onclick="openSalaModal()">Ver Casos Socráticos (Sala)</button>
            </div>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">C. Ejercicio de Valor en Vivo</p>
                <p style="color:var(--text-secondary); font-size:0.85rem;">Práctica o Role-play de un escenario de negociación o liderazgo en ese momento.</p>
            </div>
            <div style="background:rgba(255,255,255,0.02); padding:16px; border-radius:12px; border:1px solid var(--border-subtle); margin-bottom:10px;">
                <p style="color:white; font-size:0.9rem; font-weight:bold; margin-bottom:8px;">D. Asignación de Riesgo Táctico (Tarea de 48h)</p>
                <p style="color:var(--text-secondary); font-size:0.85rem;">Que aplique lo aprendido en las siguientes 48 horas y te reporte por WhatsApp.</p>
            </div>
        </div>
        <br><br><br><br>
    </div>
    """
    content = content[:old_libreta_start] + new_libreta + content[old_libreta_end:]

# Inject Modals (CRISIS_DATA, CASOS_DATA)
# I will append them at the end of the <body>
modals = """
    <!-- Sala de Casos Modal (Socrático) -->
    <div id="sala-modal" style="display:none;position:fixed;inset:0;z-index:7000;background:rgba(6,6,13,.98);padding:20px 24px 24px;overflow-y:auto">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding-top:10px">
        <h3 style="font-family:'Outfit';font-size:1.1rem;color:var(--accent-water);">SALA DE CASOS SOCRÁTICOS</h3>
        <button onclick="document.getElementById('sala-modal').style.display='none'" style="background:transparent;border:none;color:var(--text-secondary);font-size:1.6rem;cursor:pointer;width:40px;height:40px">×</button>
      </div>
      <div>
        <h4 style="color:white;margin-bottom:10px;">Preguntas Poderosas</h4>
        <ul style="color:var(--text-secondary);font-size:0.9rem;padding-left:20px;line-height:1.6;">
            <li>¿Qué es lo peor que podría pasar si tomas esa decisión?</li>
            <li>¿Qué estás evitando al no tener esa conversación difícil?</li>
            <li>Si no tuvieras miedo, ¿qué harías en este momento?</li>
            <li>¿Cómo te está limitando tu creencia actual sobre este problema?</li>
        </ul>
      </div>
    </div>

    <!-- Protocolos de Crisis Modal -->
    <div id="crisis-modal-mm" style="display:none;position:fixed;inset:0;z-index:7000;background:rgba(6,6,13,.98);padding:20px 24px 24px;overflow-y:auto">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding-top:10px">
        <h3 style="font-family:'Outfit';font-size:1.1rem;color:var(--accent-fire);">PROTOCOLOS DE CRISIS</h3>
        <button onclick="document.getElementById('crisis-modal-mm').style.display='none'" style="background:transparent;border:none;color:var(--text-secondary);font-size:1.6rem;cursor:pointer;width:40px;height:40px">×</button>
      </div>
      <div>
        <div style="background:rgba(255,69,0,0.1); border-left:4px solid #FF4500; padding:15px; margin-bottom:15px; border-radius:4px;">
            <h4 style="color:white;margin-bottom:5px;">Si la mentada llora o se desborda:</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;">Mantén el silencio empático. No intentes 'arreglarla' rápido. Ofrécele agua, pausa y di: "Tómate tu tiempo, estoy aquí contigo".</p>
        </div>
        <div style="background:rgba(255,165,0,0.1); border-left:4px solid #FFA500; padding:15px; margin-bottom:15px; border-radius:4px;">
            <h4 style="color:white;margin-bottom:5px;">Si se muestra defensiva:</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;">No debatas. Escucha hasta el final y devuelve en espejo: "Escucho que te sientes atacada por esto, ¿es así?". Redirige al objetivo.</p>
        </div>
        <div style="background:rgba(0,198,255,0.1); border-left:4px solid var(--accent-water); padding:15px; margin-bottom:15px; border-radius:4px;">
            <h4 style="color:white;margin-bottom:5px;">Si se estanca la sesión:</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;">Cambia el estado físico. "Levantémonos 1 minuto, estiremos los brazos y volvamos a sentarnos". Reinicia con otra perspectiva.</p>
        </div>
      </div>
    </div>
"""
idx_body_end = content.rfind("</body>")
if idx_body_end != -1:
    content = content[:idx_body_end] + modals + "\n" + content[idx_body_end:]

# Add JS functions to open modals
js_functions = """
window.openSalaModal = function() {
    document.getElementById('sala-modal').style.display = 'block';
};
window.openCrisisModal = function() {
    document.getElementById('crisis-modal-mm').style.display = 'block';
};
"""
idx_script = content.rfind("</script>")
if idx_script != -1:
    content = content[:idx_script] + js_functions + "\n" + content[idx_script:]


with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched playbook successfully.")
