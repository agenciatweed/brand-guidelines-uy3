# -*- coding: utf-8 -*-
from base import *
from ch12 import opener, spec_rows


def p25():
    ex = '''<div style="position:absolute;left:0;top:14mm;display:flex;align-items:flex-end;gap:12mm">
      <div style="font-family:InterD;font-size:190pt;font-weight:620;letter-spacing:-.05em;line-height:.8;color:#F6ECE6">Aa</div>
      <div style="padding-bottom:6mm;color:#B09A8D;font-size:11pt;line-height:1.6;font-feature-settings:'cv05' 1,'cv11' 1,'ss03' 1">
        <div style="color:#F6ECE6;font-weight:620;font-size:20pt;letter-spacing:-.03em">Inter</div>
        ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>ÁÂÃÀÇÉÊÍÓÔÕÚ áâãàçéêíóôõú<br>0123456789 R$ % , . ; : “ ” ( ) /</div></div>'''
    return opener(26, 4, "Tipografia", "Uma família só. A personalidade vem do tratamento: tracking negativo nos títulos, peso 620 e alternativas de glifo ativadas.", ex)


def p26():
    rows = [("Inter", "Família institucional única", "Títulos, textos, interface, botões, números, tabelas e notas legais", True),
            ("Segoe UI · system-ui · -apple-system · sans-serif", "Fallback do sistema", "Apenas quando a Inter não puder ser carregada (e-mail HTML, ambientes restritos)", None),
            ("ui-monospace (SF Mono, Cascadia Mono, Consolas)", "Monoespaçada funcional", "Exclusivamente dentro da janela de código da seção de Tecnologia do site", None)]
    tbl = "".join(f'<tr><td style="font-weight:650">{a}</td><td>{b_}</td><td>{c}</td><td>{badge(ok, "Principal" if ok else "Restrita")}</td></tr>' for a, b_, c, ok in rows)
    b = f'''<div class="g12">
      <div style="grid-column:1/6">
        <div class="eb">Famílias e papéis</div><div class="t1" style="font-size:24pt">A Regra da Família Única</div>
        <p class="mt2" style="font-size:9.2pt">Inter em toda a comunicação. Uma segunda família só entra se for monoespaçada e se o alinhamento por caractere for funcional. Não existe fonte de display separada, e criar uma rompe o compromisso de marca (DESIGN.md).</p>
        <div class="card mt3" style="padding:6mm">
          <div style="font-size:36pt;font-weight:620;letter-spacing:-.04em;line-height:1">Inter</div>
          <div style="font-size:15pt;line-height:1.35;margin-top:3mm;color:var(--ts)">Aa Bb Cc Çç Ãã Éé 0123456789</div>
          <p class="cap mt2">Desenho de Rasmus Andersson. Licença SIL Open Font License 1.1, que permite uso comercial e incorporação em PDF. Arquivo usado neste manual: Inter 4.1, variável, com instâncias estáticas para incorporação.</p></div>
        <p class="note mt3">Os títulos deste manual usam o eixo de tamanho óptico da própria Inter (corte de 32). No navegador, esse ajuste é automático com a fonte variável. Não é outra família.</p></div>
      <div style="grid-column:6/13">
        <table class="tb"><thead><tr><th>Família</th><th>Papel</th><th>Onde se aplica</th><th>Status</th></tr></thead><tbody>{tbl}</tbody></table>
        <div class="mt4" style="display:grid;grid-template-columns:1fr 1fr;gap:5mm;height:80mm">
          <div class="card" style="padding:6mm;display:flex;flex-direction:column;justify-content:space-between"><div class="cap">Comunicação</div><div style="font-size:20pt;font-weight:620;letter-spacing:-.035em;line-height:1.08;margin-top:2mm">Plugue e opere. A esteira completa já está pronta.</div><p class="mt2" style="font-size:8.6pt">Corpo em Inter 400, entrelinha 1,6, até 62 caracteres por linha.</p></div>
          <div class="card" style="padding:6mm;background:#150903;border:none;display:flex;flex-direction:column;justify-content:space-between"><div class="cap" style="color:#B09A8D">Janela de código</div>
            <div class="mono" style="color:#F6ECE6;line-height:1.85;margin-top:2mm"><span style="color:#B09A8D">01</span>&nbsp; POST /credito/simulacao<br><span style="color:#B09A8D">02</span>&nbsp; {{ "produto": "exemplo" }}<br><span style="color:#B09A8D">03</span>&nbsp; <span style="color:#FF8C45">200</span> OK<span style="display:inline-block;width:1.2mm;height:3mm;background:#F46C00;vertical-align:middle;margin-left:1mm"></span></div>
            <p class="cap mt1" style="color:#B09A8D">Conteúdo ilustrativo. Não representa endpoint real.</p></div></div>
      </div></div>'''
    return page(27, 4, b)


