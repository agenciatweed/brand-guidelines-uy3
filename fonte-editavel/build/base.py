# -*- coding: utf-8 -*-
"""Base: tokens, logotipo, utilitários e CSS do Manual de Identidade Visual UY3."""
import os

S = "/tmp/claude-0/-home-claude/1ca3015c-558b-533c-93f8-815ce1894cd1/scratchpad"
FONT = f"file://{S}/fonts/InterVariable.ttf"
FONT_I = f"file://{S}/fonts/InterVariable-Italic.ttf"

EDICAO = "Versão 1.0 · Novembro 2026"
TITULO = "Manual de Identidade Visual"

# ---------- Tokens (design.md) ----------
C = {
    "brasa": "#F46C00", "brasa-alta": "#FF8C45", "brasa-profunda": "#C4560F",
    "brasa-tinta": "#9D430B", "brasa-lavada": "rgba(244,108,0,.12)",
    "carbono-profundo": "#0C0500", "carbono": "#150903", "carbono-quente": "#261003",
    "carbono-claro": "#3A1C08", "papel": "#FFFFFF", "creme": "#F9F1ED",
    "creme-fechado": "#F1E4DC", "creme-contato": "#F4DFD2", "tinta": "#231107",
    "tinta-suave": "#6B5548", "tinta-clara": "#F6ECE6", "tinta-clara-suave": "#B09A8D",
    "rail": "#F6853A",
}

# CMYK indicativo (perfil FOGRA39, intenção colorimétrica relativa) — calculado
CMYK_IND = {
    "#F46C00": "0 · 71 · 100 · 0", "#0C0500": "66 · 66 · 51 · 100", "#150903": "56 · 68 · 51 · 100",
    "#261003": "20 · 74 · 69 · 98", "#F9F1ED": "4 · 5 · 7 · 0", "#231107": "31 · 72 · 62 · 99",
    "#6B5548": "54 · 61 · 68 · 36", "#9D430B": "0 · 73 · 100 · 43", "#C4560F": "2 · 70 · 98 · 22",
    "#FF8C45": "0 · 56 · 79 · 1", "#F4DFD2": "7 · 15 · 18 · 0", "#FFFFFF": "0 · 0 · 0 · 0",
    "#B09A8D": "33 · 38 · 42 · 7", "#F6ECE6": "5 · 7 · 10 · 0",
}


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    out = []
    for x in rgb(h):
        x = x / 255
        out.append(x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def fmt(x):
    return f"{x:.2f}".replace(".", ",")


# ---------- Logotipo (vetor original extraído de "logo UY3-.pdf") ----------
VB = "109.789 131.969 622.434 329.324"   # caixa delimitadora observada
LW, LH = 622.434, 329.324                 # proporção 1,890 : 1
STROKE = 55.6                              # espessura média das hastes (U 55,71 · Y 55,41)
P_3 = ("M 672.109375 422.265625 C 724.140625 370.230469 724.140625 285.566406 672.109375 233.535156 "
       "L 632.925781 272.714844 C 663.355469 303.144531 663.355469 352.65625 632.925781 383.085938 "
       "C 602.496094 413.515625 552.984375 413.515625 522.554688 383.085938 L 483.375 422.265625 "
       "C 509.390625 448.28125 543.566406 461.292969 577.742188 461.292969 "
       "C 611.914062 461.292969 646.09375 448.28125 672.109375 422.265625 Z")
P_Y = ("M 499.503906 131.96875 L 419.722656 211.75 L 341.121094 133.148438 L 262.757812 133.148438 "
       "L 391.820312 262.214844 L 391.820312 458.898438 L 447.234375 458.898438 L 447.234375 262.597656 "
       "L 522.453125 187.378906 L 598.445312 187.378906 L 540.300781 245.523438 L 579.480469 284.703125 "
       "L 732.222656 131.96875 Z")
P_U = ("M 357.167969 275.074219 L 357.167969 346.632812 C 354.898438 376.625 341.808594 405.953125 317.820312 428.222656 "
       "C 270.527344 472.128906 196.414062 472.125 149.128906 428.214844 C 125.144531 405.945312 112.058594 376.617188 109.792969 346.628906 "
       "L 109.789062 346.628906 L 109.789062 133.164062 L 165.496094 133.164062 L 165.496094 346.613281 "
       "C 168.386719 367.710938 181.042969 387.714844 203.519531 399.199219 C 222.269531 408.777344 244.707031 408.777344 263.457031 399.191406 "
       "C 285.921875 387.703125 299.128906 367.410156 301.464844 346.613281 L 301.464844 219.367188 Z")
P_ALL = P_3 + " " + P_Y + " " + P_U


def logo(fill=C["brasa"], h=None, w=None, style="", extra="", title="Logotipo UY3"):
    size = f"height:{h}mm;width:auto;" if h else f"width:{w}mm;height:auto;"
    return (f'<svg class="logo" role="img" aria-label="{title}" viewBox="{VB}" '
            f'style="display:block;{size}{style}" xmlns="http://www.w3.org/2000/svg">'
            f'<path fill="{fill}" d="{P_ALL}"/>{extra}</svg>')


def logo_svg_file(fill):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{VB}" width="{LW:.3f}" height="{LH:.3f}"><title>UY3</title>'
            f'<path fill="{fill}" d="{P_ALL}"/></svg>\n')


