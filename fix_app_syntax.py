import re

with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace literal \n that might be causing syntax errors
# In patch_logic.py, I appended: js_code + "\\n" + content[idx:]
# This created the literal `\n` in the JS code.
content = content.replace('\\n\nwindow.openSalaModal', '\n\nwindow.openSalaModal')
content = content.replace('\\n\nwindow.toggleReglaDigital', '\n\nwindow.toggleReglaDigital')

# To be safe, let's just use a regex to replace literal \n that are on their own line
content = re.sub(r'^\s*\\n\s*$', '\n', content, flags=re.MULTILINE)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed stray \\n literals.")
