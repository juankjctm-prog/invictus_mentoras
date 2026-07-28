import os

# Files to fix
folders = [
    "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/Mujeres mentoras",
    "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mujeres mentoras",
    "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mentadas"
]

files_to_fix = ["diagnostico_mentora.html", "diagnostico_mentoreada.html", "diagnostico_data.js"]

replacements = {
    "Termin\u01f8": "Terminé",
    "Termin\ufffd": "Terminé",
    "Termine de leer": "Terminé de leer",
    "Termin\xc3\xb8": "Terminé",
    "Diagnostico": "Diagnóstico",
    "Sesion": "Sesión",
    "sesion": "sesión",
    "atencion": "atención",
    "Mentoria": "Mentoría",
    "mentoria": "mentoría",
    "comprension": "comprensión",
    "Comprension": "Comprensión",
    "evaluaciónes": "evaluaciones",  # wait, evaluaciones shouldn't have tilde
    "dar\u00e1n": "darán",
    "daran": "darán",
    "estan": "están",
    "est\u00e1s": "estás",
    "estas tu": "estás tú",
    "donde esta": "dónde está",
    "donde estas": "dónde estás",
    "mas trabajo": "más trabajo",
    "recibiras": "recibirás",
    "proximas": "próximas",
    "actuas": "actúas",
    "comunicacion": "comunicación",
    "Comunicacion": "Comunicación",
    "evaluacion": "evaluación",
    "Autoevaluacion": "Autoevaluación",
    "estan": "están",
    "estan ": "están ",
    "est\u00e1n ": "están "
}

import re

for folder in folders:
    for filename in files_to_fix:
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Do regex replace for Terminé
        content = re.sub(r'Termin. de [Ll]eer', 'Terminé de Leer', content)
        content = re.sub(r'Termin. de leer', 'Terminé de leer', content)
        
        # Replace others
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Done fixing tildes!")
