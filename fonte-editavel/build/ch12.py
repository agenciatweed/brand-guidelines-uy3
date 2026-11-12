# -*- coding: utf-8 -*-
from base import *

MIN = f"file://{S}/build/min"


def p01():
    b = f'''
    <div style="position:absolute;left:0;top:0;right:0;display:flex;justify-content:space-between" class="cap">
      <span style="color:var(--tcs)">UY3 Sociedade de Crédito Direto S.A.</span>
      <span style="color:var(--tcs)">{EDICAO}</span></div>
    <div style="position:absolute;left:0;top:34mm">{logo(C["brasa"], h=66)}</div>
    <div style="position:absolute;left:0;right:0;bottom:0;border-top:.25mm solid var(--fioe);padding-top:6mm;display:flex;justify-content:space-between;align-items:flex-end">
      <div class="t0" style="color:var(--tc)">{TITULO}</div>
      <div class="cap" style="color:var(--tcs);text-align:right;max-width:70mm">Logotipo, cores, tipografia, linguagem visual e aplicações</div>
    </div>'''
    return page(1, 1, b, "dark", chrome=False)


def p02():
    kw = [("Precisão", "Cada elemento tem medida, origem e função. Nada entra na página sem motivo."),
          ("Consistência", "A mesma marca em qualquer formato, do painel de evento à assinatura de e-mail, sem variações improvisadas."),
          ("Calor contido", "A Brasa marca o que é ativo, o caminho e a ação. O restante é carbono e creme.")]
    kws = "".join(f'''<div style="padding:5mm 0;border-top:.25mm solid var(--fio)">
        <div style="display:flex;gap:4mm;align-items:baseline"><span class="num">0{i+1}</span>
        <div><div class="t2" style="font-size:17pt">{k}</div><p class="soft mt1" style="font-size:9pt">{d}</p></div></div></div>'''
                  for i, (k, d) in enumerate(kw))
    pub = ["Marketing e comunicação institucional", "Agências, estúdios e fornecedores gráficos",
           "Produto, design de interface e tecnologia", "Comercial e relacionamento com parceiros",
           "Jurídico e compliance, na revisão de peças com conteúdo regulatório"]
    b = f'''<div class="g12">
      <div style="grid-column:1/7">
        <div class="eb">Apresentação</div>
        <div class="t1">Para que serve<br>este manual</div>
        <p class="lede mt3">Este manual reúne as regras que fazem a UY3 ser reconhecida da mesma forma em qualquer lugar: num relatório para um FIDC, numa tela da plataforma, num painel de evento ou numa assinatura de e-mail.</p>
        <p class="mt2">Ele registra o que já está definido (o logotipo original, a cor Brasa e a tipografia Inter, documentados no arquivo da marca e no sistema de design do site) e organiza o que ainda precisa de aprovação. Quando uma regra é proposta, e não herdada, o texto diz isso.</p>
        <div class="t3 mt4">Quem usa este manual</div>
        <ul class="l mt1">{"".join(f"<li>{x}</li>" for x in pub)}</ul>
      </div>
      <div style="grid-column:8/13;align-self:end">
        <div class="eb">Três palavras de direção</div>
        {kws}
        <p class="cap mt1">Palavras de direção de arte deste manual. Não são valores institucionais declarados pela UY3.</p>
      </div></div>'''
    return page(2, 1, b)


TOC = [
    (1, "Abertura e fundamentos", [("Apresentação e finalidade", 2), ("Contexto e posicionamento visual", 4), ("Personalidade e princípios", 5), ("Visão geral do sistema", 6)]),
    (2, "Assinatura e uso do logotipo", [("Assinatura principal", 8), ("Anatomia da marca", 9), ("Versões e configurações", 10), ("Positivo, negativo e monocromia", 11), ("Área de proteção", 12), ("Tamanhos mínimos", 13), ("Fundos institucionais", 14), ("Fotografias e fundos complexos", 15), ("Posicionamento e alinhamento", 16), ("Assinatura conjunta", 17), ("Usos incorretos", 18)]),
    (3, "Sistema cromático", [("Cor institucional principal", 20), ("Composição degradê", 21), ("Cores de apoio e neutras", 22), ("Proporção cromática", 23), ("Combinações", 24), ("Acessibilidade e cores funcionais", 25)]),
    (4, "Tipografia", [("Famílias e papéis", 27), ("Pesos, estilos e caracteres", 28), ("Hierarquia tipográfica", 29), ("Tipografia aplicada", 30), ("Informação financeira", 31)]),
    (5, "Linguagem visual e composição", [("Grid, margens e composição", 33), ("Elementos gráficos e iconografia", 34), ("Fotografia e visualização de dados", 35)]),
    (6, "Aplicações e governança", [("Papelaria e documentos", 37), ("Comunicação digital e redes sociais", 38), ("Site e interfaces", 39), ("Apresentações e parcerias", 40), ("Normas finais e checklist", 41)]),
]
OPENERS = {1: 1, 2: 7, 3: 19, 4: 26, 5: 32, 6: 36}


