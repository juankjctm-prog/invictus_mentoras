import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the text: "..." inside lectura
    match = re.search(r'text: "(.*?)",\n\s*questions:', content, flags=re.DOTALL)
    if match:
        original_text = match.group(1)
        # replace literal newlines with escaped newlines
        fixed_text = original_text.replace('\n', '\\n')
        content = content[:match.start(1)] + fixed_text + content[match.end(1):]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"Match not found in {filepath}")

fix_file("D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/Mujeres mentoras/diagnostico_data.js")
fix_file("D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mentadas/diagnostico_data.js")
fix_file("D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/implementaciones/Mujeres mentoras/diagnostico_data.js")
