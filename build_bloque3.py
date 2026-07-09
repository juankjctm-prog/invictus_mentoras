import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque3.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque3_Premium.html"

with open(source_html, "r", encoding="utf-8") as f:
    template = f.read()

with open(source_md, "r", encoding="utf-8") as f:
    md_content = f.read()

def generate_playbook(paso1_1, paso1_2, paso1_3, paso2_a, paso2_b, paso2_i, paso2_ii, success=False):
    theme_color = "var(--success)" if success else "var(--accent-fire)"
    theme_water = "var(--success)" if success else "var(--accent-water)"
    
    return f"""
                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: {theme_color}; margin-top: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)
                    </div>
                    
                    <div class="note-item" style="border-left: 2px solid {theme_color};">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">1. {paso1_1[0]}</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso1_1[1]}</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">2. {paso1_2[0]}</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso1_2[1]}</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #9370DB;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">3. {paso1_3[0]}</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso1_3[1]}</p>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: {theme_water}; margin-top: 40px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        PASO 2: GUÍA DE LA SESIÓN 1-A-1
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">A. Ancla (WhatsApp 24h antes)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;"><em>"{paso2_a}"</em></p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">B. Coaching Socrático (Profundo)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso2_b[0]}</p>
                        <div style="padding: 12px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-top: 10px; font-style: italic; color: #FFF;">
                            "{paso2_b[1]}"
                        </div>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--success);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">I. {paso2_i[0]}</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso2_i[1]}</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700; background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">II. Asignación de Riesgo Táctico</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">{paso2_ii}</p>
                    </div>
"""

