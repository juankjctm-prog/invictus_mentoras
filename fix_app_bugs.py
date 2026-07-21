import re

html_file = 'app.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Bug 1: Bottom Nav on mobile
content = content.replace(
    '.bottom-nav { position: absolute; bottom: 0; width: 100%;',
    '.bottom-nav { position: fixed; bottom: 0; left: 0; width: 100%;'
)

# Bug 2: Reader hidden on init
# Remove the block in window.onload that hides the reader indiscriminately
to_remove = """        // LOAD PERSISTENT DATA ON INIT
        window.onload = function() {
            if(localStorage.getItem('invictus_recall_score')) {
                let score = localStorage.getItem('invictus_recall_score');
                let ppm = localStorage.getItem('invictus_recall_ppm');
                document.getElementById('reader-content').style.display = 'none';
                document.getElementById('btn-bionic').style.display = 'none';
                document.getElementById('btn-timer').style.display = 'none';
                document.getElementById('test-intro').style.display = 'none';
                
                const res = document.getElementById('recall-result');
                res.style.display = 'block';
                if(score == 100) {
                    res.innerHTML = `<strong>🏆 Inteligencia Consolidada</strong><br>Velocidad: ${ppm} PPM<br>Comprensión: ${score}% (Perfecto)<br><span style="font-size:0.8rem; color:var(--bg-absolute);">Conexión sináptica recuperada de tu sesión anterior.</span>`;
                    res.style.background = "var(--success)"; res.style.color = "var(--bg-absolute)";
                } else {
                    res.innerHTML = `<strong>⚠️ Retención Parcial Guardada</strong><br>Comprensión: ${score}%`;
                    res.style.background = "rgba(255, 94, 0, 0.1)"; res.style.color = "var(--accent-fire)"; res.style.border = "1px solid var(--accent-fire)";
                }
            }
        }"""
content = content.replace(to_remove, "        // Init cleared")

# Also, when loadMujeresMentorasDay is called, we should check progress
# If currentPhaseProgress >= 4, hide reader, else show it
hook_str = "updateGamificationUI();"
replacement = """updateGamificationUI();
        
        // Fix for reading text visibility based on progress
        if(currentPhaseProgress >= 3) {
            // They already passed reading/recall
            document.getElementById('reader-content').style.display = 'none';
        } else {
            document.getElementById('reader-content').style.display = 'block';
            document.getElementById('btn-bionic').style.display = 'block';
        }
"""
content = content.replace(hook_str, replacement)

# Bug 3: Bionic Reading interference
# Fix toggleBionic to only target #reader-content p
bionic_old = "const ps = document.querySelectorAll('.reader-p');"
bionic_new = "const ps = document.querySelectorAll('#reader-content .reader-p');"
content = content.replace(bionic_old, bionic_new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("App.html fixes applied.")