def p03():
    cols = [[], [], []]
    for i, (n, t, items) in enumerate(TOC):
        rows = "".join(f'<div style="display:flex;justify-content:space-between;padding:1.25mm 0;border-top:.25mm solid var(--fio2)" class="tn"><span style="font-size:8.8pt">{a}</span><span style="font-size:8.8pt" class="soft">{p:02d}</span></div>' for a, p in items)
        cols[i // 2].append(f'''<div style="margin-bottom:8mm">
          <div style="display:flex;justify-content:space-between;align-items:baseline;border-top:.35mm solid var(--tinta);padding-top:2mm">
            <div style="display:flex;gap:3mm;align-items:baseline"><span class="num">{n:02d}</span><span class="t3">{t}</span></div>
            <span class="tn" style="font-size:8.8pt;font-weight:650">{OPENERS[n]:02d}</span></div>
          <div class="mt1">{rows}</div></div>''')
    b = f'''<div class="eb">Sumário</div><div class="t1">Conteúdo</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);column-gap:10mm;margin-top:10mm">
      {"".join(f"<div>{''.join(c)}</div>" for c in cols)}</div>'''
    return page(3, 1, b)


def p04():
    desafios = [("Credibilidade", "sem conservadorismo ornamental", "Ordem, medida e respiro comunicam solidez. Brasões, dourados e serifas de época não."),
                ("Clareza", "sem frieza", "Hierarquia curta e linguagem direta. Os neutros são quentes: carbono e creme, nunca cinza."),
                ("Tecnologia", "sem efemeridade", "Nada de gradiente roxo, neon ou telas de ficção científica. A tecnologia aparece como precisão de execução.")]
    cards = "".join(f'''<div class="card" style="padding:4mm 5mm;display:grid;grid-template-columns:44mm 1fr;gap:4mm;align-items:baseline"><div><div class="t2">{a}</div><div class="cap" style="color:var(--brasa-tinta);font-weight:600">{b_}</div></div>
        <p style="font-size:9pt">{c}</p></div>''' for a, b_, c in desafios)
    restr = ["Não representar dinheiro diretamente: moedas, cédulas, cofres, sacos ou símbolos de moeda como imagem.",
             "Não usar “banco” como autodescrição, nem linguagem que equipare a UY3 a um banco.",
             "Não expor fornecedores de tecnologia, nuvem ou parceiros de integração em peças públicas.",
             "Revisar com o jurídico qualquer peça que mencione autorização, prazos de liquidação ou condições comerciais."]
    b = f'''<div class="g12">
      <div style="grid-column:1/6">
        <div class="eb">Contexto</div>
        <div class="t1" style="font-size:26pt">A infraestrutura que ninguém vê precisa de uma marca que se reconhece</div>
        <p class="mt3">A <b>UY3 Sociedade de Crédito Direto S.A.</b> opera como Sociedade de Crédito Direto, categoria de instituição financeira regulada pelo Banco Central. Seu posicionamento é o de infraestrutura de crédito (<i>Credit as a Service</i>): tecnologia que conecta quem origina crédito, quem o formaliza e quem o financia no mercado de capitais.</p>
        <p class="mt2">A missão declarada no site institucional é <b>descentralizar e democratizar o acesso ao crédito no Brasil</b>.</p>
        <p class="note mt3">O sistema de design do site resume a direção visual em uma imagem: <b>a sala de máquinas</b>. O visitante olha para dentro do motor de crédito, e o desenho diz sem legenda o que o site diz em palavras: “invisível para o cliente final, decisiva para o seu negócio”.</p>
      </div>
      <div style="grid-column:7/13">
        <div class="eb">O desafio estético</div>
        <div style="display:flex;flex-direction:column;gap:2.5mm">{cards}</div>
        <div class="t3 mt4">Restrições de expressão já estabelecidas</div>
        <ul class="l mt1">{"".join(f'<li style="font-size:9pt">{x}</li>' for x in restr)}</ul>
        <p class="cap mt1">Fontes: base de conhecimento UY3 (ago/2026), sistema de design do site (DESIGN.md) e diretrizes editoriais do projeto.</p>
      </div></div>'''
    return page(4, 1, b)


def p05():
    pares = [("Experiente", "sem ser antiquada", "Peso 620 firme nos títulos, sem ornamentos de época, serifas históricas ou dourados."),
             ("Técnica", "sem ser inacessível", "Fios de 1 px e medidas exatas na estrutura; frases curtas e diretas no texto."),
             ("Ágil", "sem parecer superficial", "Poucos elementos por página e hierarquia curta, sem efeitos de movimento decorativos."),
             ("Tecnológica", "sem se afastar do fundamento financeiro", "Dados rotulados e alinhados; a Brasa sinaliza estado e caminho, como num painel de operação."),
             ("Regulada e segura", "sem parecer burocrática", "Contraste AA, notas legais legíveis e espaço generoso, sem a cara de formulário.")]
    rows = "".join(f'''<div style="display:grid;grid-template-columns:44mm 62mm 1fr;gap:6mm;padding:2.6mm 0;border-top:.25mm solid var(--fio);align-items:baseline">
        <div class="t2" style="font-size:15pt">{a}</div><div class="t3" style="color:var(--ts);font-weight:500">{b_}</div><p style="font-size:9.2pt">{c}</p></div>''' for a, b_, c in pares)
    b = f'''<div class="eb">Personalidade</div>
      <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
        <div class="t1">Somos, sem<br>deixar de ser</div>
        <p class="cap" style="max-width:96mm">Os cinco pares vêm do <b>Guia de Tom de Voz da UY3</b> (regra geral de comunicação). A coluna da direita traduz cada par em decisão visual e é <b>direção de arte deste manual</b>.</p></div>
      <div style="display:grid;grid-template-columns:44mm 62mm 1fr;gap:6mm;margin-top:8mm" class="cap"><span>Somos</span><span>Evitamos parecer</span><span>Como isso aparece no desenho</span></div>
      <div class="mt1">{rows}</div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:7mm">
        <div><div class="tile" style="height:30mm;background:var(--papel);border:.25mm solid var(--fio);justify-content:flex-start;padding:0 5mm"><span style="font-family:InterD;font-size:20pt;font-weight:620;letter-spacing:-.04em">Crédito com método</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center" class="mt1"><span class="cap">Experiente</span>{badge(True)}</div></div>
        <div><div class="tile" style="height:30mm;background:#F3E6C8;border:.25mm solid var(--fio);justify-content:flex-start;padding:0 5mm"><span style="font-family:'DejaVu Serif',Georgia,serif;font-style:italic;font-size:18pt;color:#8A6A1F">Crédito com método</span><div class="strike"></div></div>
          <div style="display:flex;justify-content:space-between;align-items:center" class="mt1"><span class="cap">Antiquada: serifa de época e dourado</span>{badge(False)}</div></div>
        <div><div class="tile" style="height:30mm;background:var(--cp);justify-content:flex-start;gap:3mm;padding:0 5mm"><span style="width:2.6mm;height:2.6mm;border-radius:99mm;background:#F46C00"></span><span style="color:#F6ECE6;font-size:11pt;font-weight:600">Cessão concluída</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center" class="mt1"><span class="cap">Tecnológica: Brasa como estado</span>{badge(True)}</div></div>
        <div><div class="tile" style="height:30mm;background:linear-gradient(120deg,#5B2BD9,#1BA3F2);justify-content:flex-start;padding:0 5mm"><span style="color:#fff;font-size:11pt;font-weight:700;text-shadow:0 0 3mm #7af">Cessão concluída</span><div class="strike"></div></div>
          <div style="display:flex;justify-content:space-between;align-items:center" class="mt1"><span class="cap">Efêmera: gradiente e brilho</span>{badge(False)}</div></div></div>
      <p class="cap mt1">Exemplos demonstrativos. Os casos marcados como incorretos estão fora do sistema e não devem ser reproduzidos.</p>'''
    return page(5, 1, b)


def p06():
    sw = [("Brasa", "#F46C00", 5), ("Carbono Profundo", "#0C0500", 3), ("Creme", "#F9F1ED", 3), ("Tinta", "#231107", 2), ("Brasa Tinta", "#9D430B", 2)]
    strip = "".join(f'''<div style="flex:{f};background:{h};padding:2mm;display:flex;flex-direction:column;justify-content:flex-end;{'border:.25mm solid var(--fio);' if h=='#F9F1ED' else ''}">
        <span style="font-size:7pt;font-weight:600;color:{'#0C0500' if h in ('#F46C00','#F9F1ED') else '#F6ECE6'}">{n}<br><span style="font-weight:400" class="tn">{h}</span></span></div>''' for n, h, f in sw)
    b = f'''<div class="eb">Visão geral</div><div class="t1" style="font-size:24pt">O sistema em uma prancha</div>
    <div style="display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:62mm 64mm;gap:4mm;margin-top:6mm;height:130mm">
      <div class="tile" style="grid-column:1/6;grid-row:1/3;background:var(--cp);flex-direction:column;align-items:flex-start;justify-content:space-between;padding:7mm">
        <span class="cap" style="color:var(--tcs)">Assinatura principal</span>{logo(C["brasa"], w=92)}
        <span class="cap" style="color:var(--tcs)">Brasa sobre Carbono Profundo · contraste 6,74:1</span></div>
      <div style="grid-column:6/13;grid-row:1;display:flex;flex-direction:column;gap:2mm">
        <span class="cap">Cores</span><div style="flex:1;display:flex;border-radius:3mm;overflow:hidden">{strip}</div></div>
      <div class="card" style="grid-column:6/9;grid-row:2;padding:5mm;display:flex;flex-direction:column;justify-content:space-between">
        <span class="cap">Tipografia</span><div style="font-size:52pt;font-weight:620;letter-spacing:-.045em;line-height:.9">Aa</div>
        <div><div class="t3">Inter</div><div class="cap">Família única · 400 · 600 · 620 · 700</div></div></div>
      <div class="shell" style="grid-column:9/11;grid-row:2;display:flex"><div class="core" style="flex:1;padding:4mm;display:flex;flex-direction:column;justify-content:space-between">
        <span class="eb" style="margin:0;font-size:5.6pt">Casca dupla</span>
        <div class="t3" style="font-size:10pt">Da simulação à cobrança, em um único lugar.</div>
        <span class="pill" style="background:var(--brasa);color:var(--cp);font-size:7pt;padding:1.2mm 3mm;align-self:flex-start">Fale com a UY3</span></div></div>
      <div class="tile" style="grid-column:11/13;grid-row:2;background:var(--cq);flex-direction:column;align-items:flex-start;justify-content:space-between;padding:4mm;box-shadow:inset 0 .3mm 0 rgba(255,255,255,.1)">
        <span style="color:var(--brasa-alta)">{icon("fluxo", 7)}</span>
        <div class="t3" style="color:var(--tc);font-size:10pt">Tecnologia nascida no crédito.</div>
        <span class="cap" style="color:var(--tcs)">Superfície escura</span></div>
    </div>'''
    return page(6, 1, b)


# ---------------- Capítulo 2 ----------------

def opener(n, ch, title, sub, extra="", theme="dark"):
    tc = "var(--tc)" if theme == "dark" else "var(--cp)"
    sc = "var(--tcs)" if theme == "dark" else "rgba(12,5,0,.78)"
    b = f'''<div style="position:absolute;left:0;top:0"><span class="num" style="font-size:9pt;color:{'var(--brasa-alta)' if theme=='dark' else 'var(--cp)'}">Capítulo {ch:02d}</span></div>
      {extra}
      <div style="position:absolute;left:0;bottom:0;right:0;border-top:.25mm solid {'var(--fioe)' if theme=='dark' else 'rgba(12,5,0,.25)'};padding-top:6mm;display:flex;justify-content:space-between;align-items:flex-end">
        <div class="t0" style="color:{tc};font-size:52pt">{title}</div>
        <p style="color:{sc};max-width:92mm;font-size:10.5pt">{sub}</p></div>'''
    return page(n, ch, b, theme)


def p07():
    ex = f'<div style="position:absolute;left:0;top:30mm">{logo(C["brasa"], h=60)}</div>'
    return opener(7, 2, "Logotipo", "Uma assinatura, sempre igual. É a repetição sem desvios que transforma um desenho em reconhecimento.", ex)


def spec_rows(rows):
    return "".join(f'<div style="display:grid;grid-template-columns:34mm 1fr;gap:3mm;padding:1.7mm 0;border-top:.25mm solid var(--fio)"><span class="cap">{a}</span><span style="font-size:8.6pt">{b_}</span></div>' for a, b_ in rows)


def p08():
    rows = [("Nome visual", "UY3"), ("Tipo", "Assinatura tipográfica (logotipo) de três caracteres, desenho próprio"),
            ("Orientação", "Horizontal · proporção 1,890 : 1"), ("Cor", "Brasa · Pantone 1505 C · HEX #F46C00 · RGB 244 108 0 · CMYK 0 / 71 / 100 / 0"),
            ("Arquivos oficiais", "Pacote v1.0 em SVG, PDF e PNG (RGB, CMYK e Pantone 1505 C), gerado do vetor “logo UY3-.pdf” sem redesenho"),
            ("Outras versões", "Nenhuma no arquivo original. Negativa e monocromática derivadas por recoloração, autorizadas nesta edição")]
    b = f'''<div class="g12">
      <div style="grid-column:1/8;display:flex;flex-direction:column;gap:4mm">
        <div class="shell" style="height:118mm;display:flex"><div class="core" style="flex:1;background:var(--papel);display:flex;align-items:center;justify-content:center">{logo(C["brasa"], w=120)}</div></div>
        <div class="cap">Assinatura principal sobre Papel, reproduzida a partir do vetor original sem redesenho.</div></div>
      <div style="grid-column:8/13">
        <div class="eb">Assinatura principal</div><div class="t1" style="font-size:24pt">Uma única assinatura, em Brasa</div>
        <p class="mt2">A UY3 tem uma só assinatura: o logotipo “UY3” horizontal, em Brasa. Não há símbolo separado nem descritor acoplado. Use sempre os arquivos oficiais e nunca redigite o nome.</p>
        <div class="t3 mt3">Ordem de preferência</div>
        <ul class="l mt1" style="font-size:9pt">
          <li><b>1.</b> Brasa sobre Carbono Profundo, Creme ou Papel</li>
          <li><b>2.</b> Negativa (Papel) sobre Carbono e superfícies escuras</li>
          <li><b>3.</b> Monocromática (Carbono) sobre Brasa ou em impressão a uma cor</li></ul>
        <div class="mt3">{spec_rows(rows)}</div></div></div>'''
    return page(8, 2, b)


def p09():
    X = STROKE
    guides = f'''
      <line x1="80" x2="760" y1="131.97" y2="131.97" stroke="#9D430B" stroke-width=".8" stroke-dasharray="4 3" vector-effect="non-scaling-stroke"/>
      <line x1="80" x2="760" y1="458.9" y2="458.9" stroke="#9D430B" stroke-width=".8" stroke-dasharray="4 3" vector-effect="non-scaling-stroke"/>
      <line x1="109.79" x2="165.5" y1="110" y2="110" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="109.79" x2="109.79" y1="104" y2="116" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="165.5" x2="165.5" y1="104" y2="116" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="391.82" x2="447.23" y1="490" y2="490" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="391.82" x2="391.82" y1="484" y2="496" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="447.23" x2="447.23" y1="484" y2="496" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="357.17" x2="391.82" y1="300" y2="300" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="447.23" x2="483.4" y1="440" y2="440" stroke="#231107" stroke-width="1" vector-effect="non-scaling-stroke"/>
      <line x1="230" x2="420" y1="100.4" y2="290.4" stroke="#9D430B" stroke-width=".7" vector-effect="non-scaling-stroke"/>
      <line x1="560" x2="760" y1="304.18" y2="104.18" stroke="#9D430B" stroke-width=".7" vector-effect="non-scaling-stroke"/>'''
    svg = (f'<svg viewBox="70 60 720 460" style="width:156mm;display:block" xmlns="http://www.w3.org/2000/svg">'
           f'<path fill="#F46C00" fill-opacity=".9" d="{P_U}"/><path fill="#F46C00" d="{P_Y}"/><path fill="#C4560F" d="{P_3}"/>{guides}'
           f'<text x="137" y="97" font-size="12" text-anchor="middle" fill="#231107" font-family="Inter" font-weight="700">X</text>'
           f'<text x="419" y="512" font-size="12" text-anchor="middle" fill="#231107" font-family="Inter" font-weight="700">X</text>'
           f'<text x="374" y="292" font-size="10" text-anchor="middle" fill="#231107" font-family="Inter" font-weight="600">0,62X</text>'
           f'<text x="465" y="432" font-size="10" text-anchor="middle" fill="#231107" font-family="Inter" font-weight="600">0,65X</text>'
           f'<text x="765" y="128" font-size="10" fill="#9D430B" font-family="Inter" font-weight="600">topo</text>'
           f'<text x="765" y="462" font-size="10" fill="#9D430B" font-family="Inter" font-weight="600">base</text>'
           f'<text x="236" y="92" font-size="10" fill="#9D430B" font-family="Inter" font-weight="600">45°</text>'
           f'<text x="742" y="98" font-size="10" fill="#9D430B" font-family="Inter" font-weight="600">45°</text></svg>')
    obs = [("U", "Duas hastes verticais unidas por base em arco. O topo da haste direita é cortado a 45°."),
           ("Y", "Braços a 45° convergindo para uma haste vertical. O braço direito continua sem interrupção na barra superior do 3."),
           ("3", "Barra superior, diagonal interna a 45° e bojo inferior em arco. Desenhado em tom mais escuro no diagrama apenas para identificação."),
           ("X", f"Espessura das hastes, medida no arquivo: U 55,71 · Y 55,41 unidades. X ≈ 16,9% da altura total. É o módulo das regras deste manual.")]
    b = f'''<div class="g12">
      <div style="grid-column:1/5">
        <div class="eb">Anatomia</div><div class="t1" style="font-size:24pt">O que o desenho mostra</div>
        <p class="mt2" style="font-size:9.2pt">Medidas observadas no vetor original. O diagrama descreve o desenho existente e não propõe malha construtiva nem significado para as formas.</p>
        <div class="mt3">{"".join(f'<div style="display:grid;grid-template-columns:8mm 1fr;gap:2mm;padding:2.2mm 0;border-top:.25mm solid var(--fio)"><span class="t2" style="color:var(--brasa-tinta)">{a}</span><p style="font-size:8.6pt">{t}</p></div>' for a, t in obs)}</div>
      </div>
      <div style="grid-column:5/13;display:flex;flex-direction:column;justify-content:center;align-items:center">
        <div class="card" style="padding:4mm 6mm">{svg}</div>
        <div class="cap mt2" style="align-self:flex-start">Todos os cortes diagonais seguem 45°. Intervalos entre caracteres de 0,62X a 0,65X. As curvas do U e do 3 ultrapassam levemente a linha de base das hastes retas (compensação óptica do desenho original).</div></div></div>'''
    return page(9, 2, b)


def p10():
    def t(content, name, status, ok):
        st = badge(True, "Original") if ok == "orig" else (badge(True, "Autorizada") if ok else badge(None, "Não disponibilizada"))
        return f'''<div style="display:flex;flex-direction:column;gap:2.4mm"><div class="tile" style="height:96mm;{content[1]}">{content[0]}</div>
        <div style="display:flex;justify-content:space-between;align-items:center"><span class="t3" style="font-size:9.6pt">{name}</span>{st}</div>
        <p class="cap">{status}</p></div>'''
    empty = lambda txt: (f'<span class="cap" style="text-align:center;padding:0 6mm">{txt}</span>', "background:transparent;border:.35mm dashed rgba(35,17,7,.25)")
    tiles = [
        t((logo(C["brasa"], w=62), "background:var(--papel);border:.25mm solid var(--fio)"), "Horizontal · Brasa", "Assinatura principal. Única versão presente no arquivo original.", "orig"),
        t((logo("#FFFFFF", w=62), "background:var(--cp)"), "Negativa", "Mesmo vetor recolorido em Papel (#FFFFFF). Sem redesenho.", True),
        t((logo(C["carbono-profundo"], w=62), "background:var(--brasa)"), "Monocromática", "Mesmo vetor em Carbono Profundo, para Brasa e impressão a uma cor.", True),
    ]
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
        <div><div class="eb">Versões</div><div class="t1" style="font-size:24pt">Versões e configurações</div></div>
        <p class="cap" style="max-width:110mm">A UY3 tem uma única configuração, a assinatura horizontal, em três versões de cor. Negativa e monocromática foram autorizadas pela gestão da marca nesta edição. Não existem versão vertical, reduzida ou símbolo isolado, e nenhuma variação pode ser criada, nem provisoriamente.</p></div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6mm 6mm;margin-top:7mm">{"".join(tiles[:3])}</div>
      <p class="note mt3">Não use letras isoladas do logotipo (U, Y ou 3) como ícone, avatar, marca-d’água ou elemento gráfico.</p>'''
    return page(10, 2, b)


