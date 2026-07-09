#!/usr/bin/env python3
"""
Inyecta Sigma Coach en Bloques 2-8 de Mujeres Mentoras
"""

import os

BASE_DIR = r"C:\Users\mcastro\Documents\Claude\Projects\Mapa espiritual\Mujeres mentoras"

# Sigma prompts por bloque (10 días cada uno, B8 tiene 8)
SIGMA_PROMPTS = {
    2: {  # Bloque 2: días 11-20
        11: { "advice": "La comunicación de alto impacto no es lo que dices, es lo que el otro escucha. Tu mentoreada no necesita más información — necesita sentirse comprendida antes de ser corregida.", "prompt": "¿Cuándo fue la última vez que reformulaste lo que tu mentoreada dijo antes de dar tu opinión?" },
        12: { "advice": "El feedback efectivo sigue la regla 3:1: tres validaciones específicas por cada área de mejora. No es suavizar — es neurociencia. El cerebro receptivo aprende cuando no está en defensa.", "prompt": "Escribe el último feedback que diste. ¿Cuántas validaciones específicas incluiste?" },
        13: { "advice": "Las preguntas poderosas no buscan respuestas correctas — buscan expandir la perspectiva. '¿Qué pasaría si...?' abre más que '¿Por qué hiciste...?'", "prompt": "Transforma una pregunta acusadora reciente en una pregunta que expanda posibilidades." },
        14: { "advice": "La escucha activa no es silencio mientras hablan. Es detectar lo que NO se dice: el tono, la pausa, la palabra que evitan. Ahí está la información real.", "prompt": "¿Qué no dijo tu mentoreada en tu última sesión que tú notaste pero no abordaste?" },
        15: { "advice": "El cierre de bloque es un punto de inflexión. Lo que integraste en estos 10 días no es teoría — es tu nuevo operating system como mentora. No lo subestimes.", "prompt": "¿Qué habilidad de comunicación descubriste que ya tenías pero no usabas conscientemente?" },
        16: { "advice": "La influencia no es manipulación — es alinear tu mensaje con los valores del otro. Si sabes qué le importa, tu mensaje entra sin resistencia.", "prompt": "¿Cuál es el valor central de tu mentoreada que puedes usar como puente para tu próximo mensaje difícil?" },
        17: { "advice": "El silencio estratégico vale más que mil palabras. Después de una pregunta poderosa, espera 7 segundos. La magia ocurre en el silencio, no en tu siguiente frase.", "prompt": "Cuenta mentalmente hasta 7 la próxima vez que hagas una pregunta importante. Observa qué pasa." },
        18: { "advice": "Las historias transforman datos en significado. Tu mentoreada no recordará tus estadísticas — recordará cómo la hiciste sentir con una historia bien contada.", "prompt": "¿Qué historia personal puedes compartir esta semana que ilustre el punto que quieres reforzar?" },
        19: { "advice": "La confrontación compasiva no es evitar el conflicto — es nombrar la verdad con cuidado. 'Veo que...' es más poderoso que 'Tú siempre...'", "prompt": "¿Qué verdad difícil necesitas nombrar esta semana? Escríbela empezando con 'Veo que...'" },
        20: { "advice": "Tu evolución como mentora se mide en las conversaciones que antes evitabas y ahora abordas con calma. Eso es crecimiento real.", "prompt": "Escribe una oración que capture cómo ha cambiado tu forma de comunicarte en estos 10 días." }
    },
    3: {  # Bloque 3: días 21-30
        21: { "advice": "La inteligencia emocional no es controlar emociones — es usarlas como datos. Tu frustración con una mentoreada es información sobre un límite que no pusiste.", "prompt": "¿Qué emoción sentiste en tu última sesión? ¿Qué dato te está dando sobre tu liderazgo?" },
        22: { "advice": "La empatía estratégica no es sentir lo que el otro siente — es comprender su contexto para actuar con precisión. Puedes ser firme y empática simultáneamente.", "prompt": "Describe una situación donde puedes ser más firme sin perder la empatía." },
        23: { "advice": "El autoconocimiento es tu herramienta más poderosa. Los triggers que te activan no son defectos — son mapas hacia tus áreas de crecimiento.", "prompt": "¿Qué comportamiento de tu mentoreada te activa emocionalmente? ¿Qué dice eso de ti?" },
        24: { "advice": "La regulación emocional no es suprimir — es pausar entre estímulo y respuesta. Ese espacio de 3 segundos es donde vive tu poder de elección.", "prompt": "La próxima vez que sientas un trigger, cuenta 3 segundos antes de responder. ¿Qué cambia?" },
        25: { "advice": "La vulnerabilidad estratégica no es debilidad — es coraje visible. Cuando nombras tus propias luchas, das permiso para que otros hagan lo mismo.", "prompt": "¿Qué vulnerabilidad estratégica puedes mostrar esta semana que fortalezca la confianza?" },
        26: { "advice": "Las relaciones difíciles no se resuelven evitando — se transforman comprendiendo el miedo del otro. Detrás de cada comportamiento difícil hay una necesidad no expresada.", "prompt": "¿Qué necesidad no expresada hay detrás del comportamiento más desafiante de tu mentoreada?" },
        27: { "advice": "Tu estado emocional contagia. Si entras ansiosa, tu mentoreada se cierra. Si entras centrada, se abre. Tu regulación es tu mayor herramienta de influencia.", "prompt": "Antes de tu próxima sesión, haz 3 respiraciones profundas. Observa cómo cambia la dinámica." },
        28: { "advice": "El perdón no es para el otro — es para liberar tu energía. Cada resentimiento que sueltas es espacio que recuperas para tu liderazgo.", "prompt": "¿A quién necesitas perdonar para liberar energía que estás gastando en mantener el enojo?" },
        29: { "advice": "La resiliencia emocional no es no sentir dolor — es recuperarte más rápido. Cada vez que te regulas, fortaleces tu circuito de recuperación.", "prompt": "¿Cuánto te toma recuperarte de una sesión difícil? ¿Qué puedes hacer para acortar ese tiempo?" },
        30: { "advice": "Tu inteligencia emocional es un músculo. Lo que hoy te desestabiliza, en 30 días te dará datos. No busques no sentir — busca sentir con más información.", "prompt": "Escribe una oración sobre cómo ha evolucionado tu gestión emocional en estos 10 días." }
    },
    4: {  # Bloque 4: días 31-40
        31: { "advice": "El pensamiento estratégico no es predecir el futuro — es preparar múltiples escenarios. Tu mentoreada no necesita que tengas respuestas — necesita que hagas mejores preguntas.", "prompt": "¿Qué escenario no has considerado en el desarrollo de tu mentoreada?" },
        32: { "advice": "La visión sistémica ve conexiones donde otros ven eventos aislados. El problema que tu mentoreada trae hoy probablemente conecta con un patrón más grande.", "prompt": "¿Qué patrón recurrente ves en los desafíos que tu mentoreada presenta?" },
        33: { "advice": "Las decisiones estratégicas se toman con datos, no con urgencia. Si algo es urgente pero no importante, probablemente no merece tu atención ahora.", "prompt": "¿Qué decisión urgente puedes postergar para evaluar si realmente importa?" },
        34: { "advice": "El pensamiento de segundo orden pregunta '¿Y después qué?'. Cada intervención tiene consecuencias en cadena — las mentoras estratégicas las anticipan.", "prompt": "Si intervienes en la situación actual de tu mentoreada, ¿qué desencadenas a 3 meses?" },
        35: { "advice": "La priorización estratégica no es hacer más — es hacer menos con más impacto. El 20% de tus intervenciones genera el 80% del crecimiento.", "prompt": "¿Cuál es el 20% de lo que haces con tu mentoreada que genera el mayor impacto?" },
        36: { "advice": "Los modelos mentales son lentes, no verdades. Si solo ves el problema desde tu perspectiva, estás perdiendo información crítica.", "prompt": "¿Desde qué otra perspectiva puedes ver el desafío actual de tu mentoreada?" },
        37: { "advice": "La estrategia sin ejecución es filosofía. Tu plan de desarrollo solo vale si tu mentoreada puede implementarlo esta semana con recursos reales.", "prompt": "¿Qué acción específica y medible puede tomar tu mentoreada en los próximos 7 días?" },
        38: { "advice": "El pensamiento contraintuitivo pregunta '¿Y si lo opuesto fuera cierto?'. A veces la solución está en hacer lo contrario de lo que el sentido común sugiere.", "prompt": "¿Qué consejo convencional podrías invertir para generar un breakthrough?" },
        39: { "advice": "La mentalidad de portafolio diversifica el riesgo. No pongas todas tus expectativas de crecimiento en una sola área — desarrolla múltiples capacidades simultáneamente.", "prompt": "¿Qué capacidad estás descuidando porque estás enfocada solo en una?" },
        40: { "advice": "Tu pensamiento estratégico evoluciona cuando pasas de resolver problemas a prevenirlos. Las mejores mentoras ven lo que viene antes de que llegue.", "prompt": "Escribe una oración sobre cómo ha cambiado tu forma de abordar los desafíos en estos 10 días." }
    },
    5: {  # Bloque 5: días 41-50
        41: { "advice": "El poder personal no se otorga — se construye con decisiones diarias. Cada vez que honras tu palabra, tu poder crece. Cada vez que lo disculpas, disminuye.", "prompt": "¿Qué palabra te diste a ti misma que no has honrado esta semana?" },
        42: { "advice": "La autoridad legítima no viene del título — viene de la competencia visible y la integridad consistente. Tu mentoreada te sigue porque confía, no porque debes.", "prompt": "¿En qué área necesitas demostrar más competencia para fortalecer tu autoridad?" },
        43: { "advice": "El poder compartido multiplica. Cuando das crédito, cuando delegas con confianza, cuando reconoces el talento ajeno, tu poder no disminuye — se expande.", "prompt": "¿A quién puedes darle más visibilidad esta semana sin que eso te reste?" },
        44: { "advice": "Los límites no son muros — son puentes con peaje. Sin límites claros, tu energía se drena en direcciones que no eligiste.", "prompt": "¿Qué límite necesitas establecer esta semana para proteger tu energía de liderazgo?" },
        45: { "advice": "El cierre de bloque es un inventario de poder. No cuantas títulos tienes — cuentas cuántas decisiones difíciles tomaste con integridad.", "prompt": "¿Qué decisión difícil tomaste recientemente que fortaleció tu poder personal?" },
        46: { "advice": "La influencia sin autoridad es el arte de mover personas que no te deben nada. Se construye con valor aportado, no con posición exigida.", "prompt": "¿Qué valor específico puedes aportar esta semana a alguien que no te debe nada?" },
        47: { "advice": "El poder se pierde cuando se usa para controlar en lugar de para crear. Tu autoridad es una herramienta de construcción, no de coerción.", "prompt": "¿Dónde estás usando tu autoridad para controlar en lugar de para liberar potencial?" },
        48: { "advice": "La presencia ejecutiva no es actuar — es estar. Tu cuerpo, tu voz, tu silencio comunican antes de que abras la boca.", "prompt": "En tu próxima reunión, observa cómo tu presencia afecta la sala antes de hablar." },
        49: { "advice": "El poder real se mide en cuántas personas crecen bajo tu influencia. Si tu equipo no está más capaz que cuando llegó, tu poder es ilusión.", "prompt": "¿Quién en tu esfera está más capaz hoy porque tú estuviste presente?" },
        50: { "advice": "Tu relación con el poder define tu liderazgo. No es bueno ni malo — es amplificador. Si eres generosa, amplifica tu generosidad. Si tienes miedo, amplifica tu miedo.", "prompt": "Escribe una oración sobre tu relación actual con el poder y cómo ha evolucionado." }
    },
    6: {  # Bloque 6: días 51-60
        51: { "advice": "La innovación no es creatividad — es aplicación de valor. Una idea sin implementación es entretenimiento, no innovación.", "prompt": "¿Qué idea tienes pendiente de implementar que generaría valor real?" },
        52: { "advice": "El fracaso inteligente es datos, no derrota. Cada experimento que falla te dice qué no funciona, acercándote a lo que sí.", "prompt": "¿Qué 'fracaso' reciente te dio información valiosa que no tenías?" },
        53: { "advice": "La mentalidad de crecimiento no es optimismo — es la creencia verificada de que la capacidad se desarrolla con práctica deliberada.", "prompt": "¿En qué área estás fijando en lugar de crecer? ¿Qué práctica deliberada necesitas?" },
        54: { "advice": "La curiosidad estratégica pregunta '¿Qué pasaría si...?' antes de '¿Por qué siempre...?'. La primera abre posibilidades, la segunda cierra mentes.", "prompt": "Transforma una queja reciente en una pregunta curiosa que abra posibilidades." },
        55: { "advice": "El aprendizaje acelerado requiere incomodidad óptima. Si no hay fricción, no hay crecimiento. Si hay pánico, hay parálisis.", "prompt": "¿Estás en zona de confort o en pánico? ¿Cuál es tu zona de crecimiento óptimo?" },
        56: { "advice": "La adaptabilidad no es flexibilidad — es velocidad de actualización de modelos. Cuanto más rápido actualizas tus creencias con nueva información, más rápido creces.", "prompt": "¿Qué creencia tenías hace 10 días que ya actualizaste con nueva evidencia?" },
        57: { "advice": "El pensamiento divergente genera opciones; el convergente elige la mejor. Los innovadores dominan ambos modos y saben cuándo cambiar.", "prompt": "¿Necesitas divergir (generar opciones) o converger (elegir) en tu situación actual?" },
        58: { "advice": "La experimentación rápida vale más que la planificación perfecta. Un prototipo esta semana vale más que un plan perfecto en un mes.", "prompt": "¿Qué puedes prototipar esta semana en lugar de seguir planificando?" },
        59: { "advice": "El aprendizaje social acelera todo. No aprendes sola — aprendes con otros. Comparte lo que estás descubriendo y recibe feedback.", "prompt": "¿Con quién puedes compartir tu aprendizaje esta semana para acelerar tu crecimiento?" },
        60: { "advice": "Tu capacidad de aprender es tu ventaja competitiva más durable. Lo que sabes hoy será obsoleto mañana — lo que puedes aprender será tu activo.", "prompt": "Escribe una oración sobre cómo ha evolucionado tu forma de aprender en estos 10 días." }
    },
    7: {  # Bloque 7: días 61-70
        61: { "advice": "El legado no es lo que dejas — es lo que plantas en otros que sigue creciendo sin ti. Tu impacto se mide en lo que hacen otros cuando no estás.", "prompt": "¿Qué estás plantando hoy que seguirá creciendo cuando ya no estés presente?" },
        62: { "advice": "La mentoría de legado no transfiere conocimiento — transfiere sabiduría. El conocimiento es lo que sabes; la sabiduría es cómo lo usas.", "prompt": "¿Qué sabiduría (no solo conocimiento) puedes transferir esta semana?" },
        63: { "advice": "El impacto sistémico no se mide en individuos — se mide en redes. Cuando tu mentoreada mentoriza a otros, tu legado se multiplica exponencialmente.", "prompt": "¿A quién está preparando tu mentoreada para mentorizar? ¿Cómo puedes apoyar eso?" },
        64: { "advice": "La sostenibilidad del liderazgo no es equilibrio — es ritmo. No buscas no cansarte — buscas recuperarte con la misma disciplina con la que trabajas.", "prompt": "¿Cuál es tu ritmo de recuperación? ¿Es tan disciplinado como tu ritmo de trabajo?" },
        65: { "advice": "El propósito evoluciona. Lo que te motivaba hace 5 años puede no ser suficiente hoy. Permitir que tu propósito madure no es traición — es crecimiento.", "prompt": "¿Cómo ha evolucionado tu propósito desde que empezaste este camino?" },
        66: { "advice": "La generosidad estratégica no es dar todo — es dar lo correcto en el momento correcto. Dar demasiado pronto puede crear dependencia, no autonomía.", "prompt": "¿Qué necesitas retener esta semana para que tu mentoreada crezca en lugar de depender?" },
        67: { "advice": "El cierre consciente no es terminar — es integrar. Antes de cerrar un ciclo, nombra explícitamente lo que aprendiste y lo que sueltas.", "prompt": "¿Qué ciclo necesitas cerrar conscientemente antes de abrir el siguiente?" },
        68: { "advice": "La continuidad del legado requiere documentación. Lo que no se escribe se pierde. Tu sabiduría merece ser capturada para quienes vienen después.", "prompt": "¿Qué aprendizaje clave necesitas documentar esta semana para que no se pierda?" },
        69: { "advice": "El impacto más profundo no es lo que logras — es quién te convierte en el proceso. Tu transformación personal es tu mayor legado.", "prompt": "¿Quién te estás convirtiendo a través de este trabajo? ¿Es quien quieres ser?" },
        70: { "advice": "Tu legado ya está ocurriendo. No es un evento futuro — es la suma de cada conversación, cada pregunta, cada momento de presencia que ofreces hoy.", "prompt": "Escribe una oración que capture el legado que estás construyendo con cada sesión." }
    },
    8: {  # Bloque 8: días 71-78 (solo 8 días)
        71: { "advice": "La integración final no es sumar — es sintetizar. Todo lo que aprendiste en 70 días ahora debe convertirse en un sistema coherente, no en piezas sueltas.", "prompt": "¿Cuál es el principio unificador que conecta todo lo que has aprendido?" },
        72: { "advice": "La maestría no es saber más — es necesitar menos. Cuanto más dominas, menos herramientas necesitas porque usas las correctas con más precisión.", "prompt": "¿Qué herramientas has dejado de usar porque descubriste que las esenciales son menos?" },
        73: { "advice": "El cierre del programa no es el final — es la graduación de tu autonomía. Ya no necesitas seguir el programa — necesitas crear el tuyo.", "prompt": "¿Qué estructura propia crearás para continuar tu desarrollo después de este programa?" },
        74: { "advice": "La enseñanza es la forma más alta de aprendizaje. Si puedes explicar esto simplemente, lo dominas. Si no, aún hay brechas.", "prompt": "¿A quién puedes enseñar esta semana lo que aprendiste? La enseñanza revelará tus brechas." },
        75: { "advice": "Tu red de apoyo no es un lujo — es infraestructura. Los líderes sostenibles no lideran solos — tienen círculos que los sostienen.", "prompt": "¿Quién está en tu círculo de sostenimiento? ¿Necesitas agregar a alguien?" },
        76: { "advice": "La práctica deliberada no es hacer más — es hacer con más atención. 30 minutos enfocados valen más que 3 horas en automático.", "prompt": "¿Qué práctica puedes hacer esta semana con atención total en lugar de con distracción?" },
        77: { "advice": "El compromiso con la excelencia no es perfección — es la negativa a aceptar menos de lo que sabes que puedes dar. Es un estándar interno, no externo.", "prompt": "¿Dónde estás aceptando menos de lo que sabes que puedes dar? ¿Qué estándar necesitas elevar?" },
        78: { "advice": "Este no es el final — es el comienzo de tu versión más capaz. Todo lo que integraste aquí es tu nueva base. Desde aquí, todo es posible.", "prompt": "Escribe una carta a tu yo de hace 78 días. Dile quién eres ahora." }
    }
}