playbooks = {
    21: generate_playbook(
        ("Auditoría de Reacción Sensorial", "La próxima vez que recibas una crítica de tu jefe, antes de responder lógicamente, escanea tu cuerpo. ¿Dónde sientes la tensión (pecho, mandíbula)? Reconoce que tu amígdala acaba de encenderse."),
        ("El Enmarque de la Intención", "Recuérdate a ti misma: Cuando alguien me da feedback duro, no me está desterrando de la tribu. Me está dando el mapa para dominarla."),
        ("Desconexión del Ego", "Respira profundo y asume que tu mente instintiva va a querer justificarse. Toma la decisión ahora mismo de que tu primera respuesta será siempre: 'Cuéntame más sobre eso'."),
        "Mañana hablaremos sobre el miedo a equivocarse. Ven preparada para escuchar algo que probablemente no te gustará, pero que necesitas saber.",
        ("Cuando intente justificar un error culpando al proceso o a otra persona:", "Cuando te di este feedback, vi que tu primer instinto fue defenderte. ¿Sientes que mi corrección a tu trabajo es una amenaza a tu valor como persona dentro de esta empresa?"),
        ("Reestructuración de la Crítica", "Haz que escriba el feedback más doloroso que le diste. Luego, oblígala a tachar los sentimientos y a escribir al lado únicamente los HECHOS operativos de esa crítica, despojados de drama."),
        "Debe pedirle activamente a un superior que le dé una crítica dura sobre su desempeño reciente, y tiene prohibido justificar su acción. Solo puede decir 'Gracias, lo entiendo'."
    ),
    22: generate_playbook(
        ("Auditoría de Comodidad", "¿A qué miembro de tu equipo no le has dicho la verdad sobre su bajo desempeño porque te duele hacerlo sentir mal? Esa es tu Empatía Ruinosa."),
        ("El Eje del Candor", "Dibuja el cuadrante de Kim Scott. Prométete a ti misma: 'Me importa demasiado el futuro de esta persona como para dejar que siga fallando en la ignorancia'."),
        ("Preparación de la Verdad", "Selecciona una crítica constructiva severa que tengas que darle a tu mentoreada. Redáctala en tu cuaderno sin usar ningún adjetivo suavizante."),
        "Mañana cruzaremos una línea. Dejaremos de ser amables para empezar a ser implacables con tu éxito. Trae tu proyecto más rezagado.",
        ("Si ella se queja de un miembro de su equipo pero no quiere confrontarlo para no 'crear mal ambiente':", "¿Estás evitando esta conversación por proteger los sentimientos de tu colaborador, o por protegerte a ti misma de la incomodidad de liderar de verdad?"),
        ("El Simulador de Candor Radical", "Hazle formular frente a ti el feedback duro que debe darle a su empleado. Si intenta suavizarlo ('Tú siempre haces las cosas bien, pero...'), córtala y haz que lo diga directo y claro."),
        "Tiene 24 horas para tener esa conversación de Candor Radical con el empleado de bajo desempeño y reportarte el resultado. No puede usar excusas de 'tiempo'."
    ),
    23: generate_playbook(
        ("Auditoría Lingüística", "Escucha cómo te hablas a ti misma cuando fallas. ¿Dices 'Hice esto mal' o dices 'Soy una tonta'? El verbo define la plasticidad de tu cerebro."),
        ("Separación de Entidades", "Visualiza tu identidad corporativa como un diamante indestructible, y tu desempeño transaccional como la ropa que usas. La ropa puede ensuciarse o romperse, el diamante no."),
        ("Calibración del Mensaje", "Revisa el feedback que vas a darle hoy a tu mentoreada. Asegúrate de que no contenga el verbo 'Eres' y que esté enfocado estrictamente en 'Hiciste' o 'El proceso fue'."),
        "Mañana desarmaremos tu mayor fracaso de este mes. Te enseñaré por qué fracasar en un proyecto no tiene nada que ver con quién eres.",
        ("Cuando se derrumbe emocionalmente tras cometer un error visible en la empresa:", "Si separamos la táctica que usaste del valor que aportas a esta organización, ¿qué fue exactamente lo que falló en la táctica?"),
        ("La Autopsia Desapasionada", "Oblígala a dibujar un diagrama de flujo del error que cometió. Debe encontrar el punto exacto donde la maquinaria falló, sin usar ningún pronombre personal ('yo fallé'). Todo es proceso."),
        "Debe comunicar el error a su equipo usando el Growth Mindset: 'La estrategia operativa de la semana pasada no funcionó por X, Y y Z. Así es como vamos a ajustar la maquinaria ahora'."
    ),
    24: generate_playbook(
        ("Auditoría de Historias", "En tu último conflicto corporativo, ¿cuánta energía gastaste en demostrar que TÚ tenías la razón y la otra persona no?"),
        ("Desapego de la Razón", "Acepta que tener la razón en el mundo de los negocios es irrelevante si no tienes la influencia. Hoy dejarás de buscar la victoria moral para buscar el avance estructural."),
        ("Posición del Observador", "Visualízate elevándote por encima de la sala de juntas. Ya no eres tú contra tu mentoreada. Eres una consultora externa analizando la dinámica de dos piezas en un tablero."),
        "Trae a la mesa ese conflicto que tienes estancado con otra área. Mañana te enseñaré a resolverlo sin ceder ni un milímetro de poder.",
        ("Si ella pasa 10 minutos detallando todo lo que la otra persona hizo mal para justificar que ella tiene la razón:", "Si yo fuera un mediador externo contratado por el CEO para ver este conflicto de manera imparcial, ¿cómo describiría la diferencia estructural entre las prioridades de tu área y la de él?"),
        ("El Guion de la Tercera Historia", "Haz que redacte el correo de invitación a una reunión con su adversario corporativo. El correo no puede tener acusaciones ni defensas. Debe empezar con: 'He notado una brecha entre mis expectativas y las tuyas...'"),
        "Enviar el correo de la Tercera Historia hoy mismo y sostener la reunión de resolución la próxima semana sin litigar el pasado."
    ),
    25: generate_playbook(
        ("Auditoría del Ratio", "Suma las interacciones positivas vs negativas que has tenido con tu equipo esta semana. Si estás por debajo de 5 a 1, tu equipo está operando desde el miedo, no desde el alto rendimiento."),
        ("Diseño de la Validación", "Encuentra un micro-éxito conductual específico de tu mentoreada esta semana (algo que haya hecho excepcionalmente bien bajo presión) y anótalo."),
        ("El Banco Emocional", "Prepárate para depositar capital de confianza hoy. Tu validación no será un elogio vacío, será una observación táctica que ella ni siquiera sabía que hizo bien."),
        "Mañana no habrá críticas. Mañana te revelaré un patrón de brillantez ejecutiva que tú misma no has notado que posees.",
        ("Si ella minimiza su éxito diciendo 'fue suerte' o 'es mi trabajo':", "¿Por qué te resulta más fácil aceptar y creer en tu incompetencia cuando fallas, que aceptar y creer en tu maestría operativa cuando aciertas de manera brillante?"),
        ("El Anclaje de la Victoria", "Dile explícitamente: 'Quiero que notes cómo estructuraste esa presentación. Fue impecable y directiva'. Exígele que lo escriba en su cuaderno como una táctica probada que ella misma inventó y debe repetir."),
        "Debe entregar Feedback de Validación específico (no elogios genéricos) a 3 miembros de su propio equipo mañana a primera hora."
    ),
    26: generate_playbook(
        ("Auditoría de Sesgos Recibidos", "Lee tus últimas 3 evaluaciones de desempeño. ¿Qué porcentaje del feedback fue sobre tu 'actitud' y qué porcentaje sobre tus 'resultados financieros/operativos'?"),
        ("El Escudo Analítico", "Prepárate para defender a tu mentoreada del sistema. Si los demás la juzgan por su 'intensidad', tú la vas a medir estrictamente por su 'P&L' y su entrega de proyectos."),
        ("La Promesa del Candor", "Jura internamente que nunca le retendrás información técnica por miedo a que ella 'se ponga emocional'. Tratarla con fragilidad es el peor insulto a su potencial."),
        "Reúne tus últimas evaluaciones de desempeño. Mañana te enseñaré a diferenciar el feedback real del sesgo estructural corporativo.",
        ("Si ella está angustiada porque un director le dijo que 'necesita ser más dulce y menos directiva' con el equipo:", "Si fueras un hombre presentando exactamente los mismos números con la misma energía directiva de ayer, ¿crees que te habrían dado ese mismo feedback?"),
        ("El Pivotaje Táctico", "Entrénala a responder al feedback ambiguo. Haz role-play: Tú eres el jefe dándole un feedback sobre su 'tono de voz'. Ella debe responder: 'Entiendo. Para asegurar mi desarrollo, ¿podrías darme feedback específico sobre la calidad técnica de mi presentación?'"),
        "En la próxima evaluación o junta uno a uno con su jefe, debe solicitar activamente una métrica técnica de mejora operativa, no relacional."
    ),
    27: generate_playbook(
        ("Auditoría de Complejidad", "¿Realmente entiendes la neurobiología del feedback, o solo estás memorizando conceptos? Trata de explicar la relación entre la amígdala y la Empatía Ruinosa en voz alta ahora mismo."),
        ("Limpieza de Jerga", "Asegúrate de que hoy, cuando ella trate de explicar su crecimiento, no le permitas usar palabras de moda ('growth mindset', 'resiliencia'). Oblígala a usar lenguaje universal."),
        ("Posición de Silencio", "Hoy tú hablarás un 20%. Ella hablará un 80%. Tu trabajo es escuchar dónde su lógica se rompe y obligarla a reconstruirla."),
        "Llegó la prueba de fuego del Bloque 3. Mañana me explicarás cómo dar feedback como si mi vida corporativa dependiera de ello.",
        ("Cuando ella intente explicar un concepto difícil usando teoría compleja que no comprende del todo:", "Detente. Finge que soy un empleado de nivel de entrada que acaba de entrar a la empresa hoy. Explícame por qué no me das feedback negativo, sin usar ni una sola de las palabras que acabas de emplear."),
        ("La Extracción Feynman", "Haz que resuma la teoría completa de dar y recibir feedback (desde Eisenberger hasta Stone) en 3 principios innegociables aplicados a su día a día. Si es abstracto, la repruebas."),
        "Debe enseñarle a una persona externa (pareja, colega de confianza) la técnica de 'La Tercera Historia' explicándola en menos de 3 minutos y verificar si el otro lo entendió."
    ),
    28: generate_playbook(
        ("Auditoría de Subordinación", "¿Qué decisión de tu superior directo está saboteando la eficiencia de tu área, y por qué has guardado silencio? Tu silencio es complicidad operativa."),
        ("Desmitificación del Poder", "Recuerda que tus superiores no son omniscientes. Tienen puntos ciegos masivos. Darles feedback hacia arriba no es insubordinación, es el servicio de más alto nivel que puedes proveerles."),
        ("El Enmarque de Alianza", "Prepara tu mente para alinear tus críticas con los objetivos del jefe. Tú no peleas contra él; tú peleas junto a él contra el problema logístico que él no puede ver."),
        "Se acabó el esperar órdenes. Mañana diseñaremos el feedback que le vas a dar a quien tiene poder estructural sobre ti.",
        ("Si ella dice que no le puede dar feedback a su VP porque 'él se molesta si lo corrigen':", "¿Prefieres vivir con la ineficiencia diaria que destruye a tu equipo, o atravesar 10 minutos de incomodidad política para alinear a tu VP con la realidad operativa?"),
        ("El Reencuadre de Propósito Compartido", "Diseña con ella el guion exacto. Primero el objetivo que el VP valora ('Para llegar a la meta de Q3...'). Segundo el permiso ('¿Estarías abierto a...?'). Tercero el feedback operativo duro."),
        "Tiene 48 horas para agendar una reunión de 15 minutos con su superior directo y entregarle un 'Feedback hacia Arriba' usando el Reencuadre de Propósito Compartido."
    ),
    29: generate_playbook(
        ("Auditoría del Pasado", "Revisa tus últimas interacciones de corrección. ¿Cuánto tiempo pasaste debatiendo quién tuvo la culpa de lo que pasó ayer? Ese tiempo es irrecuperable."),
        ("El Cambio de Eje Temporal", "Haz una declaración hoy: El pasado no es territorio de la mentoría de élite. Todo mi enfoque a partir de ahora es cómo optimizar la próxima ejecución."),
        ("Calibración del Feedforward", "Toma un problema recurrente de tu mentoreada. Redacta una sugerencia técnica que le darás hoy que empiece exclusivamente con: 'Para la próxima vez que te enfrentes a...'"),
        "El pasado ya no nos sirve. Mañana te enseñaré a dejar de litigar el error de ayer y obsesionarte con la victoria de la próxima semana.",
        ("Si ella sigue dándole vueltas a un proyecto que fracasó el mes pasado, atascada en la culpa:", "Si aceptamos que no hay absolutamente nada que puedas hacer para cambiar lo que pasó en ese comité, ¿cuál es la micro-acción que vas a probar diferente en el comité de la semana que viene?"),
        ("El Laboratorio del Mañana", "Haz que ella identifique un comportamiento limitante que quiere cambiar. Oblígala a diseñar 2 sugerencias de 'Feedforward' para ella misma, totalmente enfocadas en cómo actuará diferente en el próximo evento."),
        "Debe pedir activamente 'Feedforward' a 3 de sus pares estratégicos usando la frase: '¿Qué sugerencia me darían para hacer X proyecto más eficiente el próximo mes?'"
    ),
    30: generate_playbook(
        ("Auditoría de Evolución", "Mira tu propio progreso. Hace 10 días, dar feedback duro te generaba ansiedad. Hoy, entiendes la arquitectura neurobiológica para hacerlo sin destrozar la identidad del otro."),
        ("El Peso del Candor", "Acepta que tu trabajo corporativo a partir de ahora será incómodo. Ser la persona que dice la verdad en un mar de 'Empatía Ruinosa' es un peso pesado, pero es el peso del liderazgo."),
        ("Presencia Estructural", "Entra a la sesión de hoy en modo diagnóstico. Ella ya sabe la teoría. Tu único objetivo hoy es forzarla a diseñar la intervención que cambiará la trayectoria de alguien más."),
        "Llegamos al Checkpoint 3. Tienes todo el poder de fuego. Mañana diseñaremos en papel la intervención correctiva más dura de tu carrera.",
        ("Para evaluar si está lista para aplicar la presión correcta a su propio equipo:", "Si yo entrevistara mañana en secreto a tu equipo de trabajo y les preguntara si tú tienes el coraje de decirles sus verdades más duras a la cara, ¿qué me responderían?"),
        ("La Auditoría del Candor", "Oblígala a elegir a un miembro de su equipo que necesita una corrección severa. Creen juntas el guion exacto: Separar identidad de desempeño, usar la Tercera Historia y cerrar con Feedforward."),
        "Debe ejecutar la intervención correctiva que acaban de diseñar con su empleado/colega esta misma semana. Sin excusas. Sin suavizar el mensaje."
    )
}

