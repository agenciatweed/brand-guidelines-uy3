# -*- coding: utf-8 -*-
from base import *
from ch12 import opener, spec_rows, PHOTO

FEAT = "font-feature-settings:'cv05' 1,'cv11' 1,'ss03' 1;"


def p31():
    t = lambda inner, name, d: f'''<div style="display:flex;flex-direction:column;gap:2.4mm"><div class="tile" style="height:46mm;background:#150903;box-shadow:inset 0 .3mm 0 rgba(255,255,255,.08)">{inner}</div>
      <div class="t3" style="color:#F6ECE6;font-size:9.6pt">{name}</div><p class="cap" style="color:#B09A8D">{d}</p></div>'''
    carb = '<div style="display:flex;width:80%;height:60%;border-radius:2mm;overflow:hidden">' + "".join(f'<div style="flex:1;background:{c}"></div>' for c in ["#0C0500", "#150903", "#261003", "#3A1C08"]) + "</div>"
    bras = '<div style="display:flex;gap:2mm;align-items:center">' + "".join(f'<div style="width:9mm;height:9mm;border-radius:99mm;background:{"#F46C00" if i == 2 else "rgba(255,255,255,.08)"}"></div>' for i in range(5)) + "</div>"
    shell = '<div style="background:rgba(255,255,255,.05);border:.25mm solid rgba(255,255,255,.10);border-radius:6mm;padding:1.5mm;width:60%;height:62%"><div style="height:100%;border-radius:4.5mm;background:rgba(255,255,255,.06);border:.25mm solid rgba(255,255,255,.10);box-shadow:inset 0 .3mm 0 rgba(255,255,255,.14)"></div></div>'
    fio = '<div style="width:75%">' + "".join('<div style="height:7mm;border-top:.25mm solid rgba(255,255,255,.12)"></div>' for _ in range(4)) + "</div>"
    ex = f'''<div style="position:absolute;left:0;right:0;top:14mm;display:grid;grid-template-columns:repeat(4,1fr);gap:5mm">
      {t(carb, "Carbono queimado", "Todo escuro é marrom, nunca preto neutro.")}{t(bras, "Brasa como sinal", "O laranja marca estado, caminho e ação.")}
      {t(shell, "Casca dupla", "Raios concêntricos calculados por subtração.")}{t(fio, "Fio de cabelo", "Bordas de 1 px, alfa de 5–10%.")}</div>'''
    return opener(32, 5, "Sistema visual", "O volume vem do material, não do brilho. Plano em repouso; a sombra só aparece como resposta.", ex)


def p32():
    W, H = 150, 106.06
    k = W / 297
    cols = "".join(f'<div style="position:absolute;top:{22*k}mm;bottom:{17*k}mm;left:{(16 + i*(265-55)/12 + i*5)*k}mm;width:{(265-55)/12*k}mm;background:rgba(244,108,0,.12)"></div>' for i in range(12))
    diag = f'''<div style="position:relative;width:{W}mm;height:{H}mm;background:#fff;border:.25mm solid var(--fio);border-radius:1mm">{cols}
      <div style="position:absolute;left:{16*k}mm;right:{16*k}mm;top:{9*k}mm;border-top:.25mm solid rgba(35,17,7,.3)"></div>
      <div style="position:absolute;left:{16*k}mm;right:{16*k}mm;top:{22*k}mm;bottom:{17*k}mm;border:.25mm dashed #C4560F"></div></div>'''
    def thumb(inner):
        return f'<div style="position:relative;width:47mm;height:33mm;background:#F9F1ED;border:.25mm solid var(--fio);border-radius:1mm;overflow:hidden">{inner}</div>'
    bl = lambda l, t, w, h, c="rgba(35,17,7,.16)": f'<div style="position:absolute;left:{l}mm;top:{t}mm;width:{w}mm;height:{h}mm;background:{c};border-radius:.6mm"></div>'
    th1 = thumb(bl(3, 5, 30, 4, "rgba(35,17,7,.8)") + bl(3, 11, 22, 4, "rgba(35,17,7,.8)") + bl(3, 26, 44, 6, "#F46C00"))
    th2 = thumb(bl(3, 5, 18, 3, "rgba(35,17,7,.8)") + "".join(bl(3, 11 + i*2.4, 22, 1) for i in range(8)) + bl(27, 5, 20, 26, "#fff"))
    th3 = thumb("".join(bl(3 + i*11.2, 12, 10, 19, "#fff") for i in range(4)) + bl(3, 5, 30, 3.4, "rgba(35,17,7,.8)"))
    site = [("Container", "1240 px (largo: 1440 px)"), ("Goteira", "clamp(1,25 rem, 4vw, 2,5 rem)"), ("Gap entre cards", "0,85 rem (Regra do Gap Apertado)"),
            ("Ritmo vertical", "seções em clamp(5,5 rem … 10,5 rem)"), ("Quebras", "1080 · 900 · 767 px"), ("Bento", "12 colunas, spans 3/4/6/8")]
    b = f'''<div class="g12">
      <div style="grid-column:1/6">
        <div class="eb">Grid e composição</div><div class="t1" style="font-size:24pt">Doze colunas para documentos</div>
        <div class="mt3">{spec_rows([("Formato", "A4 paisagem · 297 × 210 mm"), ("Margens", "16 mm laterais · 22 mm topo · 17 mm base"), ("Colunas", "12, com goteira de 5 mm (17,5 mm cada)"), ("Cabeçalho", "a 9 mm do topo, sobre fio de cabelo"), ("Escala de espaço", "2 · 4 · 6 · 9 mm entre blocos")])}</div>
        <div class="t3 mt3">Site · DESIGN.md</div><div class="mt1">{spec_rows(site)}</div>
        <p class="note mt2">O grid deste manual vale para documentos, apresentações em A4 e PDFs. O site usa outra lógica, de container centrado.</p></div>
      <div style="grid-column:6/13">
        <div style="display:flex;justify-content:center">{diag}</div>
        <div class="t3 mt3">Três composições editoriais</div>
        <div style="display:flex;gap:4mm" class="mt2">
          <div style="width:47mm">{th1}<p class="cap mt1">Abertura: título em 6 colunas, bloco de cor na base.</p></div>
          <div style="width:47mm">{th2}<p class="cap mt1">Técnica: texto em 4 colunas, demonstração em 8.</p></div>
          <div style="width:47mm">{th3}<p class="cap mt1">Comparação: 4 módulos de 3 colunas.</p></div></div></div></div>'''
    return page(33, 5, b)


