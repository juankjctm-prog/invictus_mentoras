import codecs
import re

file_path = 'app.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Sticky Timer HTML
old_timer = '<button class="btn-premium fire" id="btn-timer" style="margin-top: 16px;" onclick="toggleTimer()">Iniciar Cronómetro Real</button>'
new_timer = """
<div id="sticky-timer-wrapper" style="position: sticky; top: 10px; z-index: 1000; background: rgba(0,0,0,0.8); padding: 10px; border-radius: 8px; text-align: center; border: 1px solid var(--accent-fire); margin-bottom: 10px;">
    <button class="btn-premium fire" id="btn-timer" style="width: 100%;" onclick="toggleTimer()">Iniciar Cronómetro</button>
    <div id="re-read-prompt" style="display: none; margin-top: 10px; font-size: 0.9rem;">
        <p style="color: white; margin-bottom: 8px;">¿Hay algo que no entendiste?</p>
        <div style="display: flex; gap: 10px;">
            <button class="btn-outline" style="flex:1; font-size:0.7rem;" onclick="resetTimer()">🔁 Repetir Lectura</button>
            <button class="btn-primary" style="flex:1; font-size:0.7rem;" onclick="continueToComprension()">✅ Continuar a Comprensión</button>
        </div>
    </div>
</div>
"""
if old_timer in content:
    content = content.replace(old_timer, new_timer)
else:
    print("WARNING: Could not find old_timer button in app.html")

# 2. Timer JS Logic
old_js = """let timer, secs = 0, isRunning = false;
        function toggleTimer() {
            const btn = document.getElementById('btn-timer');
            const box = document.getElementById('ppm-box');
            if(!isRunning) {
                isRunning = true; secs = 0; box.style.display = 'none';
                btn.classList.remove('fire'); btn.style.background = 'rgba(255,255,255,0.1)';
                timer = setInterval(() => {
                    secs++; let m = Math.floor(secs/60).toString().padStart(2,'0'); let s = (secs%60).toString().padStart(2,'0');
                    btn.innerHTML = `⏱ Leyendo... ${m}:${s}`;
                }, 1000);
            } else {
                clearInterval(timer); isRunning = false;
                btn.innerHTML = 'Lectura Finalizada'; btn.style.pointerEvents = 'none'; btn.style.opacity = '0.5';
                let ppm = Math.round((262 / (secs>0?secs:1)) * 60);
                box.style.display = 'block';
                box.innerHTML = `Velocidad Registrada: <strong>${ppm} PPM</strong>`;
            }
        }"""

new_js = """let timer, secs = 0, isRunning = false;

function toggleTimer() {
    const btn = document.getElementById('btn-timer');
    if(!isRunning) {
        isRunning = true;
        btn.innerText = "Detener Cronómetro";
        btn.style.background = "linear-gradient(45deg, #10b981, #059669)";
        
        if(document.getElementById('reader-content').innerText.includes('Activa el cronómetro') === false) {
           document.getElementById('reader-content').style.filter = "none";
           document.getElementById('reader-content').style.userSelect = "auto";
        }

        timer = setInterval(() => {
            secs++;
            const m = Math.floor(secs/60).toString().padStart(2,'0');
            const s = (secs%60).toString().padStart(2,'0');
            btn.innerText = `Detener (${m}:${s})`;
        }, 1000);
    } else {
        clearInterval(timer); isRunning = false;
        const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
        btn.innerText = `PPM: ${basePPM} (Velocidad Registrada)`;
        btn.disabled = true;
        
        document.getElementById('re-read-prompt').style.display = 'block';
    }
}

function resetTimer() {
    secs = 0;
    isRunning = false;
    const btn = document.getElementById('btn-timer');
    btn.disabled = false;
    btn.innerText = "Iniciar Cronómetro";
    btn.style.background = "";
    document.getElementById('re-read-prompt').style.display = 'none';
}

function continueToComprension() {
    document.getElementById('re-read-prompt').style.display = 'none';
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
    document.getElementById('comprension-block').style.display = 'block';
    showMotivationToast("Velocidad registrada. Ahora, pongamos a prueba tu retención.");
}
"""

if old_js in content:
    content = content.replace(old_js, new_js)
else:
    print("WARNING: Could not find old_js in app.html")
    # Use regex if direct match fails
    content = re.sub(r'let timer, secs = 0, isRunning = false;\s*function toggleTimer\(\) \{.*?\}(?=\s*function iniciarTest\(\))', new_js, content, flags=re.DOTALL)


with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Timer UI and logic updated in app.html")
