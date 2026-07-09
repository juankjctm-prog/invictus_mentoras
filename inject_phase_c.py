import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CONEXIÓN tab to nav
if 'view-conexion' not in content:
    nav_tab_html = '<div class="nav-item conexion-tab-btn" onclick="switchTab(\'view-conexion\', this)"><div class="nav-icon">💬</div><span class="nav-label">CONEXIÓN</span></div>'
    content = content.replace('</nav>', f'    {nav_tab_html}\n        </nav>')

# 2. Add view-conexion HTML block
if 'id="view-conexion"' not in content:
    view_conexion_html = """
        <!-- PANEL CONEXIÓN (FASE C) -->
        <div id="view-conexion" class="view" style="padding: 80px 20px 100px; display: flex; flex-direction: column; height: 100vh;">
            <h2 id="conexion-title" style="font-family: 'Outfit'; font-weight: 300; letter-spacing: 2px;">CONEXIÓN</h2>
            
            <div id="conexion-agenda" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; margin-top: 20px; display:none;">
                <h3 style="font-size: 1rem; color: var(--accent-earth);">Próxima Sesión</h3>
                <p id="conexion-session-status" style="font-size: 0.9rem; margin-top: 5px; color: #ddd;">Cargando calendario...</p>
            </div>

            <div id="chat-container" style="flex: 1; overflow-y: auto; margin-top: 20px; display: flex; flex-direction: column; gap: 10px; padding-right: 5px;">
                <!-- Chat bubbles -->
            </div>
            
            <div id="chat-input-area" style="display: flex; gap: 10px; margin-top: 20px;">
                <input type="text" id="chat-input" placeholder="Escribe un mensaje..." style="flex: 1; background: rgba(255,255,255,0.1); border: none; padding: 15px; border-radius: 25px; color: white; font-family: 'Inter'; outline: none;">
                <button onclick="sendChatMessage()" style="background: var(--accent-water); border: none; border-radius: 50%; width: 50px; height: 50px; color: var(--bg-absolute); font-size: 1.2rem; cursor: pointer;">➤</button>
            </div>
        </div>
    """
    content = content.replace('<nav class="bottom-nav">', f'{view_conexion_html}\n        <nav class="bottom-nav">')

# 3. Add CSS for Chat Bubbles
if '.chat-bubble' not in content:
    chat_css = """
        .chat-bubble { max-width: 80%; padding: 12px 16px; border-radius: 16px; font-size: 0.95rem; line-height: 1.4; word-wrap: break-word; }
        .chat-sent { background: var(--accent-water); color: var(--bg-absolute); align-self: flex-end; border-bottom-right-radius: 4px; }
        .chat-received { background: rgba(255,255,255,0.1); color: white; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid rgba(255,255,255,0.05); }
    """
    content = content.replace('</style>', f'{chat_css}\n    </style>')

# 4. Inject Logic for Phase C
logic_script = """
<script>
// --- FASE C: CHAT Y CONEXIÓN ---
let chatPartner = null;
let realtimeSubscription = null;

async function loadConexionTab() {
    const chatContainer = document.getElementById('chat-container');
    const title = document.getElementById('conexion-title');
    
    if(!currentUser) return;
    
    // 1. Identify Partner
    if(currentUser.role === 'Mentora') {
        const { data } = await _supabase.from('mentoras_users').select('*').eq('assigned_mentor_id', currentUser.id).single();
        chatPartner = data;
    } else {
        const { data } = await _supabase.from('mentoras_users').select('*').eq('id', currentUser.assigned_mentor_id).single();
        chatPartner = data;
    }
    
    if(!chatPartner) {
        chatContainer.innerHTML = '<p style="text-align:center; color:#888; margin-top:20px;">No tienes una pareja asignada para chatear.</p>';
        document.getElementById('chat-input-area').style.display = 'none';
        return;
    }
    
    title.innerText = `CHAT CON ${chatPartner.name.toUpperCase()}`;
    document.getElementById('chat-input-area').style.display = 'flex';
    
    // 2. Fetch Message History
    const { data: messages } = await _supabase.from('mentoras_messages')
        .select('*')
        .or(`and(sender_id.eq.${currentUser.id},receiver_id.eq.${chatPartner.id}),and(sender_id.eq.${chatPartner.id},receiver_id.eq.${currentUser.id})`)
        .order('created_at', { ascending: true });
        
    renderChatMessages(messages || []);
    
    // 3. Set up Realtime WebSockets
    if(realtimeSubscription) { _supabase.removeChannel(realtimeSubscription); }
    
    realtimeSubscription = _supabase.channel('public:mentoras_messages')
        .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'mentoras_messages' }, payload => {
            const msg = payload.new;
            // Check if message belongs to this conversation
            if( (msg.sender_id === currentUser.id && msg.receiver_id === chatPartner.id) ||
                (msg.sender_id === chatPartner.id && msg.receiver_id === currentUser.id) ) {
                appendMessageToUI(msg);
            }
        })
        .subscribe();
}

function renderChatMessages(messages) {
    const container = document.getElementById('chat-container');
    container.innerHTML = '';
    messages.forEach(msg => appendMessageToUI(msg));
}

function appendMessageToUI(msg) {
    const container = document.getElementById('chat-container');
    const div = document.createElement('div');
    div.classList.add('chat-bubble');
    if(msg.sender_id === currentUser.id) {
        div.classList.add('chat-sent');
    } else {
        div.classList.add('chat-received');
    }
    div.innerText = msg.content;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight; // Auto-scroll
}

async function sendChatMessage() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if(!text || !chatPartner) return;
    
    input.value = ''; // Clear immediately
    
    // Optimistic UI (handled by realtime event, but we could append here immediately to feel faster)
    // For now, let the realtime socket append it so we ensure it reached the server.
    
    await _supabase.from('mentoras_messages').insert([{
        sender_id: currentUser.id,
        receiver_id: chatPartner.id,
        content: text
    }]);
}

// Support hitting Enter to send
document.addEventListener('DOMContentLoaded', () => {
    // Wait for elements to exist
    setTimeout(() => {
        const input = document.getElementById('chat-input');
        if(input) {
            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') sendChatMessage();
            });
        }
    }, 1000);
});

// Hook into switchTab
const originalSwitchTabC = switchTab;
switchTab = function(viewId, element) {
    originalSwitchTabC(viewId, element);
    if(viewId === 'view-conexion') {
        loadConexionTab();
    }
};
</script>
"""
if 'loadConexionTab' not in content:
    content = content.replace('</body>', logic_script + '\n</body>')


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected Phase C successfully.")
