
        // LOAD PERSISTENT DATA ON INIT
        window.onload = function() {
            if(localStorage.getItem('invictus_recall_score')) {
                let score = localStorage.getItem('invictus_recall_score');
                let ppm = localStorage.getItem('invictus_recall_ppm');
                document.getElementById('reader-content').style.display = 'none';
                document.getElementById('btn-bionic').style.display = 'none';
                document.getElementById('btn-timer').style.display = 'none';
                document.getElementById('test-intro').style.display = 'none';
                
                const res = document.getElementById('recall-result');
                res.style.display = 'block';
                if(score == 100) {
                    res.innerHTML = `<strong>🏆 Inteligencia Consolidada</strong><br>Velocidad: ${ppm} PPM<br>Comprensión: ${score}% (Perfecto)<br><span style="font-size:0.8rem; color:var(--bg-absolute);">Conexión sináptica recuperada de tu sesión anterior.</span>`;
                    res.style.background = "var(--success)"; res.style.color = "var(--bg-absolute)";
                } else {
                    res.innerHTML = `<strong>⚠️ Retención Parcial Guardada</strong><br>Comprensión: ${score}%`;
                    res.style.background = "rgba(255, 94, 0, 0.1)"; res.style.color = "var(--accent-fire)"; res.style.border = "1px solid var(--accent-fire)";
                }
            }
            if(localStorage.getItem('invictus_analog_1') === 'true') { marcarHecho(document.getElementById('btn-analog-1')); }
            if(localStorage.getItem('invictus_analog_2') === 'true') { marcarHecho(document.getElementById('btn-analog-2')); }
            if(localStorage.getItem('invictus_analog_3') === 'true') { marcarHecho(document.getElementById('btn-analog-3')); }
        }



        function switchTab(viewId, element) {

        if (viewId === 'view-kit' && typeof window.updateKitStats === 'function') {
            window.updateKitStats();
        }
    
            document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
            document.getElementById(viewId).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
            if(element.classList.contains('track-card')) document.querySelectorAll('.nav-item')[1].classList.add('active');
            else element.classList.add('active');
        }

        let isBionic = false, originalHTML = [];
        function toggleBionic() {
            const ps = document.querySelectorAll('#reader-content .reader-p');
            const btn = document.getElementById('btn-bionic');
            if(!isBionic) {
                ps.forEach((p, i) => {
                    originalHTML[i] = p.innerHTML;
                    let words = p.innerText.split(' ');
                    p.innerHTML = words.map(w => {
                        let len = Math.ceil(w.length / 2);
                        if(w.length > 3) len = Math.ceil(w.length * 0.4);
                        return `<b style="font-weight:700; color:#FFF;">${w.substring(0,len)}</b><span style="opacity:0.7;">${w.substring(len)}</span>`;
                    }).join(' ');
                });
                isBionic = true; btn.innerHTML = '🧠 Bionic: ON'; btn.style.background = 'rgba(255,255,255,0.1)';
            } else {
                ps.forEach((p, i) => p.innerHTML = originalHTML[i]);
                isBionic = false; btn.innerHTML = '⚡ Lectura Biónica'; btn.style.background = 'transparent';
            }
        }

        
function startBreathing() {
    let circle = document.getElementById('b-circle');
    let text = document.getElementById('b-text');
    let btn = document.getElementById('b-start-btn');
    btn.style.display = 'none';
    let cycles = 2;
    let currentCycle = 0;
    
    function runCycle() {
        if(currentCycle >= cycles) {
            text.innerText = "¡Oxigenación completa! Estás lista.";
            circle.style.transform = "scale(1)";
            circle.innerText = "✓";
            btn.style.display = 'inline-block';
            btn.innerText = "Rehacer Respiración";
            
            // Mark phase completed if not already done
            window.markPhaseDone(null, 1);
            showMotivationToast("¡Excelente preparación! Tu cerebro está oxigenado.");
            return;
        }
        
        currentCycle++;
        // Inhale 4s
        text.innerText = `Ciclo ${currentCycle}/2: INHALA (4s)`;
        circle.style.transition = "transform 4s linear, opacity 4s linear";
        circle.style.transform = "scale(1.5)";
        circle.style.opacity = "1";
        
        setTimeout(() => {
            // Hold 8s
            text.innerText = `Ciclo ${currentCycle}/2: RETÉN (8s)`;
            circle.style.transition = "transform 8s linear";
            circle.style.transform = "scale(1.6)";
            
            setTimeout(() => {
                // Exhale 16s
                text.innerText = `Ciclo ${currentCycle}/2: EXHALA (16s)`;
                circle.style.transition = "transform 16s linear, opacity 16s linear";
                circle.style.transform = "scale(0.8)";
                circle.style.opacity = "0.5";
                
                setTimeout(() => {
                    runCycle();
                }, 16000);
            }, 8000);
        }, 4000);
    }
    
    runCycle();
}

