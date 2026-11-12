# -*- coding: utf-8 -*-
import sys, subprocess, os, importlib
sys.path.insert(0, os.path.dirname(__file__))
from base import *

mods = ["ch12"] + [m for m in ["ch3", "ch4", "ch56"] if os.path.exists(os.path.join(os.path.dirname(__file__), m + ".py"))]
pages = []
for m in mods:
    pages += importlib.import_module(m).PAGES

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{TITULO} · UY3 · {EDICAO}</title><style>{CSS}</style></head><body>
{"".join(p() for p in pages)}
</body></html>'''
out = os.path.join(S, "out")
os.makedirs(out, exist_ok=True)
hp = os.path.join(out, "Manual_de_Identidade_Visual_UY3.html")
open(hp, "w", encoding="utf-8").write(html)
pdf = os.path.join(out, "Manual_de_Identidade_Visual_UY3.pdf")
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                "--no-pdf-header-footer", "--generate-pdf-document-outline", "--export-tagged-pdf", f"--print-to-pdf={pdf}", "file://" + hp],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
print(len(pages), "páginas →", pdf)
