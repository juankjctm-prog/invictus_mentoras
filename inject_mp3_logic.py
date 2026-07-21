import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

# Replace toggleAudio to support MP3
old_audio = r'let ctx, oscL, oscR, panL, panR, gain, isAudio = false, synth = window.speechSynthesis;\s*let currentVoiceAudio = null;\s*function toggleAudio\(\) \{.*?(?=function initUserSession)'
new_audio = r'''let ctx, oscL, oscR, panL, panR, gain, isAudio = false, synth = window.speechSynthesis;
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
            
            const txt = document.querySelector('.timeline .phase.active p').innerText;

            // Intentar cargar MP3 primero
            mp3Audio = new Audio(`audios/dia_${currentDay}.mp3`);
            mp3Audio.oncanplaythrough = () => {
                mp3Audio.play();
            };
            mp3Audio.onerror = () => {
                // Fallback a SpeechSynthesis si no existe el MP3
                console.log("No MP3 found, falling back to TTS");
                const utterance = new SpeechSynthesisUtterance(txt);
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
            };
            mp3Audio.onended = () => { if(isAudio) toggleAudio(); };
        }

        '''

if 'mp3Audio' not in text:
    text = re.sub(old_audio, new_audio, text, flags=re.IGNORECASE | re.DOTALL)
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Injected MP3 logic!")
else:
    print("Already injected.")