let timer, secs = 0, isRunning = false;

function toggleTimer() {
    const btn = document.getElementById('btn-timer');
    if(!isRunning) {
        isRunning = true;
        btn.innerText = "Detener Cronómetro";
        btn.style.background = "linear-gradient(45deg, #10b981, #059669)";
        
        if(document.getElementById('reader-content').innerText.includes('Activa el cronómetro') === false) {
           document.getElementById('reader-content').style.filter = "none";
           document.getElementById('reader-content').style.userSelect = "auto";
        }

        timer = setInterval(() => {
            secs++;
            const m = Math.floor(secs/60).toString().padStart(2,'0');
            const s = (secs%60).toString().padStart(2,'0');
            btn.innerText = `Detener (${m}:${s})`;
        }, 1000);
    } else {
        clearInterval(timer); isRunning = false;
        const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
        btn.innerText = `Velocidad: ${basePPM} PPM`;
        btn.style.fontSize = '0.9rem';
        btn.style.padding = '8px';
        btn.disabled = true;
        
        document.getElementById('re-read-prompt').style.display = 'block';
    }
}

function resetTimer() {
    secs = 0;
    isRunning = false;
    const btn = document.getElementById('btn-timer');
    btn.disabled = false;
    btn.innerText = "Iniciar Cronómetro";
    btn.style.background = "";
    document.getElementById('re-read-prompt').style.display = 'none';
}

