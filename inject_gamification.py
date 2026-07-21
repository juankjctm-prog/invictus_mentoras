import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Gamification Logic (call saveDailyProgress)
gamification_hook = """
        // Auto-complete day if phase 12 is done (or all 12 are done)
        if(currentPhaseProgress[currentDay].length === 12 || phaseNum === 12) {
            if(!completedDays.includes(currentDay)) {
                completedDays.push(currentDay);
                let score = localStorage.getItem('invictus_recall_score') || 0;
                let ppm = localStorage.getItem('invictus_recall_ppm') || 0;
                if (typeof saveDailyProgress === 'function') {
                    saveDailyProgress(currentDay, parseInt(ppm), parseInt(score));
                }
            }
"""
content = content.replace("if(currentPhaseProgress[currentDay].length === 12 || phaseNum === 12) {\n            if(!completedDays.includes(currentDay)) completedDays.push(currentDay);", gamification_hook)

# 2. Block future days in Playbook Dropdown
playbook_dropdown_hook = """
function populatePlaybookDays() {
    const selector = document.getElementById('playbook-day-selector');
    if(!selector) return;
    selector.innerHTML = '<option value="">-- Selecciona el Día --</option>';
    
    // Check maxUnlockedDay from dashboard
    let maxDay = (typeof maxUnlockedDay !== 'undefined') ? maxUnlockedDay : 78;
    
    for(let i=1; i<=maxDay; i++) {
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = `Día ${i}`;
        selector.appendChild(opt);
    }
    
    if(window.currentDayIndex && window.currentDayIndex <= maxDay) {
        selector.value = window.currentDayIndex;
        loadPlaybookDay(window.currentDayIndex);
    }
}
"""

# Find populatePlaybookDays and replace it
pattern_playbook = r'function populatePlaybookDays\(\) \{.*?\n\}'
content = re.sub(pattern_playbook, playbook_dropdown_hook.strip(), content, flags=re.DOTALL)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gamification rules injected.")
