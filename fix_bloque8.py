import re

file_path = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque8_Premium.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# DAY 71
pb71 = """
                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-water); margin-top: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)
                    </div>
                    <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.6;">El cierre es la fase más crítica. Debes prepararte emocionalmente para soltar el control.</p>
                    
                    <div class="note-item" style="border-left: 2px solid var(--accent-water);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">1. Auditoría de Cierres Pasados</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Revisa cómo han terminado tus relaciones profesionales pasadas. ¿Tiendes a desaparecer (Ghosting corporativo) o a mantener dependencias eternas? Escribe tu patrón y decide romperlo hoy.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">2. El Duelo del Control Corporativo</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Acepta que a partir de mañana ya no serás el faro exclusivo de esta ejecutiva. Escribe en tu cuaderno: "Su autonomía absoluta es mi mayor victoria como mentora".</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #9370DB;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">3. Calibración de Autoridad Desvinculada</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Respira profundo 3 veces y visualiza la sesión de hoy no como un adiós, sino como la ceremonia donde cortas el cordón umbilical operativo.</p>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-water); margin-top: 40px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        PASO 2: GUÍA DE LA SESIÓN 1-A-1
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">A. Ancla (WhatsApp 24h antes)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;"><em>"Mañana es nuestra sesión de Cierre Táctico. Ven preparada para cortar el cordón umbilical corporativo."</em></p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">B. Coaching Socrático (Profundo)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Inicia la sesión declarando el fin de su etapa de aprendiz. Lanza la pregunta de alto calibre:</p>
                        <div style="padding: 12px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-top: 10px; font-style: italic; color: #FFF;">
                            "Si yo desapareciera mañana de la industria, ¿quién hereda tu lealtad estratégica?"
                        </div>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--success);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">I. El Mapa de Transferencia de Poder</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Haz que trace en una hoja quiénes serán sus 3 nuevos consejeros tácticos (sus pares o superiores) con quienes validará decisiones de alto riesgo, ahora que tú ya no estarás disponible operativamente.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700; background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">II. Asignación de Riesgo Definitivo</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Prohíbele explícitamente enviarte dudas logísticas u operativas durante los próximos 30 días. Solo le responderás sobre Alta Estrategia Directiva. El silencio es crecimiento.</p>
                    </div>
"""

# DAY 72
pb72 = """
                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-water); margin-top: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)
                    </div>
                    
                    <div class="note-item" style="border-left: 2px solid var(--accent-water);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">1. Auditoría de Asimetría de Poder</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Reconoce internamente si tienes resistencia a ver a tu mentoreada como una igual. El ego del "mentor" a veces prefiere mantener a la estudiante pequeña. Rompe esto conscientemente.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">2. Confrontación del Ego de Experto</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Acepta que hoy tú serás la evaluada. Prepárate para recibir críticas duras de parte de alguien que hace 70 días era tu aprendiz.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #9370DB;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">3. Selección de Vulnerabilidad Táctica</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Elige un problema REAL y actual de tu propia agenda corporativa que aún no hayas resuelto. Este será el caso que le presentarás.</p>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--accent-water); margin-top: 40px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        PASO 2: GUÍA DE LA SESIÓN 1-A-1
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">A. Ancla (WhatsApp 24h antes)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;"><em>"Tengo un problema complejo con el presupuesto/estrategia de mi área. Necesito tu cerebro mañana. Cero condescendencia."</em></p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--border-glow); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">B. Coaching Socrático (Vulnerabilidad)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Preséntale tu problema real y lanza la pregunta que rompe definitivamente la asimetría de poder:</p>
                        <div style="padding: 12px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-top: 10px; font-style: italic; color: #FFF;">
                            "¿Qué riesgo crítico estoy obviando en este plan por mi propia ceguera de taller?"
                        </div>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--success);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">I. Inversión de Roles de Auditoría</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Cállate y escúchala durante 10 minutos ininterrumpidos. Toma notas de lo que te dice. Oblígala a justificar sus puntos débiles encontrados en tu estrategia.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700; background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">II. Asignación de Riesgo Táctico</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Debes implementar públicamente al menos 1 aspecto del consejo que ella te dio, y darle el crédito absoluto en tu propia junta directiva frente a otros líderes.</p>
                    </div>
"""

# DAY 78
pb78 = """
                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--success); margin-top: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        PASO 1: TU PREPARACIÓN (AUTO-MAESTRÍA)
                    </div>
                    
                    <div class="note-item" style="border-left: 2px solid var(--success);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">1. La Medición del Legado</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Revisa el impacto colateral. ¿Cuántos equipos indirectos mejoraron gracias a la transformación de tu mentoreada? Cuantifica el impacto de haber dedicado tu tiempo a esto.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">2. Aceptación del Fuego</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Asume tu nuevo rol no solo como ejecutiva de operaciones, sino como constructora de las líderes de la próxima década. Este es el pináculo de la autoridad corporativa.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #9370DB;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">3. Estado de Presencia Absoluta</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Entrarás a la sesión final sin laptop, sin celular y sin notas. Solo tú y ella. Presencia ejecutiva pura para anclar el ritual final en su neurobiología.</p>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--success); margin-top: 40px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        PASO 2: GUÍA DE LA SESIÓN 1-A-1
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--success); background: rgba(16,185,129,0.03);">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">A. Ancla (WhatsApp 24h antes)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;"><em>"Mañana es tu graduación Invictus. Ven lista para asumir tu lugar en la mesa de poder definitivo."</em></p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid var(--success); background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">B. Coaching Socrático (Legado)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Llama a tu protegida a territorio neutral. Mírala a los ojos y lanza la pregunta vitalicia:</p>
                        <div style="padding: 12px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-top: 10px; font-style: italic; color: #FFF;">
                            "Ahora que tienes el poder estructural, ¿a qué mujer joven en las trincheras vas a bajar a rescatar mañana?"
                        </div>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700;">
                        <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px;">I. El Juramento del Linaje</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Oblígala a verbalizar en voz alta que su deuda contigo no se paga dándote las gracias o regalos, sino sometiendo a otra mujer brillante al mismo nivel de excelencia implacable que vivieron ustedes.</p>
                    </div>

                    <div class="note-item" style="border-left: 2px solid #FFD700; background: transparent;">
                        <h3 style="color: white; font-size: 0.95rem; margin-bottom: 8px;">II. Asignación de Riesgo Táctico (Vitalicio)</h3>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6;">Debe elegir dentro de los próximos 3 meses a su primera mentoreada formal y convertirse ella misma en el origen de un nuevo nodo de poder femenino.</p>
                    </div>
"""

# Extract daysData array
match = re.search(r'const daysData = \[\s*\{([\s\S]+?)\];', content)
if match:
    days_data_str = match.group(0)
    
    # We replace playbook sections using a regex that finds playbook: `...` for each id
    # Since we know the order is 71, 72, 78, we can just split by 'id: ' and replace playbook: `...`
    
    def replacer(day_id, new_pb, text):
        # find the block for the given day_id
        pattern = r'(id:\s*' + str(day_id) + r',[\s\S]+?playbook:\s*`)([\s\S]*?)(`\s*\}|`\s*,)'
        return re.sub(pattern, r'\g<1>' + new_pb + r'\g<3>', text)

    days_data_str = replacer(71, pb71, days_data_str)
    days_data_str = replacer(72, pb72, days_data_str)
    days_data_str = replacer(78, pb78, days_data_str)

    new_content = content[:match.start()] + days_data_str + content[match.end():]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated Bloque 8 playbooks.")
else:
    print("Could not find daysData")