def p27():
    ws = [(400, "Regular", "Corpo, lede, legendas, tabelas"), (600, "SemiBold", "Title, subtitle, botões, rótulos de card"),
          (620, "620 (variável)", "Display e headline: a assinatura tipográfica do sistema"), (700, "Bold", "Label em caixa alta e ênfases curtas")]
    wrows = "".join(f'<div style="display:grid;grid-template-columns:64mm 1fr;gap:4mm;padding:2.4mm 0;border-top:.25mm solid var(--fio);align-items:baseline"><span style="font-size:20pt;font-weight:{w};letter-spacing:-.025em">Crédito {w}</span><span class="cap"><b style="color:var(--tinta)">{n}</b> · {d}</span></div>' for w, n, d in ws)
    feat = lambda ff, txt: f'<span style="font-feature-settings:{ff};font-size:22pt;font-weight:500;letter-spacing:-.01em">{txt}</span>'
    b = f'''<div class="g12">
      <div style="grid-column:1/7">
        <div class="eb">Pesos e caracteres</div><div class="t1" style="font-size:24pt">Quatro pesos em uso</div>
        <div class="mt3">{wrows}</div>
        <p class="cap mt2">A família oferece de 100 a 900; os demais pesos não fazem parte do sistema. O peso 620 exige a Inter variável. Em ambientes com fontes estáticas (Office, e-mail), use SemiBold 600.</p>
        <div class="t3 mt3">Português, moeda e pontuação</div>
        <div style="font-size:13pt;line-height:1.5;margin-top:2mm">ÁÂÃÀÇÉÊÍÓÔÕÚÜ áâãàçéêíóôõúü<br>0123456789 · R$ 1.234,56 · 12,5% · 12/11/2026<br>“Aspas” ‘simples’ — travessão – meia-risca … · § ª º</div></div>
      <div style="grid-column:7/13">
        <div class="t3">Alternativas de glifo ativas (DESIGN.md)</div>
        <p class="cap mt1">font-feature-settings: 'cv05' 1, 'cv11' 1, 'ss03' 1</p>
        <div class="card mt2" style="padding:4mm 5mm">
          <div style="display:grid;grid-template-columns:22mm 1fr 1fr;gap:3mm;align-items:center"><span class="cap">Recurso</span><span class="cap">Padrão de fábrica</span><span class="cap">UY3</span></div>
          <div style="display:grid;grid-template-columns:22mm 1fr 1fr;gap:3mm;align-items:center;border-top:.25mm solid var(--fio);padding:2mm 0"><span class="cap"><b>cv11</b> a de um andar</span>{feat("normal","análise")}{feat("'cv11' 1","análise")}</div>
          <div style="display:grid;grid-template-columns:22mm 1fr 1fr;gap:3mm;align-items:center;border-top:.25mm solid var(--fio);padding:2mm 0"><span class="cap"><b>cv05</b> l com cauda</span>{feat("normal","Il1 legal")}{feat("'cv05' 1","Il1 legal")}</div>
          <div style="display:grid;grid-template-columns:22mm 1fr 1fr;gap:3mm;align-items:center;border-top:.25mm solid var(--fio);padding:2mm 0"><span class="cap"><b>ss03</b> aspas e vírgulas</span>{feat("normal","“1,5”")}{feat("'ss03' 1","“1,5”")}</div></div>
        <div class="t3 mt3">Numerais tabulares para dados</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm" class="mt2">
          <div class="card" style="padding:4mm"><div class="cap">Proporcionais (padrão)</div><div style="font-size:14pt;text-align:right;line-height:1.5;margin-top:1.5mm;font-feature-settings:'cv05' 1">R$ 1.111,11<br>R$ 8.888,88<br>R$ 10.471,10</div></div>
          <div class="card" style="padding:4mm"><div class="cap">Tabulares · 'tnum' 1</div><div style="font-size:14pt;text-align:right;line-height:1.5;margin-top:1.5mm;font-feature-settings:'tnum' 1,'cv05' 1">R$ 1.111,11<br>R$ 8.888,88<br>R$ 10.471,10</div></div></div>
        <p class="cap mt1">Use numerais tabulares em tabelas, extratos e colunas de valores. Em texto corrido, mantenha os proporcionais.</p></div></div>'''
    return page(28, 4, b)


