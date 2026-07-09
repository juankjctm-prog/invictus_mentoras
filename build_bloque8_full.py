import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque8.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque8_Premium.html"

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
    71: generate_playbook(
        ("Auditoría de Cierres Pasados", "Revisa cómo han terminado tus relaciones profesionales pasadas. ¿Tiendes a desaparecer o a mantener dependencias eternas? Escribe tu patrón y decide romperlo."),
        ("El Duelo del Control Corporativo", "Acepta que a partir de mañana ya no serás el faro exclusivo. Escribe: 'Su autonomía absoluta es mi mayor victoria'."),
        ("Calibración de Autoridad Desvinculada", "Respira profundo y visualiza esta sesión no como un adiós, sino como el corte del cordón umbilical operativo."),
        "Mañana es nuestra sesión de Cierre Táctico. Ven preparada para cortar el cordón umbilical corporativo.",
        ("Inicia la sesión declarando el fin de su etapa de aprendiz. Lanza la pregunta de alto calibre:", "Si yo desapareciera mañana de la industria, ¿quién hereda tu lealtad estratégica?"),
        ("El Mapa de Transferencia de Poder", "Haz que trace en una hoja quiénes serán sus 3 nuevos consejeros tácticos con quienes validará decisiones de alto riesgo, ahora que tú ya no estarás."),
        "Prohíbele explícitamente enviarte dudas logísticas durante los próximos 30 días. Solo responderás sobre Alta Estrategia."
    ),
    72: generate_playbook(
        ("Auditoría de Asimetría de Poder", "Reconoce si tienes resistencia a ver a tu mentoreada como una igual. El ego del mentor prefiere mantener a la estudiante pequeña. Rompe esto."),
        ("Confrontación del Ego de Experto", "Acepta que hoy tú serás la evaluada. Prepárate para recibir críticas duras de alguien que hace 70 días era tu aprendiz."),
        ("Selección de Vulnerabilidad Táctica", "Elige un problema REAL y actual de tu propia agenda corporativa que aún no hayas resuelto. Este será el caso que le presentarás."),
        "Tengo un problema complejo con la estrategia de mi área. Necesito tu cerebro mañana. Cero condescendencia.",
        ("Preséntale tu problema real y lanza la pregunta que rompe definitivamente la asimetría de poder:", "¿Qué riesgo crítico estoy obviando en este plan por mi propia ceguera de taller?"),
        ("Inversión de Roles de Auditoría", "Cállate y escúchala durante 10 minutos ininterrumpidos. Toma notas. Oblígala a justificar sus puntos débiles encontrados en tu estrategia."),
        "Debes implementar públicamente al menos 1 aspecto del consejo que ella te dio, y darle el crédito absoluto en tu propia junta directiva."
    ),
    73: generate_playbook(
        ("Auditoría de Sistemas", "Observa tu empresa no como personas, sino como un sistema de engranajes. Tu trabajo con ella acaba de cambiar un engranaje. Mide el impacto sistémico."),
        ("Aceptación del Efecto Mariposa", "Reconoce que al empoderar a una líder, estás afectando a todo su equipo subordinado de manera indirecta."),
        ("El Cambio de Paradigma", "Hoy tu sesión no tratará de ella. Tratará de cómo ella va a cambiar la cultura de las personas que ella dirige."),
        "Tú ya dominaste tu rol. Mañana veremos cómo vas a obligar a toda tu área a operar bajo el mismo nivel de excelencia sistémica.",
        ("Si ella duda del impacto que puede tener en su equipo completo, oblígala a ver la red:", "Ahora que tú no aceptas mediocridad de ti misma, ¿cuál es el primer comportamiento de tu propio equipo que vas a dejar de tolerar inmediatamente?"),
        ("El Mapa de Impacto Sistémico", "Oblígala a hacer una lista de las 3 dinámicas de su equipo que cambiarán a partir del lunes gracias a su nuevo nivel de rigor operativo."),
        "Tiene 24 horas para tener una junta con su equipo directo e instalar una nueva regla de 'No Excusas Operativas', subiendo el estándar colectivo."
    ),
    74: generate_playbook(
        ("Auditoría de Kotter", "Kotter dice que los cambios mueren al final. ¿Has documentado el éxito de ella para anclarlo en la cultura corporativa?"),
        ("Institucionalizar el Mérito", "Tu trabajo hoy es diseñar cómo vas a vender el éxito de ella a la Junta Directiva para que este modelo se replique."),
        ("Preparación del Pitch de Sponsorship", "Define la métrica exacta que ella mejoró y cómo la usarás como munición política en la próxima reunión de VPs."),
        "Mañana diseñaremos cómo vamos a usar tus resultados para forzar a la organización a cambiar sus políticas de talento.",
        ("Si ella no entiende por qué sus números importan a nivel cultura, enmárcalo macro:", "Si yo muestro tus resultados del Q3 a la Junta, ¿qué nueva regla de ascenso crees que se verán obligados a aprobar para las demás ejecutivas?"),
        ("Diseño del Escudo Corporativo", "Creen juntas la narrativa de su éxito. Debe ser irrefutable, basada en datos, y estructurada para que ningún VP pueda atribuirlo a la 'suerte'."),
        "Debe enviarte (y al director del área) un informe oficial de cierre de trimestre que valide matemáticamente su nueva eficiencia operativa."
    ),
    75: generate_playbook(
        ("Auditoría del Linaje", "Mira hacia abajo en el organigrama. ¿Quién es la analista más brillante que está siendo asfixiada por el sistema ahora mismo? Esa es tu nueva misión."),
        ("El Antídoto a la Abeja Reina", "Reafirma tu promesa de que en esta empresa, el talento femenino se protege en bloque, no en aislamiento."),
        ("La Imposición del Semillero", "Hoy vas a cobrarle a tu mentoreada el costo de tu inversión en ella. Le vas a exigir que se convierta en Sponsor."),
        "Mañana me vas a pagar el tiempo que he invertido en ti. Y no será con agradecimientos. Será con tu propio liderazgo.",
        ("Cuando intente decir que 'aún no está lista para ser mentora', destrúyelo con hechos:", "Yo no te pregunto si te sientes lista. Te ordeno que escojas a la analista más brillante de tu piso y empieces a protegerla políticamente. ¿Quién es y por qué ella?"),
        ("El Semillero Obligatorio", "Haz que seleccione un nombre específico de una mujer joven en la empresa. Analicen juntas su potencial y definan cómo ella la va a intervenir."),
        "Debe invitar a almorzar a la analista seleccionada esta misma semana e iniciar informalmente el traspaso de inteligencia corporativa."
    ),
    76: generate_playbook(
        ("Auditoría de ROI", "Suma las horas invertidas. ¿Cuál es el retorno financiero para la empresa de no haber perdido a esta ejecutiva por burnout? Ten el número claro."),
        ("Mentalidad Financiera", "No evalúes la mentoría con emociones. Evalúala con la retención de talento crítico y la aceleración de toma de decisiones."),
        ("Preparación del Reporte B2B", "Estructura la Triada B2B: Retención, Decisiones y Capital. Ella debe entender el valor en dinero que acaba de sumar a la empresa."),
        "Mañana cerramos los números. Vamos a cuantificar financieramente cuánto dinero le ahorramos a la empresa con tu evolución.",
        ("Si se siente incómoda tasando su valor en millones de dólares ahorrados o generados:", "Si fueras una máquina que lograra esta eficiencia, te tasarían en 5 millones. Como eres mujer, quieres decir que 'hiciste tu trabajo'. Cuantifícame tu impacto ahora mismo en dólares."),
        ("La Matriz de Valor Ejecutivo", "Oblígala a llenar una matriz de 3 columnas: Costo de su reemplazo, horas ahorradas por su autonomía, y dinero generado por sus iniciativas. Este es su escudo político."),
        "Anotar en su evaluación de desempeño anual (o enviarlo a RRHH) las 3 métricas de ROI demostrable que han discutido en la sesión."
    ),
    77: generate_playbook(
        ("Síntesis Maestra", "Hoy es la validación total. Repasa la arquitectura del liderazgo: desde la seguridad psicológica hasta el modelo de Kotter. Ella debe dominarlo."),
        ("El Silencio del Maestro", "Hoy tú no enseñas nada. Hoy tú exiges que ella te explique la matriz completa del poder. Si falla, el programa no fue asimilado."),
        ("Calibración del Tribunal", "Asume el rol de la junta de accionistas. No muestres empatía durante su prueba; muestra exigencia directiva."),
        "Este es tu examen final. Mañana me presentarás el plano arquitectónico del liderazgo corporativo como si yo fuera un inversionista hostil.",
        ("Si ella omite la parte de la neurobiología o la política dura:", "Si solo me hablas de 'liderazgo empático', acabas de perder el financiamiento. Conecta cómo la postura física y el candor duro aseguran la rentabilidad. Tienes un minuto. Go."),
        ("Simulación de Defensa Directiva", "Ella se pone de pie. Tiene 5 minutos para defender la tesis del Liderazgo Invictus aplicada a su división. Mide su fluidez, asertividad y anclaje de conceptos."),
        "Grabar un audio de 3 minutos haciendo el Pitch del Liderazgo Invictus y guardarlo para sí misma como recordatorio de su capacidad analítica."
    ),
    78: generate_playbook(
        ("La Medición del Legado", "Revisa el impacto colateral. ¿Cuántos equipos indirectos mejoraron gracias a la transformación de tu mentoreada? Cuantifica tu impacto."),
        ("Aceptación del Fuego", "Asume tu nuevo rol como constructora de las líderes de la próxima década. Este es el pináculo de la autoridad."),
        ("Estado de Presencia Absoluta", "Entra a la sesión final sin laptop y sin celular. Solo tú y ella. Presencia ejecutiva pura para anclar el ritual."),
        "Mañana es tu graduación Invictus. Ven lista para asumir tu lugar en la mesa de poder definitivo.",
        ("Llama a tu protegida a territorio neutral. Mírala a los ojos y lanza la pregunta vitalicia:", "Ahora que tienes el poder estructural, ¿a qué mujer joven en las trincheras vas a bajar a rescatar mañana?"),
        ("El Juramento del Linaje", "Oblígala a verbalizar que su deuda no se paga con gracias, sino sometiendo a otra mujer brillante al mismo nivel de excelencia que vivieron ustedes."),
        "Debe elegir dentro de los próximos 3 meses a su primera mentoreada formal y convertirse en el origen de un nuevo nodo de poder femenino.",
        success=True
    )
}