def p11():
    items = [("Brasa sobre fundo claro", "Principal", "var(--papel)", C["brasa"], "Papel ou Creme. Uso preferencial em documentos e peças claras.", "3,00:1 sobre Papel"),
             ("Brasa sobre Carbono", "Principal em escuro", "var(--cp)", C["brasa"], "Maior contraste da marca. Preferencial em telas escuras, eventos e vídeo.", "6,74:1"),
             ("Negativa", "Alternativa", "var(--cq)", "#FFFFFF", "Papel sobre Carbono Quente ou imagens escuras quando a Brasa competir com o fundo.", "18,14:1 sobre Carbono Quente"),
             ("Monocromática Carbono", "Uso restrito", "var(--brasa)", C["carbono-profundo"], "Única versão admitida sobre a Brasa. Também em impressão a uma cor e gravação.", "6,74:1")]
    tiles = "".join(f'''<div style="display:flex;flex-direction:column;gap:2.4mm">
        <div class="tile" style="height:74mm;background:{bg};{'border:.25mm solid var(--fio);' if bg=='var(--papel)' else ''}">{logo(f, w=44)}</div>
        <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="t3" style="font-size:9.6pt">{n}</span><span class="cap" style="color:var(--brasa-tinta);font-weight:600">{tag}</span></div>
        <p class="cap">{d}</p><p class="cap tn"><b>Contraste:</b> {c}</p></div>''' for n, tag, bg, f, d, c in items)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
        <div><div class="eb">Comportamento cromático</div><div class="t1" style="font-size:24pt">Positivo, negativo e monocromia</div></div>
        <p class="cap" style="max-width:118mm">Logotipos são isentos dos critérios de contraste da WCAG, mas o contraste continua definindo a legibilidade. Por isso a Brasa sobre fundo claro (3,00:1 sobre Papel; 2,69:1 sobre Creme) exige os tamanhos mínimos da página 13, e a Brasa nunca é aplicada sobre a própria Brasa.</p></div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:8mm">{tiles}</div>'''
    return page(11, 2, b)