def p28():
    st = [("Display", "H1 · uma vez por página", "620", "46–56 pt", "41,6–86,4 px", "1,03", "−0,045em", "font-size:30pt;font-weight:620;letter-spacing:-.045em;line-height:1.03"),
          ("Headline", "H2 · abertura de seção", "620", "24–30 pt", "32,8–61,6 px", "1,03", "−0,042em", "font-size:20pt;font-weight:620;letter-spacing:-.042em;line-height:1.03"),
          ("Title", "H3 · card grande, bloco", "600", "14–16 pt", "20,8–28 px", "1,15", "−0,025em", "font-size:14pt;font-weight:600;letter-spacing:-.025em"),
          ("Subtitle", "Card pequeno, etapa, CTA", "600", "10,5–11 pt", "16,8 px", "1,30", "−0,015em", "font-size:10.5pt;font-weight:600;letter-spacing:-.015em"),
          ("Lede", "Abertura sob o headline", "400", "11,5 pt", "16,8–20,8 px", "1,60", "normal", "font-size:11.5pt"),
          ("Body", "Texto corrido", "400", "10 pt", "16–17,2 px", "1,50–1,65", "normal", "font-size:10pt"),
          ("Label", "Eyebrow, rótulo de campo", "700", "7 pt · caixa alta", "10 px", "1,20", "+0,22em", "font-size:7pt;font-weight:700;letter-spacing:.22em;text-transform:uppercase"),
          ("Legenda", "Fonte, nota de imagem", "400", "8 pt", "13–14 px", "1,40", "normal", "font-size:8pt;color:#6B5548"),
          ("Nota legal", "Avisos regulatórios", "400", "8 pt (mín. 7,5)", "13 px", "1,45", "normal", "font-size:8pt;color:#6B5548")]
    rows = "".join(f'''<tr><td style="width:84mm"><div style="{css};white-space:nowrap;overflow:hidden">{"Crédito como infraestrutura" if i < 4 else ("Da simulação à cobrança" if i < 6 else ("Infraestrutura" if i == 6 else "Fonte: base institucional UY3"))}</div></td>
        <td><b>{n}</b><br><span class="cap">{u}</span></td><td class="r">{w}</td><td class="r">{a4}</td><td class="r">{dg}</td><td class="r">{lh}</td><td class="r">{ls}</td></tr>''' for i, (n, u, w, a4, dg, lh, ls, css) in enumerate(st))
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Hierarquia</div><div class="t1" style="font-size:24pt">Contraste de escala e peso, nunca de família</div></div>
      <p class="cap" style="max-width:110mm">Coluna digital: valores do DESIGN.md (1 rem = 16 px, com a faixa mínima–máxima do clamp). Coluna A4: <b>recomendação deste manual</b> para documentos impressos e PDF. Regra do tracking negativo: quanto maior o texto, mais apertado.</p></div>
      <table class="tb mt3"><thead><tr><th>Amostra</th><th>Estilo</th><th class="r">Peso</th><th class="r">A4 / impresso</th><th class="r">Digital</th><th class="r">Entrelinha</th><th class="r">Tracking</th></tr></thead><tbody>{rows}</tbody></table>'''
    return page(29, 4, b)


def site_section():
    cards = [("Velocidade", "Simulação, condições, aprovação e liberação numa jornada contínua."), ("Modularidade", "Cada parceiro ativa só os módulos que fazem sentido para a operação."),
             ("Eficiência", "Menos sistemas, menos fornecedores, menos desenvolvimento do zero."), ("Segurança", "Cada passo é rastreável, formalizado e auditável.")]
    ic = ["relogio", "camadas", "fluxo", "documento"]
    cs = "".join(f'''<div style="background:rgba(35,17,7,.035);border:1px solid rgba(35,17,7,.10);border-radius:32px;padding:8px">
        <div style="background:#fff;border:1px solid rgba(35,17,7,.10);border-radius:24px;padding:30px;height:230px;box-shadow:0 20px 45px -38px rgba(35,17,7,.45)">
        <div style="width:44px;height:44px;border-radius:999px;background:rgba(244,108,0,.12);display:flex;align-items:center;justify-content:center;color:#C4560F">{icon(ic[i], 6.5)}</div>
        <div style="font-size:17px;font-weight:600;letter-spacing:-.015em;margin-top:26px">{t}</div>
        <div style="font-size:16px;line-height:1.65;color:#6B5548;margin-top:10px">{d}</div></div></div>''' for i, (t, d) in enumerate(cards))
    return f'''<div style="width:1440px;height:900px;background:#F9F1ED;padding:110px 100px;font-family:Inter;color:#231107;font-feature-settings:'cv05' 1,'cv11' 1,'ss03' 1">
      <span style="display:inline-flex;align-items:center;gap:8px;background:rgba(244,108,0,.12);color:#9D430B;font-size:10px;font-weight:700;letter-spacing:.22em;padding:6px 13px 6px 10px;border-radius:999px">● TECNOLOGIA</span>
      <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:26px">
        <div style="font-family:InterD;font-size:61px;font-weight:620;letter-spacing:-.042em;line-height:1.03;width:760px">A infraestrutura<br>por trás do crédito.</div>
        <div style="display:flex;gap:12px">
          <span style="display:inline-flex;align-items:center;gap:14px;background:#F46C00;color:#0C0500;font-size:16.8px;font-weight:600;padding:9px 10px 9px 23px;border-radius:999px;box-shadow:0 1px 0 rgba(255,255,255,.22) inset,0 10px 30px -12px rgba(244,108,0,.75)">Conheça a plataforma<span style="width:32px;height:32px;border-radius:999px;background:rgba(12,5,0,.12);display:flex;align-items:center;justify-content:center">{icon("seta", 4.2, "#0C0500", 2)}</span></span>
          <span style="display:inline-flex;align-items:center;gap:14px;border:1px solid rgba(35,17,7,.10);color:#231107;font-size:16.8px;font-weight:600;padding:9px 10px 9px 23px;border-radius:999px">Fale com a UY3<span style="width:32px;height:32px;border-radius:999px;background:rgba(35,17,7,.06);display:flex;align-items:center;justify-content:center">{icon("seta", 4.2, "#231107", 2)}</span></span></div></div>
      <div style="font-size:20.8px;line-height:1.6;color:#6B5548;max-width:62ch;margin-top:26px">Invisível para o cliente final, decisiva para o seu negócio. A orquestração completa da jornada de crédito, da simulação à cobrança, em uma única plataforma.</div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:13.6px;margin-top:64px">{cs}</div></div>'''


