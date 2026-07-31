import re
with open('app.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Phase 4
html = re.sub(
    r'<!-- F4 -->\s*<div class="phase" id="comprension-block".*?</div>\s*</div>',
    '''<!-- F4 -->
        <div class="phase active" id="comprension-block">
            <div class="phase-node"></div>
            <div class="phase-header"><h4>4. Recall Activo y Evaluación</h4><span class="phase-duration">4m</span></div>
            <p class="phase-desc">La extracción forzada es la base de la retención a largo plazo.</p>
            <div id="test-content" style="margin-top: 16px;">
                ${preguntasHTML}
                <button class="btn-premium fire" style="width: 100%; margin-top: 8px;" onclick="evaluarQuizReal(${dayIndex})">📊 Evaluar Comprensión</button>
            </div>
            <div id="quiz-result-${dayIndex}" style="display:none; margin-top:20px; padding:20px; border-radius:12px; border:1px solid;"></div>
        </div>''',
    html, flags=re.DOTALL
)

# Fix Phase 9
html = re.sub(
    r'<!-- F9 -->\s*<div class="phase".*?<h4>9\. Técnica Feynman</h4></div>',
    '''<!-- F9 -->
        <div class="phase active">
            <div class="phase-node"></div>
            <div class="phase-header"><h4>9. Técnica Feynman</h4></div>''',
    html
)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(html)