def p33():
    shell = '''<div style="position:relative;width:70mm;height:44mm">
      <div style="position:absolute;inset:0;background:rgba(35,17,7,.035);border:.25mm solid rgba(35,17,7,.10);border-radius:8mm"></div>
      <div style="position:absolute;inset:2mm;background:#fff;border:.25mm solid rgba(35,17,7,.10);border-radius:6mm;box-shadow:inset 0 .3mm 0 rgba(255,255,255,1),0 5mm 9mm -7mm rgba(35,17,7,.45)"></div>
      <div class="ann" style="left:72mm;top:0">Casca · raio 2 rem</div><div class="ann" style="left:72mm;top:6mm">Respiro · 0,5 rem</div>
      <div class="ann" style="left:72mm;top:12mm">Núcleo · calc(2 rem − 0,5 rem)</div><div class="ann" style="left:72mm;top:18mm">Fio · 1 px a 10%</div></div>'''
    btn = f'''<div style="display:flex;gap:4mm;align-items:center">
      <span style="display:inline-flex;align-items:center;gap:3mm;background:#F46C00;color:#0C0500;font-size:10pt;font-weight:600;padding:1.6mm 1.8mm 1.6mm 5mm;border-radius:99mm;box-shadow:0 2.6mm 7mm -3mm rgba(244,108,0,.75)">Conheça a plataforma<span style="width:7mm;height:7mm;border-radius:99mm;background:rgba(12,5,0,.12);display:flex;align-items:center;justify-content:center">{icon("seta", 3.6, "#0C0500", 2)}</span></span>
      <span style="display:inline-flex;align-items:center;gap:3mm;border:.25mm solid rgba(35,17,7,.18);font-size:10pt;font-weight:600;padding:1.6mm 1.8mm 1.6mm 5mm;border-radius:99mm">Fale com a UY3<span style="width:7mm;height:7mm;border-radius:99mm;background:rgba(35,17,7,.06);display:flex;align-items:center;justify-content:center">{icon("seta", 3.6, "#231107", 2)}</span></span></div>'''
    names = ["seta", "camadas", "fluxo", "documento", "escudo", "relogio", "api", "check"]
    icons = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:1.4mm"><div style="width:100%;height:13mm;border-radius:3mm;background:#fff;border:.25mm solid var(--fio);display:flex;align-items:center;justify-content:center">{icon(n, 6.4, "#231107")}</div><span class="cap">{n}</span></div>' for n in names)
    heavy = '<svg viewBox="0 0 24 24" style="width:7mm;height:7mm"><path d="M12 2 4 5v7c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V5z" fill="#231107"/></svg>'
    steps = ["Simulação", "Proposta", "Compliance", "Crédito", "Liquidação", "Cessão", "Cobrança"]
    esteira = f'''<div style="position:relative;background:#F46C00;border-radius:4mm;padding:6mm 5mm;display:flex;justify-content:space-between;align-items:center">
      <div style="position:absolute;left:5mm;right:5mm;top:50%;border-top:.5mm dashed rgba(12,5,0,.45)"></div>
      {"".join(f'<div style="position:relative;background:#F6853A;border-radius:2.4mm;padding:1.6mm 2.4mm;font-size:7pt;font-weight:650;color:#0C0500;text-align:center;white-space:nowrap">{s}<br><span style="font-weight:400">+</span></div>' for s in steps)}</div>'''
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Elementos gráficos</div><div class="t1" style="font-size:24pt">Peças usinadas, traço fino</div></div>
      <p class="cap" style="max-width:110mm">Elementos documentados no DESIGN.md. A UY3 não tem grafismo de marca separado do logotipo, e este manual não cria um. Os ícones abaixo são exemplos desenhados no padrão especificado.</p></div>
    <div class="g12" style="height:auto;margin-top:6mm">
      <div style="grid-column:1/7">
        <div class="t3">Casca dupla</div><div class="mt2">{shell}</div>
        <div class="t3 mt4">Botões · sempre pill, ícone aninhado</div><div class="mt2">{btn}</div>
        <p class="cap mt1">Respiro assimétrico (mais curto à direita), círculo do ícone de 2 rem. Texto Carbono sobre Brasa.</p>
        <div class="t3 mt3">A esteira · componente-assinatura</div><div class="mt2">{esteira}</div>
        <p class="cap mt1">Linha tracejada atrás das etapas opacas, com pulso de luz no site. Etapas exibidas como no material de referência; não usar como diagrama de prazos.</p></div>
      <div style="grid-column:7/13">
        <div class="t3">Iconografia</div>
        <div style="display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:1.6mm" class="mt2">{icons}</div>
        <div class="mt2">{spec_rows([("Grade", "viewBox 24 × 24"), ("Traço", "1,5 a 1,8, terminais e junções arredondados"), ("Preenchimento", "nenhum"), ("Cor", "Tinta no claro · Tinta Clara no escuro · Brasa Profunda quando ativo"), ("Fundo", "círculo em Brasa Lavada, quando houver")])}</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm" class="mt3">
          <div class="card" style="padding:4mm;display:flex;gap:4mm;align-items:center">{icon("escudo", 7, "#231107")}<div>{badge(True)}<p class="cap mt1">Traço fino, aberto</p></div></div>
          <div class="card" style="padding:4mm;display:flex;gap:4mm;align-items:center">{heavy}<div>{badge(False)}<p class="cap mt1">Preenchido ou de traço grosso</p></div></div></div>
        <p class="note mt3">Evitar: cadeados gigantes, cofres, moedas, setas de crescimento, gráficos de bolsa, gradiente roxo-azul, blobs orgânicos e ilustração isométrica.</p></div></div>'''
    return page(34, 5, b)


def p34():
    do = ["Tecnologia aplicada, interfaces, fluxos e operação real", "Luz natural ou de estúdio controlada, em tons quentes", "Pessoas em contexto profissional verossímil, com diversidade e sem pose",
          "Enquadramento com espaço negativo para título e logotipo", "Imagem deliberada e específica para a seção onde vive"]
    dont = ["Dinheiro como imagem: moedas, cédulas, cofres, símbolos de moeda", "Aperto de mão, gente sorrindo em sala de reunião, torres espelhadas",
            "Imagem genérica gerada por IA como preenchimento de fundo", "Telas de ficção científica e dashboards flutuando em ângulo"]
    frames = "".join(f'<div class="tile" style="height:30mm;background:{PHOTO[k]};display:block"><span style="position:absolute;left:2mm;bottom:2mm;font-size:5.6pt;color:rgba(255,255,255,.8);font-weight:600;background:rgba(12,5,0,.45);padding:.5mm 1.4mm;border-radius:99mm">{t}</span></div>' for k, t in [("limpa", "Operação · luz baixa"), ("escura", "Detalhe de equipamento"), ("clara", "Ambiente de trabalho")])
    bars = [("Etapa A", 42), ("Etapa B", 64), ("Etapa C", 88), ("Etapa D", 57), ("Etapa E", 35)]
    chart = "".join(f'''<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;gap:1mm">
        <span class="tn" style="font-size:7.4pt;font-weight:{700 if v == 88 else 500};color:{'#9D430B' if v == 88 else '#6B5548'}">{v}</span>
        <div style="width:11mm;height:{v*0.5}mm;background:{'#F46C00' if v == 88 else 'rgba(107,85,72,.35)'};border-radius:1mm 1mm 0 0"></div>
        <span class="cap">{n}</span></div>''' for n, v in bars)
    b = f'''<div class="g12">
      <div style="grid-column:1/7">
        <div class="eb">Fotografia</div><div class="t1" style="font-size:24pt">Imagem com função, não preenchimento</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3mm" class="mt3">{frames}</div>
        <p class="cap mt1">Molduras tonais conceituais. Não há banco de imagens aprovado nesta edição.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm" class="mt3">
          <div>{badge(True, "Buscar")}<ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.3mm 0">{x}</li>' for x in do)}</ul></div>
          <div>{badge(False, "Evitar")}<ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.3mm 0">{x}</li>' for x in dont)}</ul></div></div></div>
      <div style="grid-column:7/13">
        <div class="eb">Visualização de dados</div><div class="t2" style="font-size:17pt">Exatidão e rótulo antes de estética</div>
        <div class="card mt3" style="padding:5mm">
          <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="t3">Volume por etapa (índice)</span>{badge(None, "Dados ilustrativos")}</div>
          <div style="height:58mm;display:flex;justify-content:space-around;align-items:flex-end;border-bottom:.3mm solid #231107;margin-top:4mm;padding:0 2mm">{chart}</div>
          <p class="cap mt2">Fonte: exemplo fictício para demonstrar o padrão. Nota de rodapé em 8 pt.</p></div>
        <div class="mt3">{spec_rows([("Destaque", "Brasa em uma única série ou valor, o que está em foco"), ("Demais séries", "Tinta Suave a 35%; sem paleta arco-íris"), ("Rótulos", "valor direto na marca, numerais tabulares, sem legenda distante"), ("Eixos e grades", "fio de cabelo; sem 3D, sombras ou gradientes"), ("Fonte e data", "obrigatórias em todo gráfico publicado")])}</div></div></div>'''
    return page(35, 5, b)


# ---------------- Capítulo 6 ----------------

def report_cover(w):
    s = w / 210
    return f'''<div style="width:{w}mm;height:{297*s}mm;background:#0C0500;border-radius:1mm;position:relative;overflow:hidden;box-shadow:0 4mm 10mm -6mm rgba(0,0,0,.6)">
      <div style="position:absolute;left:{16*s}mm;top:{16*s}mm">{logo(C["brasa"], w=40*s)}</div>
      <div style="position:absolute;left:{16*s}mm;bottom:{40*s}mm;right:{16*s}mm;font-family:InterD;font-weight:620;color:#F6ECE6;font-size:{26*s*2.83:.1f}pt;line-height:1.03;letter-spacing:-.04em">Relatório<br>institucional</div>
      <div style="position:absolute;left:{16*s}mm;bottom:{16*s}mm;right:{16*s}mm;border-top:.25mm solid rgba(255,255,255,.12);padding-top:{4*s}mm;font-size:{8*s*2.83:.1f}pt;color:#B09A8D;display:flex;justify-content:space-between"><span>Título do documento</span><span>Ano</span></div></div>'''


def bcard(front=True, scale=1.0):
    w, h = 90 * scale, 50 * scale
    if front:
        inner = f'<div style="position:absolute;left:{6*scale}mm;top:{6*scale}mm">{logo(C["brasa"], w=22*scale)}</div><div style="position:absolute;left:{6*scale}mm;bottom:{6*scale}mm;font-size:{6*scale:.2f}pt;color:#B09A8D">uy3.com.br</div>'
        bg = "#0C0500"
    else:
        inner = f'''<div style="position:absolute;left:{6*scale}mm;top:{6*scale}mm;{FEAT}"><div style="font-size:{9*scale:.2f}pt;font-weight:620;letter-spacing:-.02em;color:#231107">Nome Sobrenome</div><div style="font-size:{6.4*scale:.2f}pt;color:#6B5548;margin-top:{.8*scale}mm">Cargo</div></div>
        <div style="position:absolute;left:{6*scale}mm;bottom:{6*scale}mm;font-size:{6.4*scale:.2f}pt;line-height:1.5;color:#231107">E-mail institucional<br>Telefone</div>
        <div style="position:absolute;right:{6*scale}mm;bottom:{6*scale}mm">{logo(C["brasa"], w=11.3*scale)}</div>'''
        bg = "#FFFFFF"
    return f'<div style="width:{w}mm;height:{h}mm;background:{bg};border-radius:{1*scale}mm;position:relative;overflow:hidden;box-shadow:0 0 0 .25mm rgba(128,110,100,.35),0 3mm 7mm -5mm rgba(35,17,7,.5)">{inner}</div>'


def linkedin(title, eyebrow="INFRAESTRUTURA DE CRÉDITO"):
    return f'''<div style="width:1200px;height:627px;background:#0C0500;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:72px;top:64px">{logo(C["brasa"], w=36)}</div>
      <div style="position:absolute;left:72px;top:210px;font-size:12px;font-weight:700;letter-spacing:.22em;color:#FF8C45">{eyebrow}</div>
      <div style="position:absolute;left:72px;top:244px;width:760px;font-family:InterD;font-size:64px;font-weight:620;letter-spacing:-.042em;line-height:1.03;color:#F6ECE6">{title}</div>
      <div style="position:absolute;right:72px;bottom:64px;width:150px;height:150px;border-radius:999px;border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;justify-content:center;color:#F46C00">{icon("fluxo", 16, "#F46C00", 1.2)}</div></div>'''


def p35():
    li, _ = frame(0, 0, 112, 1200, 627, linkedin("Tecnologia nascida no crédito."), radius=1.6, extra_style="position:relative;box-shadow:0 0 0 .25mm rgba(255,255,255,.12)")
    ex = f'''<div style="position:absolute;left:0;right:0;top:12mm;display:flex;gap:9mm;align-items:flex-end">
      {report_cover(64)}<div style="display:flex;flex-direction:column;gap:6mm">{bcard(True, .9)}{bcard(False, .9)}</div><div>{li}</div></div>'''
    return opener(36, 6, "Aplicações", "Poucas peças, bem resolvidas. Os modelos ensinam o padrão; não são versões novas da marca.", ex)


def p36():
    lh_s = 0.32
    letter = f'''<div style="width:{210*lh_s}mm;height:{297*lh_s}mm;background:#fff;position:relative;box-shadow:0 0 0 .25mm rgba(35,17,7,.12),0 3mm 8mm -6mm rgba(35,17,7,.5);{FEAT}">
      <div style="position:absolute;left:{20*lh_s}mm;top:{18*lh_s}mm">{logo(C["brasa"], h=8*lh_s)}</div>
      {"".join(f'<div style="position:absolute;left:{20*lh_s}mm;top:{(60 + i*6)*lh_s}mm;width:{(170 - (i%4)*18)*lh_s}mm;height:{1.6*lh_s}mm;background:rgba(35,17,7,.18)"></div>' for i in range(14))}
      <div style="position:absolute;left:{20*lh_s}mm;right:{20*lh_s}mm;bottom:{12*lh_s}mm;border-top:.2mm solid rgba(35,17,7,.12);padding-top:{3*lh_s}mm;font-size:3.4pt;color:#6B5548;display:flex;justify-content:space-between"><span>UY3 Sociedade de Crédito Direto S.A. · CNPJ 39.587.424/0001-30</span><span>Endereço institucional · uy3.com.br</span></div></div>'''
    sig = f'''<div class="card" style="padding:4mm 5mm;width:100%;{FEAT}">
      <div style="display:flex;gap:4mm;align-items:center">
        <div style="border-right:.25mm solid var(--fio);padding-right:4mm">{logo(C["brasa"], w=16)}</div>
        <div><div style="font-size:9pt;font-weight:620">Nome Sobrenome</div><div style="font-size:7.4pt;color:#6B5548">Cargo · Área</div>
          <div style="font-size:7.4pt;color:#231107;margin-top:1mm">E-mail institucional · Telefone</div><div style="font-size:7.4pt;color:#9D430B;font-weight:600">uy3.com.br</div></div></div></div>'''
    ps = 0.27
    prop = f'''<div style="width:{210*ps}mm;height:{297*ps}mm;background:#F9F1ED;position:relative;box-shadow:0 0 0 .25mm rgba(35,17,7,.12),0 3mm 8mm -6mm rgba(35,17,7,.5);overflow:hidden">
      <div style="position:absolute;left:{20*ps}mm;top:{18*ps}mm">{logo(C["brasa"], h=8*ps)}</div>
      <div style="position:absolute;left:{20*ps}mm;top:{120*ps}mm;font-size:5pt;font-weight:700;letter-spacing:.2em;color:#9D430B">PROPOSTA</div>
      <div style="position:absolute;left:{20*ps}mm;top:{128*ps}mm;width:{150*ps}mm;font-family:InterD;font-size:13pt;font-weight:620;letter-spacing:-.035em;line-height:1.03">Título da proposta para o parceiro</div>
      <div style="position:absolute;left:0;right:0;bottom:0;height:{70*ps}mm;background:#F46C00"></div>
      <div style="position:absolute;left:{20*ps}mm;bottom:{12*ps}mm;font-size:4.6pt;color:#0C0500;font-weight:600">Nome do parceiro · Mês e ano</div></div>'''
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Papelaria e documentos</div><div class="t1" style="font-size:24pt">Institucional, sem ornamento</div></div>
      <p class="cap" style="max-width:112mm">Razão social e CNPJ conforme o site institucional. Nome, cargo, e-mail, telefone e endereço são campos demonstrativos e não podem ser publicados como dados reais. Cartão de visita em escala real (90 × 50 mm).</p></div>
    <div style="display:grid;grid-template-columns:92mm 70mm 1fr;gap:8mm;margin-top:7mm">
      <div><div class="t3">Cartão de visita · frente e verso</div><div style="display:flex;flex-direction:column;gap:5mm" class="mt2">{bcard(True)}{bcard(False)}</div>
        <p class="cap mt2">Frente em Carbono Profundo com Brasa; verso em Papel. Logotipo do verso a 11,3 mm de largura (mínimo).</p></div>
      <div><div class="t3">Papel timbrado A4</div><div class="mt2">{letter}</div><p class="cap mt2">Logotipo a 8 mm de altura, alinhado à margem de 20 mm. Rodapé institucional em 7 pt.</p></div>
      <div><div class="t3">Capa de proposta · A4</div><div class="mt2">{prop}</div>
        <div class="t3 mt3">Assinatura de e-mail</div><div class="mt2">{sig}</div>
        <p class="cap mt1">HTML com Inter e fallback Segoe UI/system-ui. Logotipo em PNG a 2× com 32 px de altura mínima.</p></div></div>'''
    return page(37, 6, b)


