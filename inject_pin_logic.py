import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Keypad HTML to pass numbers
keypad_replacements = [
    ('<div class="key" onclick="pressKey()">1</div>', '<div class="key" onclick="pressKey(\'1\')">1</div>'),
    ('<div class="key" onclick="pressKey()">2</div>', '<div class="key" onclick="pressKey(\'2\')">2</div>'),
    ('<div class="key" onclick="pressKey()">3</div>', '<div class="key" onclick="pressKey(\'3\')">3</div>'),
    ('<div class="key" onclick="pressKey()">4</div>', '<div class="key" onclick="pressKey(\'4\')">4</div>'),
    ('<div class="key" onclick="pressKey()">5</div>', '<div class="key" onclick="pressKey(\'5\')">5</div>'),
    ('<div class="key" onclick="pressKey()">6</div>', '<div class="key" onclick="pressKey(\'6\')">6</div>'),
    ('<div class="key" onclick="pressKey()">7</div>', '<div class="key" onclick="pressKey(\'7\')">7</div>'),
    ('<div class="key" onclick="pressKey()">8</div>', '<div class="key" onclick="pressKey(\'8\')">8</div>'),
    ('<div class="key" onclick="pressKey()">9</div>', '<div class="key" onclick="pressKey(\'9\')">9</div>'),
    ('<div class="key" onclick="pressKey()">0</div>', '<div class="key" onclick="pressKey(\'0\')">0</div>'),
]
for old, new in keypad_replacements:
    content = content.replace(old, new)

# 2. Add shake animation to CSS
if '@keyframes shake' not in content:
    shake_css = """
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            50% { transform: translateX(5px); }
            75% { transform: translateX(-5px); }
        }
        .shake-error {
            animation: shake 0.3s ease-in-out;
        }
        .dot.error { background: var(--accent-fire); box-shadow: 0 0 10px var(--accent-fire); }
"""
    content = content.replace('</style>', shake_css + '\n    </style>')

# 3. Replace the `pressKey` and `loadMujeresMentorasDay` sections that were injected previously.
# Actually, I can replace the whole injected script starting from <script src="mujeresMentorasData.js">
start_marker = '<script src="mujeresMentorasData.js"></script>'
end_marker = '</body>'

