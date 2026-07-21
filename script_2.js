
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
            if( (msg.sender_id === currentUser.id && msg.receiver_id === chatPartner.id) ||
                (msg.sender_id === chatPartner.id && msg.receiver_id === currentUser.id) ) {
                appendMessageToUI(msg);
            }
        })
        .on('postgres_changes', { event: 'DELETE', schema: 'public', table: 'mentoras_messages' }, payload => {
            const el = document.getElementById('msg-' + payload.old.id);
            if(el) el.remove();
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
    div.id = 'msg-' + msg.id;
    
    const timeStr = new Date(msg.created_at || Date.now()).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    
    if(msg.sender_id === currentUser.id) {
        div.classList.add('chat-sent');
        div.innerHTML = `<div>${msg.content}</div><div style="font-size:0.65rem; opacity:0.7; text-align:right; margin-top:5px; display:flex; justify-content:flex-end; align-items:center; gap:5px;"><span>${timeStr}</span><span onclick="deleteMessage('${msg.id}')" style="cursor:pointer; opacity:0.6;" title="Borrar">🗑️</span></div>`;
    } else {
        div.classList.add('chat-received');
        div.innerHTML = `<div>${msg.content}</div><div style="font-size:0.65rem; opacity:0.7; text-align:left; margin-top:5px;">${timeStr}</div>`;
    }
    
    container.appendChild(div);
    container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
}

async function deleteMessage(msgId) {
    // Optimistic UI removal
    const el = document.getElementById('msg-' + msgId);
    if(el) el.remove();
    
    // Delete from Supabase
    await _supabase.from('mentoras_messages').delete().eq('id', msgId);
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
