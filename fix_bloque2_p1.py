import re

file_path = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque2_Premium.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

def generate_playbook(paso1_1, paso1_2, paso1_3, paso2_a, paso2_b, paso2_i, paso2_ii):
    return f"""
                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-fire); margin-top: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)
                    </div>
                    
                    <div class="note-item" style="border-left: 2px solid var(--accent-fire);">
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

                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-water); margin-top: 40px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
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

p11 = generate_playbook(
    ("Auditoría de Fragmentación", "Haz un escáner honesto: ¿En qué juntas directivas finges estar presente mientras resuelves correos en otra pantalla? Escribe el impacto que eso tiene en tu autoridad percibida."),
    ("El Costo de la Presencia a Medias", "Calcula cuánto tiempo pierdes reconectando tu cerebro a la tarea original. Acepta que el multitasking no es eficiencia, es ansiedad corporativa disfrazada de productividad."),
    ("El Anclaje de 3 Minutos", "Antes de que ella entre (física o virtualmente), cierra todo. Quédate mirando un punto fijo por 180 segundos. Recibe a tu mentoreada con una presencia biológica aplastante."),
    "Mañana hablaremos de la mayor fuga de poder en tu carrera: el multitasking. Trae tu agenda y tus métricas de atención.",
    ("Cuando ella presuma lo ocupada que está haciendo mil cosas a la vez, interrúmpela y lanza esta pregunta letal:", "¿De qué estás huyendo emocionalmente cuando decides revisar tu teléfono durante una junta importante en lugar de sostener la incomodidad?"),
    ("El Bloqueo Innegociable", "Haz que abra su calendario frente a ti. Exígele que bloquee 2 horas diarias de 'Trabajo Profundo' donde nadie la puede interrumpir. Ese espacio es ahora sagrado."),
    "Desactivar todas las notificaciones push de correo y chat en su celular por las próximas 24 horas. La urgencia de otros no dictará su enfoque."
)

p12 = generate_playbook(
    ("Auditoría de Interrupciones", "En la última semana, ¿cuántas veces le robaste la palabra a alguien porque ya 'sabías' lo que iba a decir? Ese es tu ego de experta. Hoy lo vas a desactivar."),
    ("Desactivar el Síndrome del 'Yo también'", "Prométete a ti misma: Hoy no usaré la historia de ella para contar una anécdota mía. El centro de gravedad de la sesión es su mente, no tus logros pasados."),
    ("Calibración de Escucha Nivel 3", "Afina tus sentidos antes de empezar. No solo escucharás lo que ella dice; escucharás lo que su respiración, sus pausas y su tono de voz están escondiendo."),
    "Mañana auditaremos cómo escuchas a tu equipo y a tus superiores. Prepárate para el silencio más profundo de tu carrera.",
    ("Si notas que ella siempre responde de inmediato en lugar de absorber la información, confronta su necesidad de control:", "¿Estás escuchando a tu equipo para entender su verdadero dolor corporativo, o para demostrarles lo rápida e inteligente que eres con tu respuesta?"),
    ("El Reto de los 10 Segundos", "Durante esta sesión, cada vez que ella termine de hablar, tú esperarás 10 segundos cronometrados antes de responder. Ella no soportará el silencio y revelará la verdad oculta."),
    "En su próxima junta de equipo, no puede dar una sola opinión ni solución. Solo se comunicará mediante preguntas durante los 45 minutos."
)

p13 = generate_playbook(
    ("Auditoría de Suposiciones", "Piensa en el último conflicto que tuviste con un colega donde asumiste que había mala intención. ¿Cuáles fueron los datos crudos y cuál fue la novela que te inventaste en la cabeza?"),
    ("Romper la Narrativa Rápida", "Acepta tu sesgo cognitivo. Tu cerebro prefiere una historia trágica y rápida antes que la incertidumbre de no saber. Perdónate y prepárate para ser objetiva."),
    ("El Descenso Consciente", "Imagina la 'Escalera de Inferencia'. Visualízate bajando de la conclusión iracunda hacia los datos observables sin filtro. Pura frialdad analítica."),
    "Trae a nuestra sesión el conflicto que más te está drenando la energía hoy. Mañana separaremos el drama de los datos crudos.",
    ("Cuando ella esté inmersa en la historia de que alguien 'la quiere perjudicar', corta la narrativa:", "Si por un minuto asumiéramos que no tienes absolutamente todos los datos sobre la intención de la otra persona, ¿qué pasaría con tu narrativa de víctima en esta historia?"),
    ("Desarmando el Conflicto", "Hazle dibujar una escalera. Arriba la emoción/juicio, abajo los hechos comprobables (lo que una cámara de video grabaría). Pídele que elimine toda la narrativa de los peldaños intermedios."),
    "Escribirle HOY MISMO a la persona con la que tiene el conflicto. El mensaje no será un ataque ni una justificación, será una solicitud objetiva de los datos que faltan: 'Necesito entender tu racional detrás de esta decisión'."
)

p14 = generate_playbook(
    ("Auditoría de Preguntas Cerradas", "¿Te pasas el día dando órdenes disfrazadas de preguntas (Ej: '¿No crees que deberíamos hacer X?')? Asume que eso es microgestión, no liderazgo."),
    ("El Miedo a la Respuesta Desconocida", "Reconoce que prefieres dar la solución porque hacer preguntas abiertas te quita el control del resultado. Hoy vas a soltar ese control."),
    ("Diseño de la Pregunta Letal", "Redacta en tu cuaderno una pregunta abierta de altísimo nivel que le harás a tu mentoreada hoy. Una que sabes que la dejará en silencio por varios minutos."),
    "Mañana dejaremos de dar órdenes y apagaremos fuegos operativos. Empezaremos a usar el lenguaje para reprogramar la realidad.",
    ("Si ella se queja de que su equipo no es proactivo y ella 'tiene que hacer todo':", "Si dejaras de darle las respuestas correctas a tu equipo, ¿qué miedo profundo tienes de que descubran sobre tu propia utilidad en la empresa?"),
    ("La Transformación de la Queja", "Toma la queja recurrente de tu mentoreada (Ej: 'Mi jefe no me valora') y oblígala a transformarla en una pregunta poderosa de posibilidad (Ej: '¿Qué estructura debo crear para que mi valor sea innegable?')."),
    "Durante las primeras 4 horas de su día laboral de mañana, tiene prohibido responder afirmando algo. Solo puede responder a los correos y mensajes de su equipo usando otra pregunta."
)

p15 = generate_playbook(
    ("Auditoría de Agotamiento Empático", "¿Cuántas veces esta semana te cargaste emocionalmente el 'mono' (problema) de un colega o subalterno? Revisa tu nivel de agotamiento."),
    ("La Barrera de la Compasión Ejecutiva", "Repítete: 'Entender su dolor no me obliga a resolver su problema'. La verdadera compasión es darles las herramientas para que ellos lo resuelvan."),
    ("Reset Energético", "Visualiza un escudo de plexiglás entre tú y tu mentoreada. Tú verás todo, escucharás todo, entenderás todo, pero ninguna de sus emociones densas penetrará tu biología."),
    "Hay una inmensa diferencia ejecutiva entre entender un dolor y cargarlo en la espalda. Mañana te enseño a devolver los monos que no son tuyos.",
    ("Si notas que ella está exhausta por estar salvando a todos a su alrededor a costa de sí misma:", "¿Sientes internamente que si no sufres el estrés de ellos junto con ellos, eres una mala líder o una persona fría?"),
    ("Devolviendo el Mono al Dueño", "Hazle mapear los 3 problemas operativos/emocionales que está resolviendo hoy que le pertenecen a su equipo. Diseñen la conversación exacta para devolverles la responsabilidad."),
    "El primer colega o subordinado que intente delegarle un problema emocional u operativo que no le corresponda, recibirá un 'No, pero confío en que tienes el criterio para resolverlo'. Me lo reportará en 24h."
)

match = re.search(r'const daysData = \[\s*\{([\s\S]+?)\];', content)
if match:
    days_data_str = match.group(0)
    
    def replacer(day_id, new_pb, text):
        pattern = r'(id:\s*' + str(day_id) + r',[\s\S]+?playbook:\s*`)([\s\S]*?)(`\s*\}|`\s*,)'
        return re.sub(pattern, r'\g<1>' + new_pb + r'\g<3>', text)

    days_data_str = replacer(11, p11, days_data_str)
    days_data_str = replacer(12, p12, days_data_str)
    days_data_str = replacer(13, p13, days_data_str)
    days_data_str = replacer(14, p14, days_data_str)
    days_data_str = replacer(15, p15, days_data_str)

    new_content = content[:match.start()] + days_data_str + content[match.end():]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated Bloque 2 (Days 11-15) playbooks.")
else:
    print("Could not find daysData")
