html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

old_str = "window.activeTrackData = currentUser.role === 'Mentada' ? window.mentadasData : window.mujeresMentorasData;"
new_str = "window.activeTrackData = currentUser.role === 'Mentada' ? (typeof mentadasData !== 'undefined' ? mentadasData : []) : (typeof mujeresMentorasData !== 'undefined' ? mujeresMentorasData : []);"

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed window data references.")
else:
    print("String not found. Check if it was already modified.")