def p12():
    X = STROKE
    pad = X
    vb = f"{109.789 - pad*1.6} {131.969 - pad*1.6} {LW + pad*3.2} {LH + pad*3.2}"
    x0, y0 = 109.789 - X, 131.969 - X
    w0, h0 = LW + 2 * X, LH + 2 * X
    sq = lambda x, y: f'<rect x="{x}" y="{y}" width="{X}" height="{X}" fill="rgba(244,108,0,.16)" stroke="#C4560F" stroke-width=".7" vector-effect="non-scaling-stroke"/><text x="{x+X/2}" y="{y+X/2+5}" font-size="14" text-anchor="middle" fill="#9D430B" font-family="Inter" font-weight="700">X</text>'
    grid = "".join(f'<line x1="{x0 + i*X/2}" x2="{x0 + i*X/2}" y1="{y0}" y2="{y0+h0}" stroke="rgba(35,17,7,.07)" stroke-width=".5" vector-effect="non-scaling-stroke"/>' for i in range(int(w0 / (X/2)) + 1))
    grid += "".join(f'<line y1="{y0 + i*X/2}" y2="{y0 + i*X/2}" x1="{x0}" x2="{x0+w0}" stroke="rgba(35,17,7,.07)" stroke-width=".5" vector-effect="non-scaling-stroke"/>' for i in range(int(h0 / (X/2)) + 1))
    svg = (f'<svg viewBox="{vb}" style="width:150mm;display:block" xmlns="http://www.w3.org/2000/svg">{grid}'
           f'<rect x="{x0}" y="{y0}" width="{w0}" height="{h0}" fill="none" stroke="#9D430B" stroke-width="1" stroke-dasharray="5 3" vector-effect="non-scaling-stroke"/>'
           f'<rect x="109.789" y="131.969" width="{LW}" height="{LH}" fill="none" stroke="rgba(35,17,7,.35)" stroke-width=".6" vector-effect="non-scaling-stroke"/>'
           f'<path fill="#F46C00" d="{P_ALL}"/>'
           f'{sq(x0, y0)}{sq(x0+w0-X, y0)}{sq(x0, y0+h0-X)}{sq(x0+w0-X, y0+h0-X)}'
           f'{sq(109.789, 131.969 - X)}</svg>')
    b = f'''<div class="g12">
      <div style="grid-column:1/5">
        <div class="eb">Área de proteção</div><div class="t1" style="font-size:24pt">Respiro mínimo de 1X em todos os lados</div>
        <p class="mt2" style="font-size:9.2pt"><b>X</b> é a espessura da haste do U, medida no vetor original (≈ 16,9% da altura do logotipo). Nenhum texto, borda, imagem ou outra marca pode invadir a área tracejada.</p>
        <div class="mt3">{spec_rows([("Módulo", "X = espessura da haste"), ("Mínimo", "1X em todos os lados"), ("Capas e peças institucionais", "2X ou mais, quando houver espaço"), ("Exemplo", "Logotipo com 20 mm de altura → X ≈ 3,4 mm")])}</div>
        <p class="note mt3">Recomendação editorial desta edição. O arquivo original não define área de proteção.</p></div>
      <div style="grid-column:5/13;display:flex;align-items:center;justify-content:center"><div class="card" style="padding:6mm">{svg}</div></div></div>'''
    return page(12, 2, b)


