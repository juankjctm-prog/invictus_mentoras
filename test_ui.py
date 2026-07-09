import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        errors = []
        page.on("pageerror", lambda err: errors.append(f"PageError: {err}"))
        page.on("console", lambda msg: errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)
        
        file_url = f"file:///{os.path.abspath('Invictus_Mentoras.html').replace(chr(92), '/')}"
        print(f"Navigating to {file_url}")
        
        await page.goto(file_url)
        await page.wait_for_timeout(1000)
        
        # Click HOME
        await page.evaluate("switchTab('view-dashboard', document.querySelector('.nav-item:nth-child(1)'))")
        
        # Click CONEXION
        await page.evaluate("switchTab('view-conexion', document.querySelector('.nav-item:nth-child(5)'))")
        
        # Click HOME again
        await page.evaluate("switchTab('view-dashboard', document.querySelector('.nav-item:nth-child(1)'))")
        
        for e in errors:
            print(e)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