def p29():
    fr, h = frame(0, 0, 196, 1440, 900, site_section(), radius=3, extra_style="box-shadow:0 0 0 .25mm rgba(35,17,7,.12)")
    s = 196 / (1440 * 0.264583)
    def ann(y_px, x_px, text, side_x=203):
        y = y_px * 0.264583 * s
        x = x_px * 0.264583 * s
        return (f'<div class="annl" style="left:{x}mm;top:{y}mm;width:{side_x - x}mm"></div>'
                f'<div style="position:absolute;left:{x-0.8}mm;top:{y-0.8}mm;width:1.6mm;height:1.6mm;border-radius:99mm;background:#C4560F"></div>'
                f'<div class="ann" style="left:{side_x+1.5}mm;top:{y-1.6}mm">{text}</div>')
    anns = (ann(116, 225, "Label · 700 · 10 px · +0,22em · Brasa Tinta") + ann(190, 700, "Headline · 620 · 61,6 px · −0,042em") +
            ann(370, 760, "Lede · 400 · 20,8 px · máx. 62 caracteres") + ann(212, 1020, "CTA · Subtitle 600 · pill · Carbono sobre Brasa") +
            ann(606, 330, "Title de card · Subtitle 600") + ann(660, 330, "Body · 400 · 16 px · entrelinha 1,65"))
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Tipografia aplicada</div><div class="t1" style="font-size:24pt">Hierarquia em uma seção do site</div></div>
      <p class="cap" style="max-width:96mm">Composição a 1440 px, montada com os tokens do DESIGN.md. Os textos vêm do conteúdo de referência do site. Os cards trazem apenas títulos e descrições, sem números de desempenho.</p></div>
    <div style="position:relative;margin-top:7mm;height:125mm">{fr}{anns}</div>'''
    return page(30, 4, b)


def p30():
    data = [("Operação A", "03/11/2026", "12 meses", "12.450,00", "18,4"), ("Operação B", "05/11/2026", "24 meses", "3.000,00", "4,4"),
            ("Operação C", "07/11/2026", "36 meses", "48.900,50", "72,2"), ("Operação D", "10/11/2026", "6 meses", "3.380,00", "5,0")]
    tr = "".join(f'<tr><td>{a}</td><td class="r">{d}</td><td class="r">{p}</td><td class="r">R$&nbsp;{v}</td><td class="r">{pc}%</td></tr>' for a, d, p, v, pc in data)
    rules = [("Moeda", "R$ 1.250,00", "R$1250.00 · 1.250,00 R$", "Símbolo antes, espaço não separável, ponto no milhar, vírgula no decimal, sempre duas casas."),
             ("Negativo", "−R$ 1.250,00", "(1.250,00) · R$ -1.250,00", "Sinal de menos (−) antes do símbolo. Não use só a cor para indicar valor negativo."),
             ("Percentual", "12,5%", "12.5 % · 12,50 por cento", "Vírgula decimal, sem espaço antes do %. Número de casas constante na mesma coluna."),
             ("Data", "12/11/2026", "11/12/26 · 12-nov", "dd/mm/aaaa em tabelas. Por extenso no texto: 12 de novembro de 2026."),
             ("Prazo", "24 meses", "24m · 2 anos", "Unidade por extenso, sem abreviação ambígua.")]
    rr = "".join(f'<div style="display:grid;grid-template-columns:20mm 30mm 40mm 1fr;gap:3mm;padding:2mm 0;border-top:.25mm solid var(--fio);align-items:baseline"><span class="t3" style="font-size:8.8pt">{a}</span><span class="tn" style="font-size:9pt;font-weight:650">{ok}</span><span class="tn" style="font-size:8.4pt;color:#9D430B;text-decoration:line-through">{no}</span><span class="cap">{d}</span></div>' for a, ok, no, d in rules)
    b = f'''<div class="g12">
      <div style="grid-column:1/7">
        <div class="eb">Informação financeira</div><div class="t1" style="font-size:24pt">Números alinhados, formatos constantes</div>
        <div class="card mt3" style="padding:5mm">
          <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="t3">Resumo de operações</span>{badge(None, "Dados ilustrativos")}</div>
          <table class="tb mt2"><thead><tr><th>Operação</th><th class="r">Data</th><th class="r">Prazo</th><th class="r">Valor</th><th class="r">Part. no total</th></tr></thead>
          <tbody>{tr}<tr><td><b>Total</b></td><td></td><td></td><td class="r"><b>R$&nbsp;67.730,50</b></td><td class="r"><b>100,0%</b></td></tr></tbody></table>
          <p class="cap mt2">Valores fictícios para demonstrar formatação. Não representam operações, condições ou ofertas da UY3. Notas e fontes vão abaixo da tabela, em 8 pt.</p></div>
        <p class="cap mt2">Números à direita, texto à esquerda, numerais tabulares, sem fio vertical. O total recebe peso 700 e fio superior.</p></div>
      <div style="grid-column:7/13">
        <div class="t3">Padrões de formatação</div>
        <div style="display:grid;grid-template-columns:20mm 30mm 40mm 1fr;gap:3mm;margin-top:3mm" class="cap"><span></span><span>Correto</span><span>Incorreto</span><span>Regra</span></div>
        <div class="mt1">{rr}</div>
        <p class="note mt3">Peças com taxas, prazos de liquidação, condições de crédito ou números institucionais passam por revisão do jurídico e do compliance antes da publicação. Sempre identifique a fonte e a data do dado.</p></div></div>'''
    return page(31, 4, b)


PAGES = [p25, p26, p27, p28, p29, p30]
