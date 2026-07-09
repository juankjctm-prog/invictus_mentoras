html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

old_btn = """        .btn-premium:hover { filter: brightness(1.1); transform: translateY(-2px); }
        .btn-premium:active { transform: scale(0.96); filter: brightness(0.9); }
        .btn-premium.fire { background: var(--gradient-fire); color: white; box-shadow: 0 8px 16px var(--accent-fire-glow); }
        .btn-premium.water { background: var(--gradient-water); color: white; box-shadow: 0 8px 16px var(--accent-water-glow); }
        .btn-outline { background: transparent; border: 1px solid var(--border-glow); color: var(--text-primary); padding: 12px 16px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s var(--ease-spring); display: inline-flex; justify-content: center;}
        .btn-outline:active { transform: scale(0.96); }"""

new_btn = """        .btn-premium:hover { filter: brightness(1.1); transform: translateY(-2px); box-shadow: 0 12px 24px rgba(255,255,255,0.1); }
        .btn-premium:active { transform: scale(0.96); filter: brightness(0.9); }
        .btn-premium.fire { background: var(--gradient-fire); color: white; box-shadow: 0 8px 16px var(--accent-fire-glow), inset 0 2px 4px rgba(255,255,255,0.3); border: 1px solid rgba(255,160,100,0.5); text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem; }
        .btn-premium.water { background: var(--gradient-water); color: white; box-shadow: 0 8px 16px var(--accent-water-glow), inset 0 2px 4px rgba(255,255,255,0.3); border: 1px solid rgba(100,200,255,0.5); text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem; }
        .btn-outline { background: rgba(255,255,255,0.03); border: 1px solid var(--border-glow); color: var(--text-primary); padding: 14px 20px; border-radius: 16px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: all 0.3s var(--ease-spring); display: inline-flex; justify-content: center; backdrop-filter: blur(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); text-transform: uppercase; letter-spacing: 0.5px; }
        .btn-outline:hover { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.3); transform: translateY(-1px); }
        .btn-outline:active { transform: scale(0.97); }"""

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected ultra-premium buttons")
else:
    print("Old button styles not found!")