days_data_list = []
for day in range(71, 79):
    # Regex to extract each day from Bloque8.md
    # the last day (78) might not have a day 79 after it, so we handle it.
    if day < 78:
        day_pattern = re.compile(rf'DÍA {day}\s+(.+?)(?=DÍA {day+1}|$)', re.DOTALL)
    else:
        day_pattern = re.compile(rf'DÍA 78\s+(.+?)(?=FIN DEL MASTER TRACK|$)', re.DOTALL)
        
    match = day_pattern.search(md_content)
    if not match:
        print(f"Failed to find DÍA {day}")
        continue
        
    day_content = match.group(0)
    title_match = re.search(rf'DÍA {day}\s+(.+?)\n', day_content)
    title = title_match.group(1).strip()
    
    reading_match = re.search(r'FASE 2 — LECTURA CRONOMETRADA.*?(\n\n.+?)(?=\n📖\s*FASE 3)', day_content, re.DOTALL)
    if reading_match:
        reading_raw = reading_match.group(1).strip()
    else:
        # Fallback
        reading_raw = "Contenido de lectura magistral."
    
    paragraphs = reading_raw.split('\n')
    reading_html = ""
    for i, p in enumerate(paragraphs):
        p = p.strip()
        if not p: continue
        if i == 0:
            reading_html += f"                        <h3 style=\"color: var(--accent-water); font-size: 1.1rem; margin-bottom: 12px;\">{p}</h3>\n"
        else:
            reading_html += f"                        <p>{p}</p>\n"
            
    # Try to extract questions if they exist
    q_literal = "En base al texto, enumera los puntos principales."
    q_infer = "Deduzca la intención estratégica detrás de las acciones mencionadas."
    q_opcion = "Aplica el concepto a un caso real en tu área de influencia."
    q_personal = "Piensa en tu propia carrera. ¿Cómo te afecta directamente esta teoría?"
    
    try:
        q_literal = re.search(r'\[Literal\](.*?)\n', day_content).group(1).strip()
    except: pass
    try:
        q_infer = re.search(r'\[Inferencial\](.*?)\n', day_content).group(1).strip()
    except: pass
    try:
        q_opcion = re.search(r'\[Opción múltiple\](.*?)\n', day_content).group(1).strip()
    except: pass
    
    # For day 78 the question block is different
    if day == 78:
        try:
            q_personal = re.search(r'\[Metacognición Abierta y Soberana\](.*?)\n(.*?)(?=\n🧠)', day_content, re.DOTALL).group(2).strip()
            q_literal = "Reflexión Soberana"
            q_infer = "Interiorización"
            q_opcion = "Asimilación del Legado"
        except: pass
    else:
        try:
            q_personal = re.search(r'\[Conexión personal\](.*?)\n', day_content).group(1).strip()
        except: 
            try:
                # If it spans lines
                q_personal = re.search(r'\[Conexión(.*?)\n(.*?)(?=\n🧠)', day_content, re.DOTALL).group(2).strip()
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
    
    # The theme color for Day 78 should be success, others standard
    theme_prop = 'theme: "success",' if day == 78 else ''
    
    day_obj = f"""
            {{
                id: {day},
                badge: "Bloque 8 • Día {day}",
                title: "{title}",
                desc: "Legado, Cultura y Sostenibilidad",
                {theme_prop}
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

# We use Bloque1_Premium as template to reconstruct it correctly
new_html = template

new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 8</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan')
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 8')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'LEGADO, CULTURA Y SOSTENIBILIDAD')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 8 • Día X')

# Also the initial badge says "B1" and "El Arquitecto del Silencio", let's fix it for Bloque 8
new_html = new_html.replace('>B1<', '>B8<')
new_html = new_html.replace('>El Arquitecto del Silencio<', '>El Cierre Maestro<')

pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

# Since we use Bloque1_Premium, we might need to apply the JS fixes
new_html = new_html.replace('${day.desc}', '${day.desc || "Estrategia Avanzada"}')

old_chunk = """            data.recall.forEach((r, idx) => {
                recallHTML += `
                    <div style="margin-bottom: 16px; background: rgba(255,94,0,0.05); border: 1px dashed rgba(255,94,0,0.3); padding: 16px; border-radius: 12px;">
                        <span style="font-size: 0.75rem; color: var(--accent-fire); text-transform: uppercase;">${r.type}</span>
                        <p style="font-size: 0.9rem; margin: 8px 0; color: white;">${r.q}</p>
                        <textarea class="input-premium" placeholder="Escribe tu respuesta analítica..."></textarea>
                    </div>
                `;
            });"""
            
new_chunk = """            if (data.recall) {
                data.recall.forEach((r, idx) => {
                    recallHTML += `
                        <div style="margin-bottom: 16px; background: rgba(255,94,0,0.05); border: 1px dashed rgba(255,94,0,0.3); padding: 16px; border-radius: 12px;">
                            <span style="font-size: 0.75rem; color: var(--accent-fire); text-transform: uppercase;">${r.type}</span>
                            <p style="font-size: 0.9rem; margin: 8px 0; color: white;">${r.q}</p>
                            <textarea class="input-premium" placeholder="Escribe tu respuesta analítica..."></textarea>
                        </div>
                    `;
                });
            }"""
new_html = new_html.replace(old_chunk, new_chunk)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque8_Premium.html successfully with full 71-78 days.")