def p13():
    hs = [(20, True), (12, True), (8, True), (6, True), (4, False)]
    reals = "".join(f'''<div style="display:flex;align-items:flex-end;gap:5mm;padding:6mm 0;border-top:.25mm solid var(--fio)">
        <div style="width:42mm;display:flex;align-items:flex-end">{logo(C["brasa"], h=h)}</div>
        <div class="tn" style="font-size:8.6pt;width:34mm"><b>{h} mm</b> de altura<br><span class="soft">{h*LW/LH:.1f} mm de largura</span></div>
        {badge(ok, "Abaixo do mínimo" if not ok else ("Mínimo" if h == 6 else "Adequado"))}</div>''' for h, ok in hs)
    pxs = [(16, False, "O miolo do 3 se fecha"), (20, None, "No limite"), (24, True, "Mínimo"), (32, True, "Recomendado")]
    digs = "".join(f'''<div style="display:flex;flex-direction:column;gap:2mm;align-items:flex-start">
        <div class="tile" style="background:var(--papel);border:.25mm solid var(--fio);height:24mm;width:100%">
        <img src="{MIN}/l{p}_c.png" style="height:{p*0.36}mm;image-rendering:pixelated" alt="Logotipo rasterizado a {p} px"></div>
        <div class="tn" style="font-size:8.6pt"><b>{p} px</b> de altura</div>{badge(ok, t)}</div>''' for p, ok, t in pxs)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
        <div><div class="eb">Tamanhos mínimos</div><div class="t1" style="font-size:24pt">Abaixo destes tamanhos, a marca deixa de ser lida</div></div></div>
      <div class="g12" style="height:auto;margin-top:6mm">
        <div style="grid-column:1/7"><div class="t3">Impressão · escala real (100%)</div>
          <p class="cap mt1">Imprima esta página sem ajuste de escala para conferir.</p><div class="mt2">{reals}</div></div>
        <div style="grid-column:7/13"><div class="t3">Digital · teste de rasterização</div>
          <p class="cap mt1">Arquivo oficial rasterizado em cada altura e ampliado para deixar os pixels visíveis.</p>
          <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3mm" class="mt2">{digs}</div>
          <div class="mt3">{spec_rows([("Impressão", "mínimo 6 mm de altura (≈ 11,3 mm de largura)"), ("Digital", "mínimo 24 px de altura (≈ 45 px); recomendado 32 px ou mais"), ("Avatar e favicon", "logotipo completo sobre Carbono, com 1X de respiro; nunca letras isoladas")])}</div>
          <p class="note mt2">Valores provisórios, definidos por teste de legibilidade nesta edição e sujeitos a validação em prova de impressão.</p></div></div>'''
    return page(13, 2, b)


def p14():
    bgs = [("Papel", "#FFFFFF", [(C["brasa"], True), (C["carbono-profundo"], True)]),
           ("Creme", "#F9F1ED", [(C["brasa"], True), (C["carbono-profundo"], True)]),
           ("Creme de Contato", "#F4DFD2", [(C["brasa"], None), (C["carbono-profundo"], True)]),
           ("Carbono Profundo", "#0C0500", [(C["brasa"], True), ("#FFFFFF", True)]),
           ("Carbono Quente", "#261003", [(C["brasa"], True), ("#FFFFFF", True)]),
           ("Brasa", "#F46C00", [(C["carbono-profundo"], True), ("#FFFFFF", False)])]
    def cell(bg, f, ok):
        c = fmt(cr(bg, f))
        return f'''<div style="display:flex;flex-direction:column;gap:1.6mm"><div class="tile" style="height:40mm;background:{bg};{'border:.25mm solid var(--fio);' if bg in ('#FFFFFF','#F9F1ED','#F4DFD2') else ''}">{logo(f, w=32)}</div>
        <div style="display:flex;justify-content:space-between;align-items:center"><span class="cap tn">{c}:1</span>{badge(ok, "Preferencial" if ok else ("Evitar" if ok is False else "Acima de 12 mm"))}</div></div>'''
    cols = "".join(f'''<div><div class="t3" style="font-size:9pt">{n}</div><div class="cap tn">{h}</div>
        <div style="display:flex;flex-direction:column;gap:4mm" class="mt2">{"".join(cell(h, f, ok) for f, ok in v)}</div></div>''' for n, h, v in bgs)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Fundos institucionais</div><div class="t1" style="font-size:24pt">Qual versão usar em cada superfície</div></div>
      <p class="cap" style="max-width:104mm">Somente superfícies do sistema. O número indica o contraste entre logotipo e fundo. Sobre Creme de Contato a Brasa cai para 2,34:1, então só a use acima de 12 mm de altura.</p></div>
      <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:4mm;margin-top:7mm">{cols}</div>'''
    return page(14, 2, b)


