import re

file_path = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/Bloque2_Premium.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

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

p16 = generate_playbook(
    ("Auditoría de Micromovimientos", "Mírate en el próximo Zoom. ¿Asientes excesivamente con la cabeza mientras un superior habla? Eso proyecta sumisión, no acuerdo. Evalúa tu encogimiento físico."),
    ("Neutralidad Facial Táctica", "Hoy vas a practicar el rostro relajado pero firme. El exceso de gesticulación agota tu poder. Las verdaderas líderes mueven su rostro solo con intención, no por nerviosismo."),
    ("El Despliegue de Espacio", "Antes de iniciar la sesión de mañana, extiende tus brazos. Reclama el espacio físico a tu alrededor. La autoridad corporativa es territorial, y tu biología lo sabe."),
    "Mañana tu cuerpo dejará de traicionar a tus palabras. Trabajaremos tu presencia ejecutiva física.",
    ("Si notas que ella termina sus instrucciones con una pequeña risa nerviosa o una sonrisa injustificada:", "¿Por qué sientes la necesidad biológica de sonreír para suavizar una instrucción directa de la que estás 100% segura?"),
    ("La Cámara Lenta", "Pídele que lea su reporte ejecutivo frente a ti. Luego, dile que reduzca la velocidad de todos sus movimientos (manos, respiración, parpadeo) un 20%. Mira cómo su autoridad se dispara."),
    "Debe dar una instrucción crítica a su equipo mañana manteniendo contacto visual ininterrumpido y sin sonreír ni un solo milímetro para 'suavizar el impacto'."
)

p17 = generate_playbook(
    ("Auditoría de Complejidad", "¿Usas demasiada jerga técnica, acrónimos o palabras en inglés para explicar lo que haces? El exceso de tecnicismos es el escudo de los inseguros."),
    ("Desintoxicación del Lenguaje Corporativo", "La verdadera prueba de tu dominio no es sonar inteligente, es hacer que lo complejo suene inevitable y simple. Purga tu vocabulario."),
    ("El Filtro del Novato", "Si no pudieras usar la jerga de tu industria, ¿serías capaz de convencerme del valor de tu proyecto en 30 segundos? Haz la prueba ahora mismo en voz alta."),
    "Si no puedes explicar tu estrategia de forma simple, no la entiendes profundamente. Mañana la ponemos a prueba.",
    ("Cuando use demasiadas palabras técnicas para justificar un proyecto estancado:", "¿Qué pasaría si tuvieras que convencer a la Junta Directiva sin poder usar ni una sola palabra técnica de tu departamento?"),
    ("Destilación Extrema (Feynman)", "Haz que explique su proyecto más complejo. Interrúmpela cada vez que use jerga. Oblígala a resumir todo el objetivo estratégico en 3 oraciones de 10 palabras máximo cada una."),
    "Debe enviar un correo/presentar un reporte a la alta dirección explicando un problema complejo en lenguaje universal, sin usar un solo acrónimo técnico de su área."
)

p18 = generate_playbook(
    ("Auditoría del Miedo al Vacío", "Cuando hay un silencio de 3 segundos en una reunión, ¿eres la primera en hablar para 'salvar la situación'? Reconoce cómo tu ansiedad rellena los espacios vacíos."),
    ("El Silencio como Herramienta de Presión", "El que habla primero en una negociación tensa, pierde. Entiende que el silencio no es ausencia de comunicación, es la comunicación más pesada de la sala."),
    ("La Pausa de 4 Segundos", "Antes de abrir la cámara para la sesión, practica mantener la boca cerrada durante 4 segundos después de que una idea termine. Sostén la presión en tu propio cuerpo."),
    "Mañana usaremos el arma más intimidante de la comunicación corporativa: el silencio.",
    ("Cuando notes que ella da una respuesta y luego sigue hablando para justificarse porque nadie le contestó de inmediato:", "¿Quién te hizo creer en el pasado que es tu obligación rescatar a los demás de la incomodidad de sus propias pausas?"),
    ("El Simulador de Tensión", "Hazle una pregunta directiva difícil (Ej: '¿Por qué falló esa métrica?'). Ella responderá. Cuando termine, NO le contestes. Quédate mirándola en silencio absoluto. Observa si ella se quiebra e intenta rellenar el silencio. Entrénala para resistir."),
    "En la próxima negociación de recursos o plazos, debe lanzar su requerimiento y quedarse en silencio absoluto hasta que la otra parte ceda o proponga una contraoferta. No puede 'suavizar' la tensión."
)

