# -*- coding: utf-8 -*-
"""Gera os arquivos oficiais do logotipo UY3 (v1.0) a partir do path vetorial original."""
import os, re, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from base import S, P_ALL, VB, LW, LH, logo_svg_file
import pikepdf

OUT = os.path.join(S, "out", "assets", "logo")
for d in ("svg", "pdf", "png"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
X0, Y0 = 109.789, 131.969


def pdf_path():
    toks = re.findall(r"[MLCZ]|-?\d+(?:\.\d+)?", P_ALL)
    out, i = [], 0
    op = {"M": ("m", 2), "L": ("l", 2), "C": ("c", 6)}
    while i < len(toks):
        t = toks[i]
        if t == "Z":
            out.append("h"); i += 1; continue
        o, n = op[t]
        nums = toks[i + 1:i + 1 + n]
        out.append(" ".join(nums) + " " + o)
        i += 1 + n
    return "\n".join(out)


def make_pdf(path, fill_ops, title, resources=None):
    pdf = pikepdf.new()
    content = f"q\n1 0 0 -1 {-X0:.3f} {LH + Y0:.3f} cm\n{fill_ops}\n{pdf_path()}\nf\nQ\n".encode()
    page = pikepdf.Dictionary(Type=pikepdf.Name.Page, MediaBox=[0, 0, LW, LH],
                              Contents=pdf.make_stream(content),
                              Resources=resources or pikepdf.Dictionary())
    pdf.pages.append(pikepdf.Page(page))
    pdf.docinfo["/Title"] = title
    pdf.docinfo["/Author"] = "UY3 · Gestão da marca"
    pdf.docinfo["/Subject"] = "Logotipo UY3 · Manual de Identidade Visual v1.0 · novembro de 2026"
    pdf.save(path)


VERS = [
    # nome, svg fill, pdf variantes
    ("UY3_logo_principal_brasa", "#F46C00", [
        ("RGB", f"{244/255:.4f} {108/255:.4f} 0 rg", None),
        ("CMYK", "0 0.71 1 0 k", None),
        ("PANTONE-1505C", "/CS0 cs 1 scn", "spot")]),
    ("UY3_logo_negativo_branco", "#FFFFFF", [("RGB", "1 1 1 rg", None)]),
    ("UY3_logo_mono_carbono", "#0C0500", [
        ("RGB", f"{12/255:.4f} {5/255:.4f} 0 rg", None),
        ("CMYK", "0.66 0.66 0.51 1 k", None)]),
]


def spot_resources(pdf_unused=None):
    fn = pikepdf.Dictionary(FunctionType=2, Domain=[0, 1], C0=[0, 0, 0, 0], C1=[0, 0.71, 1, 0], N=1)
    cs = pikepdf.Array([pikepdf.Name.Separation, pikepdf.Name("/PANTONE 1505 C"), pikepdf.Name.DeviceCMYK, fn])
    return pikepdf.Dictionary(ColorSpace=pikepdf.Dictionary(CS0=cs))


files = []
for name, hx, variants in VERS:
    p = os.path.join(OUT, "svg", name + ".svg")
    open(p, "w").write(logo_svg_file(hx)); files.append(p)
    for suf, ops, kind in variants:
        p = os.path.join(OUT, "pdf", f"{name}_{suf}.pdf")
        make_pdf(p, ops, f"Logotipo UY3 · {name} · {suf}", spot_resources() if kind == "spot" else None)
        files.append(p)

# PNG transparentes (2000 px de largura) renderizados do SVG
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    W = 2000; H = round(W * LH / LW)
    pg = b.new_page(viewport={"width": W, "height": H})
    for name, hx, _ in VERS:
        svg = logo_svg_file(hx).replace(f'width="{LW:.3f}" height="{LH:.3f}"', f'width="{W}" height="{H}"')
        pg.set_content(f"<html><body style='margin:0;background:transparent'>{svg}</body></html>")
        p = os.path.join(OUT, "png", f"{name}_{W}px.png")
        pg.screenshot(path=p, omit_background=True, clip={"x": 0, "y": 0, "width": W, "height": H}); files.append(p)
    b.close()
for f in files:
    print(os.path.relpath(f, OUT), os.path.getsize(f))
