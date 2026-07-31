import re

with open('app.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Despertador Neuronal modal alignment
html = html.replace(
    'align-items:center;padding:20px;',
    'align-items:flex-start;padding-top:12vh;'
)

# 2. Update Cortisol Affirmations
new_affirmations = """const affirmations = [
"Perdona a tu persona del pasado, estaba haciendo lo mejor que podía con la consciencia que tenía en ese momento.",
"No te des tan duro. La autoexigencia brutal destruye tu inspiración; la autocompasión la expande.",
"No necesitas ser perfecta para liderar. Tu vulnerabilidad humana es, de hecho, tu mayor fortaleza.",
"El progreso jamás es lineal. Estás exactamente en el lugar que necesitas estar para tu evolución.",
"Respira profundo. Suelta el hipercontrol. Lo que te pertenece te encontrará incluso en el descanso.",
"Hoy, elige ser tu propio refugio seguro en lugar de convertirte en tu juez más severo.",
"Tus errores no definen tu valor, solo refinan tu sabiduría. Date permiso para aprender."
];"""

html = re.sub(
    r'const affirmations = \[[^\]]*\];',
    new_affirmations,
    html,
    flags=re.DOTALL
)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Changes applied successfully!")