def p37():
    li, h1 = frame(0, 0, 128, 1200, 627, linkedin("Da simulação à cobrança, em um único lugar."), radius=2)
    post = f'''<div style="width:1080px;height:1350px;background:#F9F1ED;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:84px;top:84px">{logo(C["brasa"], w=34)}</div>
      <div style="position:absolute;left:84px;top:300px;font-size:13px;font-weight:700;letter-spacing:.22em;color:#9D430B">COMO FUNCIONA</div>
      <div style="position:absolute;left:84px;top:340px;width:880px;font-family:InterD;font-size:84px;font-weight:620;letter-spacing:-.045em;line-height:1.03;color:#231107">Uma jornada. Sete etapas. Um único ambiente.</div>
      <div style="position:absolute;left:84px;right:84px;bottom:84px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
        {"".join(f'<div style="background:#fff;border:1px solid rgba(35,17,7,.10);border-radius:24px;padding:24px;height:180px"><div style="font-size:15px;font-weight:700;color:#9D430B">0{i+1}</div><div style="font-size:24px;font-weight:600;letter-spacing:-.015em;margin-top:60px">{t}</div></div>' for i, t in enumerate(["Simulação","Proposta","Compliance","Crédito"]))}</div></div>'''
    pf, h2 = frame(0, 0, 62, 1080, 1350, post, radius=2, extra_style="box-shadow:0 0 0 .25mm rgba(35,17,7,.12)")
    edit = f'''<div style="width:1080px;height:1080px;background:#F46C00;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:84px;top:84px;font-size:13px;font-weight:700;letter-spacing:.22em;color:#0C0500">ARTIGO</div>
      <div style="position:absolute;left:84px;top:150px;width:900px;font-family:InterD;font-size:78px;font-weight:620;letter-spacing:-.045em;line-height:1.03;color:#0C0500">O que acontece com o crédito depois da contratação.</div>
      <div style="position:absolute;left:84px;bottom:84px;font-size:22px;color:rgba(12,5,0,.78)">Leitura de 5 minutos · uy3.com.br</div>
      <div style="position:absolute;right:84px;bottom:84px">{logo(C["carbono-profundo"], w=34)}</div></div>'''
    ef, h3 = frame(0, 0, 62, 1080, 1080, edit, radius=2)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Comunicação digital</div><div class="t1" style="font-size:24pt">Informação antes de promoção</div></div>
      <p class="cap" style="max-width:110mm">Frases do banco de frases do site. Sem promessas de aprovação, taxas ou chamadas de urgência. Peças de produto de crédito ao consumidor exigem revisão de compliance.</p></div>
    <div style="display:grid;grid-template-columns:128mm 62mm 62mm;gap:6mm;margin-top:8mm;align-items:start">
      <div><div style="position:relative;height:{h1:.1f}mm">{li}</div><div class="t3 mt2">Card LinkedIn · 1200 × 627 px</div><p class="cap mt1">Carbono com título em Display. Logotipo no topo esquerdo, 1X de respiro mínimo, ícone de traço fino como único elemento gráfico.</p></div>
      <div><div style="position:relative;height:{h2:.1f}mm">{pf}</div><div class="t3 mt2">Post informativo · 4:5</div><p class="cap mt1">Creme, cards de casca simples e numeração em Brasa Tinta.</p></div>
      <div><div style="position:relative;height:{h3:.1f}mm">{ef}</div><div class="t3 mt2">Peça editorial · 1:1</div><p class="cap mt1">Fundo Brasa como interrupção, texto e logotipo em Carbono.</p></div></div>'''
    return page(38, 6, b)


def site_hero():
    return f'''<div style="width:1440px;height:820px;background:radial-gradient(120% 90% at 70% 0%, #261003 0%, #0C0500 60%);position:relative;font-family:Inter;{FEAT};overflow:hidden">
      <div style="position:absolute;left:130px;right:130px;top:22px;height:64px;border-radius:999px;background:rgba(12,5,0,.34);border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;justify-content:space-between;padding:0 9px 0 26px">
        {logo(C["brasa"], w=17)}
        <div style="display:flex;gap:30px;font-size:15px;color:#B09A8D"><span style="color:#fff;background:rgba(255,255,255,.07);padding:7px 14px;border-radius:999px">Plataforma</span><span style="padding:7px 0">Soluções</span><span style="padding:7px 0">Tecnologia</span><span style="padding:7px 0">Sobre</span></div>
        <span style="display:inline-flex;align-items:center;gap:12px;background:#F46C00;color:#0C0500;font-size:15px;font-weight:600;padding:8px 8px 8px 20px;border-radius:999px">Fale com a UY3<span style="width:30px;height:30px;border-radius:999px;background:rgba(12,5,0,.12);display:flex;align-items:center;justify-content:center">{icon("seta", 3.8, "#0C0500", 2)}</span></span></div>
      <div style="position:absolute;left:130px;top:250px;font-size:10px;font-weight:700;letter-spacing:.22em;color:#FF8C45">INFRAESTRUTURA DE CRÉDITO</div>
      <div style="position:absolute;left:130px;top:285px;width:1180px;font-family:InterD;font-size:80px;font-weight:620;letter-spacing:-.045em;line-height:1.03;color:#F6ECE6">A infraestrutura que move<br>a próxima onda de crédito.</div>
      <div style="position:absolute;left:130px;top:480px;width:620px;font-size:20.8px;line-height:1.6;color:#B09A8D">Invisível para o cliente final, decisiva para o seu negócio.</div>
      <div style="position:absolute;left:130px;top:570px;display:flex;gap:12px">
        <span style="display:inline-flex;align-items:center;gap:14px;background:#F46C00;color:#0C0500;font-size:16.8px;font-weight:600;padding:9px 10px 9px 23px;border-radius:999px;box-shadow:0 1px 0 rgba(255,255,255,.22) inset,0 10px 30px -12px rgba(244,108,0,.75)">Conheça a plataforma<span style="width:32px;height:32px;border-radius:999px;background:rgba(12,5,0,.12);display:flex;align-items:center;justify-content:center">{icon("seta", 4.2, "#0C0500", 2)}</span></span>
        <span style="display:inline-flex;align-items:center;gap:14px;border:1px solid rgba(255,255,255,.28);color:#fff;font-size:16.8px;font-weight:600;padding:9px 10px 9px 23px;border-radius:999px">Ver a esteira<span style="width:32px;height:32px;border-radius:999px;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center">{icon("seta", 4.2, "#ffffff", 2)}</span></span></div></div>'''


def mobile_form():
    field = lambda lbl, val, state="": f'''<div style="margin-top:18px"><div style="font-size:10px;font-weight:700;letter-spacing:.22em;color:#6B5548">{lbl}</div>
      <div style="margin-top:8px;background:#fff;border:1px solid {'#F46C00' if state else 'rgba(35,17,7,.10)'};{'box-shadow:0 0 0 3px rgba(244,108,0,.14);' if state else ''}border-radius:16px;padding:13.6px 16px;font-size:16px;color:{'#231107' if val else '#6B5548'}">{val or 'Digite aqui'}</div>
      {f'<div style="display:flex;gap:6px;align-items:center;margin-top:8px;font-size:13px;color:#9D430B;font-weight:600">{icon("alerta", 3.6, "#9D430B")} Informe um e-mail corporativo válido.</div>' if state == "err" else ''}</div>'''
    return f'''<div style="width:390px;height:844px;background:#F4DFD2;font-family:Inter;{FEAT};padding:60px 24px;position:relative">
      <div style="display:flex;justify-content:space-between;align-items:center">{logo(C["brasa"], w=12)}<div style="width:40px;height:40px;border-radius:999px;border:1px solid rgba(35,17,7,.10);display:flex;flex-direction:column;gap:5px;align-items:center;justify-content:center"><span style="width:16px;height:1.5px;background:#231107"></span><span style="width:16px;height:1.5px;background:#231107"></span></div></div>
      <div style="font-size:10px;font-weight:700;letter-spacing:.22em;color:#9D430B;margin-top:46px">CONTATO</div>
      <div style="font-family:InterD;font-size:34px;font-weight:620;letter-spacing:-.042em;line-height:1.03;margin-top:12px;color:#231107">Fale com a UY3</div>
      {field("NOME", "Nome Sobrenome")}{field("E-MAIL CORPORATIVO", "nome@empresa", "err")}{field("EMPRESA", "")}{field("PERFIL", "Selecione")}
      <div style="margin-top:26px;display:flex;justify-content:center;align-items:center;gap:12px;background:#F46C00;color:#0C0500;font-size:16.8px;font-weight:600;padding:12px;border-radius:999px">Enviar</div></div>'''


def p38():
    hero, hh = frame(0, 0, 178, 1440, 820, site_hero(), radius=2.5, extra_style="box-shadow:0 0 0 .25mm rgba(35,17,7,.15)")
    mob, mh = frame(0, 0, 50, 390, 844, mobile_form(), radius=5, extra_style="box-shadow:0 0 0 .6mm #231107")
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Site e interfaces</div><div class="t1" style="font-size:24pt">Os tokens do DESIGN.md, aplicados</div></div>
      <p class="cap" style="max-width:112mm">Demonstrações conceituais com tokens reais. Não representam funcionalidades existentes nem condições comerciais. Formulário sem dados pessoais reais.</p></div>
    <div style="display:grid;grid-template-columns:178mm 1fr;gap:8mm;margin-top:6mm">
      <div><div style="position:relative;height:{hh:.1f}mm">{hero}</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4mm" class="mt2">
          <p class="cap"><b style="color:var(--tinta)">Navegação</b><br>Pílula flutuante, Carbono a 34% com desfoque. Logotipo à esquerda com no mínimo 24 px.</p>
          <p class="cap"><b style="color:var(--tinta)">Hero</b><br>Fundo Carbono, nunca Brasa (restrição do cliente). Display 620 a −0,045em.</p>
          <p class="cap"><b style="color:var(--tinta)">Ação</b><br>Primário em Brasa com texto Carbono e sombra de calor. Ghost com borda a 28% de branco.</p></div></div>
      <div style="display:flex;gap:5mm;align-items:flex-start"><div style="position:relative;flex:none;width:50mm;height:{mh:.1f}mm">{mob}</div>
        <div style="display:flex;flex-direction:column;gap:3mm">
          <p class="cap"><b style="color:var(--tinta)">Rótulo</b><br>Label acima do campo.</p>
          <p class="cap"><b style="color:var(--tinta)">Foco</b><br>Borda Brasa e anel de 3 px a 14%.</p>
          <p class="cap"><b style="color:var(--tinta)">Erro</b><br>Ícone e texto, nunca só cor. Token de erro a definir.</p>
          <p class="cap"><b style="color:var(--tinta)">Toque</b><br>Alvos com 44 px ou mais.</p></div></div></div>'''
    return page(39, 6, b)


