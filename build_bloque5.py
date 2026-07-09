import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque5.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque5_Premium.html"

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
    41: generate_playbook(
        ("Auditoría de Aversión Política", "Revisa tu propio prejuicio: ¿Crees que el 'lobby' y la política son sucios? Si desprecias el poder, nunca tendrás influencia sobre él."),
        ("El Fin de la Meritocracia Ingenua", "Declárate a ti misma: 'El trabajo duro sin visibilidad es agotamiento inútil'. Deja de esperar que tu trabajo hable por ti."),
        ("Postura de Jugadora", "Entra a la sesión hoy no como una figura maternal que protege a la mentoreada del 'sistema injusto', sino como la veterana que le enseña a hackear ese sistema."),
        "Dejaremos de quejarnos de lo injusta que es la empresa. Mañana te enseño cómo se ganan los ascensos en la realidad, no en los manuales de RRHH.",
        ("Si ella insiste en que 'si trabaja lo suficientemente duro, los directores lo notarán eventualmente':", "Si la meritocracia pura fuera real, ¿por qué el mes pasado ascendieron a [Nombre de Ejecutivo Mediocre] en lugar de a ti, a pesar de que tus KPIs son superiores?"),
        ("Auditoría de Invisibilidad", "Oblígala a listar las 3 personas con más poder de decisión en su área. Luego, pídele que califique del 1 al 10 cuánto conocen esas personas los resultados de su trabajo de los últimos 6 meses."),
        "Debe enviarle a su superior (o a un director) un correo conciso reportando la conclusión exitosa de un micro-proyecto, exclusivamente para ganar visibilidad."
    ),
    42: generate_playbook(
        ("Auditoría de Redes", "¿Con quién almuerzas? Si siempre comes con tu propio equipo u operaciones, estás invirtiendo el 100% de tu tiempo en Redes Operativas. Estás estancada."),
        ("El Valor del Tiempo Estratégico", "Acepta que invertir 30 minutos hablando con el VP de otra área sobre el mercado no es 'perder el tiempo', es invertir en tu seguro corporativo."),
        ("Filtro de Incomodidad", "Identifica a la persona de más alto nivel en la empresa a la que temes hablarle. Prepárate para empujar a tu mentoreada a hacer exactamente eso."),
        "Tus resultados operativos son excelentes, pero eres invisible. Mañana vamos a mapear tu Red Estratégica.",
        ("Cuando ella argumente que no tiene tiempo para hacer 'networking' porque tiene demasiado trabajo operativo:", "Si te despidieran mañana, ¿quién en la sala del Directorio (que no sea tu jefe directo) pelearía y arriesgaría su propio capital político para mantenerte en la empresa?"),
        ("El Mapa de Aliados Inexistentes", "Dibuja un círculo. Pon el nombre de ella en el centro. Hazle dibujar sus contactos frecuentes. Muéstrale cómo su círculo está aislado de la toma de decisiones financieras y estratégicas macro de la empresa."),
        "Agendar esta misma semana un café de 15 minutos (virtual o presencial) con un líder de nivel Gerencia o superior de una división completamente diferente a la suya."
    ),
    43: generate_playbook(
        ("Auditoría de Tokenismo", "Piensa en las veces que has sido la única mujer en la sala. ¿Te asignaste subconscientemente el rol de la 'Dama de Hierro' sin emociones, o el de la 'Madre' que sirve el café?"),
        ("El Radar Estructural", "Reconoce que el aislamiento que siente tu mentoreada en un comité técnico masculino no es debilidad psicológica de ella; es sociología matemática (minoría vs mayoría)."),
        ("Validación Categórica", "Prepárate para decirle las palabras mágicas hoy: 'No estás loca. El juego está diseñado para que sientas esto. Ahora te enseñaré a jugarlo.'"),
        "El aislamiento que sientes en juntas dominadas por hombres no está en tu cabeza, es matemático. Mañana te enseño a usarlo a tu favor.",
        ("Cuando ella exprese frustración por sentir que no encaja con 'el club de hombres' de la gerencia:", "¿Qué poder pierdes sobre tu propio desempeño cuando intentas adoptar el arquetipo de 'ser uno más de los hombres' en lugar de usar tu diferencia como una ventaja de visibilidad absoluta?"),
        ("Desmantelando el Arquetipo", "Haz que identifique bajo cuál de los 4 arquetipos de Kanter (Madre, Mascota, Seductora, Dama de Hierro) la está encasillando la organización. Diseñen juntas una acción disruptiva para romper ese molde."),
        "En su próxima junta de mayoría masculina, tiene prohibido ofrecerse a organizar la logística, y debe interrumpir firmemente a quien intente silenciar su punto de vista técnico."
    ),
    44: generate_playbook(
        ("Auditoría de Ceguera Política", "En tu último proyecto fallido, ¿quién fue la persona de 'Alto Poder / Bajo Interés' a la que ignoraste y que terminó saboteando tu presupuesto en la reunión final?"),
        ("La Regla del Teatro", "Internaliza la ley de acero corporativa: El comité no es para tomar decisiones, es el teatro donde se escenifican las decisiones que tú ya negociaste en privado los días anteriores."),
        ("Mentalidad de Ajedrez", "Observa a tu mentoreada como una pieza clave. Hoy le vas a enseñar a no moverse sin ver tres jugadas por adelantado en el tablero organizacional."),
        "Mañana dejaremos de improvisar. Trae tu proyecto más grande del trimestre; vamos a dibujar el mapa de quienes pueden destruirlo.",
        ("Cuando ella asuma que su plan será aprobado 'porque tiene lógica y los números tienen sentido':", "Si el éxito dependiera solo de la lógica, no habría empresas en quiebra. ¿A quién en ese comité le perjudica políticamente o le quita poder el hecho de que este proyecto tuyo sea un éxito rotundo?"),
        ("El Sociograma de Veto", "En una pizarra o papel, haz que dibuje el cuadrante (Poder vs Interés) y coloque los nombres de los 5 directivos que votarán su proyecto. Identifiquen quién es el bloqueador clave."),
        "Debe agendar una reunión '1 a 1' (Lobby previo) con el Stakeholder de mayor resistencia a su proyecto antes de la presentación oficial, para neutralizar el veto."
    ),
    45: generate_playbook(
        ("Auditoría de Autoridad Erosionada", "¿Cuántas veces hoy minimizaste un logro tuyo diciendo 'solo hago mi trabajo' o 'no me costó nada'? Date cuenta de cómo quemas tu propio capital político."),
        ("El Valor de la Reciprocidad", "Recuerda que en el mundo B2B, los favores no son actos de caridad, son depósitos de influencia a largo plazo. Tienes que enseñar a cobrarlos."),
        ("Calibración Lingüística", "Corta toda falsa modestia de tu propio vocabulario hoy para poder ser el espejo impecable de influencia ética frente a ella."),
        "Tu amabilidad operativa te está restando autoridad estratégica. Mañana te enseño a cobrar el capital político de los favores que haces.",
        ("Si ella siente culpa por insinuar que alguien de otro departamento le 'debe una' por haberlo ayudado en una crisis:", "¿Quién te convenció de que reclamar el valor equitativo del tiempo y esfuerzo que invertiste en salvar a otra área es un acto de egoísmo y no un acto básico de justicia corporativa?"),
        ("El Guion de Cialdini", "Haz que repase la última vez que le hizo un favor operativo a otro departamento. Oblígala a practicar en voz alta la respuesta de influencia: 'De nada. Sé que ustedes harían lo mismo por nuestro departamento'."),
        "La próxima vez que alguien (par o superior) le agradezca por ir más allá de su deber, debe responder exactamente con el guion de reciprocidad. Nada de 'es mi trabajo'."
    ),
    46: generate_playbook(
        ("Auditoría de Impuesto Invisible", "Revisa tu semana. ¿Cuántas horas invertiste ordenando logística, resolviendo dramas emocionales de colegas o tomando minutas, en lugar de optimizar tu P&L?"),
        ("El Radar de Microagresiones", "Prepara tu mente para detectar cómo la organización empuja a tu mentoreada hacia el 'Office Housework'. Es tu deber detener este sabotaje sutil."),
        ("Cero Tolerancia a la Servidumbre Táctica", "Siéntate derecha. Vas a exigirle a tu mentoreada que suelte las tareas domésticas corporativas que la hacen sentir 'útil' pero la mantienen abajo."),
        "Si sigues ofreciéndote a tomar las notas de la reunión, nunca serás quien dicte la estrategia de la reunión. Mañana cortamos el Impuesto Invisible.",
        ("Cuando ella justifique tomar notas u organizar la comida porque 'nadie más lo va a hacer bien' y 'solo toma un minuto':", "Mientras tú estás ocupada anotando impecablemente en un Excel lo que los demás deciden, ¿quién en esa mesa está utilizando su ancho de banda cognitivo para diseñar la siguiente jugada financiera de la empresa?"),
        ("Entrenamiento de Desvío", "Practiquen el desvío verbal. Lánzale la trampa: '¿Puedes organizar el retiro del equipo?'. Ella debe responder rápido: 'Esta vez le toca a X para fomentar su liderazgo organizativo'. Repítelo hasta que fluya sin culpa."),
        "Durante toda la semana, tiene estrictamente prohibido ofrecerse como voluntaria para cualquier tarea logística o de mantenimiento de oficina en cualquier comité o reunión."
    ),
    47: generate_playbook(
        ("Auditoría de Integración Política", "¿Puedes ver cómo el Impuesto Invisible (Día 46) se alimenta del Tokenismo (Día 43) y destruye la capacidad de armar Redes Estratégicas (Día 42)?"),
        ("El Rol del Arquitecto Sistémico", "Acepta que tu trabajo de hoy no es enseñar nada nuevo. Tu trabajo es no dejarla salir de la sesión hasta que ella pueda articular este mapa de poder sin titubear."),
        ("El Látigo Compasivo", "Prepárate para interrumpirla. Si usa lenguaje genérico o excusas ('es que la cultura es así'), oblígala a bajar a tácticas comprobables."),
        "Mañana unimos la teoría de redes y la influencia ética. Me demostrarás que entiendes el juego de poder lo suficiente para sobrevivir a él.",
        ("Si ella no logra conectar por qué hacer favores (sin usar el principio de reciprocidad de Cialdini) la condena a hacer 'Office Housework' de por vida:", "Si le resuelves los problemas operativos a otro departamento sin generar una deuda de reciprocidad política, ¿estás siendo una líder estratégica o simplemente te acabas de convertir en su asistente glorificada y gratuita?"),
        ("La Defensa del Tribunal", "Asume el rol del CEO en la simulación. Haz que te explique en 3 minutos exactos, sin jerga corporativa, por qué rechazar tareas administrativas en una junta dominada por hombres es una cuestión de supervivencia política, no de arrogancia."),
        "Debe detectar un comportamiento de 'Tokenismo' o 'Impuesto Invisible' impuesto a OTRA compañera en la empresa, y ayudar a esa colega a desviarlo políticamente esta semana."
    ),
    48: generate_playbook(
        ("Auditoría de Capital de Intercambio", "Revisa tus propias herramientas. Cuando no puedes dar órdenes, ¿qué ofreces? ¿Capital de Tarea, Posición o Personal? Conoce tu inventario."),
        ("Desactivación del Título", "Entiende que si ella depende de decir 'yo soy la gerente' para que las cosas pasen, su influencia real es cero. El título es lo que usas cuando falló la persuasión."),
        ("Calibración Transversal", "Piensa en el departamento más hostil de tu empresa. Prepárate para diseñar una estrategia de influencia sin autoridad dirigida exactamente hacia ellos."),
        "Mañana dejaremos de quejarnos de que Finanzas o Legal no nos apoyan. Te enseñaré a mover áreas enteras sobre las que no tienes autoridad formal.",
        ("Cuando ella se queje de que los gerentes de otras áreas ignoran sus correos porque 'no le reportan a ella':", "Si aceptamos que ellos no tienen ninguna obligación jerárquica de leerte ni apoyarte, ¿qué moneda de intercambio (tiempo, recursos, visibilidad directiva) les has ofrecido a cambio de su lealtad táctica a tu proyecto?"),
        ("El Diseño del Trueque", "Haz que elija a un gerente lateral no colaborativo. Diseñen en conjunto una oferta de 'Capital de Tarea' o 'Capital de Posición' que apunte directamente a los KPIs o al dolor operativo de ese gerente, para forzar su cooperación."),
        "Debe aplicar la oferta de intercambio diseñada con el gerente lateral difícil en las próximas 48 horas, logrando destrabar un proceso o recurso."
    ),
    49: generate_playbook(
        ("Auditoría de Secretos", "¿Qué información crítica sobre 'quién odia a quién' o 'quién tiene el oído del CEO' no le has dicho a tu mentoreada por intentar ser 'profesional'?"),
        ("El Compromiso Cartográfico", "Acepta que retener el mapa de riesgos sociopolíticos de la empresa por mantener la 'diplomacia' es dejar a tu pupila caminar ciega por un campo minado."),
        ("El Trazo Fino", "Revisa mentalmente el historial de fallas tectónicas de la empresa. Identifica la trampa política más peligrosa que se avecina en el departamento de ella. Esa será tu revelación de hoy."),
        "Mañana cerramos la puerta, nadie escucha. Te voy a entregar el mapa político no escrito de esta empresa. Prepárate para la verdad operativa pura.",
        ("Si ella presenta una propuesta que va en contra de la agenda de un Vicepresidente muy silencioso pero muy poderoso:", "Tu proyecto es técnicamente impecable, pero dime una cosa: ¿Qué crees que va a hacer el Vicepresidente de [Área] cuando vea que tu propuesta le quita 20% de su presupuesto de control operativo?"),
        ("La Cartografía Brutal", "Revelación de información táctica asimétrica. Cuéntale a tu mentoreada un caso real y clasificado de la empresa donde un proyecto falló exclusivamente por un veto político no escrito. Explícale cómo las dinámicas informales mataron a la técnica."),
        "Ninguna acción operativa hacia afuera. Su única tarea es trazar un mapa de alianzas ocultas de su propio equipo, basándose en la nueva inteligencia estratégica que le acabas de entregar."
    ),
    50: generate_playbook(
        ("Auditoría de Crecimiento Sistémico", "Mira a la mujer que tienes enfrente. En el Bloque 1 no sabía regular su cortisol. Hoy, entiende la diferencia entre Capital de Posición y Redes Estratégicas. Siente el impacto de tu trabajo."),
        ("Cambio de Piel", "Prepárate para la última sesión de este formato. En el Bloque 6 pasaremos a Estrategia Pura. Hoy debes cerrar definitivamente la etapa de 'política y relaciones'."),
        ("La Observación de Vuelo", "Tu objetivo hoy no es sostenerle la mano. Es hacerle preguntas directivas rápidas y verificar si su instinto de supervivencia corporativa ya opera en automático."),
        "Llegamos al Checkpoint 5. El entrenamiento político ha terminado. Mañana demostraremos si ya puedes navegar el poder sin mi mapa.",
        ("Para probar su capacidad de leer el terreno político por sí sola frente a un dilema futuro imaginario:", "Si el próximo mes te promocionan a Directora y te das cuenta de que la persona de RRHH detesta tu estilo de liderazgo, sabiendo lo que sabes hoy de influencia ética, ¿cuál es tu jugada de la semana 1?"),
        ("Evaluación de Resiliencia Política", "Usa la 'Plantilla Invictus'. Discutan la Matriz de Stakeholders que ella armó. Si identificas un error de lectura (alguien de alto poder que ella cree que no importa), corrígela con candor radical. Documenten el mapa final."),
        "Desconexión operativa absoluta por 24 horas. Debe asimilar el peso del poder corporativo que ahora entiende antes de entrar al Bloque 6: Visión Sistémica y Estrategia.",
        success=True
    )
}

