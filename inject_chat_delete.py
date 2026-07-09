import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update appendMessageToUI
old_append = """function appendMessageToUI(msg) {
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
}"""

new_append = """function appendMessageToUI(msg) {
    const container = document.getElementById('chat-container');
    const div = document.createElement('div');
    div.classList.add('chat-bubble');
    div.id = 'msg-' + msg.id; // Assign ID
    
    if(msg.sender_id === currentUser.id) {
        div.classList.add('chat-sent');
        // Add delete button for own messages
        div.innerHTML = `<span>${msg.content}</span> <span onclick="deleteMessage('${msg.id}')" style="font-size:0.8rem; cursor:pointer; opacity:0.6; margin-left:10px;" title="Borrar mensaje">🗑️</span>`;
    } else {
        div.classList.add('chat-received');
        div.innerText = msg.content;
    }
    
    container.appendChild(div);
    container.scrollTop = container.scrollHeight; // Auto-scroll
}

async function deleteMessage(msgId) {
    // Optimistic UI removal
    const el = document.getElementById('msg-' + msgId);
    if(el) el.remove();
    
    // Delete from Supabase
    await _supabase.from('mentoras_messages').delete().eq('id', msgId);
}"""

if "function appendMessageToUI(msg) {" in content and "deleteMessage" not in content:
    content = content.replace(old_append, new_append)

# 2. Update realtime subscription to handle DELETE
old_realtime = """realtimeSubscription = _supabase.channel('public:mentoras_messages')
        .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'mentoras_messages' }, payload => {
            const msg = payload.new;
            // Check if message belongs to this conversation
            if( (msg.sender_id === currentUser.id && msg.receiver_id === chatPartner.id) ||
                (msg.sender_id === chatPartner.id && msg.receiver_id === currentUser.id) ) {
                appendMessageToUI(msg);
            }
        })
        .subscribe();"""

new_realtime = """realtimeSubscription = _supabase.channel('public:mentoras_messages')
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
        .subscribe();"""

if "event: 'DELETE'" not in content:
    content = content.replace(old_realtime, new_realtime)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected message deletion logic.")