def slide_cover():
    return f'''<div style="width:1920px;height:1080px;background:#0C0500;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:120px;top:110px">{logo(C["brasa"], w=40)}</div>
      <div style="position:absolute;left:120px;bottom:250px;width:1300px;font-family:InterD;font-size:120px;font-weight:620;letter-spacing:-.045em;line-height:1.03;color:#F6ECE6">Título da<br>apresentação</div>
      <div style="position:absolute;left:120px;right:120px;bottom:110px;border-top:1px solid rgba(255,255,255,.10);padding-top:30px;display:flex;justify-content:space-between;font-size:26px;color:#B09A8D"><span>Subtítulo ou evento</span><span>Mês e ano</span></div></div>'''


def slide_content():
    items = [("Originação", "Corbans, fintechs e empresas que oferecem crédito."), ("Infraestrutura", "Esteira de ponta a ponta, da simulação à cobrança."), ("Capital", "Conexão com FIDCs e mercado de capitais.")]
    return f'''<div style="width:1920px;height:1080px;background:#F9F1ED;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:120px;top:90px;right:120px;display:flex;justify-content:space-between;font-size:22px;color:#6B5548;border-bottom:1px solid rgba(35,17,7,.10);padding-bottom:22px"><span>Seção</span>{logo(C["brasa"], w=14)}</div>
      <div style="position:absolute;left:120px;top:220px;font-size:18px;font-weight:700;letter-spacing:.22em;color:#9D430B">COMO A UY3 SE ORGANIZA</div>
      <div style="position:absolute;left:120px;top:270px;width:1100px;font-family:InterD;font-size:72px;font-weight:620;letter-spacing:-.042em;line-height:1.03;color:#231107">Três camadas, uma única operação.</div>
      <div style="position:absolute;left:120px;right:120px;bottom:120px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">
        {"".join(f'<div style="background:#fff;border:1px solid rgba(35,17,7,.10);border-radius:36px;padding:44px;height:320px"><div style="font-size:24px;font-weight:700;color:#9D430B">0{i+1}</div><div style="font-size:40px;font-weight:600;letter-spacing:-.025em;margin-top:90px;color:#231107">{t}</div><div style="font-size:26px;line-height:1.5;color:#6B5548;margin-top:14px">{d}</div></div>' for i, (t, d) in enumerate(items))}</div>
      <div style="position:absolute;right:120px;bottom:50px;font-size:20px;color:#6B5548">02</div></div>'''


