import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

tracking_logic = """
<script>
// --- PLAYBOOK & KIT SYNC (Supabase: user_mentee_tracking) ---
let currentTracking = {
    mentee_name: '',
    objetivos: [],
    compromisos: [],
    toolkit: {}
};

async function loadMenteeTracking() {
    if (!currentUser) return;
    try {
        const { data, error } = await _supabase
            .from('user_mentee_tracking')
            .select('*')
            .eq('user_pin', currentUser.pin)
            .single();
            
        if (data) {
            currentTracking = {
                mentee_name: data.mentee_name || '',
                objetivos: data.objetivos || [],
                compromisos: data.compromisos || [],
                toolkit: data.toolkit || {}
            };
            renderPlaybookUI();
            renderKitUI();
        } else if (error && error.code === 'PGRST116') {
            // Not found, insert new record
            await _supabase.from('user_mentee_tracking').insert([{
                user_pin: currentUser.pin,
                mentee_name: '',
                objetivos: [],
                compromisos: [],
                toolkit: {}
            }]);
        }
    } catch(e) {
        console.error("Error loadMenteeTracking:", e);
    }
}

async function saveMenteeTracking() {
    if (!currentUser) return;
    try {
        const { error } = await _supabase
            .from('user_mentee_tracking')
            .update({
                mentee_name: currentTracking.mentee_name,
                objetivos: currentTracking.objetivos,
                compromisos: currentTracking.compromisos,
                toolkit: currentTracking.toolkit
            })
            .eq('user_pin', currentUser.pin);
            
        if (error) console.error("Error saveMenteeTracking:", error);
    } catch(e) {
        console.error(e);
    }
}

// --- PLAYBOOK UI BINDINGS ---
function guardarMenteeName() {
    const el = document.getElementById('mp-name');
    if (el) {
        currentTracking.mentee_name = el.value;
        saveMenteeTracking();
    }
}

function renderPlaybookUI() {
    const nameEl = document.getElementById('mp-name');
    if (nameEl) nameEl.value = currentTracking.mentee_name;
    
    // Render Goals
    const goalsContainer = document.getElementById('mp-goals-list');
    if (goalsContainer) {
        goalsContainer.innerHTML = currentTracking.objetivos.map((obj, i) => `
            <div class="mp-item">
                <input type="checkbox" onchange="toggleObjetivo(${i})" ${obj.done ? 'checked' : ''}>
                <span style="text-decoration: ${obj.done ? 'line-through' : 'none'}; opacity: ${obj.done ? '0.5' : '1'}">${obj.text}</span>
            </div>
        `).join('') || '<div style="color:var(--text-dim);font-size:0.85rem;">No hay objetivos registrados.</div>';
    }
    const goalsCount = document.getElementById('mp-goals-count');
    if(goalsCount) goalsCount.innerText = currentTracking.objetivos.filter(o => o.done).length + '/' + currentTracking.objetivos.length;

    // Render Commitments
    const commitsContainer = document.getElementById('mp-commits-list');
    if (commitsContainer) {
        commitsContainer.innerHTML = currentTracking.compromisos.map((com, i) => `
            <div class="mp-item">
                <input type="checkbox" onchange="toggleCompromiso(${i})" ${com.done ? 'checked' : ''}>
                <span style="text-decoration: ${com.done ? 'line-through' : 'none'}; opacity: ${com.done ? '0.5' : '1'}">${com.text}</span>
            </div>
        `).join('') || '<div style="color:var(--text-dim);font-size:0.85rem;">No hay compromisos registrados.</div>';
    }
    const commitCount = document.getElementById('mp-commit-count');
    if(commitCount) commitCount.innerText = currentTracking.compromisos.filter(c => c.done).length + '/' + currentTracking.compromisos.length;
}

window.addObjetivo = function() {
    const text = prompt("Nuevo objetivo para la mentoreada:");
    if (text && text.trim()) {
        currentTracking.objetivos.push({ text: text.trim(), done: false });
        renderPlaybookUI();
        saveMenteeTracking();
    }
}

window.toggleObjetivo = function(i) {
    currentTracking.objetivos[i].done = !currentTracking.objetivos[i].done;
    renderPlaybookUI();
    saveMenteeTracking();
}

window.addCompromiso = function() {
    const text = prompt("Nuevo compromiso de la sesión:");
    if (text && text.trim()) {
        currentTracking.compromisos.push({ text: text.trim(), done: false });
        renderPlaybookUI();
        saveMenteeTracking();
    }
}

window.toggleCompromiso = function(i) {
    currentTracking.compromisos[i].done = !currentTracking.compromisos[i].done;
    renderPlaybookUI();
    saveMenteeTracking();
}

// --- MI KIT UI BINDINGS ---
function renderKitUI() {
    // Populate textarea inputs if they exist with toolkit data
    document.querySelectorAll('.kit-view textarea').forEach(ta => {
        if (ta.id && currentTracking.toolkit[ta.id]) {
            ta.value = currentTracking.toolkit[ta.id];
        }
    });
}

function guardarKit(id) {
    const el = document.getElementById(id);
    if (el) {
        currentTracking.toolkit[id] = el.value;
        saveMenteeTracking();
    }
}

// Hook into initUserSession
const oldInit = window.initUserSession;
window.initUserSession = function() {
    if(oldInit) oldInit();
    loadMenteeTracking();
};

</script>
</body>
"""

if 'user_mentee_tracking' not in text:
    text = text.replace('</body>', tracking_logic)
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Injected user_mentee_tracking sync logic!")
else:
    print("Already injected.")
