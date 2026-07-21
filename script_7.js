
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



// --- INJECTED KIT PROTOCOL LOGIC ---
const CRISIS_DATA = [{"id": "no_avanza", "icon": "😶", "title": "Mi mentoreada no avanza", "steps": ["Define: es un problema de habilidad o de voluntad? Son soluciones distintas.", "Si es habilidad: redisena el ejercicio de riesgo tactico. Hazlo mas pequeno y concreto.", "Si es voluntad: preguntale directamente: 'En una escala del 1 al 10, que tan comprometida estas con este cambio?'", "Cualquier numero menor a 7: 'Que tendria que pasar para que sea un 10?' Escucha sin interrumpir."]}, {"id": "llora", "icon": "😢", "title": "Rompe en llanto en sesion", "steps": ["No la interrumpas. No busques el panuela. No digas 'no llores'. Sostenla con silencio.", "Despues de 60 segundos: 'Gracias por confiar en este espacio. Que necesitas ahora?'", "No conviertas la sesion en terapia. Si el llanto revela algo mas profundo, deriva a un profesional.", "Cierra con un pequeno acto de agencia: 'Dime una cosa que SI puedes controlar esta semana'."]}, {"id": "resistencia", "icon": "🧱", "title": "Resistencia y defensividad", "steps": ["No argumentes. La resistencia no se vence con logica, se disuelve con preguntas.", "Lanza: 'Entiendo que esto se siente injusto. Que tendria que ser verdad para que este feedback fuera valioso para ti?'", "Si sigue resistente: 'No tengo que convencerte. Toma lo que te sirve y deja lo que no. Que fue lo unico util de hoy?'", "Termina ahi. La sesion que produce una sola pepita de oro fue exitosa."]}, {"id": "dependencia", "icon": "🔗", "title": "Se esta volviendo dependiente", "steps": ["Detecta la senal: te llama fuera de sesion, te pide permiso para decidir, espera tu aprobacion.", "En la proxima sesion nombralo directo: 'Noto que buscas mi validacion antes de actuar. Que pasaria si actuaras sin pedirmela?'", "Redirige la pregunta hacia ella siempre: cuando te pregunte que hacer, responde '?Tu que crees?'", "Recuerda: tu éxito como mentora es hacerte innecesaria. Mide tu impacto en su autonomia."]}, {"id": "limites", "icon": "⚠️", "title": "Cruzo un limite", "steps": ["Nombra lo que ocurrio en el momento, no dias despues: 'Cuando dijiste X, senti que ese espacio cruzo el limite de nuestra relacion de mentoria.'", "Reafirma el marco: 'Esta relacion es de mentoria profesional. Eso significa...'", "Si cruzo un limite etico grave (confidencialidad, acoso): documenta y consulta con tu supervisor antes de la proxima sesion.", "No necesitas disculparte por tener limites. Los limites claros son el regalo mas grande que le puedes dar."]}, {"id": "estancada", "icon": "🔄", "title": "La sesion no llego a ningún lado", "steps": ["Acepta que no todas las sesiones producen avances visibles. Algunas siembran.", "Preguntate: di demasiados consejos? Hable mas del 40% del tiempo? Esas son senales de que la sesion fue tuya, no de ella.", "En la proxima sesion abre con: 'La ultima vez senti que no llegamos a nada profundo. Que crees que faltó?'", "Recalibra tu rol: tu trabajo no es resolver, es preguntar. Prepara 3 preguntas poderosas antes de la sesion."]}];