PHOTO = {
    "limpa": "radial-gradient(120% 90% at 75% 40%, #3a2416 0%, #1d0f07 55%, #0c0500 100%)",
    "escura": "linear-gradient(115deg, #120802 0%, #2a170b 45%, #5a3a24 75%, #8b6a50 100%)",
    "clara": "linear-gradient(120deg, #f4e8de 0%, #e5d2c3 45%, #c9ab94 100%)",
    "carregada": "repeating-linear-gradient(65deg, #6b4a33 0 2.2mm, #c08f63 2.2mm 3.4mm, #3a2416 3.4mm 5mm, #e0c3a5 5mm 6mm), radial-gradient(circle at 30% 30%, #fff 0, transparent 60%)",
}


def p15():
    sit = [("Área limpa", "limpa", f'<div style="position:absolute;left:6mm;top:6mm">{logo(C["brasa"], w=30)}</div>', True, "Preferencial: logotipo em área uniforme e escura da imagem, com 1X de respiro."),
           ("Região escura", "escura", f'<div style="position:absolute;left:6mm;bottom:6mm">{logo("#FFFFFF", w=30)}</div>', True, "Use a negativa quando a região tiver tons médios que reduzam a Brasa."),
           ("Região clara", "clara", f'<div style="position:absolute;right:6mm;top:6mm">{logo(C["carbono-profundo"], w=30)}</div>', None, "Na área clara, prefira a Brasa se o fundo for uniforme. A versão Carbono é a alternativa."),
           ("Fundo carregado", "carregada", f'<div style="position:absolute;left:6mm;bottom:6mm;background:var(--cp);padding:3.2mm;border-radius:2mm">{logo(C["brasa"], w=26)}</div>', None, "Sem área limpa, aplique uma placa sólida de Carbono com 1X de respiro. Melhor ainda é trocar a imagem.")]
    tiles = "".join(f'''<div style="display:flex;flex-direction:column;gap:2.4mm">
        <div class="tile" style="height:82mm;background:{PHOTO[k]};display:block">{lg}
        <span style="position:absolute;right:3mm;bottom:3mm;font-size:6pt;color:rgba(255,255,255,.7);font-weight:600;background:rgba(12,5,0,.45);padding:.6mm 1.6mm;border-radius:99mm">Exemplo conceitual</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center"><span class="t3" style="font-size:9.6pt">{n}</span>{badge(ok, "Preferencial" if ok else "Com condição")}</div>
        <p class="cap">{d}</p></div>''' for n, k, lg, ok, d in sit)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Imagens e fundos complexos</div><div class="t1" style="font-size:24pt">Sobre imagens, a marca precisa de área limpa</div></div>
      <p class="cap" style="max-width:104mm">Nunca posicione o logotipo sobre rostos, números, textos ou o ponto de interesse da imagem. As molduras abaixo são composições tonais conceituais e não substituem fotografia aprovada.</p></div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:7mm">{tiles}</div>'''
    return page(15, 2, b)


