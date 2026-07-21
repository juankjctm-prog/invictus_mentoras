import json
import codecs
import re

for js_file in ['mujeresMentorasData.js', 'mentadasData.js']:
    with codecs.open(js_file, 'r', 'utf-8') as f:
        content = f.read()

    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])

    for day in data:
        if day['dia'] == 1:
            texto = day['fase2_lectura']['texto']
            texto = texto.replace('Dispenza', 'Richard Davidson')
            day['fase2_lectura']['texto'] = texto

        if day['dia'] == 9:
            texto = day['fase2_lectura']['texto']
            
            # Replace the Dispenza paragraphs with Richard Davidson paragraphs
            old_para1 = "La investigación de Joe Dispenza, neurocientífico y médico quiropráctico que estudió con varios de los investigadores de punta en neuroplasticidad, se enfocó en documentar los cambios neurológicos producidos por prácticas de meditación y visualización intensa."
            new_para1 = "La investigación del Dr. Richard Davidson, neurocientífico de la Universidad de Wisconsin-Madison y fundador del Center for Healthy Minds, se ha enfocado en documentar los cambios neurológicos producidos por prácticas de meditación y visualización intensa."
            
            old_para2 = "Su colaboración con el Laboratorio de Neurociencia de la Universidad de California en San Diego produjo, en un estudio publicado en Nature Communications en 2026, evidencia de que una intervención de siete días de práctica meditativa intensiva produce cambios medibles en marcadores de neuroplasticidad en plasma sanguíneo — incluyendo niveles elevados de BDNF (factor neurotrófico derivado del cerebro), mayor conectividad en redes asociadas con regulación emocional y atención, y reducción de actividad en la red de modo por defecto, que es la red asociada con el parloteo mental interno no dirigido."
            new_para2 = "Su colaboración en estudios longitudinales, incluyendo investigaciones publicadas en PNAS (Proceedings of the National Academy of Sciences), ha producido evidencia de que incluso intervenciones breves de práctica meditativa intensiva generan cambios medibles en marcadores de neuroplasticidad y conectividad estructural — incluyendo mayor interconexión en redes asociadas con regulación emocional y atención sostenida, y reducción de actividad en la red de modo por defecto, que es la red asociada con el parloteo mental interno no dirigido."
            
            texto = texto.replace(old_para1, new_para1).replace(old_para2, new_para2)
            day['fase2_lectura']['texto'] = texto

    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    var_name = 'mujeresMentorasData' if 'mujeres' in js_file.lower() else 'mentadasData'
    final_content = f"const {var_name} = " + new_json + f";\n\nwindow.{var_name} = {var_name};\n"

    with codecs.open(js_file, 'w', 'utf-8') as f:
        f.write(final_content)

print("Sources corrected in Day 1 and Day 9.")
