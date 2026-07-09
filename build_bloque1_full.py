import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1.md"
target_html = source_html # Overwrite it

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
    1: generate_playbook(
        ("Auditoría de tu Historia", "Escribe 3 momentos clave donde lograste resultados excepcionales pero internamente sentiste que fue 'suerte' o 'ayuda de otros'. Resignifícalos asumiendo el 100% del crédito."),
        ("Confrontando a tu Impostor", "Identifica la voz crítica que más te frena hoy. Escribe al lado la verdad objetiva basada en tus resultados históricos. Destruye la mentira."),
        ("Compromiso de Acción Frontal", "Define 1 acción incómoda que ejecutarás esta misma semana (Ej: liderar una junta). Al tomar acción, ganas autoridad moral para exigir lo mismo."),
        "Mañana destruiremos tu síndrome del impostor. Repasa tus 3 mayores logros. No me traigas suerte, tráeme hechos.",
        ("Si usa frases minimizando su éxito ('me ayudaron', 'tuve suerte'), interrúmpela y lanza esta pregunta:", "Si tuvieras la autoridad absoluta hoy, ¿qué orden directa darías que no te atreves a dar ahora?"),
        ("Auditoría del Lenguaje Interno", "Haz que anote sus creencias limitantes. Trabajen juntas para tacharlas y escribir la reformulación objetiva."),
        "Oblígala a comprometerse a hablar primero en la junta directiva más importante de su semana. Acuerden el reporte."
    ),
    2: generate_playbook(
        ("Reconocimiento de Linaje", "Identifica un temor corporativo profundo. Rastrea cómo se comportaban las mujeres de tu familia frente a la autoridad."),
        ("Romper el Código Biológico", "Escribe: 'Hoy rompo este código biológico. Mi estrés no me pertenece, fue heredado'. Respira profundo 3 veces."),
        ("Calibración de Postura", "Adopta la postura de mayor poder físico que conozcas durante 2 minutos. Sube tu testosterona y baja tu cortisol."),
        "Tu cansancio no es tuyo, es generacional. Mañana mapearemos qué miedo le heredaste a tu linaje. Ven lista.",
        ("Cuando exprese agotamiento por querer controlarlo todo, valídala y confronta con esta pregunta:", "¿Estás tomando esta decisión desde la supervivencia biológica de tus ancestros, o desde el poder de tu cargo actual?"),
        ("Validando el Cansancio", "Dile: 'Tu cansancio no es debilidad, es el esfuerzo metabólico de romper una estructura generacional'. Esta validación cambia su neuroquímica."),
        "Oblígala a delegar hoy mismo una tarea operativa crítica que retiene por miedo. Debe copiarte en el correo."
    ),
    3: generate_playbook(
        ("Auditoría de Trauma", "Reflexiona: ¿Reaccionas con hipervigilancia cuando tu jefe directo cambia su tono de voz? Identifica si tu respuesta es desproporcionada al estímulo real."),
        ("Reescribiendo los Circuitos", "Recuerda el principio de LeDoux: El miedo no se borra, se inhibe con confianza nueva. Tu objetivo no es hacerla sentir 'segura', es hacerla sentir 'competente'."),
        ("Postura de Seguridad", "Antes de la sesión, baja tu propio ritmo cardíaco. Tu tranquilidad biológica regulará el sistema nervioso de ella mediante neuronas espejo."),
        "El miedo que sientes ante el conflicto no te pertenece. Mañana descubriremos de quién es. Prepárate para incomodarte.",
        ("Si ella evita confrontar a un par argumentando que 'no vale la pena pelear', ataca el circuito subyacente:", "Si estuvieras absolutamente segura de que tu puesto no corre peligro, ¿qué le dirías a esa persona mañana por la mañana?"),
        ("Exposición Calibrada", "Diseñen un micro-conflicto seguro. Oblígala a decir 'No' a una petición menor hoy, sin dar justificaciones extensas."),
        "Debe sostener contacto visual por 3 segundos adicionales en su próxima negociación difícil antes de hablar."
    ),
    4: generate_playbook(
        ("Diagnóstico del Arquetipo", "Revisa los 5 arquetipos de Valerie Young (Experta, Perfeccionista, etc). ¿Bajo qué máscara se esconde tu propio impostor? Desármalo antes de verla."),
        ("El Blindaje Estadístico", "Asume que ella sufre de amenaza de estereotipo. No la trates con fragilidad; trátala con los datos fríos de su propia rentabilidad corporativa."),
        ("Alineación de Pertenencia", "Toma la decisión consciente de hacerla sentir que la mesa directiva le pertenece por derecho, no por invitación."),
        "Mañana quiero ver tu historial de proyectos exitosos impreso. Vamos a desarmar a la estafadora que vive en tu cabeza.",
        ("Cuando ella argumente que no está lista para una promoción porque le falta una habilidad X:", "¿Estás esperando que un título te dé el permiso para actuar con la autoridad que ya ejerces todos los días en la sombra?"),
        ("La Matriz de Evidencia", "Haz que divida una hoja en dos: 'Lo que siento que soy' vs 'Lo que los números dicen que he logrado'. Solo se permite argumentar con la segunda columna."),
        "Debe aplicar a una oportunidad, panel o proyecto para el cual siente que solo cumple el 60% de los requisitos."
    ),
    5: generate_playbook(
        ("Auditoría de Carga", "¿Qué estás reteniendo en tu mente que debería estar en papel? El estrés no procesado destruye la estrategia."),
        ("El Compromiso del Papel", "Antes de exigirle que escriba, toma tu cuaderno y redacta tu mayor miedo profesional actual. Siente el alivio biológico."),
        ("Calibración del Espacio", "Esta sesión requiere silencio absoluto. Asegúrate de no interrumpirla mientras procesa su propio lenguaje."),
        "El estrés que cargas pesa porque no tiene nombre. Mañana le pondremos palabras. Trae tu cuaderno y tu mente clara.",
        ("Si ella se queja de estar abrumada por múltiples frentes sin poder priorizar:", "Deja de pensar en voz alta. Toma el bolígrafo. Escribe la peor consecuencia posible si uno de esos frentes colapsa. ¿Sobrevivirás a ello?"),
        ("La Purga Semántica", "Dale 5 minutos de silencio cronometrado en la sesión para que escriba sin filtro su frustración actual. Luego, oblígala a destruir el papel."),
        "Implementar el 'Brain Dump' de 10 minutos al final de cada jornada laboral por los próximos 3 días. Sin excepciones."
    ),
    6: generate_playbook(
        ("Auditoría de Renconres Corporativos", "Haz una lista mental de la gente en la oficina a la que aún le guardas rencor por un error pasado. Ese rencor te cuesta dinero y eficiencia."),
        ("El Ego del Agravio", "Acepta que no perdonar a un colega es darle control de renta vitalicia en tu cerebro. Córtale el contrato hoy."),
        ("Preparación para la Incomodidad", "Ella querrá justificar por qué tiene razón en estar enojada. Prepárate para no validar su papel de víctima."),
        "El rencor corporativo es un lujo que las líderes de alto impacto no pueden pagar. Mañana aprenderás a soltarlo estratégicamente.",
        ("Cuando dedique más de 2 minutos de la sesión a quejarse de lo injusto que fue alguien con ella:", "Si tuvieras que pagar 100 dólares por cada minuto que pasas hablando del error de él en lugar de tu próxima estrategia, ¿estarías dispuesta a arruinarte?"),
        ("El Reencuadre Transaccional", "Haz que redacte los hechos de la ofensa eliminando cualquier verbo emocional. Conviértanlo en un problema logístico, no personal."),
        "Tener una reunión de 10 minutos con la persona con la que tiene conflicto para alinear objetivos operativos futuros, sin mencionar el problema pasado."
    ),
    7: generate_playbook(
        ("Auditoría de Sesgos", "¿Cuándo fue la última vez que juzgaste a alguien de tu equipo por 'falta de compromiso' cuando en realidad tenían un cuello de botella sistémico?"),
        ("El Cambio de Prisma", "Recuerda: Los errores de los demás suelen ser de contexto, tus propios errores también. Despersonaliza el error."),
        ("Calibración de Empatía Estructural", "Entra a la sesión no como jueza de la moral, sino como ingeniera de sistemas. El problema nunca es la persona, es el proceso."),
        "Mañana cambiaremos los lentes con los que juzgas a tu equipo. Descubriremos que estabas resolviendo el problema equivocado.",
        ("Si ella afirma categóricamente que un empleado 'simplemente no tiene la actitud':", "Si cambiaras mágicamente a ese empleado por uno perfecto, pero mantuvieras el mismo sistema de incentivos y procesos, ¿cuánto tardaría el nuevo en fallar igual?"),
        ("Mapeo del Entorno", "Oblígala a dibujar el ecosistema del empleado que falla. Identifiquen 3 barreras invisibles que ella, como líder, no le ha quitado del camino."),
        "Eliminar un reporte, proceso redundante o barrera burocrática del escritorio del empleado de menor rendimiento antes del viernes."
    ),
    8: generate_playbook(
        ("Auditoría de Resistencia", "Revisa tu propio historial. ¿Qué feedback duro recibiste hace un año que descartaste por estar 'mal dicho', pero que en el fondo era verdad?"),
        ("Separación del Mensajero y el Mensaje", "Prepárate para enseñarle a extraer oro de la basura. El feedback importa, incluso si quien lo da es incompetente."),
        ("Estado de Alta Receptividad", "Sé un modelo de lo que vas a enseñar. Inicia la sesión pidiéndole que te dé feedback sobre tu estilo de mentoría."),
        "Mañana aprenderás a recibir las críticas que más te duelen. Tu ego no está invitado a nuestra reunión.",
        ("Cuando ella se defienda diciendo que quien le dio feedback no tiene autoridad moral para hacerlo:", "Separemos al incompetente que te entregó el paquete, del paquete en sí. Si le quitas el tono ofensivo, ¿qué 10% de lo que te dijo es absolutamente cierto?"),
        ("La Criba del Feedback", "Analicen la última evaluación negativa que ella recibió. Oblígala a encontrar 1 verdad operativa indiscutible en medio del sesgo."),
        "Solicitar proactivamente a un par crítico que le señale su mayor 'punto ciego' operativo, y solo responder: 'Gracias'."
    ),
    9: generate_playbook(
        ("Auditoría de Seguridad", "¿Quién en tu propio equipo tiene miedo de decirte que una idea tuya es pésima? Si la respuesta es 'nadie', eres un peligro para la empresa."),
        ("El Poder de la Ignorancia Declarada", "La mayor demostración de poder de un líder es decir 'No sé'. Ensáyalo antes de verla."),
        ("Diseño del Espacio Seguro", "Hoy debes premiar la disidencia. Si ella te contradice en la sesión, valídala inmediatamente."),
        "Si tu equipo no te está dando malas noticias, es porque tú eres la mala noticia. Mañana cambiaremos eso.",
        ("Si ella se enorgullece de que en su equipo 'nunca hay errores ni quejas':", "El silencio en la base no significa eficiencia; significa terror operativo. ¿Qué desastre está ocurriendo ahora mismo que no te están diciendo porque tienen miedo de tu reacción?"),
        ("El Ritual de la Falla Celebrada", "Oblígala a diseñar cómo va a revelar un fracaso propio frente a su equipo para demostrar que el error es permitido y funcional."),
        "Iniciar la próxima junta de equipo diciendo: 'Me equivoqué en la decisión X de la semana pasada, y esto es lo que aprendí. Ahora, ¿dónde nos estamos equivocando hoy?'"
    ),
    10: generate_playbook(
        ("Síntesis del Bloque 1", "Revisa la transformación de los últimos 10 días. Hemos reconstruido su identidad desde la epigenética hasta la seguridad psicológica. Ella ya no es la misma."),
        ("El Peso de la Responsabilidad", "Acepta que ella ahora tiene las herramientas. Ya no puede usar la excusa de 'no sabía cómo'. Eleva tu nivel de exigencia al máximo."),
        ("Postura de Transición", "Esta no es una sesión más. Es el cierre del Bloque de Raíz. Habla menos, exige más."),
        "Mañana cerramos el Bloque 1. Es el examen final de tu identidad corporativa. Trae tu mente afilada.",
        ("Para evaluar la consolidación de la nueva identidad de liderazgo:", "De todo lo que hemos destruido y reconstruido en estos 10 días, ¿cuál es la mentira que te contabas a ti misma a la que ya nunca más podrás volver?"),
        ("La Declaración de Autoridad", "Oblígala a verbalizar su nueva tesis de identidad de liderazgo en una sola oración, sin justificaciones, sin pedir disculpas, mirando a los ojos."),
        "Escribir una carta a su 'Yo' de hace 10 días, explicando por qué ya no necesita permiso para ocupar su espacio en la mesa directiva."
    )
}

