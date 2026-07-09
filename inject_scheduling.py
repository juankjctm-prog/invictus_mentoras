import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Show the agenda box in the HTML by removing `display:none;`
content = content.replace('id="conexion-agenda" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; margin-top: 20px; display:none;"',
                          'id="conexion-agenda" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; margin-top: 20px;"')

# 2. Inject scheduling JS logic
agenda_script = """
<script>
// --- MODULO DE AGENDAMIENTO ---
let currentSessionId = null;

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
            <div style="display:flex; gap:10px; align-items:center; margin-top:10px;">
                <input type="datetime-local" id="agenda-date" style="background:rgba(255,255,255,0.1); border:none; padding:10px; color:white; border-radius:8px; font-family:'Inter'; font-size:0.9rem;">
                <button onclick="proposeSession()" style="background:var(--accent-earth); color:var(--bg-absolute); border:none; padding:10px 15px; border-radius:8px; font-family:'Outfit'; font-weight:600; cursor:pointer;">Agendar</button>
            </div>
        `;
        currentSessionId = null;
    } else {
        currentSessionId = session.id;
        const dateObj = new Date(session.proposed_date);
        const dateString = dateObj.toLocaleString('es-ES', { dateStyle: 'long', timeStyle: 'short' });
        
        if(session.status === 'Pendiente') {
            agendaStatus.innerHTML = `
                <div style="margin-top:10px;">
                    <p style="color:#ddd; margin-bottom:10px;">Propuesta para: <strong>${dateString}</strong> (Pendiente)</p>
                    <button onclick="updateSessionStatus('Confirmada')" style="background:var(--accent-water); color:var(--bg-absolute); border:none; padding:8px 15px; border-radius:6px; cursor:pointer; margin-right:10px;">Aceptar</button>
                    <button onclick="updateSessionStatus('Cancelada')" style="background:transparent; color:#aaa; border:1px solid #555; padding:8px 15px; border-radius:6px; cursor:pointer;">Cancelar</button>
                </div>
            `;
        } else if (session.status === 'Confirmada') {
            agendaStatus.innerHTML = `
                <div style="margin-top:10px;">
                    <p style="color:var(--success); margin-bottom:10px;">✨ Confirmada para: <strong>${dateString}</strong></p>
                    <button onclick="updateSessionStatus('Completada')" style="background:rgba(255,255,255,0.1); color:#fff; border:1px solid rgba(255,255,255,0.2); padding:8px 15px; border-radius:6px; cursor:pointer;">Marcar como Realizada</button>
                </div>
            `;
        }
    }
}

async function proposeSession() {
    const input = document.getElementById('agenda-date');
    if(!input || !input.value) return;
    
    let mentoraId = currentUser.role === 'Mentora' ? currentUser.id : chatPartner.id;
    let mentadaId = currentUser.role === 'Mentada' ? currentUser.id : chatPartner.id;
    
    await _supabase.from('mentoras_sessions').insert([{
        mentora_id: mentoraId,
        mentada_id: mentadaId,
        proposed_date: new Date(input.value).toISOString(),
        status: 'Pendiente'
    }]);
    
    // Auto-send a chat message
    const dateStr = new Date(input.value).toLocaleString('es-ES', { dateStyle: 'short', timeStyle: 'short' });
    await _supabase.from('mentoras_messages').insert([{
        sender_id: currentUser.id,
        receiver_id: chatPartner.id,
        content: `🗓️ He propuesto una nueva sesión para el ${dateStr}. Revisa tu calendario arriba.`
    }]);
    
    loadAgenda();
}

async function updateSessionStatus(newStatus) {
    if(!currentSessionId) return;
    
    if(newStatus === 'Cancelada') {
        await _supabase.from('mentoras_sessions').delete().eq('id', currentSessionId);
    } else {
        await _supabase.from('mentoras_sessions').update({ status: newStatus }).eq('id', currentSessionId);
    }
    loadAgenda();
}
</script>
"""

if 'loadAgenda()' not in content:
    content = content.replace('</body>', agenda_script + '\n</body>')

# 3. Hook loadAgenda inside loadConexionTab
# Find `renderChatMessages(messages || []);` and append `loadAgenda();`
if 'loadAgenda();' not in content:
    content = content.replace('renderChatMessages(messages || []);', 'renderChatMessages(messages || []);\n    loadAgenda();')


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected Scheduling logic successfully.")
