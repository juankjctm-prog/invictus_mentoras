import codecs

with codecs.open('app.html', 'r', 'utf-8') as f:
    content = f.read()

# Make the button text smaller and hide the wrapper on continue
old_toggle = """btn.innerText = `PPM: ${basePPM} (Velocidad Registrada)`;
        btn.disabled = true;"""
new_toggle = """btn.innerText = `Velocidad: ${basePPM} PPM`;
        btn.style.fontSize = '0.9rem';
        btn.style.padding = '8px';
        btn.disabled = true;"""

old_continue = """function continueToComprension() {
    document.getElementById('re-read-prompt').style.display = 'none';
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
    document.getElementById('comprension-block').style.display = 'block';
    showMotivationToast("Velocidad registrada. Ahora, pongamos a prueba tu retención.");
}"""
new_continue = """function continueToComprension() {
    document.getElementById('sticky-timer-wrapper').style.display = 'none';
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
    document.getElementById('comprension-block').style.display = 'block';
    showMotivationToast("Velocidad registrada. Ahora, pongamos a prueba tu retención.");
}"""

if old_toggle in content:
    content = content.replace(old_toggle, new_toggle)
else:
    print("WARNING: Could not find old_toggle")

if old_continue in content:
    content = content.replace(old_continue, new_continue)
else:
    print("WARNING: Could not find old_continue")

with codecs.open('app.html', 'w', 'utf-8') as f:
    f.write(content)

print("Timer UI tweaks applied.")