# Regex to replace daysData array inside target_html
pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)

# Now let's extract readings from markdown
days_data_list = []
for day in range(1, 11):
    day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=DÍA {day+1}|$)', re.DOTALL)
    match = day_pattern.search(md_content)
    if not match:
        continue
    day_content = match.group(0)
    
    title_match = re.search(rf'DÍA {day}\s+(.+?)\n', day_content)
    title = title_match.group(1).strip()
    
    # Extract reading (between FASE 2 and FASE 3 or FASE 4)
    reading_match = re.search(r'FASE 2 — LECTURA CRONOMETRADA.*?(\n\n.+?)(?=\n📖\s*FASE 3|\n🔍\s*FASE 4)', day_content, re.DOTALL)
    if reading_match:
        reading_raw = reading_match.group(1).strip()
    else:
        reading_raw = "Contenido de lectura..."
        
    paragraphs = reading_raw.split('\n')
    reading_html = ""
    for i, p in enumerate(paragraphs):
        p = p.strip()
        if not p: continue
        if i == 0:
            reading_html += f"                        <h3 style=\"color: var(--accent-water); font-size: 1.1rem; margin-bottom: 12px;\">{p}</h3>\n"
        else:
            reading_html += f"                        <p>{p}</p>\n"
            
    q_literal = "Reflexión Literal"
    q_infer = "Reflexión Inferencial"
    q_opcion = "Aplicación Múltiple"
    q_personal = "Conexión Personal"
    try: q_literal = re.search(r'\[Literal\]\n(.*?)\n', day_content).group(1).strip()
    except: pass
    try: q_infer = re.search(r'\[Inferencial\]\n(.*?)\n', day_content).group(1).strip()
    except: pass
    try: q_opcion = re.search(r'\[Opción múltiple\]\n(.*?)\n', day_content).group(1).strip()
    except: pass
    try: q_personal = re.search(r'\[Conexión personal\]\n(.*?)\n', day_content).group(1).strip()
    except: pass
    
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
                badge: "Bloque 1 • Día {day}",
                title: "{title}",
                desc: "Fundamentos y Raíces",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

new_html = pattern.sub('const daysData = ' + days_data_array_str, template)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque1_Premium.html with days 1 to 10 successfully.")
