import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add mentadasData.js script tag
if '<script src="mentadasData.js"></script>' not in content:
    content = content.replace(
        '<script src="mujeresMentorasData.js"></script>', 
        '<script src="mujeresMentorasData.js"></script>\n<script src="mentadasData.js"></script>'
    )

# 2. Modify initUserSession()
old_init = "function initUserSession() {\n    if(!currentUser) return;"
new_init = "function initUserSession() {\n    if(!currentUser) return;\n    \n    window.activeTrackData = currentUser.role === 'Mentada' ? window.mentadasData : window.mujeresMentorasData;"
content = content.replace(old_init, new_init)

# 3. Modify target calculation
old_target = "if(target > window.mujeresMentorasData.length) target = window.mujeresMentorasData.length;"
new_target = "if(target > window.activeTrackData.length) target = window.activeTrackData.length;"
content = content.replace(old_target, new_target)

# 4. Modify loadMujeresMentorasDay
old_load = "const data = window.mujeresMentorasData.find(d => d.dia === dayIndex);"
new_load = "const data = window.activeTrackData.find(d => d.dia === dayIndex);"
content = content.replace(old_load, new_load)

# 5. Modify DOMContentLoaded
old_dom = "if (window.mujeresMentorasData) {"
new_dom = "if (true) {"
content = content.replace(old_dom, new_dom)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected dynamic routing based on user role.")