def cobrand():
    return f'''<div style="width:1920px;height:1080px;background:#FFFFFF;position:relative;font-family:Inter;{FEAT}">
      <div style="position:absolute;left:120px;top:110px;font-size:18px;font-weight:700;letter-spacing:.22em;color:#9D430B">EVENTO</div>
      <div style="position:absolute;left:120px;top:160px;width:1400px;font-family:InterD;font-size:104px;font-weight:620;letter-spacing:-.045em;line-height:1.03;color:#231107">Nome do encontro<br>com o parceiro</div>
      <div style="position:absolute;left:120px;right:120px;bottom:110px;border-top:1px solid rgba(35,17,7,.10);padding-top:60px;display:flex;align-items:center">
        {logo(C["brasa"], h=17)}<div style="width:110px"></div><div style="width:2px;height:110px;background:rgba(35,17,7,.25)"></div><div style="width:110px"></div>
        <div style="width:330px;height:64px;border:3px dashed rgba(35,17,7,.35);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:600;color:#6B5548">Marca parceira</div></div></div>'''


def p39():
    a, ha = frame(0, 0, 124, 1920, 1080, slide_cover(), radius=2)
    bb, hb = frame(0, 0, 124, 1920, 1080, slide_content(), radius=2, extra_style="box-shadow:0 0 0 .25mm rgba(35,17,7,.12)")
    c, hc = frame(0, 0, 124, 1920, 1080, cobrand(), radius=2, extra_style="box-shadow:0 0 0 .25mm rgba(35,17,7,.12)")
    b = f'''<div style="display:grid;grid-template-columns:124mm 1fr;gap:8mm;height:100%">
      <div style="display:flex;flex-direction:column;gap:3mm">
        <div class="eb" style="margin:0">Apresentações e parcerias</div>
        <div style="position:relative;height:{ha:.1f}mm">{a}</div><p class="cap">Capa 16:9 · Carbono, título Display, logotipo no topo esquerdo.</p>
        <div style="position:relative;height:{hb:.1f}mm">{bb}</div><p class="cap">Conteúdo · Creme, cabeçalho com fio, cards de casca simples, numeração de página.</p></div>
      <div style="display:flex;flex-direction:column;gap:3mm">
        <div class="t1" style="font-size:24pt">Mesma marca em 16:9 e em co-branding</div>
        <div style="position:relative;height:{hc:.1f}mm;margin-top:3mm">{c}</div><p class="cap">Peça com marca parceira fictícia. O bloco é demonstrativo e não representa parceria real.</p>
        <div class="mt2">{spec_rows([("Formato", "16:9 · 1920 × 1080 px"), ("Margem", "120 px (6,25%) em todos os lados"), ("Títulos", "Display 620 a 104–120 px na capa; Headline 72 px no conteúdo"), ("Texto mínimo", "22 px em projeção; nada abaixo de 18 px"), ("Logotipo", "40 px de altura na capa; 14 mm de largura equivalente no cabeçalho"), ("Co-branding", "regras da página 17: equivalência óptica, 2X e separador")])}</div></div></div>'''
    return page(40, 6, b)


