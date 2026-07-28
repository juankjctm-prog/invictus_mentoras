import os
import re

file_path = "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/Mujeres mentoras/diagnostico_data.js"
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

correct_lectura = """// Datos compartidos para los diagnosticos de Mentora y Mentoreada
const DIAG_DATA = {
    lectura: {
        words: 393,
        text: "El liderazgo femenino en América Latina está en un momento de inflexión. Según el Informe Global de Género 2024 del Foro Económico Mundial, la región ha avanzado en educación y salud, pero la brecha política y económica sigue siendo significativa. Las mujeres ocupan menos del 30 por ciento de los puestos directivos en las empresas más grandes, a pesar de que en muchos países latinoamericanos son mayoría en las universidades y obtienen mejores promedios académicos que los hombres. Esta contradicción no es casual. Refleja barreras estructurales, culturales y psicológicas que operan simultáneamente para limitar el ascenso profesional de las mujeres.\\n\\nLa investigación académica ha identificado varios mecanismos que explican esta brecha. En primer lugar, la psicóloga social Shelley Correll, de la Universidad Stanford, demostró a través de numerosos experimentos que las expectativas de género afectan las evaluaciones de competencia incluso cuando el desempeño es idéntico. En uno de sus estudios más citados, publicado en American Journal of Sociology, Correll encontró que cuando hombres y mujeres presentaban la misma calificación académica, los evaluadores seguían considerando que los hombres tenían mayor capacidad matemática. Este sesgo no siempre es consciente, pero sí sistemático, y se reproduce en procesos de contratación, promoción y asignación de proyectos.\\n\\nEn segundo lugar, el trabajo de Herminia Ibarra en INSEAD y London Business School muestra que el acceso a redes informales de poder es un determinante crítico del avance profesional. Las redes no son solo relaciones personales; son canales por donde circulan información privilegiada, oportunidades visibles y validación social. Ibarra encontró que las mujeres tienden a tener redes más cercanas y homogéneas, mientras que los hombres suelen construir redes más amplias y estratégicas. Esta diferencia no es un defecto individual, sino el resultado de años de dinámicas sociales que asignan espacios de sociabilidad diferentes a hombres y mujeres.\\n\\nFinalmente, el concepto de seguridad psicológica, desarrollado por Amy Edmondson en Harvard Business School, ayuda a entender por qué muchas mujeres no se arriesgan a visibilizar sus ideas o a pedir lo que necesitan. Edmondson define la seguridad psicológica como la creencia compartida de que un equipo es seguro para tomar riesgos interpersonales. En ambientes donde esta seguridad es baja, las personas minoritarias —incluidas las mujeres— silencian sus opiniones para evitar repercusiones. Construir liderazgo femenino efectivo requiere, por tanto, intervenir simultáneamente en las estructuras organizacionales, las redes de poder y las creencias individuales.",
        questions: [
            { q: "Según el texto, ¿qué porcentaje aproximado de puestos directivos ocupan las mujeres en las empresas más grandes de América Latina?", options: ["A) Menos del 20%", "B) Menos del 30%", "C) Alrededor del 40%", "D) Más del 50%"], answer: 1 },
            { q: "¿Qué encontró Shelley Correll en sus estudios sobre evaluaciones de competencia?", options: ["A) Las mujeres son evaluadas de forma más estricta en humanidades.", "B) Con la misma calificación, se percibe a los hombres con mayor capacidad matemática.", "C) Los hombres obtienen mejores promedios académicos generales.", "D) Las mujeres prefieren proyectos menos técnicos."], answer: 1 },
            { q: "Según Herminia Ibarra, ¿cuál es una característica de las redes informales de las mujeres en comparación con las de los hombres?", options: ["A) Son más amplias pero menos profundas.", "B) Son más estratégicas y diversas.", "C) Son más cercanas y homogéneas.", "D) Se centran exclusivamente en el entorno familiar."], answer: 2 },
            { q: "¿Cuál es la definición de 'seguridad psicológica' según Amy Edmondson?", options: ["A) La capacidad individual de manejar el estrés en el trabajo.", "B) La creencia compartida de que un equipo es seguro para tomar riesgos interpersonales.", "C) Políticas de recursos humanos contra el acoso laboral.", "D) La confianza en la estabilidad financiera de la empresa."], answer: 1 },
            { q: "Según el texto, ¿cuál no es uno de los elementos en los que se debe intervenir para construir un liderazgo femenino efectivo?", options: ["A) Las estructuras organizacionales.", "B) Las redes de poder.", "C) Las creencias individuales.", "D) Los promedios académicos universitarios."], answer: 3 }
        ]
    },"""

# Replace the reading section
content = re.sub(r'// Datos compartidos para los diagnosticos.*?(?=brechas: \[)', correct_lectura + '\n    ', content, flags=re.DOTALL)

# Now fix specifically known bad characters in the brechas questions without breaking json structure
replacements = {
    "America Latina": "América Latina",
    "estan": "están",
    "estn": "están",
    "estás tu": "estás tú",
    "Que tan": "Qué tan",
    "Que tanto": "Qué tanto",
    "Cual de": "Cuál de",
    "Cual es": "Cuál es",
    "Como te": "Cómo te",
    "Como ": "Cómo ",
    "Que ": "Qué ",
    "Cual ": "Cuál ",
    "Quien ": "Quién ",
    "Cuando ": "Cuándo ",
    "Donde ": "Dónde ",
    "Por que ": "Por qué ",
    "tambien": "también",
    "mas ": "más ",
    "estan": "están",
    "esta ": "está ",
    "accion": "acción",
    "organizacion": "organización",
    "tension": "tensión",
    "situacion": "situación",
    "emocion": "emoción",
    "intuicion": "intuición",
    "opinion": "opinión",
    "comunicacion": "comunicación",
    "resolucion": "resolución",
    "decision": "decisión",
    "vision": "visión",
    "evaluacion": "evaluación",
    "autoevaluacion": "autoevaluación",
    "exito": "éxito",
    "facil": "fácil",
    "dificil": "difícil",
    "lider": "líder",
    "estrategica": "estratégica",
    "critica": "crítica",
    "basica": "básica",
    "tecnica": "técnica",
    "practica": "práctica",
    "unica": "única",
    "responsabilidad": "responsabilidad", # correct
    "desafio": "desafío",
    "vac\u00edo": "vacío",
    "dia": "día",
    "d\u00eda": "día",
    "energia": "energía",
    "mentoria": "mentoría",
    "sesion": "sesión",
    "reunion": "reunión"
}

# we only replace inside quotes to avoid code syntax issues
def replace_in_string(match):
    text = match.group(0)
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

content = re.sub(r'\"[^\"]+\"', replace_in_string, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("diagnostico_data.js completely fixed!")

# Sync to implementaciones
copies = [
    "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mujeres mentoras/diagnostico_data.js",
    "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mentadas/diagnostico_data.js"
]
for cp in copies:
    if os.path.exists(cp):
        with open(cp, 'w', encoding='utf-8') as f:
            f.write(content)