def p16():
    def mini(w, h, inner, bg="var(--papel)", border=True):
        return f'<div style="width:{w}mm;height:{h}mm;background:{bg};position:relative;border-radius:1.5mm;{"border:.25mm solid var(--fio);" if border else ""}overflow:hidden">{inner}</div>'
    marg = lambda w, h, m: f'<div style="position:absolute;left:{m}mm;top:{m}mm;width:{w-2*m}mm;height:{h-2*m}mm;border:.25mm dashed rgba(196,86,15,.55)"></div>'
    lines = lambda n, w, top, left: "".join(f'<div style="position:absolute;left:{left}mm;top:{top+i*2.2}mm;width:{w-(i%3)*6}mm;height:.8mm;background:rgba(35,17,7,.14);border-radius:1mm"></div>' for i in range(n))
    capa = mini(46, 65, marg(46, 65, 4) + f'<div style="position:absolute;left:4mm;top:4mm">{logo(C["brasa"], w=12)}</div>' + f'<div style="position:absolute;left:4mm;bottom:12mm;width:30mm;height:2.6mm;background:rgba(35,17,7,.8)"></div>' + lines(2, 30, 55, 4))
    doc = mini(46, 65, marg(46, 65, 4) + lines(10, 36, 8, 4) + f'<div style="position:absolute;left:4mm;right:4mm;bottom:4mm;border-top:.25mm solid var(--fio);padding-top:1mm;display:flex;justify-content:space-between;align-items:center">{logo(C["brasa"], w=7)}<span style="font-size:4pt" class="soft">01</span></div>')
    site = mini(92, 52, f'<div style="position:absolute;left:4mm;right:4mm;top:3mm;height:7mm;border-radius:99mm;background:rgba(255,255,255,.07);display:flex;align-items:center;justify-content:space-between;padding:0 2mm 0 3mm">{logo(C["brasa"], w=9)}<div style="width:9mm;height:3.4mm;border-radius:99mm;background:var(--brasa)"></div></div><div style="position:absolute;left:8mm;top:20mm;width:50mm;height:4mm;background:rgba(246,236,230,.85)"></div><div style="position:absolute;left:8mm;top:26mm;width:38mm;height:4mm;background:rgba(246,236,230,.85)"></div>', "var(--cp)", False)
    story = mini(30, 53, f'<div style="position:absolute;left:3mm;top:3mm">{logo(C["brasa"], w=9)}</div><div style="position:absolute;left:3mm;bottom:9mm;width:22mm;height:2.6mm;background:rgba(246,236,230,.85)"></div><div style="position:absolute;left:3mm;bottom:5mm;width:16mm;height:2.6mm;background:rgba(246,236,230,.85)"></div>', "var(--cq)", False)
    wide = mini(80, 45, f'<div style="position:absolute;left:5mm;top:5mm;width:40mm;height:4mm;background:rgba(12,5,0,.85)"></div><div style="position:absolute;left:5mm;top:11mm;width:30mm;height:4mm;background:rgba(12,5,0,.85)"></div><div style="position:absolute;right:5mm;bottom:5mm">{logo(C["carbono-profundo"], w=14)}</div>', "var(--brasa)", False)
    items = [(capa, "Capa de documento", "Canto superior esquerdo, alinhado à margem. O título ocupa o terço inferior."),
             (doc, "Rodapé de documento", "Logotipo pequeno (mínimo 6 mm) à esquerda, numeração à direita, sobre fio de cabelo."),
             (site, "Cabeçalho de interface", "À esquerda, dentro da navegação. Altura mínima de 24 px."),
             (story, "Formato vertical", "Topo esquerdo. O texto se ancora na base."),
             (wide, "Formato horizontal sobre Brasa", "Versão Carbono no canto inferior direito, como assinatura de fechamento.")]
    cells = "".join(f'<div style="display:flex;flex-direction:column;gap:2.4mm"><div style="height:56mm;display:flex;align-items:flex-end"><div style="zoom:.82">{m}</div></div><div class="t3" style="font-size:9.4pt">{t}</div><p class="cap">{d}</p></div>' for m, t, d in items)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Posicionamento</div><div class="t1" style="font-size:24pt">Alinhado à margem, nunca solto</div></div>
      <p class="cap" style="max-width:110mm">O logotipo se alinha à margem e à primeira coluna do grid. As posições preferenciais são os cantos superior esquerdo (abertura) e inferior direito (assinatura). Centralize apenas em capas e vinhetas de composição simétrica. A linha tracejada marca a margem.</p></div>
      <div style="display:grid;grid-template-columns:38mm 38mm 76mm 26mm 1fr;gap:5mm;margin-top:22mm">{cells}</div>'''
    return page(16, 2, b)


def p17():
    partner = lambda w, h: f'<div style="width:{w}mm;height:{h}mm;border:.35mm dashed rgba(35,17,7,.35);border-radius:1mm;display:flex;align-items:center;justify-content:center;font-size:7pt;font-weight:600;color:var(--ts)">Marca parceira</div>'
    h1 = f'''<div class="card" style="height:56mm;display:flex;align-items:center;justify-content:center;gap:0">
        {logo(C["brasa"], h=12)}<div style="width:8mm"></div><div style="width:.3mm;height:16mm;background:rgba(35,17,7,.25)"></div><div style="width:8mm"></div>{partner(34, 12)}</div>'''
    h2 = f'''<div class="card" style="height:56mm;display:flex;flex-direction:column;align-items:flex-start;justify-content:center;padding:0 12mm;gap:4mm">
        <span class="eb" style="margin:0">Realização</span>{logo(C["brasa"], h=9)}<div style="width:100%;border-top:.25mm solid var(--fio)"></div>
        <span class="eb" style="margin:0">Parceiros</span><div style="display:flex;gap:6mm">{partner(26, 9)}{partner(26, 9)}{partner(26, 9)}</div></div>'''
    regras = [("Equivalência óptica", "As marcas têm a mesma altura visual, não a mesma largura. Ajuste pela massa, sem esticar."),
              ("Distância", "2X entre o logotipo UY3 e o separador, e 2X entre o separador e a marca parceira."),
              ("Separador", "Fio vertical de 1 px em Tinta a 25%, com 1,3 vez a altura do logotipo."),
              ("Ordem", "Quem realiza assina primeiro, à esquerda ou acima. Em listas de parceiros, siga a ordem acordada em contrato."),
              ("Autorização", "Use marcas de terceiros só com autorização formal e a partir dos arquivos oficiais de cada uma.")]
    b = f'''<div class="g12">
      <div style="grid-column:1/5"><div class="eb">Assinatura conjunta</div><div class="t1" style="font-size:24pt">Convivência com outras marcas</div>
        <div class="mt3">{"".join(f'<div style="padding:2.2mm 0;border-top:.25mm solid var(--fio)"><div class="t3" style="font-size:9.2pt">{a}</div><p class="cap mt1" style="color:var(--tinta)">{t}</p></div>' for a, t in regras)}</div></div>
      <div style="grid-column:5/13;display:flex;flex-direction:column;gap:5mm">
        <div class="cap">Lado a lado: parceria entre iguais</div>{h1}
        <div class="cap">Hierárquica: realização e apoio</div>{h2}
        <p class="note">Os blocos “Marca parceira” são demonstrativos e não representam parceria real. Distâncias e separador são recomendação editorial desta edição.</p></div></div>'''
    return page(17, 2, b)


def p18():
    L = lambda f=C["brasa"], st="", w=38: logo(f, w=w, style=st)
    typed = '<span style="font-family:Inter;font-weight:800;font-size:30pt;color:#F46C00;letter-spacing:-.02em">UY3</span>'
    mod = (f'<svg viewBox="{VB}" style="width:38mm;display:block"><path fill="#F46C00" d="{P_U}"/>'
           f'<path fill="#F46C00" d="{P_Y}" transform="translate(-30 0)"/><path fill="#F46C00" d="{P_3}" transform="translate(40 0)"/></svg>')
    cases = [
        ("Não distorcer", L(st="transform:scaleX(1.45)"), "var(--papel)"),
        ("Não girar", L(st="transform:rotate(-14deg)"), "var(--papel)"),
        ("Não alterar a cor", L("#2F6BD8"), "var(--papel)"),
        ("Não aplicar sombra ou brilho", L(st="filter:drop-shadow(1.2mm 1.2mm 1mm rgba(0,0,0,.55))"), "var(--papel)"),
        ("Não modificar componentes", mod, "var(--papel)"),
        ("Não recriar com tipografia", typed, "var(--papel)"),
        ("Não reduzir abaixo do mínimo", L(w=7), "var(--papel)"),
        ("Não comprometer o contraste", L(C["brasa"]), "var(--brasa-alta)"),
    ]
    tiles = "".join(f'''<div style="display:flex;flex-direction:column;gap:2mm"><div class="tile" style="height:56mm;background:{bg};border:.25mm solid var(--fio)">{content}
        <div class="strike"></div><div style="position:absolute;left:2.4mm;top:2.4mm">{badge(False)}</div></div>
        <div class="t3" style="font-size:9.4pt">{t}</div></div>''' for t, content, bg in cases)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Usos incorretos</div><div class="t1" style="font-size:24pt">O que nunca fazer com a marca</div></div>
      <p class="cap" style="max-width:104mm">As alterações abaixo são demonstrativas e estão marcadas como incorretas. Valem também para as versões negativa e monocromática.</p></div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm 5mm;margin-top:7mm">{tiles}</div>'''
    return page(18, 2, b)


PAGES = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, p15, p16, p17, p18]