# Now let's extract readings from markdown
# The markdown structure is: DÍA XX ... FASE 1 ... FASE 2 ... text ... FASE 3 ... FASE 4 ...
days_data_list = []
for day in range(21, 31):
    # Regex to find the block for a day
    day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=DÍA {day+1}|$)', re.DOTALL)
    match = day_pattern.search(md_content)
    if not match:
        continue
    day_content = match.group(0)
    
    # Extract title
    title_match = re.search(rf'DÍA {day}\s+(.+?)\n', day_content)
    title = title_match.group(1).strip()
    
    # Extract reading (between FASE 2 and FASE 3)
    reading_match = re.search(r'FASE 2 — LECTURA CRONOMETRADA.*?(\n\n.+?)(?=\n📖\s*FASE 3)', day_content, re.DOTALL)
    reading_raw = reading_match.group(1).strip()
    
    # format reading paragraphs
    paragraphs = reading_raw.split('\n')
    reading_html = ""
    for i, p in enumerate(paragraphs):
        p = p.strip()
        if not p: continue
        if i == 0:
            reading_html += f"                        <h3 style=\"color: var(--accent-water); font-size: 1.1rem; margin-bottom: 12px;\">{p}</h3>\n"
        else:
            reading_html += f"                        <p>{p}</p>\n"
            
    # Extract recall questions
    q_literal = re.search(r'\[Literal\]\n(.*?)\n', day_content).group(1).strip()
    q_infer = re.search(r'\[Inferencial\]\n(.*?)\n', day_content).group(1).strip()
    q_opcion = re.search(r'\[Opción múltiple\]\n(.*?)\n', day_content).group(1).strip()
    q_personal = re.search(r'\[Conexión personal\]\n(.*?)\n', day_content).group(1).strip()
    
    reading_html += f"""
                        <div class="recall-box" style="margin-top: 30px; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; border-left: 3px solid var(--accent-water);">
                            <h4 style="color: white; margin-bottom: 15px; font-size: 1rem;">🔍 Recall Activo</h4>
                            <ul style="color: var(--text-secondary); font-size: 0.9rem; padding-left: 20px; display: flex; flex-direction: column; gap: 12px;">
                                <li><strong>Literal:</strong> {q_literal}</li>
                                <li><strong>Inferencial:</strong> {q_infer}</li>
                                <li><strong>Aplicación:</strong> {q_opcion}</li>
                                <li><strong>Conexión:</strong> {q_personal}</li>
                            </ul>
                        </div>
"""
    
    playbook_str = playbooks[day]
    
    day_obj = f"""
            {{
                id: {day},
                badge: "Bloque 3 • Día {day-20}",
                title: "{title}",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

# Now modify the template
new_html = template

# Replace global titles
new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 3</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan') # keep it
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 3')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'EL FEEDBACK QUE TRANSFORMA')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 3 • Día X')

# Replace the data structure
# using regex to replace the entire daysData array
pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque3_Premium.html successfully.")