days_data_list = []
for day in range(41, 51):
    day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=DÍA {day+1}|$)', re.DOTALL)
    match = day_pattern.search(md_content)
    if not match:
        day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=RESUMEN DEL BLOQUE|$)', re.DOTALL)
        match = day_pattern.search(md_content)
    
    if not match:
        print(f"Failed to find DÍA {day}")
        continue
        
    day_content = match.group(0)
    title_match = re.search(rf'DÍA {day}\s+(.+?)\n', day_content)
    title = title_match.group(1).strip()
    
    reading_match = re.search(r'FASE 2 — LECTURA CRONOMETRADA.*?(\n\n.+?)(?=\n📖\s*FASE 3)', day_content, re.DOTALL)
    reading_raw = reading_match.group(1).strip()
    
    paragraphs = reading_raw.split('\n')
    reading_html = ""
    for i, p in enumerate(paragraphs):
        p = p.strip()
        if not p: continue
        if i == 0:
            reading_html += f"                        <h3 style=\"color: var(--accent-water); font-size: 1.1rem; margin-bottom: 12px;\">{p}</h3>\n"
        else:
            reading_html += f"                        <p>{p}</p>\n"
            
    q_literal = re.search(r'\[Literal\](.*?)\n', day_content).group(1).strip()
    q_infer = re.search(r'\[Inferencial\](.*?)\n', day_content).group(1).strip()
    try:
        q_opcion = re.search(r'\[Opción múltiple\](.*?)\n', day_content).group(1).strip()
    except AttributeError:
        q_opcion = "Diseña una prueba situacional que desafíe este conocimiento."
    q_personal = re.search(r'\[Conexión(.*?)\n(.*?)(?=\n🧠)', day_content, re.DOTALL).group(2).strip()
    
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
                badge: "Bloque 5 • Día {day-40}",
                title: "{title}",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

new_html = template

new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 5</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan')
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 5')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'NAVEGANDO LA RED DE PODER Y POLÍTICA')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 5 • Día X')

pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque5_Premium.html successfully.")
