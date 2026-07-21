import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

dashboard_html = """
            <div id="view-dashboard" class="view active">
                <div class="hero-progress stagger-1" style="display:flex; flex-direction:column; align-items:center;">
                    <div class="ring-wrapper" style="position:relative; width:200px; height:200px;">
                        <svg width="200" height="200" viewBox="0 0 200 200" style="transform: rotate(-90deg);">
                            <defs><linearGradient id="fire-grad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#FF4500" /><stop offset="100%" stop-color="#FF8C00" /></linearGradient></defs>
                            <circle class="ring-bg" cx="100" cy="100" r="90" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="12"></circle>
                            <circle id="progress-ring-circle" class="ring-progress" cx="100" cy="100" r="90" fill="none" stroke="url(#fire-grad)" stroke-width="12" stroke-dasharray="565.48" stroke-dashoffset="565.48" style="transition: stroke-dashoffset 1s ease-in-out;"></circle>
                        </svg>
                        <div class="ring-content" style="position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                            <h2 id="dashboard-day-number" class="text-gradient" style="font-size:3rem; margin:0; line-height:1;">1</h2>
                            <p style="margin:0; font-size:0.9rem; color:var(--text-secondary);">Día de 78</p>
                        </div>
                    </div>
                </div>

                <div class="stagger-2" style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; margin-top:20px;">
                    <div style="background:rgba(255,255,255,0.05); padding:15px; border-radius:12px; text-align:center; border:1px solid rgba(255,255,255,0.1);">
                        <div style="font-size:1.8rem; font-family:'Outfit'; color:var(--accent-water);" id="dash-ppm">0</div>
                        <div style="font-size:0.7rem; color:var(--text-secondary);">Velocidad (PPM)</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.05); padding:15px; border-radius:12px; text-align:center; border:1px solid rgba(255,255,255,0.1);">
                        <div style="font-size:1.8rem; font-family:'Outfit'; color:var(--success);" id="dash-score">0%</div>
                        <div style="font-size:0.7rem; color:var(--text-secondary);">Comprensión</div>
                    </div>
                </div>

                <div class="blocks-list stagger-3" style="margin-top:30px;">
                    <h3 style="font-family:'Outfit'; font-size:1.2rem; margin-bottom:15px;">Tu Roadmap (Bloques)</h3>
                    <div id="roadmap-container" style="display:flex; flex-direction:column; gap:12px;">
                        <!-- JS injected roadmap -->
                    </div>
                    
                    <button class="btn-outline" style="width: 100%; margin-top: 24px; padding: 16px; border-color: rgba(255,255,255,0.1); color: var(--text-secondary); font-family: 'Outfit'; font-weight: 500; font-size: 0.95rem; display: flex; gap: 8px; justify-content: center; background: var(--bg-surface-elevated);" onclick="openSOS()">
                        <span>🆘</span> Protocolo SOS: Regulación de Cortisol
                    </button>
                </div>
            </div>
"""

