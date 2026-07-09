import re

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Supabase SDK
if 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2' not in content:
    content = content.replace(
        '</body>',
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\n</body>'
    )

# 2. Inject Supabase Init and Replace Logic
supabase_logic = """
<script>
// --- SUPABASE CONFIG ---
const supabaseUrl = 'https://unbaagnuwdhavqkajory.supabase.co';
const supabaseKey = 'sb_publishable_8G_qiAoStdmRsEwPfvaa0g__2XlfLjV';
const _supabase = supabase.createClient(supabaseUrl, supabaseKey);

// --- REFACTOR: AUTH & PROGRESS ---
window.pressKey = async function(num) {
    if(!num) num = ''; // fallback
    if(pinCount < 6) {
        currentPin += num;
        document.querySelectorAll('.pin-dots .dot')[pinCount].classList.add('filled');
        pinCount++;
        
        if(pinCount === 6) {
            // Verify with Supabase
            const { data: user, error } = await _supabase.from('mentoras_users').select('*').eq('pin', currentPin).single();
            if(user) {
                // Success
                currentUser = user;
                
                // Update Header
                const headerTitle = document.querySelector('.header-greeting h1');
                const profilePic = document.querySelector('.profile-pic');
                if(headerTitle) headerTitle.innerText = `Hola, ${user.name}`;
                if(profilePic) profilePic.innerText = user.name.charAt(0);
                
                setTimeout(() => {
                    document.getElementById('auth-overlay').classList.add('hidden');
                    initUserSession(); // Load their specific data
                }, 400);
            } else {
                // Error
                const dotsContainer = document.querySelector('.pin-dots');
                const dots = document.querySelectorAll('.pin-dots .dot');
                dots.forEach(d => d.classList.add('error'));
                dotsContainer.classList.add('shake-error');
                
                setTimeout(() => {
                    dotsContainer.classList.remove('shake-error');
                    dots.forEach(d => {
                        d.classList.remove('filled');
                        d.classList.remove('error');
                    });
                    currentPin = '';
                    pinCount = 0;
                }, 500);
            }
        }
    }
};

async function initUserSession() {
    if(!currentUser) return;
    
    window.activeTrackData = currentUser.role === 'Mentada' ? window.mentadasData : window.mujeresMentorasData;
    
    // Fetch from Supabase
    const { data, error } = await _supabase.from('mentoras_progress').select('*').eq('user_id', currentUser.id).single();
    
    if(data) {
        currentDay = data.current_day || 1;
        completedDays = data.completed_days || [];
        currentPhaseProgress = data.phase_progress || {};
    } else {
        currentDay = 1;
        completedDays = [];
        currentPhaseProgress = {};
    }
    
    // Find highest incomplete day or 1
    let target = 1;
    while(completedDays.includes(target)) target++;
    if(target > window.activeTrackData.length) target = window.activeTrackData.length;
    
    // Check if target day was manually overridden in currentDay
    if(currentDay > target && completedDays.includes(currentDay-1)) target = currentDay;
    
    loadMujeresMentorasDay(target);
    renderDaySwitcher();
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
        updated_at: new Date().toISOString()
    });
}
</script>
"""

# Replace the block from window.pressKey to saveProgress() with the new logic.
# Wait, replacing using a script is easier if I just find and replace the whole block or append it to override.
# Given JS allows redefining functions, I can just append `supabase_logic` right before </body>.
# But `window.pressKey` and `initUserSession` might get called before? No, they are user-triggered.

# Let's clean the old logic by replacing it, or just injecting it. 
# It's cleaner to remove the old functions and replace them, but they are in a <script> block with other things.
# So I'll use regex to remove them.

pattern = re.compile(r'window\.pressKey = function.*?saveProgress\(\) \{.*?updateVisualProgress\(\);\n\}', re.DOTALL)
content = pattern.sub('', content)

# Remove the old initUserSession if it's there
pattern2 = re.compile(r'function initUserSession\(\) \{.*?renderDaySwitcher\(\);\n\}', re.DOTALL)
content = pattern2.sub('', content)

# Now inject the new logic before </body>
content = content.replace('</body>', supabase_logic + '\n</body>')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected Supabase Logic successfully.")
