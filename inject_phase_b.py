import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add currentAnswers global variable (if not exists)
if 'let currentAnswers = {};' not in content:
    content = content.replace('let currentPhaseProgress = {};', 'let currentPhaseProgress = {};\nlet currentAnswers = {};')

# 2. Add MI MENTADA tab to nav
if 'view-mentada' not in content:
    nav_tab_html = '<div class="nav-item mentada-tab-btn" style="display:none;" onclick="switchTab(\'view-mentada\', this)"><div class="nav-icon">👥</div><span class="nav-label">MI MENTADA</span></div>'
    content = content.replace('</nav>', f'    {nav_tab_html}\n        </nav>')

# 3. Add view-mentada HTML block
if 'id="view-mentada"' not in content:
    view_mentada_html = """
        <!-- PANEL MI MENTADA -->
        <div id="view-mentada" class="view" style="padding: 80px 20px 100px;">
            <h2 style="font-family: 'Outfit'; font-weight: 300; letter-spacing: 2px;">PANEL DE MONITOREO</h2>
            <div id="mentada-dashboard-content" style="margin-top: 30px;">
                <!-- Rendered via JS -->
            </div>
        </div>
    """
    content = content.replace('<nav class="bottom-nav">', f'{view_mentada_html}\n        <nav class="bottom-nav">')

# 4. Inject script logic
logic_script = """
<script>
// --- FASE B: DASHBOARD Y RESPUESTAS ---
async function loadMentadaDashboard() {
    const content = document.getElementById('mentada-dashboard-content');
    content.innerHTML = '<p style="color:#aaa;">Buscando conexión con tu mentada...</p>';
    
    // Get Mentada ID
    const { data: mentadaUser } = await _supabase.from('mentoras_users').select('*').eq('assigned_mentor_id', currentUser.id).single();
    if(!mentadaUser) {
        content.innerHTML = '<p style="color:#aaa;">Aún no tienes una mentada asignada en el sistema.</p>';
        return;
    }
    
    // Get Mentada Progress
    const { data: mentadaProgress } = await _supabase.from('mentoras_progress').select('*').eq('user_id', mentadaUser.id).single();
    
    let day = mentadaProgress ? mentadaProgress.current_day : 1;
    let answers = mentadaProgress && mentadaProgress.answers ? mentadaProgress.answers : {};
    
    let html = `<div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; margin-bottom: 30px;">
         <h3 style="margin-bottom: 5px; color: var(--accent-water); font-size:1.3rem;">${mentadaUser.name} ${mentadaUser.full_name.replace(mentadaUser.name, '').trim()}</h3>
         <p style="font-size: 0.9rem; color: #aaa; text-transform: uppercase; letter-spacing: 1px;">Día actual: ${day} de 78</p>
    </div>`;
    
    html += `<h3 style="font-family: 'Outfit'; font-weight:300; letter-spacing:1px; margin-bottom:15px;">Respuestas y Reflexiones</h3>`;
    html += `<div style="display:flex; flex-direction:column; gap:15px;">`;
    
    let hasAnswers = false;
    for(let d in answers) {
        if(answers[d].trim() !== '') {
            hasAnswers = true;
            html += `<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">
                 <span style="color: var(--accent-earth); font-size: 0.8rem; text-transform: uppercase;">Día ${d}</span>
                 <p style="margin-top: 10px; font-size: 0.95rem; line-height: 1.5; color: #ddd; white-space: pre-wrap;">${answers[d]}</p>
            </div>`;
        }
    }
    
    if(!hasAnswers) {
        html += `<p style="font-size: 0.9rem; color: #888;">Tu mentada aún no ha guardado respuestas de texto en el sistema.</p>`;
    }
    html += `</div>`;
    content.innerHTML = html;
}

// Hook into switchTab
const originalSwitchTab = switchTab;
switchTab = function(viewId, element) {
    originalSwitchTab(viewId, element);
    if(viewId === 'view-mentada') {
        loadMentadaDashboard();
    }
};
</script>
"""
if 'loadMentadaDashboard' not in content:
    content = content.replace('</body>', logic_script + '\n</body>')


# 5. Patch saveProgress to include currentAnswers
# We need to find the injected saveProgress and update it.
# The previous injection was:
# await _supabase.from('mentoras_progress').upsert({
#    user_id: currentUser.id,
#    current_day: currentDay,
#    completed_days: completedDays,
#    phase_progress: currentPhaseProgress,
#    updated_at: new Date().toISOString()
#});

if 'answers: currentAnswers' not in content:
    content = content.replace(
        'phase_progress: currentPhaseProgress,', 
        'phase_progress: currentPhaseProgress,\n        answers: currentAnswers,'
    )

# 6. Patch initUserSession to load answers and show Mentada tab
if 'currentAnswers = data.answers || {};' not in content:
    content = content.replace(
        'currentPhaseProgress = data.phase_progress || {};',
        'currentPhaseProgress = data.phase_progress || {};\n        currentAnswers = data.answers || {};'
    )
    content = content.replace(
        'currentPhaseProgress = {};\n    }',
        'currentPhaseProgress = {};\n        currentAnswers = {};\n    }'
    )
    
    # Show mentada tab if role is Mentora
    show_tab_logic = """
    if(currentUser.role === 'Mentora') {
        const mentadaTab = document.querySelector('.mentada-tab-btn');
        if(mentadaTab) mentadaTab.style.display = 'flex';
    }
    """
    content = content.replace('renderDaySwitcher();', 'renderDaySwitcher();\n' + show_tab_logic)


# 7. Patch marcarHecho to save answers
# We need to find function marcarHecho(btn)
# When the user clicks the button, if there is a textarea in the previous sibling or same container, extract it.
# Let's override marcarHecho entirely or just inject inside it.
# function marcarHecho(btn) is defined around line 603.
patch_marcar = """
    // FASE B: Extract textarea answers before marking complete
    const container = btn.closest('.content-box');
    if(container) {
        const textareas = container.querySelectorAll('textarea');
        if(textareas.length > 0) {
            let combinedAnswer = '';
            textareas.forEach(ta => {
                if(ta.value.trim()) combinedAnswer += ta.value.trim() + "\\n\\n";
            });
            if(combinedAnswer) {
                currentAnswers[currentDay] = combinedAnswer.trim();
            }
        }
    }
"""

if 'const container = btn.closest' not in content:
    # Inject right after function marcarHecho(btn) {
    content = content.replace('function marcarHecho(btn) {\n', 'function marcarHecho(btn) {\n' + patch_marcar)


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected Phase B successfully.")
