import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque6.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque6_Premium.html"

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
    51: generate_playbook(
        ("Auditoría de Inversión", "¿Tu relación actual con ella es de consejería (Mentoring) o de inversión política (Sponsorship)? Hoy la evalúas como activo corporativo."),
        ("El Límite del Consejo", "Acepta que darle consejos para que 'trabaje mejor' ya no sirve. Si ella no entra a las salas de decisión, sus horas de trabajo no valen nada."),
        ("Postura de Patrocinadora", "Prepárate para endurecer el tono. Un Sponsor exige un nivel de ejecución impecable porque la reputación del Sponsor está en juego."),
        "Dejaremos de hablar de cómo hacer tu trabajo y empezaremos a hablar de quién decide tu futuro. Mañana subimos el nivel.",
        ("Si ella asume que sus resultados excepcionales automáticamente atraerán la atención de un VP para ascenderla:", "Si observas a los últimos 3 hombres que ascendieron a la alta gerencia, ¿crees sinceramente que subieron solo por su Excel perfecto, o porque un director puso su capital político sobre la mesa por ellos?"),
        ("Auditoría de Apuestas", "Haz que nombre a 2 personas de nivel gerencial superior que, según ella, apostarían su propio nombre por ella a puerta cerrada. Si duda o dice 'no sé', esa es su brecha de Sponsorship."),
        "Debe identificar a un posible 'Sponsor' en la empresa (Alguien con Alto Poder) con el que agendará una interacción estratégica en los próximos 15 días, no operativa."
    ),
    52: generate_playbook(
        ("Auditoría de Monedas", "¿Cuántas horas invierte tu mentoreada asegurándose de que su 'Capital de Desempeño' sea perfecto, descuidando su 'Capital de Relación'?"),
        ("Corte de Perfeccionismo", "El perfeccionismo es el refugio de quien tiene miedo a construir relaciones. Oblígala a soltar el teclado y salir al pasillo corporativo."),
        ("El Valor de tu Agenda", "Enséñale que el trabajo operativo la mantiene en la nómina, pero las relaciones estratégicas la mantienen en la carrera por el poder."),
        "Trabajar 12 horas al día ya no es suficiente. Mañana auditamos tu cuenta de Capital de Relación.",
        ("Cuando ella se justifique diciendo que prefiere enfocarse en 'los resultados' en lugar de 'tomar café con los jefes':", "El Capital de Desempeño sufre de rendimientos decrecientes. ¿En qué momento vas a aceptar que entregar un reporte al 100% de calidad hoy te genera menos influencia que entregarlo al 90% e invertir esa hora en construir lealtad con Finanzas?"),
        ("El Cambio de Moneda", "Haz que dibuje dos columnas: Capital de Desempeño vs Capital de Relación. Oblígala a reducir el 15% de su energía del primero y a redactar una acción concreta para invertirla en el segundo."),
        "Debe rechazar hacer horas extras este viernes para 'perfeccionar' un documento, y usar esa hora para tomar un café estratégico con un líder lateral."
    ),
    53: generate_playbook(
        ("Auditoría de Riesgo Propio", "¿Estás dispuesta a apostar tu propio nombre por ella en este comité? Si no, ¿es porque te falta valentía política o porque ella no está lista?"),
        ("El Guion del Escudo", "Practica cómo la defenderías. En tu mente, ¿cuál es el 'Air Cover' (cobertura aérea) que le darías a sus puntos ciegos si un VP la ataca en el comité?"),
        ("Transparencia Brutal", "Hoy le dirás exactamente qué falta para que tú seas su Sponsor oficial. Cero ambigüedad."),
        "Mañana te revelaré exactamente qué necesitas hacer para que yo esté dispuesta a pelear por tu ascenso en el comité directivo.",
        ("Si ella no entiende por qué los ejecutivos dudan en ascenderla a roles de altísima visibilidad:", "Si yo apostara mi prestigio corporativo exigiendo que te den la Gerencia Regional, y tú cometes un error grave por falta de comunicación, ¿te das cuenta de que el comité no cuestionará tu capacidad, sino la mía por haberte respaldado?"),
        ("El Simulacro de Cobertura", "Haz el rol de un Director hostil. Ataca su debilidad más grande. Enséñale cómo un Sponsor hace 'Air Cover': reconociendo la debilidad y neutralizándola con el impacto en el P&L."),
        "Ella debe redactar un P&L de impacto directo de su gestión y enviártelo en 24 horas, argumentando por qué es financieramente 'patrocinable'."
    ),
    54: generate_playbook(
        ("Auditoría de Ansiedad", "Reconoce tu propia 'Ansiedad de Apostar el Nombre'. Como mujer líder, el sistema es menos tolerante con tus errores de patrocinio. Acepta el riesgo."),
        ("El Filtro de Fuego", "Tu responsabilidad es probarla antes de patrocinarla. Prepárate para diseñarle un 'test de lealtad operativa' en la sesión de hoy."),
        ("Protección de Capital", "Internaliza: Si ella se queja, evade o falla en comunicación temprana, el Sponsorship se revoca. No eres su terapeuta; eres su inversionista."),
        "El Sponsorship es una transacción de alto riesgo. Mañana pondremos a prueba tu capacidad para sostener mi prestigio corporativo.",
        ("Cuando ella asuma que tu patrocinio es incondicional por ser mujeres:", "El Sponsorship no es sororidad emocional; es una alianza táctica. Si mi reputación está amarrada a la tuya frente a la Junta, ¿por qué debería confiar en que no me enteraré de tus errores por la boca del CEO antes que por la tuya?"),
        ("Diseño del Early Warning", "Pactar el protocolo de 'Alerta Temprana'. Oblígala a verbalizar frente a ti el compromiso: 'Jamás te sorprenderé con un error táctico del que no estés previamente informada'."),
        "Debe asignarle a su propio equipo un proyecto delegado asumiendo ella misma el riesgo de Sponsorship (Apostar su nombre por un talento joven)."
    ),
    55: generate_playbook(
        ("Auditoría de Redes Cerradas", "¿Tienes acceso a las Redes Cerradas donde se define el destino de la empresa? Si no, ¿cómo vas a introducirla a ellas? Evalúa tu propia influencia."),
        ("El Código No Escrito", "Tu tarea es decodificar la etiqueta del poder. Enséñale qué temas son aceptables y cuáles son suicidio político en los círculos informales del directorio."),
        ("El Factor 'Fit'", "Prepara a tu mentoreada para entender que en los niveles más altos, el 'cultural fit' (qué tan cómoda se siente la mesa con ella) importa más que su currículum técnico."),
        "La excelencia técnica no te abrirá la puerta de la Alta Dirección. Mañana te revelo cómo funcionan las Redes Cerradas.",
        ("Si ella cree que ser la más inteligente técnicamente garantiza su entrada a la Alta Gerencia:", "En el comité ejecutivo no debaten manuales de ingeniería, debaten lealtades. Si la Red Cerrada te percibe como una operadora brillante pero no confían en tu alineación política, ¿quién crees que obtendrá el ascenso?"),
        ("Simulación de Infiltración", "Role-play: Ella está en una cena con 3 Vicepresidentes de la Red Cerrada. Haz que te demuestre cómo interactúa sin parecer desesperada por probar su conocimiento técnico (Capital de Desempeño), enfocándose en construir Capital de Relación."),
        "Participar en un evento social/informal de la empresa con el objetivo estricto de escuchar y mapear las alianzas de la Red Cerrada, prohibido hablar de sus métricas técnicas."
    ),
    56: generate_playbook(
        ("Auditoría del Contrato", "¿Estás lista para formalizar la relación? Si vas a transicionar a Sponsor, necesitas escribir el contrato psicológico en tu Libreta Invictus."),
        ("La Regla de Fricción", "Adviértele que el Sponsorship le va a traer fricción con sus pares. Cuando tú comiences a protegerla e impulsarla, otros sentirán envidia. Ella debe resistir la presión de volver al promedio."),
        ("Elevación de Estándares", "Hoy dejas de ser 'suave'. La mentoreada tiene que sentir la gravedad de que alguien con poder apueste su vida corporativa por ella."),
        "Se acabó la etapa de los consejos de pasillo. Mañana firmaremos el contrato táctico de Sponsorship. Ven lista para asumir el peso.",
        ("Para asegurar que ella entienda que representar a un Sponsor exige abandonar la mediocridad:", "A partir de hoy, si tú entregas un proyecto mediocre, la corporación no dirá 'ella falló'; dirán 'el talento que [Tu Nombre] respalda es mediocre'. ¿Estás dispuesta a sostener esa presión bajo fuego cruzado?"),
        ("Formalización del Pacto", "Exígele que recite sus dos obligaciones insalvables: Rendimiento Excepcional y Alerta Temprana (Early Warning). Si duda un segundo en aceptar las condiciones, cancela la transición al Sponsorship."),
        "Debe redactar y enviarte un resumen ejecutivo de su proyecto más grande, demostrando el estándar letal que mantendrá como tu patrocinada oficial."
    ),
    57: generate_playbook(
        ("Auditoría de Secuencia (Feynman)", "¿Entiendes tú misma la cadena económica del patrocinio? De Capital de Desempeño a Relación, de Mentoring a Air Cover, hasta inyectarla en la Red Cerrada."),
        ("El Rol del Banco Central Corporativo", "Recuérdate a ti misma: Tú controlas el flujo del capital político. Tú decides cuándo invertir en ella y cuándo retirar los fondos si ella incumple el contrato."),
        ("Alineación Estructural", "No dejes que ella hable en abstracto hoy. Oblígala a demostrarte que entiende que el Sponsorship es una operación de negocio, no una terapia de amigas."),
        "Mañana unes todas las piezas económicas del poder. Demuéstrame que sabes la diferencia entre que te dé un consejo o que invierta en ti.",
        ("Cuando ella no logre articular la diferencia entre el riesgo de un mentor vs el riesgo de un sponsor:", "Si yo te doy un consejo sobre cómo manejar un conflicto, mi riesgo es cero. Si yo obligo al CEO a darte la dirección de operaciones y tú colapsas el proyecto, ¿quién paga la factura política de ese desastre en la siguiente reunión de directorio?"),
        ("La Presentación del Inversor", "Oblígala a hacer un pitch de 3 minutos como si estuviera convenciendo al Director General de ser su Sponsor Oficial. Debe justificar el Retorno de Inversión (ROI) político que ella le generaría a la empresa."),
        "Identificar a una profesional junior en su área y comenzar a fungir como su Sponsor activo para micro-proyectos de 2 semanas de duración."
    ),
    58: generate_playbook(
        ("Auditoría de Círculos", "¿A quiénes estás conectando? Si solo la patrocinas hacia arriba (hacia los VP) pero no la conectas lateralmente con otras mujeres fuertes, la estás dejando vulnerable."),
        ("Desactivación de la Abeja Reina", "El síndrome de la Abeja Reina es la enfermedad de las Redes Cerradas. Rompe eso forzando la colaboración entre patrocinadas de diferentes divisiones."),
        ("Mente de Enjambre", "Prepárate para tejer la red. Vas a presentarla a otra de tus aliadas tácticas corporativas. Las alianzas cruzan los silos de la organización."),
        "El aislamiento corporativo te hace frágil frente a los vetos. Mañana construiremos tu bloque de poder aliado.",
        ("Cuando ella vea a otra mujer exitosa en otra área como una 'competencia' por los recursos del directorio:", "Si el sistema corporativo asume que solo hay una silla en la mesa directiva para una mujer, y tú peleas por ella sola, pierdes. ¿Qué pasa si te alías con esa mujer de finanzas y exigen DOS sillas con respaldo cruzado?"),
        ("El Cruce de Inteligencia", "Dile explícitamente: 'Necesito que conozcas a la Directora de Legal a quien también estoy respaldando. Tienen 48 horas para agendar una llamada y encontrar una sinergia operativa entre sus departamentos'."),
        "Ejecutar la llamada de sinergia con la aliada cruzada, y encontrar al menos un 'Capital de Tarea' que intercambiar en el mes en curso."
    ),
    59: generate_playbook(
        ("Auditoría de Alineación", "Mapea su meta. ¿Ella quiere ser VP de Marketing, pero el directorio solo piensa en cómo reducir la deuda del P&L? Su propuesta de ascenso está muerta si no ataca la deuda."),
        ("El Enfoque del Triángulo", "Visualiza los 3 vértices: La ambición de ella, tu capital de riesgo y el KPI del CEO. Tu labor hoy es reescribir su ambición en el lenguaje del dolor del CEO."),
        ("Destrucción del Ego", "No importa cuánto ella 'merezca' el ascenso. Si su ascenso no resuelve la úlcera del directorio, tú no puedes patrocinarla porque fallarías. Sé dura en esto."),
        "Pedir un ascenso argumentando 'es que he trabajado muy duro' es un error de novatos. Mañana alineamos tu ambición con el dolor del Directorio.",
        ("Si ella presenta una propuesta de promoción enfocada 100% en sus logros pasados y no en los dolores futuros de la alta dirección:", "A la Junta Directiva no le importa tu currículum, le importa su propia supervivencia financiera. Si tú fueras el CEO ahora mismo, ¿por qué ascenderte a ti mitigaría el riesgo operativo más urgente que tiene esta compañía hoy?"),
        ("Re-Ingeniería de la Propuesta de Ascenso", "Oblígala a borrar su discurso de ascenso y redactarlo utilizando el Triángulo Estratégico. Primer párrafo: 'La compañía está perdiendo X'. Segundo párrafo: 'Mi plan resuelve X generando Y de ahorro'. Tercer párrafo: 'Pido la autoridad para ejecutarlo'."),
        "Reestructurar completamente su currículum o plan de desarrollo individual, eliminando métricas de 'esfuerzo' y dejándolo 100% enfocado en alineación al KPI supremo del negocio."
    ),
    60: generate_playbook(
        ("Auditoría de Evolución Directiva", "Contempla el viaje. Ha superado la Carga Alostática, el Impostor, y el aislamiento político. Hoy se gradúa como una ejecutiva digna de ser Patrocinada en la élite."),
        ("El Despacho del Sponsor", "No habrá lecciones tácticas hoy. Entrarás a la reunión, validarás su contrato tácito y exigirás resultados. A partir de hoy, si ella pierde, tú pierdes."),
        ("El Próximo Horizonte", "En el Bloque 7 dejaremos la maquinaria interna y nos enfocaremos en proyectar su Marca Personal hacia la industria global. Pero primero, debes asegurar el acuerdo interno."),
        "El entrenamiento táctico está completo. Mañana evaluamos si tu nivel operativo justifica que yo apueste mi vida corporativa por ti en el próximo comité.",
        ("Para evaluar su comprensión final del nivel de lealtad estratégica que el Sponsorship le exige:", "A partir de hoy, yo asumo el riesgo de ser tu escudo y tu espada en los comités a los que no tienes acceso. Si te atacan, te cubriré. ¿Entiendes la responsabilidad operativa y táctica que adquieres al aceptar mi nombre como tu garantía corporativa?"),
        ("Auditoría del Patrocinio Activo", "Usen la Plantilla Invictus. Identifiquen juntas la 'Puerta Cerrada' exacta de la empresa a la que tú la vas a ayudar a infiltrarse en el próximo trimestre, usando tu influencia directa (El Triángulo Estratégico)."),
        "No requiere acciones en la empresa hoy. Requiere preparación psicológica para el Bloque 7: Marca Personal y Visibilidad de Mercado Global.",
        success=True
    )
}

days_data_list = []
for day in range(51, 61):
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
                badge: "Bloque 6 • Día {day-50}",
                title: "{title}",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

new_html = template

new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 6</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan')
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 6')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'DEL MENTORING AL SPONSORSHIP')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 6 • Día X')

pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque6_Premium.html successfully.")
