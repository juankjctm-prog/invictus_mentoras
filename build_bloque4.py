import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque4.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque4_Premium.html"

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
    31: generate_playbook(
        ("Auditoría de Percepción", "Antes de entrar a la sesión, clasifica a tu mentoreada: ¿Es la Perfeccionista, la Experta o la Superhumana? Si no sabes de qué está huyendo, no puedes guiarla."),
        ("El Falso Confort", "Acepta que el elogio genérico ('Eres excelente') no cura a una Experta, solo aumenta su terror de ser descubierta. Prométete no usar elogios vacíos hoy."),
        ("Ajuste de Espectro", "Toma el arquetipo que identificaste y diseña el antídoto. Si es Perfeccionista, prepárate para exigir velocidad. Si es Superhumana, prepárate para exigir límites."),
        "Mañana auditaremos las reglas con las que mides tu propio valor. Ven lista para desmantelar tus expectativas imposibles.",
        ("Si ella se agobia porque un proyecto salió bien pero la ejecución tuvo pequeñas fallas:", "Si el cliente firmó el contrato de 5 millones, ¿por qué estás evaluando tu valor como ejecutiva basándote en que hubo un error tipográfico en la diapositiva 12?"),
        ("El Mapeo del Arquetipo", "Pon los 5 arquetipos de Valerie Young frente a ella. Haz que elija cuál es el suyo y obligala a describir en voz alta cómo ese arquetipo está frenando su próximo ascenso directivo."),
        "Obligarla a entregar su próximo reporte o análisis al 85% de perfección. Prohibido pulirlo obsesivamente. Debe entregarlo en crudo a su superior inmediato."
    ),
    32: generate_playbook(
        ("Auditoría de Rescate", "¿Cuántas veces has intentado convencer a tu mentoreada de lo valiosa que es, solo para verla dudar de nuevo al día siguiente? Entiende que la autoestima no es la métrica."),
        ("Cambio de Enfoque", "Acepta que tu trabajo no es hacerla sentir bien consigo misma (Autoestima). Tu trabajo es hacer que crea en su capacidad para ejecutar bajo fuego (Autoeficacia)."),
        ("El Inventario de Dominio", "Revisa la historia operativa de tu mentoreada. Haz una lista mental de 3 crisis graves que ella resolvió impecablemente. Esos son los hechos que usarás hoy."),
        "Dejaremos de hablar de cómo te sientes y empezaremos a hablar de lo que puedes construir. Trae las métricas de tu último éxito.",
        ("Si ella duda de su capacidad para el nuevo rol argumentando que 'no se siente lista':", "Si eliminas cómo te 'sientes' hoy y observas exclusivamente el historial de crisis que has resuelto en los últimos dos años, ¿los datos duros dicen que estás lista o no?"),
        ("El Tablero de Autoeficacia", "Haz que escriba en una hoja las 3 batallas más duras que ha ganado en la empresa. Oblígala a leerlas en voz alta y declarar: 'Mi competencia es un hecho comprobable, no un sentimiento'."),
        "Debe tomar un proyecto pequeño pero de alto perfil operativo, presentarse voluntaria para liderarlo y enviar la confirmación en las próximas 24 horas."
    ),
    33: generate_playbook(
        ("Auditoría de Retos", "Revisa lo que le delegaste el último mes. ¿Estaba en su zona de confort (aburrimiento) o la lanzaste al vacío sin red (pánico)?"),
        ("Cálculo del Punto Óptimo", "Define el 'Punto Óptimo' para hoy. ¿Qué tarea la empujará exactamente un 15% fuera de su control actual? Diseña la caída para que duela, pero no la mate."),
        ("Renuncia al Control", "Mentalízate: Para que ella tenga una Experiencia de Dominio, tú tienes que hacerte a un lado y dejar que ella tome el volante, aunque choque un poco."),
        "Mañana te pondré al mando de una situación que no dominás al 100%. Descansa, vas a necesitar claridad.",
        ("Si ella intenta devolverte el control de una tarea para la que ya tiene las herramientas:", "¿Qué riesgo específico estás evitando al pedirme que yo revise este documento antes de que lo mandes al cliente?"),
        ("El Diseño del Salto", "Asignarle en tiempo real, frente a ti, una tarea operativa que la asuste. Definan juntas el 'Peor Escenario Posible' y cómo lo mitigarían. Luego, dile: 'El volante es tuyo'."),
        "Liderar una reunión importante (15% fuera de su zona de confort) la próxima semana, sin permitir que nadie la interrumpa en los primeros 10 minutos."
    ),
    34: generate_playbook(
        ("Auditoría de Ceguera Estructural", "Reconoce tu privilegio si no eres una minoría en la mesa. Y si lo eres, recuerda el agotamiento de 'representar' a tu género o etnia."),
        ("La Externalización del Miedo", "Prepárate para nombrar al monstruo. Si no le dices a tu mentoreada que su hipervigilancia es normal y sistémica, ella pensará que es una falla de su propio cerebro."),
        ("El Escudo de Validación", "Repítete: 'Mi trabajo hoy es quitarle el peso del estereotipo de los hombros, para que recupere su ancho de banda cognitivo'."),
        "Sé lo agotador que es ser la única mujer en esa mesa. Mañana desactivaremos la presión biológica de tener que demostrarles tu valor.",
        ("Cuando ella admita que se paraliza en juntas donde solo hay hombres por miedo a equivocarse:", "Si supieras con total certeza que un error tuyo hoy no confirmaría ningún estereotipo sobre las mujeres ejecutivas en esta industria, ¿qué decisión habrías tomado en esa junta?"),
        ("Reafirmación de Valores", "Haz que haga una lista de sus 3 competencias técnicas más letales. Antes de entrar a su próxima junta hostil, debe leer esa lista y anclar su identidad en sus datos duros, no en su demografía."),
        "Debe presentar una idea contraria al consenso en una reunión donde esté en minoría, enfocándose exclusivamente en la métrica financiera y sosteniendo contacto visual."
    ),
    35: generate_playbook(
        ("Auditoría Lingüística", "Presta atención a cómo habla ella de sus éxitos. ¿Usa el 'nosotros' para logros personales y el 'yo' para los fracasos? Detecta la renuncia a la agencia."),
        ("Corte de Modestia", "Prepárate para interrumpirla. La modestia corporativa falsa es veneno para la autoeficacia. No le permitas usar la palabra 'suerte' bajo ninguna circunstancia."),
        ("El Verbo Directivo", "Selecciona tres verbos fuertes (Ejecutar, Liderar, Decidir) que la obligarás a usar durante la sesión para reconstruir su neurobiología lingüística."),
        "Mañana auditaremos el vocabulario con el que describes tus victorias. Ven lista para reclamar la autoría absoluta de tus resultados.",
        ("Cuando ella describa un proyecto exitoso diciendo 'bueno, el equipo ayudó mucho y tuvimos suerte':", "Si yo entrevistara a tu equipo a solas y les preguntara si ellos habrían logrado este mismo resultado sin tu dirección estratégica exacta, ¿qué me dirían?"),
        ("La Reescritura de Agencia", "Haz que reescriba en voz alta el éxito de su último proyecto eliminando el plural y las excusas circunstanciales. Debe decir: 'YO diseñé esta estrategia, YO gestioné al equipo, y YO entregué este resultado'."),
        "En su próximo correo de estatus de proyecto a sus superiores, debe redactarlo usando voz activa y primera persona del singular para las decisiones clave: 'Decidí...', 'Implementé...'."
    ),
    36: generate_playbook(
        ("Auditoría de Agotamiento", "Mírala a los ojos a través de la cámara o en la oficina. ¿Ves las ojeras sistémicas? ¿Ves la Carga Alostática de la Triple Jornada destruyendo su memoria a corto plazo?"),
        ("El Diagnóstico Duro", "Reconoce que ningún hack de 'gestión del tiempo' solucionará el hecho de que ella está absorbiendo el estrés emocional de 3 dimensiones distintas (trabajo, hijos, pareja)."),
        ("Autorización de Mediosidad", "Prepárate para darle el permiso que nadie más le da: El permiso para que algunas cosas de su vida colapsen un poco para que ella pueda sobrevivir."),
        "Tu agotamiento no es falta de organización, es una sobrecarga neurológica. Mañana desactivamos la trampa de la Supermujer.",
        ("Cuando ella confiese que se siente culpable si no tiene la casa perfecta, los niños perfectos y los reportes perfectos:", "¿En qué momento de tu vida compraste la mentira de que tu valor como ser humano depende de tu capacidad para resolver los problemas de absolutamente todo el mundo al mismo tiempo?"),
        ("La Estrategia de lo Suficientemente Bueno", "Oblígala a elegir 2 áreas de su vida (ej. limpieza de la casa, proyectos menores del equipo) donde a partir de hoy el estándar será 'Suficientemente Bueno' (80%), no 'Perfecto' (100%)."),
        "Delegar o abandonar por completo una tarea logística (del hogar o del trabajo) que le consume al menos 3 horas semanales. Prohibido hacerla ella misma durante todo el mes."
    ),
    37: generate_playbook(
        ("Auditoría de Roles Ancestrales", "¿Estás tratando a tu mentoreada como a una hija corporativa (Cuidadora) o le estás exigiendo como a una futura líder (Matriarca)? Ajusta tu propia energía primero."),
        ("El Paso al Vacío", "Entiende que para que ella transicione a Matriarca, va a tener que soportar que su equipo se enoje porque ella dejará de hacer el trabajo operativo por ellos."),
        ("El Centro de Gravedad", "Visualízate a ti misma como una fuerza inamovible. Hoy no la vas a consolar; la vas a invocar a su propio centro de poder."),
        "El arquetipo de la ejecutiva agotada que rescata a todos ya no te sirve. Mañana transicionamos a la energía de la Matriarca Corporativa.",
        ("Cuando ella se justifique diciendo que su equipo 'no sabe hacerlo tan bien como ella' y por eso termina haciéndolo todo:", "Al hacer el trabajo operativo de tu equipo para salvarlos del error, ¿te das cuenta de que les estás robando la oportunidad de desarrollar su propia competencia, manteniéndolos dependientes de ti?"),
        ("Renuncia de la Cuidadora", "Haz que escriba 3 tareas operativas que actualmente hace por sus subalternos. Oblígala a trazar el plan para soltarlas hoy mismo, declarando que su nuevo rol es marcar la visión, no llenar los vacíos."),
        "Debe rechazar la próxima solicitud de rescate operativo de su equipo diciendo: 'Tengo plena confianza en que ustedes encontrarán la manera de resolverlo. Mándenme la propuesta final el viernes'."
    ),
    38: generate_playbook(
        ("Auditoría de Vulnerabilidad", "¿Cuándo fue la última vez que le dijiste a tu mentoreada: 'No sé cómo resolver esto, acompáñame a averiguarlo'? Modela tú primero la vulnerabilidad táctica."),
        ("El Costo del Escudo", "Reconoce que si exiges perfección antes de actuar, estás educando a una ejecutiva temerosa, no a una líder innovadora. Deshazte de tu propio perfeccionismo antes de la sesión."),
        ("Desactivación de Armaduras", "Visualiza cómo vas a penetrar las excusas racionales que ella usará para no lanzar su proyecto ('es que le falta diseño', 'es que el cliente podría quejarse')."),
        "El perfeccionismo te está haciendo lenta en un mercado que premia la velocidad. Mañana te quitaré la armadura.",
        ("Cuando ella insista en retrasar la entrega de un proyecto por revisar detalles minúsculos por quinta vez:", "¿Qué miedo profundo te está obligando a esconderte detrás de la perfección de este documento para no tener que exponer tu trabajo al juicio del mercado?"),
        ("Exposición al Riesgo (Mínimo Producto Viable)", "Haz que identifique un proyecto que tiene estancado por perfeccionismo. Oblígala a reducir el alcance a lo más básico y a establecer una fecha de entrega inamovible para esa versión imperfecta."),
        "Debe entregar o lanzar un proyecto crítico esta semana estando solo al 80% de su satisfacción personal, y resistir la ansiedad de querer 'corregirlo' antes de que el superior lo vea."
    ),
    39: generate_playbook(
        ("Auditoría de Secuencia", "Revisa mentalmente la secuencia del bloque: Arquetipo -> Autoeficacia -> Carga Alostática -> Perfeccionismo. ¿Entiendes cómo un componente detona al siguiente?"),
        ("El Rol del Arquitecto", "Acepta que curar el síndrome del impostor no es trabajo motivacional, es re-estructuración cognitiva. Tú eres el arquitecto del andamiaje que sostiene a la mentoreada."),
        ("Sintonización Fina", "Prepárate para ser implacable con sus respuestas. Hoy no permitirás ni una sola excusa, justificación o uso de 'suerte'. Serás un muro de contención lingüística."),
        "Hoy unimos las piezas. Mañana me demostrarás que sabes desmantelar tu propio síndrome del impostor sin mi ayuda.",
        ("Cuando ella no logre conectar cómo su perfeccionismo (Día 38) está directamente causando su carga alostática (Día 36):", "Si usaras la misma energía que gastas en intentar ser la 'Superhumana' perfecta para todo el mundo, pero la enfocaras exclusivamente en construir métricas que demuestren tu autoeficacia, ¿dónde estarías hoy en el organigrama?"),
        ("El Mapeo de Evasión (Feynman)", "Haz que ella dibuje su propio ciclo de autosabotaje: 'Cuando siento X, mi arquetipo de Impostor hace Y, lo que me lleva a usar Lenguaje sin Agencia Z'. Oblígala a explicarlo fluidamente."),
        "Debe identificar a una mujer en su propio equipo de menor rango que sufra del síndrome del impostor, y aplicar con ella la desactivación de la 'Amenaza del Estereotipo'."
    ),
    40: generate_playbook(
        ("Auditoría de Impacto Directo", "Mira a la ejecutiva frente a ti. Compara su postura verbal de hoy con la que tenía en el Día 31. Reconoce la autoridad que tu mentoría ha forjado en ella."),
        ("El Desapego Táctico", "Llegaste a la mitad del programa Master Track. Tu mentoreada ya tiene las herramientas cognitivas base. Prepárate para empezar a alejarte y exigirle más autonomía estructural."),
        ("Visión Sistémica", "A partir del Bloque 5 entraremos en política corporativa y redes de poder. Cierra los temas de 'desarrollo interior' de tu mentoreada hoy. Es hora de llevarla a la guerra corporativa exterior."),
        "Llegamos a la mitad del programa Master Track. Cierra la puerta y respira. Mañana trazaremos tu intervención cognitiva maestra.",
        ("Para evaluar si ella está lista para dejar de enfocarse en sí misma y empezar a liderar el sistema:", "Viendo la mujer en la que te has convertido en estos 40 días, y sabiendo que el Síndrome del Impostor es una falla estructural y no tuya, ¿cuál es tu responsabilidad moral hacia las mujeres jóvenes que acaban de entrar a la empresa?"),
        ("Auditoría del Checkpoint", "Usa la 'Plantilla Invictus'. Discutan en conjunto cuál ha sido el micro-desafío (Punto Óptimo) que más dolió pero que más crecimiento le generó en este bloque. Documenten ese hito."),
        "Desconexión absoluta. No se permiten reuniones tácticas hoy. Debe preparar su mente para el Bloque 5, donde pasaremos del mundo interior a la Política y las Redes de Poder corporativas.",
        success=True
    )
}

days_data_list = []
for day in range(31, 41):
    day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=DÍA {day+1}|$)', re.DOTALL)
    match = day_pattern.search(md_content)
    if not match:
        # Fallback for the last day
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
                badge: "Bloque 4 • Día {day-30}",
                title: "{title}",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

new_html = template

new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 4</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan')
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 4')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'LA AUTOEFICACIA Y EL IMPOSTOR EN LA MENTOREADA')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 4 • Día X')

pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque4_Premium.html successfully.")
