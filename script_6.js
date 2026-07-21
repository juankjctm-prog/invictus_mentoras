
// --- SIGMA COACH LOGIC ---
let isSigmaOpen = false;

function toggleSigmaChat() {
    const modal = document.getElementById('sigma-modal');
    isSigmaOpen = !isSigmaOpen;
    if(isSigmaOpen) {
        modal.style.opacity = '1';
        modal.style.pointerEvents = 'auto';
        modal.style.transform = 'translateY(0)';
        document.getElementById('sigma-input').focus();
    } else {
        modal.style.opacity = '0';
        modal.style.pointerEvents = 'none';
        modal.style.transform = 'translateY(20px)';
    }
}

function appendSigmaMessage(text, sender) {
    const history = document.getElementById('sigma-chat-history');
    const msgDiv = document.createElement('div');
    msgDiv.className = `sigma-msg ${sender}`;
    msgDiv.innerText = text;
    history.appendChild(msgDiv);
    history.scrollTop = history.scrollHeight;
}

function sendSigmaMessage() {
    const input = document.getElementById('sigma-input');
    const text = input.value.trim();
    if(!text) return;
    
    appendSigmaMessage(text, 'sent');
    input.value = '';
    
    // Simulate Sigma thinking
    setTimeout(() => {
        getSigmaResponse(text);
    }, 800);
}

function getSigmaResponse(userText) {
    const lowerText = userText.toLowerCase();
    let response = "Interesante. Continúa desarrollando esa idea en tu Playbook. La clarificación viene de la acción.";
    
    // Simulated "Smart" Responses based on Invictus concepts
    if(lowerText.includes('impostor') || lowerText.includes('insegura') || lowerText.includes('duda')) {
        response = "El síndrome del impostor es solo una señal de que estás expandiendo tu zona de confort. Recuerda la auditoría de tu historia: no estás aquí por suerte. ¿Qué evidencia tienes hoy de tu propia competencia?";
    } else if (lowerText.includes('lectura') || lowerText.includes('ppm') || lowerText.includes('velocidad')) {
        response = "La lectura cronometrada (Fase 2) no se trata de leer rápido, sino de apagar la subvocalización. Intenta activar el modo Bionic y respira profundamente antes de empezar.";
    } else if (lowerText.includes('ansiedad') || lowerText.includes('estrés')) {
        response = "Entendido. La ansiedad a menudo es energía mal canalizada. Usa el botón SOS (arriba a la derecha) para recalibrar tu frecuencia con una respiración de 8 segundos. Luego vuelve al trabajo.";
    } else if (lowerText.includes('mentada') || lowerText.includes('alumna')) {
        response = "Como mentora, tu trabajo no es darle las respuestas, sino hacer las preguntas socráticas correctas para que ella destruya sus propias excusas. Usa la guía de la sesión 1-a-1 de tu Playbook.";
    } else if (lowerText.includes('hola') || lowerText.includes('buen día')) {
        response = "¡Hola! Tu identidad de liderazgo te trajo aquí. ¿Qué área de tu maestría vamos a fortalecer hoy?";
    }

    appendSigmaMessage(response, 'received');
}
