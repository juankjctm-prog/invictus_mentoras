import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

nav_match = re.search(r'<nav class="bottom-nav">(.*?)</nav>', text, re.IGNORECASE | re.DOTALL)
if nav_match:
    new_nav = """
            <div class="nav-item active" onclick="switchTab('view-dashboard', this)"><div class="nav-icon">⚲</div><span class="nav-label">HOME</span></div>
            <div class="nav-item" onclick="switchTab('view-session', this)"><div class="nav-icon">⚡</div><span class="nav-label">SESIÓN</span></div>
            <div class="nav-item" onclick="switchTab('view-libreta', this)"><div class="nav-icon">▤</div><span class="nav-label">PLAYBOOK</span></div>
            <div class="nav-item" onclick="switchTab('view-kit', this)"><div class="nav-icon">🛡️</div><span class="nav-label">MI KIT</span></div>
            <div class="nav-item mentada-tab-btn" style="display:none;" onclick="switchTab('view-mentada', this)"><div class="nav-icon">👥</div><span class="nav-label">MI MENTADA</span></div>
            <div class="nav-item conexion-tab-btn" onclick="switchTab('view-conexion', this)"><div class="nav-icon">🌐</div><span class="nav-label">CONEXIÓN</span></div>
        """
    text = text.replace(nav_match.group(1), new_nav)
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Fixed bottom-nav!")
else:
    print('Not found')