p19 = generate_playbook(
    ("Auditoría de Transferencia", "Repasa tu impacto. ¿Estás resolviéndole los problemas a tu mentoreada como si fuera tu asistente, o le estás transfiriendo el fuego de la responsabilidad?"),
    ("La Visión de la Mentora de Élite", "Hoy se invierten los roles. Ella ya no es la aprendiz pasiva, ella ahora debe diseñar cómo va a liderar a otros. Mírala hoy como a tu sucesora."),
    ("Arquitectura del Espacio Seguro", "Prepara tu mente para exigir sin destrozar. Estás a punto de pedirle que ejecute con otra persona el nivel de rigor que tú le aplicaste a ella."),
    "Estás lista para sentarte del lado del poder directivo. Mañana diseñaremos tu primera intervención formal como mentora.",
    ("Si ella duda en aplicar presión a su propio equipo para ayudarlos a crecer:", "Si la carrera de otra mujer en tu equipo dependiera exclusivamente de tu nivel de rigor, ¿serías tan suave con ella como lo fuiste hoy contigo misma?"),
    ("El Mapa del Dolor Organizacional", "Haz que elija a un miembro clave de su equipo. Diseñen juntas una 'sesión de mentoría 1-A-1' estructurada para que ella la aplique y destrabe el potencial de esa persona."),
    "Debe citar formalmente a una persona de su equipo a una sesión de 'Calibración de Carrera' (Mentoría) aplicando la estructura que han diseñado hoy juntas."
)

p20 = generate_playbook(
    ("Auditoría de Identidad Reconstruida", "Mira hacia atrás, al Día 1 de este bloque. ¿En qué has cambiado? Ya no toleras excusas, ya no validas la fragmentación mental. Celebra tu propio endurecimiento."),
    ("Medición del Capital de Presencia", "Tu autoridad física, tu uso del silencio y tu escucha profunda han creado un capital de presencia inmenso. Ya no necesitas gritar para que te escuchen en la mesa."),
    ("Consolidación Neurológica", "Hoy no empujarás nueva información. Tu único trabajo en la preparación de hoy es sentir gratitud profunda por la ejecutiva en la que se está convirtiendo."),
    "Llegamos al Checkpoint 2. Cierra tu laptop y respira. Mañana solo repasaremos la evolución táctica y tu metamorfosis corporativa.",
    ("Para forzarla a verbalizar su propia transformación y anclar el poder ganado:", "Viendo a la ejecutiva insegura que eras en el Día 1 de este bloque, ¿qué orden directa le daría la mujer poderosa que eres hoy en este Checkpoint?"),
    ("Extracción de los Principios Intocables", "Oblígala a escribir a mano los 3 principios de comunicación y presencia (silencio, postura, escucha táctica) de este bloque que ya NUNCA volverá a romper bajo ninguna circunstancia."),
    "Riesgo de Recuperación: Cero ejecución operativa hoy. Tiene prohibido revisar correos después de la jornada. Debe desconectarse 24h para asimilar biológicamente todo este poder antes del Bloque 3.",
    success=True
)

match = re.search(r'const daysData = \[\s*\{([\s\S]+?)\];', content)
if match:
    days_data_str = match.group(0)
    
    def replacer(day_id, new_pb, text):
        pattern = r'(id:\s*' + str(day_id) + r',[\s\S]+?playbook:\s*`)([\s\S]*?)(`\s*\}|`\s*,)'
        return re.sub(pattern, r'\g<1>' + new_pb + r'\g<3>', text)

    days_data_str = replacer(16, p16, days_data_str)
    days_data_str = replacer(17, p17, days_data_str)
    days_data_str = replacer(18, p18, days_data_str)
    days_data_str = replacer(19, p19, days_data_str)
    days_data_str = replacer(20, p20, days_data_str)

    new_content = content[:match.start()] + days_data_str + content[match.end():]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated Bloque 2 (Days 16-20) playbooks.")
else:
    print("Could not find daysData")
