html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS
css_old_bottom_nav = """        .bottom-nav { position: absolute; bottom: 0; width: 100%; height: 90px; background: rgba(10, 10, 12, 0.8); backdrop-filter: blur(20px); border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-around; align-items: center; padding-bottom: 20px; z-index: 50; }
        .nav-item { display: flex; flex-direction: column; align-items: center; color: var(--text-tertiary); cursor: pointer; width: 33%; transition: color 0.3s; }
        .nav-item.active { color: var(--text-primary); }
        .nav-icon { font-size: 1.4rem; margin-bottom: 4px; }"""

css_new_bottom_nav = """        .bottom-nav { position: absolute; bottom: 0; width: 100%; height: 95px; background: rgba(10, 10, 12, 0.85); backdrop-filter: blur(24px); border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-around; align-items: center; padding: 10px 10px 25px; z-index: 50; }
        .nav-item { display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--text-tertiary); cursor: pointer; flex: 1; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); padding: 8px 0; border-radius: 12px; }
        .nav-item:hover { color: var(--text-secondary); transform: translateY(-2px); }
        .nav-item:active { transform: scale(0.95); }
        .nav-item.active { color: var(--text-primary); background: rgba(255,255,255,0.06); }
        .nav-icon { font-size: 1.5rem; margin-bottom: 4px; filter: grayscale(1); opacity: 0.6; transition: all 0.3s; }
        .nav-item.active .nav-icon { filter: grayscale(0); opacity: 1; transform: scale(1.1); }
        .nav-label { font-size: 0.7rem; font-weight: 500; font-family: 'Outfit'; letter-spacing: 0.5px; }"""

if css_old_bottom_nav in content:
    content = content.replace(css_old_bottom_nav, css_new_bottom_nav)

css_old_btn = """        .btn-premium:active { transform: scale(0.98); }
        .btn-premium.fire { background: var(--gradient-fire); color: white; box-shadow: 0 10px 20px var(--accent-fire-glow); }
        .btn-premium.water { background: var(--gradient-water); color: white; box-shadow: 0 10px 20px var(--accent-water-glow); }
        .btn-outline { background: transparent; border: 1px solid var(--border-glow); color: var(--text-primary); padding: 12px 16px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s var(--ease-spring); display: inline-flex; justify-content: center;}"""

css_new_btn = """        .btn-premium:hover { filter: brightness(1.1); transform: translateY(-2px); }
        .btn-premium:active { transform: scale(0.96); filter: brightness(0.9); }
        .btn-premium.fire { background: var(--gradient-fire); color: white; box-shadow: 0 8px 16px var(--accent-fire-glow); }
        .btn-premium.water { background: var(--gradient-water); color: white; box-shadow: 0 8px 16px var(--accent-water-glow); }
        .btn-outline { background: transparent; border: 1px solid var(--border-glow); color: var(--text-primary); padding: 12px 16px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s var(--ease-spring); display: inline-flex; justify-content: center;}
        .btn-outline:active { transform: scale(0.96); }"""

if css_old_btn in content:
    content = content.replace(css_old_btn, css_new_btn)

css_old_glass = """.glass-card { background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 20px; padding: 20px; backdrop-filter: blur(12px); transition: transform 0.4s var(--ease-spring); }"""
css_new_glass = """.glass-card { background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 20px; padding: 24px; backdrop-filter: blur(16px); box-shadow: 0 8px 32px rgba(0,0,0,0.4); transition: transform 0.4s var(--ease-spring); }"""
if css_old_glass in content:
    content = content.replace(css_old_glass, css_new_glass)

css_old_reader = """.reader-premium { margin-top: 16px; background: var(--bg-surface-elevated); border-radius: 16px; padding: 20px; font-size: 0.9rem; color: var(--text-secondary); max-height: 300px; overflow-y: auto; border: 1px solid var(--border-subtle); line-height: 1.7; }
        .reader-p { margin-bottom: 16px; }"""
css_new_reader = """.reader-premium { margin-top: 20px; background: rgba(255,255,255,0.02); border-radius: 16px; padding: 24px; font-size: 0.95rem; color: var(--text-secondary); max-height: 320px; overflow-y: auto; border: 1px solid var(--border-subtle); line-height: 1.8; box-shadow: inset 0 2px 10px rgba(0,0,0,0.3); }
        .reader-p { margin-bottom: 18px; }"""
if css_old_reader in content:
    content = content.replace(css_old_reader, css_new_reader)

css_old_phase = """.phase { position: relative; margin-bottom: 40px; opacity: 0.5; transition: opacity 0.3s; }"""
css_new_phase = """.phase { position: relative; margin-bottom: 48px; opacity: 0.5; transition: opacity 0.3s; }"""
if css_old_phase in content:
    content = content.replace(css_old_phase, css_new_phase)

# 2. Update HTML for Bottom Nav
html_old_nav = """        <nav class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('view-dashboard', this)"><div class="nav-icon"></div><span class="nav-label">HOME</span></div>
            <div class="nav-item" onclick="switchTab('view-session', this)"><div class="nav-icon"></div><span class="nav-label">SESIÓN</span></div>
            <div class="nav-item" onclick="switchTab('view-libreta', this)"><div class="nav-icon"></div><span class="nav-label">PLAYBOOK</span></div>
            <div class="nav-item mentada-tab-btn" style="display:none;" onclick="switchTab('view-mentada', this)"><div class="nav-icon"></div><span class="nav-label">MI MENTADA</span></div>
            <div class="nav-item conexion-tab-btn" onclick="switchTab('view-conexion', this)"><div class="nav-icon"></div><span class="nav-label">CONEXIÓN</span></div>
        </nav>"""

html_new_nav = """        <nav class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('view-dashboard', this)"><div class="nav-icon">🏠</div><span class="nav-label">HOME</span></div>
            <div class="nav-item" onclick="switchTab('view-session', this)"><div class="nav-icon">🎧</div><span class="nav-label">SESIÓN</span></div>
            <div class="nav-item" onclick="switchTab('view-libreta', this)"><div class="nav-icon">📖</div><span class="nav-label">PLAYBOOK</span></div>
            <div class="nav-item mentada-tab-btn" style="display:none;" onclick="switchTab('view-mentada', this)"><div class="nav-icon">👥</div><span class="nav-label">MENTADA</span></div>
            <div class="nav-item conexion-tab-btn" onclick="switchTab('view-conexion', this)"><div class="nav-icon">💬</div><span class="nav-label">CONEXIÓN</span></div>
        </nav>"""

if html_old_nav in content:
    content = content.replace(html_old_nav, html_new_nav)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected UX improvements.")
