import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

nav_match = re.search(r'<nav class="bottom-nav">(.*?)</nav>', text, re.IGNORECASE | re.DOTALL)
if nav_match:
    nav_inner = nav_match.group(1)
    if 'view-kit' not in nav_inner:
        print("Mi Kit button is missing. Injecting it.")
        kit_btn = '''
        <div class="nav-item" onclick="switchTab('view-kit', this)">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            <span>Mi Kit</span>
        </div>
        '''
        # Inject it before the Library item (view-library)
        new_nav = nav_inner.replace('<div class="nav-item" onclick="switchTab(\'view-library\'', kit_btn + '\n        <div class="nav-item" onclick="switchTab(\'view-library\'')
        
        text = text.replace(nav_match.group(1), new_nav)
        
        with codecs.open('app.html', 'w', 'utf-8') as f:
            f.write(text)
        print("Button injected!")
    else:
        print("Button already exists.")
else:
    print("Could not find bottom-nav")