def p40():
    faca = ["Usar sempre os arquivos oficiais do logotipo", "Respeitar 1X de área de proteção e os tamanhos mínimos", "Texto Carbono sobre Brasa; Brasa Tinta para acento sobre claro",
            "Inter em tudo; numerais tabulares em tabelas", "Rotular dados ilustrativos e citar fonte e data", "Submeter peças regulatórias ao jurídico e compliance"]
    evite = ["Redesenhar, recolorir fora das três versões ou criar símbolo", "Laranja decorativo ou fundo Brasa no hero", "Preto neutro, cinza sem matiz e bordas opacas",
             "Segunda família tipográfica ou fonte de display", "Imagens de dinheiro, cofres, setas de crescimento", "Chamar a UY3 de banco ou prometer aprovação"]
    files = [("UY3_logo_principal_brasa.svg", "Digital · #F46C00"), ("UY3_logo_negativo_branco.svg", "Digital · #FFFFFF"), ("UY3_logo_mono_carbono.svg", "Digital · #0C0500"),
             ("UY3_logo_principal_brasa_PANTONE-1505C.pdf", "Impressão · cor especial"), ("UY3_logo_principal_brasa_CMYK.pdf", "Impressão · 0/71/100/0"),
             ("UY3_logo_*_2000px.png", "Office, e-mail · transparente")]
    fl = "".join(f'<div style="display:flex;justify-content:space-between;gap:3mm;padding:1.5mm 0;border-top:.25mm solid var(--fio)"><span class="mono" style="font-size:7.2pt">{a}</span><span class="cap">{b_}</span></div>' for a, b_ in files)
    b = f'''<div class="g12">
      <div style="grid-column:1/5">
        <div class="eb">Normas finais</div><div class="t1" style="font-size:24pt">Checklist de aplicação</div>
        <div style="display:grid;grid-template-columns:1fr;gap:4mm" class="mt3">
          <div>{badge(True, "Faça")}<ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.2mm 0">{x}</li>' for x in faca)}</ul></div>
          <div>{badge(False, "Evite")}<ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.2mm 0">{x}</li>' for x in evite)}</ul></div></div></div>
      <div style="grid-column:5/9">
        <div class="t3">Nomenclatura dos ativos</div><div class="mt2">{fl}</div>
        <div class="t3 mt3">Exportação</div>
        <div class="mt1">{spec_rows([("Impressão", "PDF/X-4, CMYK, perfil indicado pela gráfica; prova de cor obrigatória"), ("Digital", "SVG para web; PNG transparente; sRGB"), ("Documentos", "PDF com fontes incorporadas e texto selecionável")])}</div></div>
      <div style="grid-column:9/13;display:flex;flex-direction:column;justify-content:space-between">
        <div><div class="t3">Governança</div>
          <p class="mt1" style="font-size:8.8pt">Este manual é a referência da marca a partir da versão 1.0. Novas variações do logotipo, cores funcionais, banco de imagens e qualquer regra marcada como recomendação dependem de aprovação da gestão da marca UY3 antes do uso.</p>
          <p class="cap mt2">Dúvidas e solicitações de arquivos: área de Marketing da UY3.</p></div>
        <div class="tile" style="height:64mm;background:var(--cp);flex-direction:column;justify-content:center;gap:5mm">{logo(C["brasa"], w=58)}<span class="cap" style="color:#B09A8D">{EDICAO}</span></div></div></div>'''
    return page(41, 6, b)


PAGES = [p31, p32, p33, p34, p35, p36, p37, p38, p39, p40]
