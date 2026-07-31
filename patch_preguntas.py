import re

with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1
content = content.replace(
    "if (d && d.preguntas) qData = d.preguntas;",
    "if (d && (d.preguntas || d.comprension)) qData = (d.preguntas || d.comprension);"
)

# Fix 2
content = content.replace(
    "if (d && d.preguntas) {\n        preguntasHTML = d.preguntas.map((q, i) => `",
    "if (d && (d.preguntas || d.comprension)) {\n        let arr = d.preguntas || d.comprension;\n        preguntasHTML = arr.map((q, i) => `"
)

# Handle CRLF if needed
content = content.replace(
    "if (d && d.preguntas) {\r\n        preguntasHTML = d.preguntas.map((q, i) => `",
    "if (d && (d.preguntas || d.comprension)) {\r\n        let arr = d.preguntas || d.comprension;\r\n        preguntasHTML = arr.map((q, i) => `"
)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched app.html questions handling")