def inject_sigma(block_num):
    """Inyecta Sigma Coach en un bloque específico"""
    filename = f"Bloque{block_num}_Premium.html"
    filepath = os.path.join(BASE_DIR, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar que no tenga ya Sigma
    if 'SIGMA_DATA' in content:
        print(f"  [SKIP] {filename} ya tiene Sigma")
        return
    
    # Obtener prompts para este bloque
    prompts = SIGMA_PROMPTS[block_num]
    
    # Construir SIGMA_DATA
    sigma_data_lines = []
    for day_id, data in prompts.items():
        sigma_data_lines.append(f'            {day_id}: {{ advice: "{data["advice"]}", prompt: "{data["prompt"]}" }},')
    
    sigma_data_js = '\n'.join(sigma_data_lines)
    
    # Script de Sigma
    sigma_script = f'''    <script>
        // --- SIGMA COMPANION DATA ---
        const SIGMA_DATA = {{
{sigma_data_js}
        }};

        function openSigma() {{
            const d = SIGMA_DATA[currentDayId] || {{ advice: "Sigma está contigo. Elige un día para recibir orientación.", prompt: "¿Qué te detiene hoy?" }};
            const m = document.getElementById('sigma-modal');
            const c = document.getElementById('sigma-content');
            c.innerHTML = `
                <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px;margin-bottom:16px">
                    <div style="font-size:.72rem;color:${{ACCENT}};text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Consejo de Sigma — Día ${{currentDayId}}</div>
                    <p style="font-size:.9rem;color:#fff;line-height:1.7;font-style:italic">"${{d.advice}}"</p>
                </div>
                <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">Reflexión para hoy</div>
                <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px;margin-bottom:12px">
                    <p style="font-size:.85rem;color:#ddd;line-height:1.5">${{d.prompt}}</p>
                </div>
                <textarea id="sigma-answer" style="width:100%;min-height:70px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:12px;color:#fff;font-family:Inter;font-size:.85rem" placeholder="Anota tu reflexión aquí..."></textarea>
                <button onclick="guardarSigma()" style="margin-top:12px;width:100%;padding:13px;background:linear-gradient(135deg,${{ACCENT}},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer">Guardar reflexión</button>
            `;
            m.classList.add('active');
        }}
        function closeSigma() {{
            document.getElementById('sigma-modal').classList.remove('active');
        }}
        function guardarSigma() {{
            const ans = document.getElementById('sigma-answer');
            if (ans && ans.value.trim()) {{
                localStorage.setItem('mm_b{block_num}_sigma_' + currentDayId, ans.value.trim());
            }}
            closeSigma();
        }}
    </script>'''
    
    # Insertar el script antes del </body>
    # Buscar el último </script> antes de </body>
    body_end = content.rfind('</body>')
    if body_end == -1:
        print(f"  [ERROR] No se encontró </body> en {filename}")
        return
    
    # Insertar Sigma antes de </body>
    sigma_html = '''<!-- SIGMA COACH: Modal + Botón Flotante -->
<style>
    #sigma-modal { display:none; }
    #sigma-modal.active { display:flex !important; flex-direction:column; }
</style>
<div id="sigma-modal" style="position:fixed;inset:0;z-index:7000;background:rgba(0,0,0,.95);padding:20px 20px 60px;overflow-y:auto">
    <div style="display:flex;justify-content:space-between;align-items:center;margin:24px 0 16px">
        <h3 style="font-family:Outfit;font-size:1.1rem;color:#fff">🧠 Coach Sigma</h3>
        <button onclick="closeSigma()" style="background:none;border:none;color:#fff;font-size:1.4rem;cursor:pointer">×</button>
    </div>
    <div id="sigma-content"></div>
</div>
<button onclick="openSigma()" style="position:fixed;bottom:110px;right:16px;width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#FF5E00,#FF8C00);border:none;box-shadow:0 8px 24px rgba(255,94,0,.35);display:flex;align-items:center;justify-content:center;font-size:1.6rem;cursor:pointer;z-index:3000;transition:transform .2s" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" title="Coach Sigma">🧠</button>
'''
    
    # Insertar script + HTML
    new_content = content[:body_end] + sigma_script + '\n' + sigma_html + content[body_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  [OK] {filename} - Sigma inyectado ({len(prompts)} días)")

# Ejecutar para bloques 2-8
print("Inyectando Sigma Coach en Bloques 2-8...")
for i in range(2, 9):
    inject_sigma(i)
print("\nCompletado.")
