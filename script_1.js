
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