window.abrirCrisisMM = function(id) {
    const data = CRISIS_DATA.find(c => c.id === id);
    if (!data) return;
    const m = document.getElementById('crisis-modal-mm');
    const t = document.getElementById('crisis-mm-title');
    const ct = document.getElementById('crisis-mm-content');
    if (!m || !t || !ct) return;
    t.textContent = data.icon + ' ' + data.title;
    let html = '<div style="display:flex;flex-direction:column;gap:14px;margin-bottom:40px">';
    data.steps.forEach((s, i) => {
      html += '<div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:16px;padding:16px;display:flex;gap:12px;align-items:flex-start">';
      html += '<div style="min-width:28px;height:28px;border-radius:50%;background:' + ACCENT + ';display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.78rem;color:#fff;flex-shrink:0">' + (i+1) + '</div>';
      html += '<p style="font-size:.85rem;color:#fff;line-height:1.6;margin-top:1px">' + s + '</p></div>';
    });
    html += '</div>';
    ct.innerHTML = html;
    m.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  window.cerrarCrisisMM = function() {
    const m = document.getElementById('crisis-modal-mm');
    if (m) m.classList.remove('active');
    document.body.style.overflow = '';
  };

  window.abrirCaso = function(idx) {
    const caso = CASOS_DATA[idx];
    if (!caso) return;
    const m = document.getElementById('sala-modal');
    const t = document.getElementById('sala-title');
    const ct = document.getElementById('sala-content');
    if (!m || !t || !ct) return;
    t.textContent = caso.title;
    let html = '<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px;margin-bottom:20px;font-size:.85rem;color:#ddd;line-height:1.7">' + caso.setup + '</div>';
    html += '<div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px">OPCIONES</div>';
    html += '<div id="sala-opts">';
    caso.options.forEach((opt, i) => {
      html += '<button class="opt-btn" onclick="elegirOpcion(' + idx + ',' + i + ')">';
      html += '<strong>' + ['A','B','C','D'][i] + '.</strong> ' + opt.label;
      html += '</button>';
    });
    html += '</div>';
    html += '<div id="sala-feedback" style="display:none;margin-top:20px"></div>';
    html += '<div id="sala-prompt-wrap" style="display:none;margin-top:20px"><div style="font-size:.78rem;color:' + ACCENT + ';font-weight:600;margin-bottom:10px">' + (caso.prompt||'Tu reflexión:') + '</div><textarea id="sala-answer" style="width:100%;min-height:90px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:12px;color:#fff;font-family:Inter;font-size:.85rem" placeholder="Escribe aquí..."></textarea><button onclick="guardarCaso(' + idx + ')" style="margin-top:12px;width:100%;padding:13px;background:linear-gradient(135deg,' + ACCENT + ',#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer">Guardar mi reflexión</button></div>';
    ct.innerHTML = html;
    m.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  window.elegirOpcion = function(casoIdx, optIdx) {
    const caso = CASOS_DATA[casoIdx];
    const opt = caso.options[optIdx];
    document.querySelectorAll('.opt-btn').forEach((btn, i) => {
      btn.style.borderColor = (i === optIdx) ? (opt.correct ? '#10b981' : '#ef4444') : 'rgba(255,255,255,.06)';
      btn.style.opacity = (i === optIdx) ? '1' : '.4';
    });
    const fb = document.getElementById('sala-feedback');
    const color = opt.correct ? '#10b981' : '#ef4444';
    fb.style.display = 'block';
    fb.innerHTML = '<div style="background:rgba(255,255,255,.03);border:1px solid ' + color + ';border-radius:14px;padding:16px"><div style="color:' + color + ';font-weight:600;margin-bottom:8px">' + (opt.correct ? '✓ ' : '✗ ') + opt.concept + '</div><p style="font-size:.83rem;color:#ddd;line-height:1.6">' + opt.feedback + '</p></div>';
    document.getElementById('sala-prompt-wrap').style.display = 'block';
  };

  window.guardarCaso = function(idx) {
    const ans = document.getElementById('sala-answer').value.trim();
    if (!ans) return;
    localStorage.setItem('mm_b1_caso_' + idx, ans);
    window.cerrarSala();
    window.renderKitMentoria();
  };

  window.cerrarSala = function() {
    const m = document.getElementById('sala-modal');
    if (m) m.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Render on tab switch
  const _origSwitch = window.switchTab;
  window.switchTab = function(viewId, navEl) {
    if (_origSwitch) _origSwitch(viewId, navEl);
    if (viewId === 'view-kit') window.renderKitMentoria();
    if (viewId === 'view-libreta' && typeof window.renderMenteePanel === 'function') window.renderMenteePanel();
  };

})();

/* MI MENTOREADA — Objetivos SMART, Calendario, Bitácora, Compromisos (MVP) */
/* Llaves globales (no prefijadas por bloque) para que persistan entre los 8 archivos Bloque_Premium.html */
(function(){
  const K = {
    name: 'invictus_pair_mentee_name',
    goals: 'invictus_pair_goals',
    calendar: 'invictus_pair_calendar',
    bitacora: 'invictus_pair_bitacora',
    compromisos: 'invictus_pair_compromisos'
  };
  const ACCENT2 = '#FF5E00';

  function getArr(key) {
    try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch(e) { return []; }
  }
  function setArr(key, arr) { localStorage.setItem(key, JSON.stringify(arr)); }
  function newId() { return 'id' + Date.now() + Math.floor(Math.random()*1000); }
  function fmtDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso + 'T00:00:00');
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleDateString('es-ES', { day: '2-digit', month: 'short' });
  }

  window.guardarMenteeName = function() {
    const el = document.getElementById('mp-name');
    if (el) localStorage.setItem(K.name, el.value);
  };

  window.renderMenteePanel = function() {
    const nameEl = document.getElementById('mp-name');
    if (nameEl) nameEl.value = localStorage.getItem(K.name) || '';

    const goals = getArr(K.goals);
    const activeGoals = goals.filter(g => g.status !== 'logrado' && g.status !== 'pausado');
    const goalsCountEl = document.getElementById('mp-goals-count');
    if (goalsCountEl) goalsCountEl.textContent = activeGoals.length;

    const cal = getArr(K.calendar).filter(c => !c.done).sort((a,b) => (a.date||'').localeCompare(b.date||''));
    const nextEl = document.getElementById('mp-next-session');
    if (nextEl) nextEl.textContent = cal.length ? fmtDate(cal[0].date) : '—';

    const comp = getArr(K.compromisos).filter(c => !c.done);
    const compEl = document.getElementById('mp-compromisos-count');
    if (compEl) compEl.textContent = comp.length;
  };

  window.cerrarMentee = function() {
    document.getElementById('mentee-modal').style.display = 'none';
  };

  window.abrirMentee = function(section) {
    const titles = { goals: '🎯 Objetivos SMART', calendar: '📅 Calendario de Sesiones', bitacora: '📓 Bitácora', compromisos: '✅ Compromisos y Seguimiento' };
    document.getElementById('mentee-modal-title').textContent = titles[section] || '';
    renderSection(section);
    document.getElementById('mentee-modal').style.display = 'block';
  };

  function renderSection(section) {
    const ct = document.getElementById('mentee-modal-content');
    if (section === 'goals') ct.innerHTML = goalsHTML();
    else if (section === 'calendar') ct.innerHTML = calendarHTML();
    else if (section === 'bitacora') ct.innerHTML = bitacoraHTML();
    else if (section === 'compromisos') ct.innerHTML = compromisosHTML();
  }

  function itemCard(inner, extraStyle) {
    return '<div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px;margin-bottom:10px;' + (extraStyle||'') + '">' + inner + '</div>';
  }

  // --- OBJETIVOS SMART ---
  function goalsHTML() {
    const goals = getArr(K.goals);
    let list = goals.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Todavía no hay objetivos. Define el primero abajo — específico, medible y con fecha.</p>';
    goals.slice().reverse().forEach(g => {
      const doneStyle = g.status === 'logrado' ? 'opacity:.5;text-decoration:line-through;' : '';
      list += itemCard(
        '<p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + g.text + '</p>' +
        '<p style="color:' + ACCENT2 + ';font-size:.75rem;margin-top:6px;">Meta: ' + g.metric + ' · Fecha: ' + fmtDate(g.date) + '</p>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (g.status !== 'logrado' ? '<button onclick="marcarGoalLogrado(\'' + g.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Logrado</button>' : '') +
        '<button onclick="eliminarGoal(\'' + g.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nuevo objetivo SMART</div>
        <input id="goal-text" placeholder="¿Qué quiere lograr? (Específico)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="goal-metric" placeholder="¿Cómo se mide el éxito? (Medible)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="goal-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarGoal()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar objetivo</button>
      </div>`;
    return list;
  }
  window.agregarGoal = function() {
    const text = document.getElementById('goal-text').value.trim();
    const metric = document.getElementById('goal-metric').value.trim();
    const date = document.getElementById('goal-date').value;
    if (!text) return;
    const goals = getArr(K.goals);
    goals.push({ id: newId(), text: text, metric: metric || 'Sin definir', date: date, status: 'activo' });
    setArr(K.goals, goals);
    renderSection('goals');
    window.renderMenteePanel();
  };
  window.marcarGoalLogrado = function(id) {
    const goals = getArr(K.goals);
    const g = goals.find(x => x.id === id);
    if (g) g.status = 'logrado';
    setArr(K.goals, goals);
    renderSection('goals');
    window.renderMenteePanel();
  };
  window.eliminarGoal = function(id) {
    setArr(K.goals, getArr(K.goals).filter(x => x.id !== id));
    renderSection('goals');
    window.renderMenteePanel();
  };

  // --- CALENDARIO ---
  function calendarHTML() {
    const cal = getArr(K.calendar).slice().sort((a,b) => (a.date||'').localeCompare(b.date||''));
    let list = cal.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">No hay sesiones agendadas todavía.</p>';
    cal.forEach(c => {
      const doneStyle = c.done ? 'opacity:.5;text-decoration:line-through;' : '';
      list += itemCard(
        '<div style="display:flex;justify-content:space-between;align-items:flex-start;">' +
        '<div><p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + fmtDate(c.date) + ' — ' + (c.note || 'Sesión de mentoría') + '</p></div>' +
        '</div>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (!c.done ? '<button onclick="marcarSesionHecha(\'' + c.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Realizada</button>' : '') +
        '<button onclick="eliminarSesion(\'' + c.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Agendar sesión</div>
        <input id="cal-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="cal-note" placeholder="Tema o nota (opcional)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarSesion()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Agendar</button>
      </div>`;
    return list;
  }
  window.agregarSesion = function() {
    const date = document.getElementById('cal-date').value;
    const note = document.getElementById('cal-note').value.trim();
    if (!date) return;
    const cal = getArr(K.calendar);
    cal.push({ id: newId(), date: date, note: note, done: false });
    setArr(K.calendar, cal);
    renderSection('calendar');
    window.renderMenteePanel();
  };
  window.marcarSesionHecha = function(id) {
    const cal = getArr(K.calendar);
    const c = cal.find(x => x.id === id);
    if (c) c.done = true;
    setArr(K.calendar, cal);
    renderSection('calendar');
    window.renderMenteePanel();
  };
  window.eliminarSesion = function(id) {
    setArr(K.calendar, getArr(K.calendar).filter(x => x.id !== id));
    renderSection('calendar');
    window.renderMenteePanel();
  };

  // --- BITÁCORA ---
  function bitacoraHTML() {
    const log = getArr(K.bitacora).slice().reverse();
    let list = log.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Sin entradas todavía. Registra lo que pasó en tu última sesión.</p>';
    log.forEach(b => {
      list += itemCard(
        '<p style="color:' + ACCENT2 + ';font-size:.72rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">' + fmtDate(b.date) + '</p>' +
        '<p style="color:#ddd;font-size:.85rem;line-height:1.6;">' + b.text + '</p>' +
        '<button onclick="eliminarBitacora(\'' + b.id + '\')" style="margin-top:10px;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:6px 10px;font-size:.72rem;cursor:pointer;">Eliminar</button>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nueva entrada (hoy)</div>
        <textarea id="bit-text" placeholder="¿Qué pasó en la sesión? ¿Qué notaste?" style="width:100%;min-height:90px;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;"></textarea>
        <button onclick="agregarBitacora()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar en bitácora</button>
      </div>`;
    return list;
  }
  window.agregarBitacora = function() {
    const text = document.getElementById('bit-text').value.trim();
    if (!text) return;
    const log = getArr(K.bitacora);
    const today = new Date().toISOString().slice(0,10);
    log.push({ id: newId(), date: today, text: text });
    setArr(K.bitacora, log);
    renderSection('bitacora');
  };
  window.eliminarBitacora = function(id) {
    setArr(K.bitacora, getArr(K.bitacora).filter(x => x.id !== id));
    renderSection('bitacora');
  };

  // --- COMPROMISOS Y SEGUIMIENTO ---
  function compromisosHTML() {
    const comp = getArr(K.compromisos).slice().reverse();
    let list = comp.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Sin compromisos registrados todavía.</p>';
    comp.forEach(c => {
      const doneStyle = c.done ? 'opacity:.5;text-decoration:line-through;' : '';
      const ownerTag = c.owner === 'mentora' ? 'Tuyo (mentora)' : 'De ella (mentoreada)';
      list += itemCard(
        '<p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + c.text + '</p>' +
        '<p style="color:' + ACCENT2 + ';font-size:.72rem;margin-top:6px;">' + ownerTag + (c.date ? (' · Vence: ' + fmtDate(c.date)) : '') + '</p>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (!c.done ? '<button onclick="marcarCompromisoHecho(\'' + c.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Cumplido</button>' : '') +
        '<button onclick="eliminarCompromiso(\'' + c.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nuevo compromiso</div>
        <input id="comp-text" placeholder="¿Qué se comprometió a hacer?" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <select id="comp-owner" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
          <option value="mentoreada">De la mentoreada</option>
          <option value="mentora">Tuyo (mentora)</option>
        </select>
        <input id="comp-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarCompromiso()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar compromiso</button>
      </div>`;
    return list;
  }
  window.agregarCompromiso = function() {
    const text = document.getElementById('comp-text').value.trim();
    const owner = document.getElementById('comp-owner').value;
    const date = document.getElementById('comp-date').value;
    if (!text) return;
    const comp = getArr(K.compromisos);
    comp.push({ id: newId(), text: text, owner: owner, date: date, done: false });
    setArr(K.compromisos, comp);
    renderSection('compromisos');
    window.renderMenteePanel();
  };
  window.marcarCompromisoHecho = function(id) {
    const comp = getArr(K.compromisos);
    const c = comp.find(x => x.id === id);
    if (c) c.done = true;
    setArr(K.compromisos, comp);
    renderSection('compromisos');
    window.renderMenteePanel();
  };
  window.eliminarCompromiso = function(id) {
    setArr(K.compromisos, getArr(K.compromisos).filter(x => x.id !== id));
    renderSection('compromisos');
    window.renderMenteePanel();
  };

})();


/* THETA SCRIPTS DATA */
window.THETA_SCRIPTS = {1: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza a la mujer que eras cuando recibiste tu primer cargo de liderazgo... Como se veia? Como se movia? Ahora visualiza a la mujer que eres hoy. Nota la distancia entre ellas... esa distancia es tu identidad construida... no heredada, no prestada... construida. Ahora preguntate: en tu proxima sesion con tu mentoreada... ¿desde cual de estas dos mujeres vas a hablar? La que esperaba permiso... o la que ya sabe que el permiso era suyo desde el principio. Siente como tu columna se alarga. Tu voz se asienta. Tu presencia ocupa el espacio completo que te corresponde. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 2: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Imagina que puedes ver tu propia biologia... millones de celulas que no son un destino fijo sino una conversacion constante con tu entorno. Cada vez que decides actuar como lider antes de sentirte lista... esas celulas reciben una instruccion nueva. Cada vez que pones en cuestion una creencia limitante... la expresion genetica cambia. Visualiza ahora a tu mentoreada. Ella lleva en su biologia patrones de mujeres que no tuvieron voz. Tu presencia como mentora le da a esas celulas una instruccion diferente: el poder es posible. El liderazgo es tuyo. No estas solo cambiando su carrera. Estas modificando su linea biologica. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 3: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza la voz critica que mas te visita antes de una sesion difícil. No la pelees. Solo observala como si fuera un personaje pequeno que grita desde lejos... Sus palabras llegan pero no tienen poder sobre tu cuerpo. Tu respiras. Tu permaneces. Ahora visualiza a tu mentoreada... ella tiene su propia voz critica que grita mas fuerte que la tuya. Cuando tu aprendas a observar la tuya sin obedecer... ensenandole como se hace. No con palabras. Con tu presencia. Siente ese regalo que le estas dando cada vez que eliges no obedecer al miedo. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 4: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Cierra los ojos y recuerda una decisión que tomaste donde no tenias toda la información pero actuaste de todos modos... y funciono. Siente eso en el cuerpo. Eso es autoeficacia. Eso es lo que Bandura llamo la creencia en tu propia capacidad de ejecutar lo necesario. Ahora imagina a tu mentoreada frente a esa misma situacion... paralizada... esperando tener mas datos mas certeza mas permiso. Tu trabajo no es darle los datos. Es ayudarle a recordar su propia evidencia. Tres momentos donde ella también actuo sin certeza... y también funciono. Prepara esas preguntas ahora en tu mente. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 5: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza una red de mujeres latinas liderando con poder real... no el poder del permiso sino el poder de la competencia reconocida. Cada una de ellas tiene una mentora que en algun momento dijo: te veo. Eres capaz. Actua ahora. Tu eres esa mentora. Siente el peso y el privilegio de ese rol. No eres solo una guia profesional. Eres un punto de inflexion en la cadena de liderazgo femenino latinoamericano. Lo que tu hagas hoy en esta sesion... se multiplica en generaciones. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 6: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza el momento justo antes de que comience tu proxima sesion de mentoria. Estas sola... un minuto antes de que ella entre. Que esta pasando en tu cuerpo? Si sientes tension... respirala. Si sientes impaciencia... sueltala. Si sientes el impulso de tener ya preparado el consejo perfecto... dejalo ir. Tu trabajo hoy no es impresionarla. Es escucharla con una calidad de atención que ella raramente ha experimentado. Una atención tan completa que ella se sienta vista. Y cuando alguien se siente vista de verdad... algo en ella se mueve. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 7: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Imagina que puedes ver todas las negociaciones que tendras esta semana antes de que ocurran. En cada una de ellas... eres alguien que conoce su valor antes de entrar al cuarto. No porque tengas mas titulos. Sino porque has hecho el trabajo interno de saber exactamente que traes a la mesa. Ahora visualiza a tu mentoreada haciendo lo mismo... entrando a su siguiente negociacion sabiendo su valor. Tu la preparaste. Le mostraste que negociar no es pedir... es intercambiar valor con valor. Siente el orgullo silencioso de quien entrena lideres de verdad. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 8: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza un grafico de datos que parece contradecir lo que tu intuicion dice. La mayoria de las personas en esa sala creen el grafico sin cuestionarlo. Tu no. Tu has aprendido a hacer la pregunta que nadie hace: de donde viene este dato? Quien lo recogio? Que no esta siendo medido aquí? Ahora imagina a tu mentoreada en esa misma sala... haciendo esa misma pregunta... con la confianza de quien sabe que el pensamiento critico no es arrogancia. Es responsabilidad. Tu le diste esa herramienta. Esa pregunta que ella hace hoy... tiene tu nombre aunque nadie lo sepa. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 9: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza tu cuerpo como un sistema complejo... no solo un vehiculo para tu mente. Tu ritmo cardiaco cambia cuando entras en conversaciones de alto riesgo. Tu respiracion se acorta cuando sientes que tu competencia esta siendo cuestionada. Tu postura se comprime cuando el ambiente es hostil. Ahora visualiza aprender a leer esas senales antes de que dominen tu comportamiento. Un latido acelerado que te dice: esto importa. Una respiracion corta que te dice: percibo amenaza. Un cuerpo que comprime que te dice: necesito mas espacio. Eres una lider que escucha su cuerpo. Y eso te hace imparable. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 10: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Es el final del Bloque 1. Diez dias de mirarte. De examinar tu historia. De construir las bases de una mentora que opera desde valores en lugar de desde patrones automaticos. Visualiza ahora a la version de ti que comenzo este bloque... y a la version que lo termina. No es la misma mujer. Esta mujer sabe mas sobre si misma. Tiene mas vocabulario para lo que antes eran solo sensaciones sin nombre. Y eso... lo traslada directamente a la calidad de sus sesiones. Honra el trabajo que hiciste. Respira tu propia evolucion. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela."};

/* THETA TTS ENGINE */
var thetaUtt = null;
var thetaPlaying = false;

window.toggleTheta = function(dayId) {
    var btn = document.getElementById('theta-btn-' + dayId);
    if (thetaPlaying) {
        window.speechSynthesis.cancel();
        thetaPlaying = false;
        if (btn) { btn.textContent = 'Iniciar Meditacion Guiada'; btn.style.background = ''; }
        return;
    }
    var scripts = window.THETA_SCRIPTS || {};
    var script = scripts[dayId] || 'Respira profundo. Integra el aprendizaje de hoy.';
    thetaUtt = new SpeechSynthesisUtterance(script);
    thetaUtt.lang = 'es-ES';
    thetaUtt.rate = 0.82;
    thetaUtt.pitch = 1.0;
    thetaUtt.volume = 1.0;
    thetaUtt.onend = function() {
        thetaPlaying = false;
        if (btn) { btn.textContent = 'Iniciar Meditacion Guiada'; btn.style.background = ''; }
    };
    window.speechSynthesis.speak(thetaUtt);
    thetaPlaying = true;
    if (btn) { btn.textContent = 'Detener'; btn.style.background = 'rgba(0,198,255,0.15)'; }
};

window.cerrarCrisisMM = function() {
    const m = document.getElementById('crisis-modal-mm');
    if (m) m.classList.remove('active');
    document.body.style.overflow = '';
  };

  window.abrirCaso = function(idx) {
    const caso = CASOS_DATA[idx];
    if (!caso) return;
    const m = document.getElementById('sala-modal');
    const t = document.getElementById('sala-title');
    const ct = document.getElementById('sala-content');
    if (!m || !t || !ct) return;
    t.textContent = caso.title;
    let html = '<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px;margin-bottom:20px;font-size:.85rem;color:#ddd;line-height:1.7">' + caso.setup + '</div>';
    html += '<div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px">OPCIONES</div>';
    html += '<div id="sala-opts">';
    caso.options.forEach((opt, i) => {
      html += '<button class="opt-btn" onclick="elegirOpcion(' + idx + ',' + i + ')">';
      html += '<strong>' + ['A','B','C','D'][i] + '.</strong> ' + opt.label;
      html += '</button>';
    });
    html += '</div>';
    html += '<div id="sala-feedback" style="display:none;margin-top:20px"></div>';
    html += '<div id="sala-prompt-wrap" style="display:none;margin-top:20px"><div style="font-size:.78rem;color:' + ACCENT + ';font-weight:600;margin-bottom:10px">' + (caso.prompt||'Tu reflexión:') + '</div><textarea id="sala-answer" style="width:100%;min-height:90px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:12px;color:#fff;font-family:Inter;font-size:.85rem" placeholder="Escribe aquí..."></textarea><button onclick="guardarCaso(' + idx + ')" style="margin-top:12px;width:100%;padding:13px;background:linear-gradient(135deg,' + ACCENT + ',#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer">Guardar mi reflexión</button></div>';
    ct.innerHTML = html;
    m.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  window.elegirOpcion = function(casoIdx, optIdx) {
    const caso = CASOS_DATA[casoIdx];
    const opt = caso.options[optIdx];
    document.querySelectorAll('.opt-btn').forEach((btn, i) => {
      btn.style.borderColor = (i === optIdx) ? (opt.correct ? '#10b981' : '#ef4444') : 'rgba(255,255,255,.06)';
      btn.style.opacity = (i === optIdx) ? '1' : '.4';
    });
    const fb = document.getElementById('sala-feedback');
    const color = opt.correct ? '#10b981' : '#ef4444';
    fb.style.display = 'block';
    fb.innerHTML = '<div style="background:rgba(255,255,255,.03);border:1px solid ' + color + ';border-radius:14px;padding:16px"><div style="color:' + color + ';font-weight:600;margin-bottom:8px">' + (opt.correct ? '✓ ' : '✗ ') + opt.concept + '</div><p style="font-size:.83rem;color:#ddd;line-height:1.6">' + opt.feedback + '</p></div>';
    document.getElementById('sala-prompt-wrap').style.display = 'block';
  };

  window.guardarCaso = function(idx) {
    const ans = document.getElementById('sala-answer').value.trim();
    if (!ans) return;
    localStorage.setItem('mm_b1_caso_' + idx, ans);
    window.cerrarSala();
    window.renderKitMentoria();
  };

  window.cerrarSala = function() {
    const m = document.getElementById('sala-modal');
    if (m) m.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Render on tab switch
  const _origSwitch = window.switchTab;
  window.switchTab = function(viewId, navEl) {
    if (_origSwitch) _origSwitch(viewId, navEl);
    if (viewId === 'view-kit') window.renderKitMentoria();
    if (viewId === 'view-libreta' && typeof window.renderMenteePanel === 'function') window.renderMenteePanel();
  };

})();

/* MI MENTOREADA — Objetivos SMART, Calendario, Bitácora, Compromisos (MVP) */
/* Llaves globales (no prefijadas por bloque) para que persistan entre los 8 archivos Bloque_Premium.html */
(function(){
  const K = {
    name: 'invictus_pair_mentee_name',
    goals: 'invictus_pair_goals',
    calendar: 'invictus_pair_calendar',
    bitacora: 'invictus_pair_bitacora',
    compromisos: 'invictus_pair_compromisos'
  };
  const ACCENT2 = '#FF5E00';

  function getArr(key) {
    try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch(e) { return []; }
  }
  function setArr(key, arr) { localStorage.setItem(key, JSON.stringify(arr)); }
  function newId() { return 'id' + Date.now() + Math.floor(Math.random()*1000); }
  function fmtDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso + 'T00:00:00');
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleDateString('es-ES', { day: '2-digit', month: 'short' });
  }

  window.guardarMenteeName = function() {
    const el = document.getElementById('mp-name');
    if (el) localStorage.setItem(K.name, el.value);
  };

  window.renderMenteePanel = function() {
    const nameEl = document.getElementById('mp-name');
    if (nameEl) nameEl.value = localStorage.getItem(K.name) || '';

    const goals = getArr(K.goals);
    const activeGoals = goals.filter(g => g.status !== 'logrado' && g.status !== 'pausado');
    const goalsCountEl = document.getElementById('mp-goals-count');
    if (goalsCountEl) goalsCountEl.textContent = activeGoals.length;

    const cal = getArr(K.calendar).filter(c => !c.done).sort((a,b) => (a.date||'').localeCompare(b.date||''));
    const nextEl = document.getElementById('mp-next-session');
    if (nextEl) nextEl.textContent = cal.length ? fmtDate(cal[0].date) : '—';

    const comp = getArr(K.compromisos).filter(c => !c.done);
    const compEl = document.getElementById('mp-compromisos-count');
    if (compEl) compEl.textContent = comp.length;
  };

  window.cerrarMentee = function() {
    document.getElementById('mentee-modal').style.display = 'none';
  };

  window.abrirMentee = function(section) {
    const titles = { goals: '🎯 Objetivos SMART', calendar: '📅 Calendario de Sesiones', bitacora: '📓 Bitácora', compromisos: '✅ Compromisos y Seguimiento' };
    document.getElementById('mentee-modal-title').textContent = titles[section] || '';
    renderSection(section);
    document.getElementById('mentee-modal').style.display = 'block';
  };

  function renderSection(section) {
    const ct = document.getElementById('mentee-modal-content');
    if (section === 'goals') ct.innerHTML = goalsHTML();
    else if (section === 'calendar') ct.innerHTML = calendarHTML();
    else if (section === 'bitacora') ct.innerHTML = bitacoraHTML();
    else if (section === 'compromisos') ct.innerHTML = compromisosHTML();
  }

  function itemCard(inner, extraStyle) {
    return '<div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px;margin-bottom:10px;' + (extraStyle||'') + '">' + inner + '</div>';
  }

  // --- OBJETIVOS SMART ---
  function goalsHTML() {
    const goals = getArr(K.goals);
    let list = goals.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Todavía no hay objetivos. Define el primero abajo — específico, medible y con fecha.</p>';
    goals.slice().reverse().forEach(g => {
      const doneStyle = g.status === 'logrado' ? 'opacity:.5;text-decoration:line-through;' : '';
      list += itemCard(
        '<p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + g.text + '</p>' +
        '<p style="color:' + ACCENT2 + ';font-size:.75rem;margin-top:6px;">Meta: ' + g.metric + ' · Fecha: ' + fmtDate(g.date) + '</p>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (g.status !== 'logrado' ? '<button onclick="marcarGoalLogrado(\'' + g.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Logrado</button>' : '') +
        '<button onclick="eliminarGoal(\'' + g.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nuevo objetivo SMART</div>
        <input id="goal-text" placeholder="¿Qué quiere lograr? (Específico)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="goal-metric" placeholder="¿Cómo se mide el éxito? (Medible)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="goal-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarGoal()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar objetivo</button>
      </div>`;
    return list;
  }
  window.agregarGoal = function() {
    const text = document.getElementById('goal-text').value.trim();
    const metric = document.getElementById('goal-metric').value.trim();
    const date = document.getElementById('goal-date').value;
    if (!text) return;
    const goals = getArr(K.goals);
    goals.push({ id: newId(), text: text, metric: metric || 'Sin definir', date: date, status: 'activo' });
    setArr(K.goals, goals);
    renderSection('goals');
    window.renderMenteePanel();
  };
  window.marcarGoalLogrado = function(id) {
    const goals = getArr(K.goals);
    const g = goals.find(x => x.id === id);
    if (g) g.status = 'logrado';
    setArr(K.goals, goals);
    renderSection('goals');
    window.renderMenteePanel();
  };
  window.eliminarGoal = function(id) {
    setArr(K.goals, getArr(K.goals).filter(x => x.id !== id));
    renderSection('goals');
    window.renderMenteePanel();
  };

  // --- CALENDARIO ---
  function calendarHTML() {
    const cal = getArr(K.calendar).slice().sort((a,b) => (a.date||'').localeCompare(b.date||''));
    let list = cal.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">No hay sesiones agendadas todavía.</p>';
    cal.forEach(c => {
      const doneStyle = c.done ? 'opacity:.5;text-decoration:line-through;' : '';
      list += itemCard(
        '<div style="display:flex;justify-content:space-between;align-items:flex-start;">' +
        '<div><p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + fmtDate(c.date) + ' — ' + (c.note || 'Sesión de mentoría') + '</p></div>' +
        '</div>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (!c.done ? '<button onclick="marcarSesionHecha(\'' + c.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Realizada</button>' : '') +
        '<button onclick="eliminarSesion(\'' + c.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Agendar sesión</div>
        <input id="cal-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <input id="cal-note" placeholder="Tema o nota (opcional)" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarSesion()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Agendar</button>
      </div>`;
    return list;
  }
  window.agregarSesion = function() {
    const date = document.getElementById('cal-date').value;
    const note = document.getElementById('cal-note').value.trim();
    if (!date) return;
    const cal = getArr(K.calendar);
    cal.push({ id: newId(), date: date, note: note, done: false });
    setArr(K.calendar, cal);
    renderSection('calendar');
    window.renderMenteePanel();
  };
  window.marcarSesionHecha = function(id) {
    const cal = getArr(K.calendar);
    const c = cal.find(x => x.id === id);
    if (c) c.done = true;
    setArr(K.calendar, cal);
    renderSection('calendar');
    window.renderMenteePanel();
  };
  window.eliminarSesion = function(id) {
    setArr(K.calendar, getArr(K.calendar).filter(x => x.id !== id));
    renderSection('calendar');
    window.renderMenteePanel();
  };

  // --- BITÁCORA ---
  function bitacoraHTML() {
    const log = getArr(K.bitacora).slice().reverse();
    let list = log.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Sin entradas todavía. Registra lo que pasó en tu última sesión.</p>';
    log.forEach(b => {
      list += itemCard(
        '<p style="color:' + ACCENT2 + ';font-size:.72rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">' + fmtDate(b.date) + '</p>' +
        '<p style="color:#ddd;font-size:.85rem;line-height:1.6;">' + b.text + '</p>' +
        '<button onclick="eliminarBitacora(\'' + b.id + '\')" style="margin-top:10px;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:6px 10px;font-size:.72rem;cursor:pointer;">Eliminar</button>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nueva entrada (hoy)</div>
        <textarea id="bit-text" placeholder="¿Qué pasó en la sesión? ¿Qué notaste?" style="width:100%;min-height:90px;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;"></textarea>
        <button onclick="agregarBitacora()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar en bitácora</button>
      </div>`;
    return list;
  }
  window.agregarBitacora = function() {
    const text = document.getElementById('bit-text').value.trim();
    if (!text) return;
    const log = getArr(K.bitacora);
    const today = new Date().toISOString().slice(0,10);
    log.push({ id: newId(), date: today, text: text });
    setArr(K.bitacora, log);
    renderSection('bitacora');
  };
  window.eliminarBitacora = function(id) {
    setArr(K.bitacora, getArr(K.bitacora).filter(x => x.id !== id));
    renderSection('bitacora');
  };

  // --- COMPROMISOS Y SEGUIMIENTO ---
  function compromisosHTML() {
    const comp = getArr(K.compromisos).slice().reverse();
    let list = comp.length ? '' : '<p style="color:#8A8F98;font-size:.85rem;margin-bottom:16px;">Sin compromisos registrados todavía.</p>';
    comp.forEach(c => {
      const doneStyle = c.done ? 'opacity:.5;text-decoration:line-through;' : '';
      const ownerTag = c.owner === 'mentora' ? 'Tuyo (mentora)' : 'De ella (mentoreada)';
      list += itemCard(
        '<p style="color:#fff;font-size:.9rem;' + doneStyle + '">' + c.text + '</p>' +
        '<p style="color:' + ACCENT2 + ';font-size:.72rem;margin-top:6px;">' + ownerTag + (c.date ? (' · Vence: ' + fmtDate(c.date)) : '') + '</p>' +
        '<div style="display:flex;gap:8px;margin-top:10px;">' +
        (!c.done ? '<button onclick="marcarCompromisoHecho(\'' + c.id + '\')" style="flex:1;background:rgba(16,185,129,.15);color:#10b981;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">✓ Cumplido</button>' : '') +
        '<button onclick="eliminarCompromiso(\'' + c.id + '\')" style="flex:1;background:rgba(255,255,255,.05);color:#8A8F98;border:none;border-radius:8px;padding:8px;font-size:.78rem;cursor:pointer;">Eliminar</button>' +
        '</div>'
      );
    });
    list += `
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);">
        <div style="font-size:.72rem;color:#8A8F98;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Nuevo compromiso</div>
        <input id="comp-text" placeholder="¿Qué se comprometió a hacer?" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <select id="comp-owner" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
          <option value="mentoreada">De la mentoreada</option>
          <option value="mentora">Tuyo (mentora)</option>
        </select>
        <input id="comp-date" type="date" style="width:100%;padding:12px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);color:#fff;margin-bottom:10px;font-family:Inter;">
        <button onclick="agregarCompromiso()" style="width:100%;padding:13px;background:linear-gradient(135deg,${ACCENT2},#FF8C00);color:#fff;border:none;border-radius:12px;font-family:Outfit;font-size:.95rem;cursor:pointer;">Guardar compromiso</button>
      </div>`;
    return list;
  }
  window.agregarCompromiso = function() {
    const text = document.getElementById('comp-text').value.trim();
    const owner = document.getElementById('comp-owner').value;
    const date = document.getElementById('comp-date').value;
    if (!text) return;
    const comp = getArr(K.compromisos);
    comp.push({ id: newId(), text: text, owner: owner, date: date, done: false });
    setArr(K.compromisos, comp);
    renderSection('compromisos');
    window.renderMenteePanel();
  };
  window.marcarCompromisoHecho = function(id) {
    const comp = getArr(K.compromisos);
    const c = comp.find(x => x.id === id);
    if (c) c.done = true;
    setArr(K.compromisos, comp);
    renderSection('compromisos');
    window.renderMenteePanel();
  };
  window.eliminarCompromiso = function(id) {
    setArr(K.compromisos, getArr(K.compromisos).filter(x => x.id !== id));
    renderSection('compromisos');
    window.renderMenteePanel();
  };

})();


/* THETA SCRIPTS DATA */
window.THETA_SCRIPTS = {1: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza a la mujer que eras cuando recibiste tu primer cargo de liderazgo... Como se veia? Como se movia? Ahora visualiza a la mujer que eres hoy. Nota la distancia entre ellas... esa distancia es tu identidad construida... no heredada, no prestada... construida. Ahora preguntate: en tu proxima sesion con tu mentoreada... ¿desde cual de estas dos mujeres vas a hablar? La que esperaba permiso... o la que ya sabe que el permiso era suyo desde el principio. Siente como tu columna se alarga. Tu voz se asienta. Tu presencia ocupa el espacio completo que te corresponde. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 2: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Imagina que puedes ver tu propia biologia... millones de celulas que no son un destino fijo sino una conversacion constante con tu entorno. Cada vez que decides actuar como lider antes de sentirte lista... esas celulas reciben una instruccion nueva. Cada vez que pones en cuestion una creencia limitante... la expresion genetica cambia. Visualiza ahora a tu mentoreada. Ella lleva en su biologia patrones de mujeres que no tuvieron voz. Tu presencia como mentora le da a esas celulas una instruccion diferente: el poder es posible. El liderazgo es tuyo. No estas solo cambiando su carrera. Estas modificando su linea biologica. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 3: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza la voz critica que mas te visita antes de una sesion difícil. No la pelees. Solo observala como si fuera un personaje pequeno que grita desde lejos... Sus palabras llegan pero no tienen poder sobre tu cuerpo. Tu respiras. Tu permaneces. Ahora visualiza a tu mentoreada... ella tiene su propia voz critica que grita mas fuerte que la tuya. Cuando tu aprendas a observar la tuya sin obedecer... ensenandole como se hace. No con palabras. Con tu presencia. Siente ese regalo que le estas dando cada vez que eliges no obedecer al miedo. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 4: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Cierra los ojos y recuerda una decisión que tomaste donde no tenias toda la información pero actuaste de todos modos... y funciono. Siente eso en el cuerpo. Eso es autoeficacia. Eso es lo que Bandura llamo la creencia en tu propia capacidad de ejecutar lo necesario. Ahora imagina a tu mentoreada frente a esa misma situacion... paralizada... esperando tener mas datos mas certeza mas permiso. Tu trabajo no es darle los datos. Es ayudarle a recordar su propia evidencia. Tres momentos donde ella también actuo sin certeza... y también funciono. Prepara esas preguntas ahora en tu mente. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 5: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza una red de mujeres latinas liderando con poder real... no el poder del permiso sino el poder de la competencia reconocida. Cada una de ellas tiene una mentora que en algun momento dijo: te veo. Eres capaz. Actua ahora. Tu eres esa mentora. Siente el peso y el privilegio de ese rol. No eres solo una guia profesional. Eres un punto de inflexion en la cadena de liderazgo femenino latinoamericano. Lo que tu hagas hoy en esta sesion... se multiplica en generaciones. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 6: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza el momento justo antes de que comience tu proxima sesion de mentoria. Estas sola... un minuto antes de que ella entre. Que esta pasando en tu cuerpo? Si sientes tension... respirala. Si sientes impaciencia... sueltala. Si sientes el impulso de tener ya preparado el consejo perfecto... dejalo ir. Tu trabajo hoy no es impresionarla. Es escucharla con una calidad de atención que ella raramente ha experimentado. Una atención tan completa que ella se sienta vista. Y cuando alguien se siente vista de verdad... algo en ella se mueve. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 7: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Imagina que puedes ver todas las negociaciones que tendras esta semana antes de que ocurran. En cada una de ellas... eres alguien que conoce su valor antes de entrar al cuarto. No porque tengas mas titulos. Sino porque has hecho el trabajo interno de saber exactamente que traes a la mesa. Ahora visualiza a tu mentoreada haciendo lo mismo... entrando a su siguiente negociacion sabiendo su valor. Tu la preparaste. Le mostraste que negociar no es pedir... es intercambiar valor con valor. Siente el orgullo silencioso de quien entrena lideres de verdad. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 8: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza un grafico de datos que parece contradecir lo que tu intuicion dice. La mayoria de las personas en esa sala creen el grafico sin cuestionarlo. Tu no. Tu has aprendido a hacer la pregunta que nadie hace: de donde viene este dato? Quien lo recogio? Que no esta siendo medido aquí? Ahora imagina a tu mentoreada en esa misma sala... haciendo esa misma pregunta... con la confianza de quien sabe que el pensamiento critico no es arrogancia. Es responsabilidad. Tu le diste esa herramienta. Esa pregunta que ella hace hoy... tiene tu nombre aunque nadie lo sepa. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 9: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Visualiza tu cuerpo como un sistema complejo... no solo un vehiculo para tu mente. Tu ritmo cardiaco cambia cuando entras en conversaciones de alto riesgo. Tu respiracion se acorta cuando sientes que tu competencia esta siendo cuestionada. Tu postura se comprime cuando el ambiente es hostil. Ahora visualiza aprender a leer esas senales antes de que dominen tu comportamiento. Un latido acelerado que te dice: esto importa. Una respiracion corta que te dice: percibo amenaza. Un cuerpo que comprime que te dice: necesito mas espacio. Eres una lider que escucha su cuerpo. Y eso te hace imparable. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela.", 10: "Cierra los ojos. Permite que tu cuerpo encuentre una posicion comoda... Inhala lentamente por la nariz contando hasta cuatro... Sostén el aire... uno, dos, tres, cuatro... y exhala lentamente por la boca... soltando cualquier tension del día. Otra vez. Inhala... dos, tres, cuatro... sostén... y exhala... Bien. Con cada respiracion tu sistema nervioso entra en un estado mas receptivo. Tus hombros se relajan. Tu mandibula se suelta. Tus manos se abren. Estas entrando en un estado de frecuencia theta donde el aprendizaje se convierte en identidad. Es el final del Bloque 1. Diez dias de mirarte. De examinar tu historia. De construir las bases de una mentora que opera desde valores en lugar de desde patrones automaticos. Visualiza ahora a la version de ti que comenzo este bloque... y a la version que lo termina. No es la misma mujer. Esta mujer sabe mas sobre si misma. Tiene mas vocabulario para lo que antes eran solo sensaciones sin nombre. Y eso... lo traslada directamente a la calidad de sus sesiones. Honra el trabajo que hiciste. Respira tu propia evolucion. Ahora lleva una mano a tu corazon. Siente tu propio latido. Este es el pulso de una lider que eligio crecer hoy. Todo lo que exploraste en esta sesion no esta solo en tu mente... esta grabado en tu biologia. En tus celulas. En tu forma de estar en el mundo manana. Cuando estes lista, comienza a mover los dedos lentamente... luego las manos... abre los ojos con suavidad... y lleva contigo el estado de quien ya es la lider que este programa revela."};

/* THETA TTS ENGINE */
var thetaUtt = null;
var thetaPlaying = false;

window.toggleTheta = function(dayId) {
    var btn = document.getElementById('theta-btn-' + dayId);
    if (thetaPlaying) {
        window.speechSynthesis.cancel();
        thetaPlaying = false;
        if (btn) { btn.textContent = 'Iniciar Meditacion Guiada'; btn.style.background = ''; }
        return;
    }
    var scripts = window.THETA_SCRIPTS || {};
    var script = scripts[dayId] || 'Respira profundo. Integra el aprendizaje de hoy.';
    thetaUtt = new SpeechSynthesisUtterance(script);
    thetaUtt.lang = 'es-ES';
    thetaUtt.rate = 0.82;
    thetaUtt.pitch = 1.0;
    thetaUtt.volume = 1.0;
    thetaUtt.onend = function() {
        thetaPlaying = false;
        if (btn) { btn.textContent = 'Iniciar Meditacion Guiada'; btn.style.background = ''; }
    };
    window.speechSynthesis.speak(thetaUtt);
    thetaPlaying = true;
    if (btn) { btn.textContent = 'Detener'; btn.style.background = 'rgba(0,198,255,0.15)'; }
};


window.updateKitStats = function() {
    let diasActivos = 0;
    let maxStreak = 0;
    let currentStreak = 0;
    let bestPpm = 0;
    let scoreSum = 0;
    let scoreCount = 0;

    const dataArr = window.mujeresMentorasData || [];
    const total = dataArr.length > 0 ? dataArr.length : 1;

    for (let d of dataArr) {
        if (progresoLocal[d.dia] && progresoLocal[d.dia].completado) {
            diasActivos++;
            currentStreak++;
            if (currentStreak > maxStreak) maxStreak = currentStreak;
            
            if (progresoLocal[d.dia].ppm && progresoLocal[d.dia].ppm > bestPpm) {
                bestPpm = progresoLocal[d.dia].ppm;
            }
            if (progresoLocal[d.dia].comprension) {
                scoreSum += progresoLocal[d.dia].comprension;
                scoreCount++;
            }
        } else {
            currentStreak = 0;
        }
    }

    const pct = Math.round((diasActivos / total) * 100);
    const avgComp = scoreCount > 0 ? Math.round(scoreSum / scoreCount) : null;

    const el = id => document.getElementById(id);
    if (el('km-dias')) el('km-dias').textContent = diasActivos;
    if (el('km-streak')) el('km-streak').textContent = maxStreak;
    if (el('km-ppm')) el('km-ppm').textContent = bestPpm || '0';
    if (el('km-comp')) el('km-comp').textContent = avgComp !== null ? (avgComp + '%') : '0%';
    if (el('km-pct')) el('km-pct').textContent = pct + '%';
    if (el('km-bar')) el('km-bar').style.width = pct + '%';

    // Profile
    if (diasActivos >= 5) {
        const profiles = [
            {n:'Mentora Socrática', d:'Preguntas poderosas sobre consejos. Genera autonomía profunda en sus mentoreadas.'},
            {n:'Mentora Catalizadora', d:'Activa el potencial dormido. Transforma la ambivalencia en movimiento.'},
            {n:'Mentora Espejo', d:'Refleja verdades difíciles con gracia. Sus mentoreadas se ven a sí mismas con claridad brutal.'},
            {n:'Mentora Estratega', d:'Conecta el desarrollo personal con la visión organizacional. Piensa en sistemas.'},
        ];
        const p = profiles[diasActivos % profiles.length];
        const wrap = el('km-mirror-profile');
        if (wrap) { wrap.style.display = 'block'; }
        if (el('km-profile-name')) el('km-profile-name').textContent = p.n;
        if (el('km-profile-desc')) el('km-profile-desc').textContent = p.d;
    }
};

// -----------------------------------

