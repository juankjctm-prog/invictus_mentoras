import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update appendMessageToUI
new_append_message = """
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
"""
content = re.sub(r'function appendMessageToUI\(msg\) \{.*?\n\}', new_append_message.strip(), content, flags=re.DOTALL)


# 2. Update loadAgenda styling
new_load_agenda = """
async function loadAgenda() {
    if(!chatPartner || !currentUser) return;
    const agendaStatus = document.getElementById('conexion-session-status');
    
    // Determine IDs based on role
    let mentoraId = currentUser.role === 'Mentora' ? currentUser.id : chatPartner.id;
    let mentadaId = currentUser.role === 'Mentada' ? currentUser.id : chatPartner.id;
    
    // Fetch latest active session
    const { data: session } = await _supabase.from('mentoras_sessions')
        .select('*')
        .eq('mentora_id', mentoraId)
        .eq('mentada_id', mentadaId)
        .neq('status', 'Completada')
        .order('created_at', { ascending: false })
        .limit(1)
        .single();
        
    if(!session) {
        // Form to propose
        agendaStatus.innerHTML = `
            <div style="display:flex; flex-direction:column; gap:10px; margin-top:10px;">
                <p style="color:#aaa; font-size:0.85rem; margin:0;">No hay sesiones programadas.</p>
                <div style="display:flex; gap:10px; align-items:center;">
                    <input type="datetime-local" id="agenda-date" style="flex:1; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); padding:12px; color:white; border-radius:12px; font-family:'Inter'; font-size:0.9rem; outline:none;">
                    <button onclick="proposeSession()" style="background:var(--accent-earth); color:var(--bg-absolute); border:none; padding:12px 18px; border-radius:12px; font-family:'Outfit'; font-weight:600; cursor:pointer;">Agendar</button>
                </div>
            </div>
        `;
        currentSessionId = null;
    } else {
        currentSessionId = session.id;
        const dateObj = new Date(session.proposed_date);
        
        // Custom formatting
        const options = { weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' };
        const dateString = dateObj.toLocaleString('es-ES', options).replace(',', ' -');
        
        if(session.status === 'Pendiente') {
            agendaStatus.innerHTML = `
                <div style="margin-top:10px; display:flex; flex-direction:column; gap:12px; background:rgba(255,255,255,0.02); padding:10px; border-radius:12px; border:1px dashed rgba(255,255,255,0.2);">
                    <div style="display:flex; align-items:center; gap:15px;">
                        <div style="font-size:2rem; background:rgba(255,255,255,0.1); width:50px; height:50px; border-radius:12px; display:flex; justify-content:center; align-items:center;">🗓️</div>
                        <div>
                            <p style="color:#aaa; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin:0;">Propuesta de Sesión</p>
                            <strong style="color:white; font-size:1.1rem;">${dateString}</strong>
                        </div>
                    </div>
                    <div style="display:flex; gap:10px;">
                        <button onclick="updateSessionStatus('Confirmada')" style="flex:1; background:var(--success); color:var(--bg-absolute); border:none; padding:12px; border-radius:8px; cursor:pointer; font-weight:600; font-family:'Outfit';">✅ Aceptar</button>
                        <button onclick="updateSessionStatus('Cancelada')" style="flex:1; background:rgba(255,50,50,0.1); color:#ff6b6b; border:1px solid rgba(255,50,50,0.3); padding:12px; border-radius:8px; cursor:pointer; font-weight:600; font-family:'Outfit';">❌ Rechazar</button>
                    </div>
                </div>
            `;
        } else if (session.status === 'Confirmada') {
            agendaStatus.innerHTML = `
                <div style="margin-top:10px; display:flex; align-items:center; gap:15px; background:linear-gradient(135deg, rgba(0, 229, 255, 0.1), rgba(0,0,0,0)); padding:15px; border-radius:12px; border:1px solid rgba(0, 229, 255, 0.3);">
                    <div style="font-size:2rem; background:var(--accent-water); width:50px; height:50px; border-radius:12px; display:flex; justify-content:center; align-items:center; box-shadow:0 0 15px rgba(0,229,255,0.4);">✨</div>
                    <div style="flex:1;">
                        <p style="color:var(--accent-water); font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin:0; font-weight:bold;">Sesión Confirmada</p>
                        <strong style="color:white; font-size:1.1rem;">${dateString}</strong>
                    </div>
                    <button onclick="updateSessionStatus('Completada')" style="background:transparent; color:#aaa; border:1px solid #555; padding:8px 12px; border-radius:8px; cursor:pointer; font-size:0.8rem; font-family:'Inter'; transition:all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">Finalizar</button>
                </div>
            `;
        }
    }
}
"""
content = re.sub(r'async function loadAgenda\(\) \{.*?\n\}\n\nasync function proposeSession', new_load_agenda.strip() + '\n\nasync function proposeSession', content, flags=re.DOTALL)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Chat UI polished.")
