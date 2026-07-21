
// --- PLAYBOOK LOGIC ---
let playbookSaveTimeout = null;

async function loadPlaybookDay(dayIndex) {
    if(!currentUser) return;
    const contentArea = document.getElementById('playbook-content-area');
    
    if(!dayIndex) {
        contentArea.innerHTML = '<div style="text-align:center; padding: 40px 0; color: var(--text-tertiary);">Selecciona un día para ver o escribir tus apuntes...</div>';
        return;
    }
    
    contentArea.innerHTML = '<div style="text-align:center; padding: 40px 0; color: var(--text-tertiary);">Cargando tus apuntes...</div>';
    
    // Fetch existing notes for this day
    const { data: notes, error } = await _supabase
        .from('user_playbook_notes')
        .select('*')
        .eq('user_pin', currentUser.pin)
        .eq('day_index', parseInt(dayIndex));
        
    let noteDict = {};
    if(notes) {
        notes.forEach(n => noteDict[n.note_type] = n.note_content || '');
    }
    
    const renderTextarea = (type, placeholder, label, color) => `
        <div style="background: rgba(255,255,255,0.03); border-left: 2px solid ${color}; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <h3 style="color: white; font-size: 1.05rem; margin-bottom: 8px; font-family:'Outfit';">${label}</h3>
            <textarea 
                data-note-type="${type}" 
                data-day="${dayIndex}"
                oninput="debouncedSavePlaybookNote(this)"
                placeholder="${placeholder}"
                style="width: 100%; height: 120px; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); color: #fff; padding: 12px; border-radius: 8px; font-family: 'Inter'; font-size: 0.9rem; resize: vertical; outline: none; transition: border-color 0.3s;"
                onfocus="this.style.borderColor='${color}'"
                onblur="this.style.borderColor='rgba(255,255,255,0.1)'"
            >${noteDict[type] || ''}</textarea>
            <div class="save-status" id="status-${type}" style="font-size: 0.75rem; color: var(--text-tertiary); margin-top: 5px; text-align: right; min-height: 15px;"></div>
        </div>
    `;

    contentArea.innerHTML = `
        <h3 style="color: var(--accent-water); margin-bottom: 20px; font-family: 'Outfit'; font-weight: 300;">DÍA ${dayIndex}</h3>
        ${renderTextarea('recall_activo', 'Tus reflexiones personales de la Fase 4 (Recall Activo)...', 'Recall Activo (Fase 4)', 'var(--accent-water)')}
        ${renderTextarea('ejercicio_fase8', 'Tus apuntes tácticos, aprendizajes o tareas de la Fase 8...', 'Ejercicio Práctico (Fase 8)', '#FFD700')}
        ${renderTextarea('reflexion_libre', 'Insights adicionales, ideas espontáneas o victorias del día...', 'Reflexión Libre', '#9370DB')}
    `;
}

function debouncedSavePlaybookNote(textarea) {
    const type = textarea.getAttribute('data-note-type');
    const statusDiv = document.getElementById(`status-${type}`);
    statusDiv.innerText = 'Guardando...';
    
    if(playbookSaveTimeout) clearTimeout(playbookSaveTimeout);
    playbookSaveTimeout = setTimeout(() => {
        savePlaybookNote(textarea.getAttribute('data-day'), type, textarea.value, statusDiv);
    }, 1500); // 1.5 second debounce
}

async function savePlaybookNote(dayIndex, noteType, content, statusDiv) {
    if(!currentUser) return;
    
    // Upsert note
    const { error } = await _supabase
        .from('user_playbook_notes')
        .upsert({
            user_pin: currentUser.pin,
            day_index: parseInt(dayIndex),
            note_type: noteType,
            note_content: content
        }, { onConflict: 'user_pin, day_index, note_type' });
        
    if(error) {
        console.error("Error guardando nota:", error);
        if(statusDiv) statusDiv.innerText = 'Error al guardar';
    } else {
        if(statusDiv) {
            statusDiv.innerText = 'Guardado en la nube ✓';
            setTimeout(() => { if(statusDiv.innerText.includes('✓')) statusDiv.innerText = ''; }, 3000);
        }
    }
}

// Hook into the tab switcher to populate the day selector
const originalPlaybookSwitchTab = switchTab;
switchTab = function(viewId, element) {
    originalPlaybookSwitchTab(viewId, element);
    if(viewId === 'view-libreta') {
        populatePlaybookDays();
    }
};

function populatePlaybookDays() {
    const selector = document.getElementById('playbook-day-selector');
    if(!selector) return;
    selector.innerHTML = '<option value="">-- Selecciona el Día --</option>';
    
    // Check maxUnlockedDay from dashboard
    let maxDay = (typeof maxUnlockedDay !== 'undefined') ? maxUnlockedDay : 78;
    
    for(let i=1; i<=maxDay; i++) {
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = `Día ${i}`;
        selector.appendChild(opt);
    }
    
    if(window.currentDayIndex && window.currentDayIndex <= maxDay) {
        selector.value = window.currentDayIndex;
        loadPlaybookDay(window.currentDayIndex);
    }
}