function continueToComprension() {
    document.getElementById('sticky-timer-wrapper').style.display = 'none';
    const basePPM = Math.round((currentDay === 1 ? 1560 : 1920) / (secs>0?secs:1) * 60);
    document.getElementById('comprension-block').style.display = 'block';
    showMotivationToast("Velocidad registrada. Ahora, pongamos a prueba tu retención.");
}


        function iniciarTest() {
            document.getElementById('reader-content').style.display = 'none';
            document.getElementById('btn-bionic').style.display = 'none';
            document.getElementById('btn-timer').style.display = 'none';
            document.getElementById('test-intro').style.display = 'none';
            document.getElementById('test-content').style.display = 'block';
            window.scrollTo({ top: document.getElementById('test-content').offsetTop - 50, behavior: 'smooth' });
        }

        function evaluarRecall() {
            let correctas = 0;
            for(let i=1; i<=5; i++) {
                const radios = document.getElementsByName('q' + i);
                let selected = false;
                for(let r of radios) {
                    if(r.checked) {
                        selected = true;
                        if(r.value === "1") correctas++;
                    }
                }
            }
            let score = (correctas / 5) * 100;
            let ppmText = document.getElementById('ppm-box').innerText;
            let basePPM = ppmText.includes('PPM') ? ppmText.match(/\d+/)[0] : "Pendiente";
            
            localStorage.setItem('invictus_recall_score', score);
            localStorage.setItem('invictus_recall_ppm', basePPM);
            
            const res = document.getElementById('recall-result');
            res.style.display = 'block';
            
            if(score === 100) {
                res.innerHTML = `<strong>🏆 Inteligencia Consolidada</strong><br>Velocidad: ${basePPM} PPM<br>Comprensión: ${score}% (Perfecto)<br><span style="font-size:0.8rem; color:var(--bg-absolute);">Conexión sináptica completada.</span>`;
                res.style.background = "var(--success)"; res.style.color = "var(--bg-absolute)";
            } else if (score >= 60) {
                res.innerHTML = `<strong>⚠️ Retención Parcial</strong><br>Comprensión: ${score}%<br><span style="font-size:0.8rem; color:var(--text-secondary);">Fallaste en ${5 - correctas} pregunta(s). Revisa tus sesgos cognitivos.</span>`;
                res.style.background = "rgba(255, 94, 0, 0.1)"; res.style.color = "var(--accent-fire)"; res.style.border = "1px solid var(--accent-fire)";
            } else {
                res.innerHTML = `<strong>🚨 Fuga Cognitiva</strong><br>Comprensión: ${score}%<br><span style="font-size:0.8rem; color:var(--text-secondary);">Tu atención divagó. Debes mejorar el enfoque mañana.</span>`;
                res.style.background = "rgba(255, 69, 0, 0.2)"; res.style.color = "#FF4500"; res.style.border = "1px solid #FF4500";
            }
        }

        let ctx, oscL, oscR, panL, panR, gain, isAudio = false, synth = window.speechSynthesis;
        let currentVoiceAudio = null;
        let mp3Audio = null;

        function toggleAudio() {
            const pill = document.getElementById('audio-pill');
            const circle = document.getElementById('play-circle');
            const icon = circle.querySelector('.play-icon');
            
            if (isAudio) {
                // Stop audio
                if (ctx) ctx.close();
                synth.cancel();
                if (mp3Audio) {
                    mp3Audio.pause();
                    mp3Audio.currentTime = 0;
                }
                isAudio = false;
                pill.classList.remove('active');
                icon.style.borderLeft = "10px solid #fff";
                icon.style.borderRight = "none";
                icon.style.width = "0";
                icon.style.height = "0";
                icon.style.borderTop = "7px solid transparent";
                icon.style.borderBottom = "7px solid transparent";
                return;
            }

            // Start Audio
            isAudio = true;
            pill.classList.add('active');
            icon.style.borderLeft = "4px solid #fff";
            icon.style.borderRight = "4px solid #fff";
            icon.style.borderTop = "none";
            icon.style.borderBottom = "none";
            icon.style.width = "12px";
            icon.style.height = "14px";
            
            let msgText = "Respira profundo. Estás entrando en un estado de paz absoluta. La identidad de liderazgo no se espera; se ejerce. Empieza a tomar decisiones como la líder que ya eres, y tu mente terminará creyéndolo. Reclama tu éxito en primera persona. El síndrome del impostor se desvanece mientras tu neuroplasticidad graba tu verdadera autoridad. Duerme profundamente y despierta imparable.";
                
                if (window.activeTrackData) {
                    const d = window.activeTrackData.find(x => x.dia === currentDay);
                    if (d && d.fase12_sueno && d.fase12_sueno.resumen) {
                        msgText = d.fase12_sueno.resumen + " " + d.fase12_sueno.conceptos + " " + d.fase12_sueno.afirmacion;
                    }
                }

            // Intentar cargar MP3 primero
            mp3Audio = new Audio(`audios/dia_${currentDay}.mp3`);
            mp3Audio.play().catch(err => {
                // Fallback a SpeechSynthesis si no existe el MP3
                console.log("No MP3 found, falling back to TTS", err);
                const utterance = new SpeechSynthesisUtterance(msgText);
                utterance.lang = 'es-ES';
                utterance.pitch = 0.9;
                utterance.rate = 0.9;
                utterance.onend = () => { if(isAudio) toggleAudio(); };
                
                // Theta Binaural
                ctx = new (window.AudioContext || window.webkitAudioContext)();
                oscL = ctx.createOscillator(); oscR = ctx.createOscillator();
                panL = ctx.createStereoPanner(); panR = ctx.createStereoPanner();
                gain = ctx.createGain();
                
                oscL.frequency.value = 136.1; oscR.frequency.value = 142.1;
                panL.pan.value = -1; panR.pan.value = 1;
                gain.gain.value = 0.05;
                
                oscL.connect(panL); panL.connect(gain);
                oscR.connect(panR); panR.connect(gain);
                gain.connect(ctx.destination);
                
                oscL.start(); oscR.start();
                synth.speak(utterance);
            });
            mp3Audio.onended = () => { if(isAudio) toggleAudio(); };
        }

        async function initUserSession() {
    if(!currentUser) return;
    
    window.activeTrackData = currentUser.role === 'Mentada' ? (typeof mentadasData !== 'undefined' ? mentadasData : []) : (typeof mujeresMentorasData !== 'undefined' ? mujeresMentorasData : []);
    
    // Fetch from Supabase
    const { data, error } = await _supabase.from('mentoras_progress').select('*').eq('user_id', currentUser.id).single();
    
    if(data) {
        currentDay = data.current_day || 1;
        completedDays = data.completed_days || [];
        currentPhaseProgress = data.phase_progress || {};
        currentAnswers = data.answers || {};
    } else {
        currentDay = 1;
        completedDays = [];
        currentPhaseProgress = {};
        currentAnswers = {};
    }
    
    // Find highest incomplete day or 1
    let target = 1;
    while(completedDays.includes(target)) target++;
    if(target > window.activeTrackData.length) target = window.activeTrackData.length;
    
    // Check if target day was manually overridden in currentDay
    if(currentDay > target && completedDays.includes(currentDay-1)) target = currentDay;
    
    loadMujeresMentorasDay(target);
    renderDaySwitcher();

    if(currentUser.role === 'Mentora') {
        const mentadaTab = document.querySelector('.mentada-tab-btn');
        if(mentadaTab) mentadaTab.style.display = 'flex';
    }
    
}

async function saveProgress() {
    if(!currentUser) return;
    
    // Optimistic UI Update
    updateVisualProgress();
    
    // Persist to Supabase
    await _supabase.from('mentoras_progress').upsert({
        user_id: currentUser.id,
        current_day: currentDay,
        completed_days: completedDays,
        phase_progress: currentPhaseProgress,
        answers: currentAnswers,
        updated_at: new Date().toISOString()
    });
}
