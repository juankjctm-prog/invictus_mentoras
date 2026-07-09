import re
import os

source_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque1_Premium.html"
source_md = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque7.md"
target_html = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque7_Premium.html"

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
    61: generate_playbook(
        ("Auditoría de Recompensa", "Identifica si tú misma sigues creyendo en el 'Síndrome de la Corona'. Si crees que trabajar duro en silencio es virtud, hoy despertarás a tu mentoreada hacia el precipicio político."),
        ("El Reclamo de Espacio", "Prepárate para empujarla a la luz. Si a ella le incomoda hablar de sus logros, recuerda que su comodidad no es tu prioridad; su éxito estructural sí lo es."),
        ("Postura de Directora de RRHH", "En la sesión de hoy tú eres la junta evaluadora. Si ella no sabe venderte sus KPIs, repruébala en el acto."),
        "Dejaremos de esperar que alguien descubra tu talento. Mañana auditamos el costo financiero de tu humildad corporativa.",
        ("Si ella dice que se siente 'arrogante' o 'presumida' enviando correos sobre el éxito de su equipo a la alta gerencia:", "Si mantienes en secreto las victorias tácticas de tu área porque tienes miedo de parecer arrogante, ¿no le estás robando a la empresa la oportunidad de replicar ese modelo de éxito a nivel global?"),
        ("El Hackeo de la Visibilidad", "Oblígala a redactar en tiempo real el 'Correo de Visibilidad'. Debe dirigirlo al VP de su área, marcando copia a un líder lateral. Primeras 3 líneas: El problema operativo masivo, la acción rápida de ella, y el dinero salvado."),
        "Enviar el correo redactado hoy mismo. Está prohibido utilizar palabras atenuantes como 'humildemente' o 'con un poco de suerte'."
    ),
    62: generate_playbook(
        ("Auditoría de Lenguaje", "Escucha tus propios correos leídos en voz alta. ¿Cuántos emojis de carita feliz usas para suavizar una orden técnica? Corta el ritual de equidad de raíz."),
        ("El Doble Vínculo Asumido", "Acepta que a veces no le caerás bien a todos cuando des órdenes. La simpatía no te asciende; el respeto al perímetro de tu autoridad sí."),
        ("El Filtro del Sistema", "Prepárate para enseñarle a canalizar su agresión y firmeza hacia la 'protección de la empresa' para neutralizar la penalización."),
        "Si tu comunicación sigue disculpándose antes de exigir resultados, nunca te verán como directora. Mañana blindamos tu asertividad.",
        ("Cuando ella suaviza una exigencia operativa diciendo 'Oigan, si no es molestia, ¿podemos revisar la métrica?':", "Si fueras el CEO protegiendo tu patrimonio, ¿pedirías permiso para auditar una métrica que está sangrando la rentabilidad del mes, o lo exigirías como una directriz innegociable por el bien del negocio?"),
        ("Enmarcado Organizacional (Role Play)", "Ella es la Gerente exigiendo resultados a un equipo rebelde. Haz que practique el guion 3 veces: Suprimiendo el pronombre 'Yo' y usando 'Para proteger la meta de Q3 del Directorio, esto debe entregarse a las 5pm'."),
        "La próxima vez que envíe un correo de exigencia logística, debe usar el Enmarcado Organizacional y eliminar todas las palabras atenuantes ('tal vez', 'creo', 'un poquito')."
    ),
    63: generate_playbook(
        ("Auditoría Fisiológica", "Siéntate derecha ahora mismo. Tu cuerpo está enviando señales a tu cerebro de sumisión o dominio. Calibra tu testosterona y cortisol antes de que ella entre a la sesión."),
        ("Lectura de Siluetas", "Hoy no escucharás lo que ella dice; observarás cuánto espacio físico ocupa en la cámara o en la silla. Si se encoge al hablar de sus logros, detén la sesión."),
        ("La Postura del Sponsor", "No le pidas que se expanda; modélalo. Ocupa tú la pantalla, habla con volumen bajo pero firme. Proyecta gravedad."),
        "El liderazgo no empieza en tus palabras, empieza en tu neuroquímica. Mañana te enseño a hackear tu biología antes de las reuniones.",
        ("Cuando ella cruza los brazos o se encoge físicamente al explicar un proyecto de alto impacto:", "Detente. Mira cómo está tu cuerpo en este instante. Si me estás pidiendo un millón de dólares de presupuesto corporativo con la postura de alguien que pide disculpas por existir, ¿crees que mi amígdala va a confiar en ti?"),
        ("El Re-Cableado Postural", "Haz que se ponga de pie. Postura expansiva por 2 minutos (Superman/WonderWoman) respirando profundo. Luego hazle la misma pregunta de negocios. Nota la caída del timbre de voz y la desaparición de las muletillas."),
        "Antes de su próxima reunión crítica (virtual o presencial), debe pasar 3 minutos exactos sola en expansión postural, y entrar a la junta manteniendo contacto visual asimétrico con el líder."
    ),
    64: generate_playbook(
        ("Auditoría de Impacto", "¿Tus presentaciones también aburren al Directorio? Si muestras 20 diapositivas de historia antes del KPI, estás sobrecargando su Sistema 2."),
        ("Sintonización del Instinto", "Prepárate para destrozar la presentación de tu mentoreada. El Sistema 1 de los VP solo reacciona al dinero, al riesgo y al estatus. Enséñale a golpear ahí."),
        ("El Veto a la Paja", "No le permitas justificar por qué su Excel es tan detallado. A la Junta no le importa su esfuerzo; le importa su resultado."),
        "Tus presentaciones son muy técnicas y los VP se desconectan a los 5 minutos. Mañana aprendemos a hackear su atención primaria.",
        ("Si ella insiste en explicar todo el contexto técnico de la auditoría en los primeros 10 minutos de la junta:", "El Sistema Límbico de un Director General que ha tomado 50 decisiones hoy, a las 4 de la tarde, está agotado. Si en los primeros 30 segundos no le dices si este proyecto le hará ganar dinero o evitar una demanda, ¿por qué creería que vale la pena encender su córtex prefrontal para escucharte?"),
        ("La Cirugía B.L.U.F. (Bottom Line Up Front)", "Haz que abra la última presentación PPT que envió. Oblígala a mover la diapositiva final (La Conclusión Financiera y la Petición de Capital) para que sea estrictamente la primera diapositiva de la presentación."),
        "El próximo resumen ejecutivo o documento que envíe hacia arriba debe seguir el estándar militar BLUF: La conclusión/impacto exacto va en el primer párrafo del correo."
    ),
    65: generate_playbook(
        ("Auditoría de Narrativa", "¿Puedes contar el último éxito de tu equipo con arco narrativo (conflicto, acción, triunfo) en menos de 60 segundos?"),
        ("El Diseño del Oxitocina", "Reconoce que a los humanos nos aburren los números sin alma. Tu trabajo hoy es forzar a tu ejecutiva técnica a convertirse en una 'Storyteller' de la rentabilidad."),
        ("Eliminación de Arrogancia", "Contar la historia no es decir 'soy genial y los salvé'. Es decir 'enfrentamos el abismo operativo y así es como rediseñamos los motores'."),
        "A nadie le importan tus números fríos en un Excel. Mañana te enseño cómo inyectarles vida y química para que no te olviden.",
        ("Cuando ella entregue un KPI final ('logramos 15% de reducción de accidentes') sin contexto emocional o fricción previa:", "Si yo te digo que gané un partido 1-0 sin oposición, bostezo. Si te digo que íbamos perdiendo 3-0 en el segundo tiempo, cambiamos la táctica, hubo un jugador lesionado y logramos el 4-3 en el último minuto, tienes mi lealtad. ¿Dónde está el conflicto operativo de ese KPI que me acabas de dar?"),
        ("El Laboratorio Zak", "Haz que redacte el 'Pitch del Trimestre'. Debe empezar detallando la crisis o el riesgo inminente (Cortisol), luego describir su intervención técnica (Agencia), y cerrar con el ahorro o eficiencia lograda (Oxitocina)."),
        "En su próxima presentación de resultados frente a su jefe, no puede empezar con la tabla de datos. Debe abrir usando un arco narrativo del peor momento del proyecto y cómo lo resolvió."
    ),
    66: generate_playbook(
        ("Auditoría de Reclamación", "Si eres honesta, ¿has estado escondiéndote detrás del 'equipo' para no asumir la responsabilidad aplastante del liderazgo solitario?"),
        ("Validación del 'Pivot'", "Hoy le darás a tu mentoreada el escudo político perfecto. Usar al equipo como vehículo de promoción la protege del likability penalty. Es manipulación sociológica pura."),
        ("El Tono Inflexible", "No dejes que se disculpe al reclamar la autoría intelectual ('fui yo pero...'). Exige firmeza vocal."),
        "Tu humildad te está robando crédito frente al comité de sucesión. Mañana aprendemos el pivote táctico para reclamar autoría sin que te ataquen.",
        ("Si ella se niega a tomar el crédito individual del proyecto porque siente que 'traiciona' a su equipo de ingenieros operativos:", "Si tú no reclamas la propiedad intelectual y el liderazgo estratégico de este diseño en la Junta, el Vicepresidente asumirá que fue un 'esfuerzo orgánico' y nadie, ni tú ni tu equipo, recibirá el presupuesto para el próximo año. ¿Estás sacrificando la viabilidad de tu departamento por un falso sentido de 'humildad'?"),
        ("La Prueba del Pivot", "Practica el 'We-to-I' Pivot en voz alta. Ella: 'El equipo trabajó 50 horas, lo que me permitió validar la hipótesis de eficiencia global que diseñé para este P&L'. Haz que lo repita sin bajar la mirada."),
        "Enviar un correo Post-Mortem de un proyecto cerrado a sus superiores, utilizando el enmarque de 'Transferencia de Conocimiento' para publicitar una idea propia brillante bajo la excusa de 'educar' a las demás áreas."
    ),
    67: generate_playbook(
        ("Auditoría Feynman (Mentalidad de Patrocinadora)", "¿Puedes unir todos los puntos? Postura de poder -> Sistema 1 -> BLUF -> Oxitocina -> Pivot. El engranaje de persuasión es neurobiología, no magia."),
        ("Diagnóstico Letal", "Tu mentoreada ya no es novata. Hoy le exiges la teoría completa. No aceptes respuestas cortas ni vacilaciones. Si duda, es que el sistema no está asimilado en su subconsciente."),
        ("El Silencio Estructural", "Durante el recall activo hoy, haz preguntas duras y mantén el silencio estratégico (Bloque 2) por 10 segundos para ver cómo maneja el estrés bajo la presión de la mentora."),
        "El Checkpoint de persuasión está aquí. Mañana debes conectar postura, neuroquímica y sociología corporativa frente a mí sin dudar.",
        ("Si ella no logra integrar cómo la postura expansiva (Cuddy) es un requisito previo para poder hackear la atención del directorio (Kahneman) mediante el BLUF:", "Si tienes el mejor correo B.L.U.F del mundo y la historia más intensa de conflicto operativo, pero te sientas en la junta con el cuello encogido, cruzada de brazos, disculpándote y secretando cortisol... ¿Qué señal biológica recibe el Sistema 1 del Vicepresidente, por encima de todos tus datos lógicos?"),
        ("Simulación Feynman Ejecutiva", "Ella debe explicar el ecosistema de la 'Visibilidad Estructural'. De pie, postura expansiva, proyectando la voz como si le diera una charla TED a los gerentes de Tecna. Evalúa ritmo, aplomo y falta de atenuantes."),
        "Ejecutar y documentar (grabar o escribir) su auto-presentación o 'Elevator Pitch' combinando B.L.U.F, el arco de Oxitocina y la reclamación táctica del Pivot 'We-to-I'."
    ),
    68: generate_playbook(
        ("Auditoría de Marca Propia", "Antes de entrar a la sesión, piensa: ¿Si te despiden hoy, la industria B2B de tu país sabe exactamente qué problema resuelves a nivel directivo?"),
        ("El Diagnóstico de Estancamiento", "Acepta que tu mentoreada puede ser la mejor operadora del mundo, pero si no la asocian con el futuro estratégico del negocio (su Marca), no la van a patrocinar."),
        ("El Despertar", "Hoy la vas a forzar a escoger un nicho de autoridad innegociable. No la dejes usar la palabra 'liderazgo' sin adjuntarle una métrica dura (financiera, operaciones, riesgo)."),
        "Hacer tu trabajo perfecto te da un sueldo; tener una marca corporativa letal te da un ascenso directivo. Mañana definiremos quién eres.",
        ("Cuando ella no pueda diferenciar entre su Reputación operativa ('todos saben que no fallo') y su Marca estratégica ('por esto me pagarían el doble mañana'):", "Si el CEO de la competencia nos llamara mañana, tu reputación diría que eres una empleada confiable. Pero, ¿cuál es la tesis técnica y de innovación específica que TÚ defiendes en esta industria por la cual ese CEO justificaría pagar tu liquidación y triplicar tu sueldo?"),
        ("El Laboratorio de Marca B2B", "Oblígala a rellenar el espacio: 'Yo soy la ejecutiva que transforma el caos operativo en [Ventaja competitiva X] a través de la optimización del proceso de [Métrica dura Y]'. Pulir hasta que suene a Vicepresidencia."),
        "Debe actualizar su perfil de LinkedIn corporativo y su biografía en la intranet, erradicando adjetivos genéricos ('dinámica, proactiva') y reemplazándolos por su nueva tesis de Marca B2B P&L."
    ),
    69: generate_playbook(
        ("Auditoría de Blindaje", "¿Alguna vez alguien a quien patrocinaste se derrumbó en el comité porque nadie la preparó para el ataque directo? Hoy la vacunarás contra el pánico."),
        ("El Disfraz del Villano (Red Teaming)", "La mentoría tierna termina hoy. Para asegurar su supervivencia en el Bloque 7, en la sesión de hoy debes encarnar la peor pesadilla corporativa de ella. Frialdad absoluta."),
        ("El Monitoreo de Quiebre", "Atácala en el simulacro, pero no dejes que su identidad se fracture. Si su amígdala colapsa, pausa, hazla respirar y recablear su respuesta hacia el 'Enmarcado Organizacional'."),
        "Mañana voy a ser implacable contigo en un simulacro a puerta cerrada. Prepárate para defender tu proyecto más grande del trimestre. No tendré piedad.",
        ("Si ella se ofende, se calla o intenta justificarse emocionalmente ante el ataque brutal de tu simulacro de Red Teaming:", "[Pausa el simulacro]. Acabas de perder la junta. Tu amígdala acaba de secuestrar tu córtex prefrontal porque tomaste el cuestionamiento técnico de mis números como un ataque personal. Respira. Expande tu cuerpo. ¿Cómo me atacas de vuelta usando el Enmarcado Organizacional y la lógica del negocio?"),
        ("El Horno Hipobárico (Simulacro)", "Arranca el Red Teaming sin aviso. Ella empieza su presentación. En la diapositiva 2, interrúmpela: 'Tus números operativos del trimestre pasado no respaldan esta proyección absurda. Defiéndelo en 60 segundos'. Mide su reacción biológica."),
        "Recuperación fisiológica. Debe escuchar una meditación o audiolibro desconectado del trabajo por 20 minutos para bajar la carga de cortisol residual producida por el Red Teaming."
    ),
    70: generate_playbook(
        ("Auditoría Final de Patrocinio", "Contempla a tu mentoreada. Entró a este programa pidiendo consejos logísticos. Hoy la miras a los ojos y sabes que puede sostener la mirada de cualquier Vicepresidente."),
        ("El Pase de Antorcha", "Acepta que tu trabajo táctico pesado terminó. En el Checkpoint 7 cierras la etapa de intervención. A partir del Bloque 8, entrará la etapa del Legado. Es la ceremonia de graduación corporativa."),
        ("Postura de Matriarca", "Mantén el rigor. Revisa la Plantilla Invictus con ella. Ella es el producto de tu capital político, y ella ahora es un arma letal en la empresa."),
        "Llegamos al final del diseño táctico. Mañana auditamos tu Marca Personal y validamos si estás lista para el nivel global de la Alta Dirección.",
        ("Para evaluar su transformación identitaria de operadora técnica a ejecutiva de visibilidad global:", "Sabiendo cómo operan el Doble Vínculo (likability penalty), el Tokenismo y el Impuesto Invisible contra ti, ¿cuál es tu plan de Visibilidad Estructural inquebrantable para los próximos 6 meses que garantizará que tu nombre esté en la mesa de decisiones, aunque no te inviten formalmente?"),
        ("Revisión de la Plantilla Estratégica", "Usa la 'Campaña de Visibilidad Ejecutiva' (Plantilla Invictus). Validen que su marca técnica esté pulida, que haya eliminado atenuantes verbales, y que tenga claro su próximo 'Correo B.L.U.F' hacia el poder central. Este es su mapa de ruta post-programa."),
        "Debe organizar y agendar en las próximas dos semanas una reunión lateral '1 a 1' con alguien de muy alto rango con el único propósito de transferir inteligencia estratégica y asegurar visibilidad pura.",
        success=True
    )
}

days_data_list = []
for day in range(61, 71):
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
                badge: "Bloque 7 • Día {day-60}",
                title: "{title}",
                readingHTML: `
{reading_html}
                `,
                playbook: `{playbook_str}`
            }}"""
    days_data_list.append(day_obj)

days_data_array_str = "[\n" + ",\n".join(days_data_list) + "\n        ];"

new_html = template

new_html = new_html.replace("<title>Invictus Mind Premium - Bloque 1</title>", "<title>Invictus Mind Premium - Bloque 7</title>")
new_html = new_html.replace('onclick="window.location.href=\'index.html\'">Volver al Master Plan', 'onclick="window.location.href=\'index.html\'">Volver al Master Plan')
new_html = new_html.replace('BLOQUE 1', 'BLOQUE 7')
new_html = new_html.replace('EL PODER DEL SILENCIO Y LA POSTURA', 'VISIBILIDAD, MARCA E INFLUENCIA')
new_html = new_html.replace('Bloque 1 • Día X', 'Bloque 7 • Día X')

pattern = re.compile(r'const daysData = \[\s*\{([\s\S]+?)\];', re.DOTALL)
new_html = pattern.sub('const daysData = ' + days_data_array_str, new_html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Created Bloque7_Premium.html successfully.")