# ---------- Ícones (traço fino 1,6 · viewBox 24 · sem preenchimento) ----------
ICONS = {
    "seta": '<path d="M7 17 17 7M9 7h8v8"/>',
    "camadas": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
    "fluxo": '<circle cx="5" cy="12" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 12h4m0 0 6-5m-6 5 6 5"/>',
    "documento": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="m10 14 2 2 4-4"/>',
    "escudo": '<path d="M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "relogio": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "api": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 6l-3 12"/>',
    "check": '<path d="m5 12 5 5 9-10"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18"/>',
    "alerta": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.2v.3"/>',
}


def icon(name, size=6, color="currentColor", sw=1.6):
    return (f'<svg viewBox="0 0 24 24" style="width:{size}mm;height:{size}mm;display:block" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


CHAPTERS = {
    1: "Abertura e fundamentos", 2: "Assinatura e uso do logotipo", 3: "Sistema cromático",
    4: "Tipografia", 5: "Linguagem visual e composição", 6: "Aplicações e governança",
}
CH_SHORT = {1: "Fundamentos", 2: "Logotipo", 3: "Cores", 4: "Tipografia", 5: "Sistema visual", 6: "Aplicações"}


def page(n, ch, body, theme="light", chrome=True, label=None):
    cls = {"light": "pg", "dark": "pg dark", "brasa": "pg brasa", "papel": "pg papel"}[theme]
    hd = ""
    if chrome:
        hd = (f'<div class="hd"><span>UY3 · {TITULO}</span>'
              f'<span>{ch:02d} &nbsp;{CH_SHORT[ch]}</span></div>'
              f'<div class="ft"><span>{EDICAO}</span><span class="pn">{n:02d}</span></div>')
    return f'<section class="{cls}" id="p{n}" aria-label="Página {n}">{hd}<div class="ct">{body}</div></section>'


def badge(ok, text=None, theme="light"):
    if ok is True:
        t = text or "Correto"
        return f'<span class="bdg ok">{icon("check", 2.6, sw=2.4)}{t}</span>'
    if ok is False:
        t = text or "Incorreto"
        return f'<span class="bdg no">{icon("x", 2.6, sw=2.4)}{t}</span>'
    return f'<span class="bdg cond">{icon("alerta", 2.6, sw=2.2)}{text or "Com condição"}</span>'


CSS = f"""
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-400.ttf') format('truetype'); font-weight: 400; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-500.ttf') format('truetype'); font-weight: 500; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-600.ttf') format('truetype'); font-weight: 600; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-620.ttf') format('truetype'); font-weight: 620; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-650.ttf') format('truetype'); font-weight: 650; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-700.ttf') format('truetype'); font-weight: 700; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-800.ttf') format('truetype'); font-weight: 800; font-style: normal; }}
@font-face {{ font-family: 'Inter'; src: url('file://{S}/fonts/static/InterUY3-400i.ttf') format('truetype'); font-weight: 400; font-style: italic; }}
@font-face {{ font-family: 'InterD'; src: url('file://{S}/fonts/static/InterUY3-620d.ttf') format('truetype'); font-weight: 620; }}
@page {{ size: 297mm 210mm; margin: 0; }}
:root {{
  --brasa:#F46C00; --brasa-alta:#FF8C45; --brasa-prof:#C4560F; --brasa-tinta:#9D430B; --brasa-lav:rgba(244,108,0,.12);
  --cp:#0C0500; --cb:#150903; --cq:#261003; --cc:#3A1C08; --papel:#FFFFFF; --creme:#F9F1ED; --cf:#F1E4DC; --ccont:#F4DFD2;
  --tinta:#231107; --ts:#6B5548; --tc:#F6ECE6; --tcs:#B09A8D;
  --fio:rgba(35,17,7,.10); --fio2:rgba(35,17,7,.05); --fioe:rgba(255,255,255,.10); --fioe2:rgba(255,255,255,.055);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #ccc; }}
body {{ font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; color: var(--tinta);
  font-feature-settings: 'cv05' 1, 'cv11' 1, 'ss03' 1; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.pg {{ width: 297mm; height: 210mm; position: relative; overflow: hidden; background: var(--creme);
  page-break-after: always; break-after: page; --txt: var(--tinta); --soft: var(--ts); --hair: var(--fio); --acc: var(--brasa-tinta); color: var(--txt); }}
.pg.papel {{ background: var(--papel); }}
.pg.dark {{ background: var(--cp); --txt: var(--tc); --soft: var(--tcs); --hair: var(--fioe); --acc: var(--brasa-alta); }}
.pg.brasa {{ background: var(--brasa); --txt: var(--cp); --soft: rgba(12,5,0,.78); --hair: rgba(12,5,0,.22); --acc: var(--cp); }}
.hd, .ft {{ position: absolute; left: 16mm; right: 16mm; display: flex; justify-content: space-between;
  font-size: 7pt; letter-spacing: .01em; color: var(--soft); font-weight: 500; }}
.hd {{ top: 9mm; padding-bottom: 2.2mm; border-bottom: .25mm solid var(--hair); }}
.ft {{ bottom: 8mm; }}
.ft .pn {{ font-weight: 650; color: var(--txt); font-feature-settings: 'tnum' 1; }}
.ct {{ position: absolute; top: 22mm; left: 16mm; right: 16mm; bottom: 17mm; }}
.g12 {{ display: grid; grid-template-columns: repeat(12, 1fr); column-gap: 5mm; height: 100%; }}
.eb {{ font-size: 7pt; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: var(--acc); margin-bottom: 3.2mm; }}
.t1 {{ font-family: 'InterD', 'Inter', sans-serif; font-size: 30pt; font-weight: 620; line-height: 1.04; letter-spacing: -.035em; }}
.t0 {{ font-family: 'InterD', 'Inter', sans-serif; font-size: 46pt; font-weight: 620; line-height: 1.0; letter-spacing: -.042em; }}
.t2 {{ font-size: 14pt; font-weight: 600; line-height: 1.22; letter-spacing: -.018em; }}
.t3 {{ font-size: 10.5pt; font-weight: 600; line-height: 1.3; letter-spacing: -.01em; }}
p, li {{ font-size: 10pt; line-height: 1.5; }}
.lede {{ font-size: 11.5pt; line-height: 1.5; color: var(--txt); }}
.soft {{ color: var(--soft); }}
.cap {{ font-size: 8pt; line-height: 1.4; color: var(--soft); }}
.mono {{ font-family: ui-monospace, 'DejaVu Sans Mono', monospace; font-size: 7.6pt; }}
.tn {{ font-feature-settings: 'tnum' 1, 'cv05' 1, 'cv11' 1; }}
.mt1 {{ margin-top: 2mm; }} .mt2 {{ margin-top: 4mm; }} .mt3 {{ margin-top: 6mm; }} .mt4 {{ margin-top: 9mm; }}
.hr {{ border-top: .25mm solid var(--hair); }}
ul.l {{ list-style: none; }} ul.l li {{ padding: 1.6mm 0; border-top: .25mm solid var(--hair); }}
ul.l li:last-child {{ border-bottom: .25mm solid var(--hair); }}
.card {{ background: var(--papel); border: .25mm solid var(--fio); border-radius: 4mm; }}
.dark .card {{ background: linear-gradient(168deg, rgba(255,255,255,.055), rgba(255,255,255,.012)); border-color: var(--fioe);
  box-shadow: inset 0 .3mm 0 rgba(255,255,255,.10); }}
.shell {{ background: rgba(35,17,7,.035); border: .25mm solid var(--fio); border-radius: 6mm; padding: 1.5mm; }}
.core {{ background: var(--papel); border: .25mm solid var(--fio); border-radius: 4.5mm; }}
.tile {{ border-radius: 3mm; position: relative; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
.lbl {{ font-size: 7.4pt; font-weight: 600; color: var(--txt); }}
.bdg {{ display: inline-flex; align-items: center; gap: 1.2mm; font-size: 7.2pt; font-weight: 700; padding: .9mm 2.4mm .9mm 1.6mm; border-radius: 99mm; white-space: nowrap; }}
.bdg.ok {{ background: var(--tinta); color: var(--tc); }}
.bdg.no {{ background: var(--papel); color: var(--tinta); border: .35mm solid var(--tinta); }}
.bdg.cond {{ background: var(--brasa-lav); color: var(--brasa-tinta); }}
.dark .bdg.ok {{ background: var(--tc); color: var(--cp); }}
.strike {{ position: absolute; inset: 0; background: linear-gradient(to top right, transparent calc(50% - .2mm), var(--tinta) calc(50% - .2mm), var(--tinta) calc(50% + .2mm), transparent calc(50% + .2mm)); opacity: .55; }}
.pill {{ display: inline-flex; align-items: center; border-radius: 99mm; font-weight: 600; }}
.sw {{ border-radius: 3mm; position: relative; }}
.ann {{ position: absolute; font-size: 6.8pt; color: var(--brasa-tinta); font-weight: 600; white-space: nowrap; }}
.dark .ann {{ color: var(--brasa-alta); }}
.annl {{ position: absolute; border-top: .25mm solid var(--brasa-prof); }}
.dark .annl {{ border-color: var(--brasa-alta); }}
table.tb {{ width: 100%; border-collapse: collapse; font-size: 8pt; }}
table.tb th {{ text-align: left; font-size: 6.4pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--soft); padding: 1.6mm 1.4mm; border-bottom: .3mm solid var(--txt); }}
table.tb td {{ padding: 1.5mm 1.4mm; border-bottom: .25mm solid var(--hair); vertical-align: middle; }}
table.tb td.r, table.tb th.r {{ text-align: right; font-feature-settings: 'tnum' 1; }}
.chip {{ display: inline-block; width: 4.5mm; height: 4.5mm; border-radius: 1mm; vertical-align: middle; border: .25mm solid var(--fio); }}
.frame {{ position: absolute; overflow: hidden; contain: strict; }}
.frame > .inner {{ transform-origin: 0 0; position: absolute; top: 0; left: 0; }}
.num {{ font-size: 8pt; font-weight: 700; color: var(--acc); font-feature-settings: 'tnum' 1; }}
.mute {{ opacity: .45; }}
.note {{ font-size: 7.6pt; line-height: 1.45; color: var(--soft); padding-left: 2.5mm; border-left: .5mm solid var(--brasa); }}
"""


def frame(x_mm, y_mm, w_mm, design_w_px, design_h_px, inner_html, radius=0, extra_style=""):
    """Moldura que escala uma composição desenhada em px (tokens do site) para mm."""
    px_mm = 0.264583
    scale = w_mm / (design_w_px * px_mm)
    h_mm = design_h_px * px_mm * scale
    return (f'<div class="frame" style="left:{x_mm}mm;top:{y_mm}mm;width:{w_mm}mm;height:{h_mm:.2f}mm;'
            f'border-radius:{radius}mm;{extra_style}"><div class="inner" style="width:{design_w_px}px;'
            f'height:{design_h_px}px;transform:scale({scale:.5f})">{inner_html}</div></div>'), h_mm
