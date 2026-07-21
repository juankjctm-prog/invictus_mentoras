import codecs
import json

file_path = 'mujeresMentorasData.js'

with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Extract JSON
start_idx = content.find('[')
end_idx = content.rfind(']') + 1

json_str = content[start_idx:end_idx]
data = json.loads(json_str)

texto_lectura = """En 2010, Herminia Ibarra, profesora de comportamiento organizacional en INSEAD y posteriormente en la London Business School, publicó un hallazgo que contradecía una de las premisas más extendidas del desarrollo de liderazgo: que la transformación genuina requiere primero un cambio interno de identidad para luego manifestarse en comportamiento externo. Su investigación longitudinal con más de 200 ejecutivos en transición demostró exactamente lo contrario. El cambio de identidad no precede al comportamiento — lo sigue. Las personas que esperan sentirse líderes antes de actuar como líderes esperan indefinidamente. Las que actúan como líderes y luego ajustan su autoimagen en función de esa experiencia son las que consolidan una identidad de liderazgo sostenible.

Este hallazgo tiene implicaciones específicas para las mujeres profesionales latinoamericanas que más tarde exploraremos. Pero antes de llegar ahí, es necesario entender qué es exactamente la identidad de liderazgo y por qué es tan difícil de construir para ciertos perfiles.

La identidad de liderazgo es la respuesta interna a la pregunta '¿soy el tipo de persona que lidera?' Es distinta de las habilidades de liderazgo — que son lo que sabes hacer — y de la posición de liderazgo — que es el cargo que ocupas. Una persona puede tener todas las habilidades técnicas de liderazgo y el cargo correspondiente, y aun así no tener una identidad de liderazgo consolidada. El síntoma más común: la persona que ocupa la posición pero constantemente busca validación externa de que está haciéndolo bien, que necesita el permiso implícito del grupo para tomar decisiones que técnicamente son suyas, o que en el momento de mayor presión regresa automáticamente a un modo de ejecución individual en lugar de sostenerse en el modo de coordinación que su rol exige.

La investigación de Ibarra identifica tres mecanismos principales por los que se construye la identidad de liderazgo. El primero es la observación activa de referentes: personas que admiramos y cuyo estilo de liderazgo estudiamos conscientemente, no para imitarlo sino para extraer principios transferibles. El segundo es el ensayo de comportamientos de liderazgo en contextos seguros donde el costo del error es bajo — exactamente lo que produce una relación de mentoría bien diseñada. El tercero, y el más poderoso, es la narración retrospectiva: la capacidad de articular en primera persona, con lenguaje de agencia, los momentos donde ejerciste liderazgo real. No 'el equipo logró X' sino 'yo tomé la decisión de hacer Y porque vi Z'.

Hay un cuarto mecanismo que Ibarra nombra pero no desarrolla completamente, y que la investigación posterior de Amy Edmondson en Harvard Business School complementa: la seguridad psicológica como condición de posibilidad. La identidad de liderazgo no se construye en entornos donde el error tiene costo social alto. Se construye donde hay suficiente confianza para probar, equivocarse, ajustar y volver a intentar sin que eso genere consecuencias sobre el estatus o la percepción de competencia. Este es precisamente el recurso más escaso en las organizaciones latinoamericanas y el que una mentora bien formada puede crear de manera deliberada.

El estudio INCAE Business School de 2022 sobre liderazgo femenino en Centroamérica y los Andes reveló que el 67% de las mujeres en roles de mando medio reportaban no verse a sí mismas como líderes, a pesar de liderar equipos de entre 5 y 30 personas. El 78% atribuía sus ascensos a factores externos — suerte, red de contactos, momento oportuno — en lugar de a competencia propia. Este patrón de atribución externa del éxito no es un rasgo de personalidad ni un problema de autoestima en sentido clínico. Es el resultado predecible de operar durante años en entornos donde la competencia de las mujeres es sistemáticamente subevaluada, donde el estándar de excelencia requerido para obtener el mismo reconocimiento que un par masculino es consistentemente más alto, y donde la cultura organizacional envía señales contradictorias: se espera que la mujer líder sea asertiva pero no agresiva, segura pero no arrogante, visible pero no difícil.

Las implicaciones para la práctica de la mentoría son directas. Una mentora que no ha examinado su propia identidad de liderazgo — sus mecanismos de atribución, sus patrones de respuesta bajo presión, sus supuestos sobre lo que significa liderar bien — no puede acompañar a su mentoreada en ese proceso. No porque carezca de experiencia, sino porque transmite inconscientemente los mismos patrones que pretende ayudar a superar. La mentoría sin autoexamen de la mentora es, en el mejor caso, transmisión de competencias técnicas. En el peor caso, es replicación de los mismos límites que la mentoreada ya tiene.

Este bloque de diez días trabaja exactamente eso: el autoexamen como condición previa de la mentoría efectiva. No para que la mentora esté perfecta antes de empezar — la perfección no es el criterio. Sino para que tenga suficiente claridad sobre sus propios patrones como para no operar en automático cuando está frente a la mentoreada. La diferencia entre una mentora que actúa desde sus patrones y una que actúa desde sus valores es la diferencia entre una relación que reproduce el problema y una que lo transforma.

La investigación de Bandura sobre autoeficacia, publicada originalmente en 1977 y extendida durante tres décadas, demuestra que la creencia en la propia capacidad de ejecutar una conducta específica es predictora del desempeño en esa conducta de manera más consistente que las habilidades objetivas. Dicho de manera directa: una mujer con habilidades de liderazgo moderadas y alta autoeficacia de liderazgo consistentemente supera en rendimiento a una mujer con habilidades superiores pero baja autoeficacia. Y la autoeficacia se construye, en primer lugar, por experiencias de dominio — momentos donde la persona ejecuta con éxito la conducta en cuestión. La mentoría es una fábrica deliberada de experiencias de dominio."""

data[0]["fase2_lectura"]["texto"] = texto_lectura

data[0]["fase2_lectura"]["comprension"] = {
    "q": "Según el texto original de Herminia Ibarra, ¿cómo se logra la transformación genuina en la identidad de liderazgo?",
    "options": [
        "Sintiéndote líder antes de empezar a actuar como líder.",
        "Actuando primero de manera diferente y ajustando tu autoimagen basada en esa experiencia.",
        "Memorizando técnicas avanzadas de comunicación asertiva."
    ],
    "answer": 1
}

# Save back
new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_content = "const mujeresMentorasData = " + new_json_str + ";\n\nwindow.mujeresMentorasData = mujeresMentorasData;\n"

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(final_content)

print("Original text extracted from DOCX and injected into database!")