dashboard_js = """
// --- DASHBOARD LOGIC ---
let userProgress = []; // [{day: 1, ppm: 250, comprehension_score: 100}, ...]
let maxUnlockedDay = 1;

async function loadDashboard() {
    if(!currentUser) return;
    
    // 1. Fetch user progress from Supabase
    const { data, error } = await _supabase
        .from('user_progress')
        .select('*')
        .eq('user_id', currentUser.id)
        .order('day', { ascending: true });
        
    if(!error && data) {
        userProgress = data;
    }
    
    // 2. Calculate max unlocked day
    let maxCompleted = 0;
    if(userProgress.length > 0) {
        maxCompleted = Math.max(...userProgress.map(p => p.day));
    }
    maxUnlockedDay = Math.min(maxCompleted + 1, 78);
    
    // 3. Calculate avg PPM and Score
    let avgPPM = 0, avgScore = 0;
    if(userProgress.length > 0) {
        avgPPM = Math.round(userProgress.reduce((sum, p) => sum + (p.ppm || 0), 0) / userProgress.length);
        avgScore = Math.round(userProgress.reduce((sum, p) => sum + (p.comprehension_score || 0), 0) / userProgress.length);
    }
    
    document.getElementById('dash-ppm').innerText = avgPPM;
    document.getElementById('dash-score').innerText = avgScore + '%';
    document.getElementById('dashboard-day-number').innerText = maxUnlockedDay;
    
    // 4. Update Progress Ring (0 to 78)
    const ring = document.getElementById('progress-ring-circle');
    if(ring) {
        const radius = ring.r.baseVal.value;
        const circumference = radius * 2 * Math.PI; // ~565.48
        const percent = Math.min((maxCompleted / 78) * 100, 100);
        const offset = circumference - (percent / 100) * circumference;
        ring.style.strokeDashoffset = offset;
    }
    
    // 5. Render Roadmap
    renderRoadmap();
}

function renderRoadmap() {
    const container = document.getElementById('roadmap-container');
    container.innerHTML = '';
    
    // Group days by Bloque (assuming 10 days per bloque approx, though data says 8 bloques x ~10 days)
    // We will use window.mujeresMentorasData to build the roadmap
    if(!window.mujeresMentorasData) return;
    
    let bloquesMap = {};
    window.mujeresMentorasData.forEach(d => {
        if(!bloquesMap[d.bloque]) bloquesMap[d.bloque] = [];
        bloquesMap[d.bloque].push(d);
    });
    
    let isPreviousBlockCompleted = true; // Block 1 is always unlocked
    
    Object.keys(bloquesMap).forEach((bloqueName, index) => {
        const daysInBloque = bloquesMap[bloqueName];
        const minDay = Math.min(...daysInBloque.map(d => d.dia));
        const maxDay = Math.max(...daysInBloque.map(d => d.dia));
        
        let statusClass = "locked";
        let icon = "🔒";
        let subtitle = `Bloqueado (Días ${minDay}-${maxDay})`;
        let opacity = "0.5";
        let onClickAction = "";
        
        if (maxUnlockedDay > maxDay) {
            statusClass = "completed";
            icon = "✓";
            subtitle = `Completado`;
            opacity = "1";
            onClickAction = `onclick="loadDay(${minDay}); switchTab('view-session', this);"`;
        } else if (maxUnlockedDay >= minDay && maxUnlockedDay <= maxDay) {
            statusClass = "active";
            icon = "🔥";
            subtitle = `En progreso (Día actual: ${maxUnlockedDay})`;
            opacity = "1";
            onClickAction = `onclick="loadDay(${maxUnlockedDay}); switchTab('view-session', this);"`;
        }
        
        const blockHtml = `
            <div class="glass-card" style="opacity:${opacity}; display:flex; align-items:center; cursor:${statusClass !== 'locked' ? 'pointer' : 'not-allowed'};" ${onClickAction}>
                <div style="font-size:1.5rem; margin-right:15px; width:30px; text-align:center;">${icon}</div>
                <div>
                    <h4 style="font-size: 0.95rem; color: white; margin-bottom:4px;">${bloqueName}</h4>
                    <p style="font-size: 0.8rem; color: ${statusClass === 'active' ? 'var(--accent-fire)' : 'var(--text-secondary)'};">${subtitle}</p>
                </div>
            </div>
        `;
        container.innerHTML += blockHtml;
    });
}

// Function to save daily progress
async function saveDailyProgress(dayNum, ppm, score) {
    if(!currentUser) return;
    
    const { data, error } = await _supabase
        .from('user_progress')
        .upsert({ 
            user_id: currentUser.id, 
            day: dayNum, 
            ppm: ppm, 
            comprehension_score: score,
            completed_at: new Date().toISOString()
        }, { onConflict: 'user_id, day' });
        
    if(!error) {
        console.log("Progress saved");
        await loadDashboard(); // refresh
    }
}

// Hook loadDashboard into auth flow
const oldHandleLoginResponse = handleLoginResponse;
handleLoginResponse = async function(response) {
    await oldHandleLoginResponse(response);
    if(currentUser) {
        await loadDashboard();
        if(maxUnlockedDay <= window.mujeresMentorasData.length) {
            loadDay(maxUnlockedDay);
        }
    }
}
"""

# Replace Dashboard HTML
pattern = r'<div id="view-dashboard" class="view active">.*?<!-- SESIÓN -->'
content = re.sub(pattern, dashboard_html + '\n            <!-- SESIÓN -->', content, flags=re.DOTALL)

# Add Dashboard JS
if "loadDashboard" not in content:
    content = content.replace("</script>\n</body>", dashboard_js + "\n</script>\n</body>")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard injected.")