if start_marker in content:
    pre_content = content.split(start_marker)[0]
    
    new_script = """<script src="mujeresMentorasData.js"></script>
<script>
// --- USER DATABASE MOCK ---
const authUsers = [
    { id: 'usr_01', pin: '1111', name: 'Marjorie' },
    { id: 'usr_02', pin: '2222', name: 'Valentina' },
    { id: 'usr_03', pin: '3333', name: 'Camila' },
    { id: 'usr_04', pin: '4444', name: 'Sofia' },
    { id: 'usr_05', pin: '5555', name: 'Isabella' },
    { id: 'usr_06', pin: '6666', name: 'Martina' },
    { id: 'usr_07', pin: '7777', name: 'Lucia' },
    { id: 'usr_08', pin: '8888', name: 'Elena' },
    { id: 'usr_09', pin: '9999', name: 'Victoria' },
    { id: 'usr_10', pin: '0000', name: 'Antonella' }
];

let currentUser = null;
let currentPin = '';
let pinCount = 0;

// Remove the old dummy pressKey if it exists outside this block (wait, the old one was in the original HTML)
// Actually, let's just redefine pressKey here to override it.
window.pressKey = function(num) {
    if(!num) num = ''; // fallback
    if(pinCount < 4) {
        currentPin += num;
        document.querySelectorAll('.pin-dots .dot')[pinCount].classList.add('filled');
        pinCount++;
        
        if(pinCount === 4) {
            // Verify
            const user = authUsers.find(u => u.pin === currentPin);
            if(user) {
                // Success
                currentUser = user;
                
                // Update Header
                const headerTitle = document.querySelector('.header-greeting h1');
                const profilePic = document.querySelector('.profile-pic');
                if(headerTitle) headerTitle.innerText = `Hola, ${user.name}`;
                if(profilePic) profilePic.innerText = user.name.charAt(0);
                
                setTimeout(() => {
                    document.getElementById('auth-overlay').classList.add('hidden');
                    initUserSession(); // Load their specific data
                }, 400);
            } else {
                // Error
                const dotsContainer = document.querySelector('.pin-dots');
                const dots = document.querySelectorAll('.pin-dots .dot');
                dots.forEach(d => d.classList.add('error'));
                dotsContainer.classList.add('shake-error');
                
                setTimeout(() => {
                    dotsContainer.classList.remove('shake-error');
                    dots.forEach(d => {
                        d.classList.remove('filled');
                        d.classList.remove('error');
                    });
                    currentPin = '';
                    pinCount = 0;
                }, 500);
            }
        }
    }
};

// Remove original pressKey from the document scope if possible by overriding it.
</script>
<script>
// --- STATE MANAGEMENT ---
let currentDay = 1;
let completedDays = [];
let currentPhaseProgress = {};

function initUserSession() {
    if(!currentUser) return;
    
    currentDay = parseInt(localStorage.getItem('mm_currentDay_' + currentUser.id)) || 1;
    completedDays = JSON.parse(localStorage.getItem('mm_completedDays_' + currentUser.id)) || [];
    currentPhaseProgress = JSON.parse(localStorage.getItem('mm_phaseProgress_' + currentUser.id)) || {};
    
    // Find highest incomplete day or 1
    let target = 1;
    while(completedDays.includes(target)) target++;
    if(target > window.mujeresMentorasData.length) target = window.mujeresMentorasData.length;
    
    // Check if target day was manually overridden in currentDay
    if(currentDay > target && completedDays.includes(currentDay-1)) target = currentDay;
    
    loadMujeresMentorasDay(target);
    renderDaySwitcher();
}

function saveProgress() {
    if(!currentUser) return;
    localStorage.setItem('mm_currentDay_' + currentUser.id, currentDay);
    localStorage.setItem('mm_completedDays_' + currentUser.id, JSON.stringify(completedDays));
    localStorage.setItem('mm_phaseProgress_' + currentUser.id, JSON.stringify(currentPhaseProgress));
    updateVisualProgress();
}

function completePhase(phaseNum) {
    if(!currentPhaseProgress[currentDay]) currentPhaseProgress[currentDay] = [];
    if(!currentPhaseProgress[currentDay].includes(phaseNum)) {
        currentPhaseProgress[currentDay].push(phaseNum);
        
        // Auto-complete day if phase 12 is done (or all 12 are done)
        if(currentPhaseProgress[currentDay].length === 12 || phaseNum === 12) {
            if(!completedDays.includes(currentDay)) completedDays.push(currentDay);
        }
        
        saveProgress();
    }
}

function updateVisualProgress() {
    // 1. Overall Track Progress (Day X of 78)
    const ringContent = document.querySelector('.ring-content h2');
    const ringLabel = document.querySelector('.ring-content p');
    if(ringContent) ringContent.innerText = currentDay;
    if(ringLabel) ringLabel.innerText = "Día de 78";
    
    const ringProgress = document.querySelector('.ring-progress');
    if(ringProgress) {
        const total = 78;
        const percentage = currentDay / total;
        // Dasharray is 565. offset = 565 - (565 * percentage)
        const offset = 565 - (565 * percentage);
        ringProgress.style.strokeDashoffset = offset;
    }
    
    // 2. Session Progress (Phases completed)
    const phases = document.querySelectorAll('.timeline .phase');
    const completedInSession = currentPhaseProgress[currentDay] || [];
    
    phases.forEach((phase, idx) => {
        const phaseNum = idx + 1;
        // Update styling
        if(completedInSession.includes(phaseNum)) {
            phase.classList.add('completed');
            phase.classList.remove('active');
        } else if (phaseNum === completedInSession.length + 1) {
            phase.classList.add('active');
            phase.classList.remove('completed');
        } else {
            phase.classList.remove('active');
            phase.classList.remove('completed');
        }
    });
}

function renderComprensionLectora(data, container) {
    if(!data.fase2_lectura.comprension) return;
    const comp = data.fase2_lectura.comprension;
    
    let html = `
    <div style="margin-top: 24px; padding: 16px; background: rgba(0, 198, 255, 0.05); border: 1px solid rgba(0, 198, 255, 0.2); border-radius: 12px;">
        <h5 style="color: var(--accent-water); font-family: 'Outfit'; margin-bottom: 8px;">EXTRA: COMPRENSIÓN LECTORA</h5>
        <p style="font-size: 0.9rem; color: white; margin-bottom: 12px;">${comp.q}</p>
    `;
    
    comp.options.forEach((opt, idx) => {
        html += `
        <label style="display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-secondary); cursor:pointer;">
            <input type="radio" name="comprension" value="${idx}" onchange="checkComprension(${comp.answer}, this)"> ${opt}
        </label>`;
    });
    
    html += `<div id="comp-feedback" style="margin-top: 10px; font-weight:bold; font-size: 0.85rem;"></div></div>`;
    
    const div = document.createElement('div');
    div.innerHTML = html;
    container.appendChild(div);
}

window.checkComprension = function(correctIdx, el) {
    const feedback = document.getElementById('comp-feedback');
    if(parseInt(el.value) === correctIdx) {
        feedback.innerText = "✓ Respuesta correcta. Excelente comprensión táctica.";
        feedback.style.color = "var(--success)";
        completePhase(2); // Auto-complete phase 2
    } else {
        feedback.innerText = "✗ Incorrecto. Revisa el texto e intenta de nuevo.";
        feedback.style.color = "var(--accent-fire)";
    }
}

// Global func to mark manual phases done
window.markPhaseDone = function(btn, phaseNum) {
    btn.innerText = "✓ Completado";
    btn.style.borderColor = "var(--success)";
    btn.style.color = "var(--success)";
    completePhase(phaseNum);
}

function loadMujeresMentorasDay(dayIndex) {
    const data = window.mujeresMentorasData.find(d => d.dia === dayIndex);
    if (!data) return;

    currentDay = dayIndex;
    
    // Update Header
    const badge = document.querySelector('.session-hero .badge-premium');
    if (badge) badge.innerText = `${data.bloque} • Día ${data.dia}`;
    const title = document.querySelector('.session-hero .display-font');
    if (title) title.innerText = data.titulo;

    const phases = document.querySelectorAll('.timeline .phase');
    
    // Generate completion buttons for phases that require manual check
    const manualPhases = [1, 5, 6, 7, 8, 9, 10, 11, 12];
    
    manualPhases.forEach(num => {
        const p = phases[num-1];
        // Clean previous buttons if day changed
        const existingBtn = p.querySelector('.btn-done-phase');
        if(existingBtn) existingBtn.remove();
        
        if(p) {
            const btn = document.createElement('button');
            btn.className = "btn-outline btn-done-phase";
            btn.style = "width: 100%; margin-top: 12px; font-size: 0.8rem;";
            
            // If already done from loaded state, mark it visually
            const completedInSession = currentPhaseProgress[currentDay] || [];
            if(completedInSession.includes(num)) {
                btn.innerText = "✓ Completado";
                btn.style.borderColor = "var(--success)";
                btn.style.color = "var(--success)";
            } else {
                btn.innerText = "Marcar Fase como Completada";
            }
            
            btn.onclick = function() { window.markPhaseDone(this, num); };
            p.appendChild(btn);
        }
    });

    // F1: Ancla
    if (phases[0]) {
        const desc = phases[0].querySelector('.phase-desc');
        if (desc) desc.innerHTML = `<strong>Respiración de Oxigenación:</strong> ${data.fase1_ancla}`;
    }

    // F2: Lectura + Comprension
    if (phases[1]) {
        const reader = document.getElementById('reader-content');
        if (reader) {
            let html = `<h4 style="color: white; margin-bottom: 12px; font-family: 'Outfit'; text-transform: uppercase;">${data.titulo}</h4>`;
            data.fase2_lectura.texto.split('\\n').forEach(p => {
                if(p.trim()) html += `<p class="reader-p">${p}</p>`;
            });
            reader.innerHTML = html;
            
            // Clean old feedback
            const existingComp = phases[1].querySelector('#comp-feedback');
            if(existingComp) existingComp.parentElement.remove();
            
            renderComprensionLectora(data, phases[1]);
        }
    }

    // F3: Vocabulario
    if (phases[2]) {
        const desc = phases[2].querySelector('.phase-desc');
        if (desc) {
            let html = `<strong>Vocabulario Activo:</strong><br>`;
            if(data.fase3_vocabulario) {
                data.fase3_vocabulario.forEach(v => {
                    html += `<span style="color:var(--accent-fire)">${v.palabra}</span>: ${v.definicion}<br>`;
                });
            }
            desc.innerHTML = html;
        }
    }

    // F4: Recall
    if (phases[3]) {
        const testContent = document.getElementById('test-content');
        if (testContent) {
            let html = '';
            data.fase4_recall.forEach((r, idx) => {
                html += `
                <div style="margin-bottom: 20px;" class="recall-q">
                    <span style="font-size: 0.7rem; color: var(--accent-fire); text-transform: uppercase;">${r.type}</span>
                    <p style="font-size: 0.9rem; margin-bottom: 12px; color: white;"><strong>${idx+1}. ${r.q}</strong></p>
                    <textarea class="input-premium" placeholder="Escribe tu respuesta analítica..."></textarea>
                </div>
                `;
            });
            html += `<button class="btn-outline" style="width: 100%; margin-top: 8px;" onclick="window.markPhaseDone(this, 4)">📊 Terminar Evaluación y Avanzar</button>`;
            testContent.innerHTML = html;
        }
    }

    // Replace F5 to F11 texts
    if (phases[4]) { const desc = phases[4].querySelectorAll('.phase-desc')[1]; if(desc) desc.innerText = data.fase5_codificacion_dual; }
    if (phases[5]) { const desc = phases[5].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase6_loci; }
    if (phases[6]) { const desc = phases[6].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase7_analogia; }
    if (phases[7]) { const desc = phases[7].querySelectorAll('.phase-desc')[1]; if(desc) desc.innerText = data.fase8_ejercicio; }
    if (phases[8]) { const desc = phases[8].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase9_feynman ? "Aplica la Técnica Feynman hoy." : "Aplica cada 7 sesiones. Hoy descansa."; }
    if (phases[9]) { const desc = phases[9].querySelectorAll('.phase-desc')[1]; if(desc) desc.innerText = data.fase10_metacognicion; }
    if (phases[10]) { const desc = phases[10].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase11_ensayo; }

    updateVisualProgress();
}

// Navigation UI to switch days
function renderDaySwitcher() {
    const list = document.querySelector('.blocks-list');
    if(!list) return;
    
    let html = `<div style="margin-bottom: 24px; font-family:'Outfit'; font-size:1.1rem; border-bottom:1px solid var(--border-subtle); padding-bottom:10px;">Tu Progreso</div>`;
    
    // We render first 5 days for the pilot
    for(let i=1; i<=10; i++) {
        let isDone = completedDays.includes(i);
        let isActive = currentDay === i;
        
        let isLocked = false;
        if(!isDone && !isActive && i > currentDay) {
            // Check if all previous days are done
            for(let j=1; j<i; j++) {
                if(!completedDays.includes(j)) {
                    isLocked = true;
                    break;
                }
            }
        }
        
        html += `
        <div class="glass-card track-card ${isActive ? 'active' : ''} ${isLocked ? 'locked' : ''}" onclick="if(!${isLocked}) { loadMujeresMentorasDay(${i}); document.querySelector('.blocks-list').innerHTML=''; renderDaySwitcher(); switchTab('view-session', this); }">
            <div class="track-number">${i}</div>
            <div>
                <h4 style="font-size: 0.95rem; color: white;">Día ${i}</h4>
                <p style="font-size: 0.8rem; color: var(--text-secondary);">${isDone ? '✓ Completado' : (isActive ? 'Activo' : 'Bloqueado')}</p>
            </div>
        </div>`;
    }
    
    list.innerHTML = html;
}

document.addEventListener("DOMContentLoaded", () => {
    if (window.mujeresMentorasData) {
        // Let's hook into the dashboard button so we can render the switcher
        const oldSwitchTab = window.switchTab;
        window.switchTab = function(viewId, el) {
            if(oldSwitchTab) oldSwitchTab(viewId, el);
            if(viewId === 'view-dashboard') {
                renderDaySwitcher();
            }
        };
    }
    
    // We remove the old static dummy pressKey and initialization.
    // Initialization now only happens when a user types the correct PIN (initUserSession).
});

// Clean up original pressKey from the global scope if it exists as a script block
// (The previous pressKey in the old code is effectively overridden because this script block is after it).
</script>
</body>"""

    # Wait, the original pressKey() was inside the old HTML block, before the start_marker.
    # To prevent two pressKey declarations, I can remove the old pressKey function from the HTML using regex.
    content = re.sub(r'let pinCount = 0;\s*function pressKey\(\) \{.*?\n\s*\}\s*\}', '', content, flags=re.DOTALL)
    
    content = pre_content + new_script
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected PIN logic and user database.")
else:
    print("Could not find start marker.")
