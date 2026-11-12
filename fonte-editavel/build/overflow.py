from playwright.sync_api import sync_playwright
S="/tmp/claude-0/-home-claude/1ca3015c-558b-533c-93f8-815ce1894cd1/scratchpad"
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1123,"height":794})
    pg.goto("file://"+S+"/out/Manual_de_Identidade_Visual_UY3.html"); pg.wait_for_timeout(800)
    r=pg.evaluate("""()=>{const out=[];document.querySelectorAll('section.pg').forEach(s=>{const ct=s.querySelector('.ct').getBoundingClientRect();
       s.querySelectorAll('.ct *').forEach(e=>{ if(e.closest('.frame')||e.closest('.tile')||e.closest('svg')&&e.tagName!=='svg') return;
         const r=e.getBoundingClientRect(); if(r.width==0) return;
         if(r.right>ct.right+1.5||r.bottom>ct.bottom+1.5||r.left<ct.left-1.5||r.top<ct.top-1.5) out.push([s.id,e.tagName,Math.round(r.right-ct.right),Math.round(r.bottom-ct.bottom),(e.textContent||'').trim().slice(0,30)])}) });
       return out}""")
    for x in r: print(x)
    print("ocorrências:",len(r))
    b.close()
