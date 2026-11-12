# -*- coding: utf-8 -*-
from base import *
from ch12 import opener, spec_rows


def p19():
    ex = '''<div style="position:absolute;right:0;top:0;width:150mm;height:118mm;display:grid;grid-template-columns:5fr 2fr 2fr;gap:0;border-radius:4mm;overflow:hidden;box-shadow:0 0 0 .25mm rgba(12,5,0,.25)">
      <div style="background:#F46C00;border-right:.25mm solid rgba(12,5,0,.25);padding:4mm;display:flex;align-items:flex-end"><span style="font-size:8pt;font-weight:650;color:#0C0500">Brasa<br><span style="font-weight:400">#F46C00</span></span></div>
      <div style="background:#0C0500;padding:4mm;display:flex;align-items:flex-end"><span style="font-size:8pt;font-weight:650;color:#F6ECE6">Carbono<br>Profundo</span></div>
      <div style="background:#F9F1ED;padding:4mm;display:flex;align-items:flex-end"><span style="font-size:8pt;font-weight:650;color:#231107">Creme</span></div></div>'''
    return opener(19, 3, "Cores", "Uma paleta travada em uma única matiz. Do carbono mais fechado ao creme mais claro, tudo orbita o laranja, e não há cinza neutro no sistema.", ex, "brasa")


def p20():
    rows = [("Pantone", "PANTONE 1505 C"), ("CMYK", "0 · 71 · 100 · 0"), ("RGB", "244 · 108 · 0"), ("HEX", "#F46C00"),
            ("Impressão", "Pantone 1505 C em cor especial; CMYK em quadricromia, sempre com prova de cor"),
            ("Token no código", "--flame · brasa"), ("Origem", "Especificação da gestão da marca · novembro de 2026")]
    good = ["Botão primário e ação principal", "Estado selecionado, item ativo e ícone ativo", "Caminho da operação (a esteira)", "Superfície de interrupção: esteira e rodapé", "Logotipo sobre Carbono, Creme e Papel"]
    bad = ["Texto sobre fundo claro (2,69:1 sobre Creme)", "Texto branco sobre Brasa (3,00:1)", "Fundo inteiro de hero, por restrição do cliente", "Ornamento sem função de estado, caminho ou ação"]
    b = f'''<div class="g12">
      <div style="grid-column:1/7;display:flex;flex-direction:column">
        <div class="sw" style="flex:1;background:#F46C00;padding:7mm;display:flex;flex-direction:column;justify-content:space-between">
          <span class="eb" style="color:var(--cp);margin:0">Cor institucional principal</span>
          <div><div class="t0" style="color:var(--cp);font-size:56pt">Brasa</div><div class="t2 tn" style="color:var(--cp)">PANTONE 1505 C · #F46C00</div></div></div></div>
      <div style="grid-column:7/13">
        <div class="t1" style="font-size:22pt">A cor da marca e o único acento do sistema</div>
        <p class="mt2" style="font-size:9.2pt">A Brasa é definida pelo <b>Pantone 1505 C</b>, com valores equivalentes em CMYK, RGB e HEX. Esta especificação substitui o laranja anterior (#F47626 no site e CMYK 0 / 66,8 / 96,5 / 0 no vetor original). Logotipo, peças, interfaces e tokens do site passam a usar os valores desta página.</p>
        <div class="mt2">{spec_rows(rows)}</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm" class="mt3">
          <div><div style="display:flex;gap:2mm;align-items:center">{badge(True, "Use para")}</div><ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.2mm 0">{x}</li>' for x in good)}</ul></div>
          <div><div style="display:flex;gap:2mm;align-items:center">{badge(False, "Não use para")}</div><ul class="l mt1">{"".join(f'<li style="font-size:8.4pt;padding:1.2mm 0">{x}</li>' for x in bad)}</ul></div></div>
      </div></div>'''
    return page(20, 3, b)



def p_grad():
    G = "linear-gradient(90deg, #F46C00 0%, #D04D27 100%)"
    def spec(nome, pant, cmyk, rgbv, hx, papel):
        return f"""<div class="card" style="padding:4mm 5mm;display:grid;grid-template-columns:16mm 1fr;gap:4mm;align-items:center">
          <div style="width:16mm;height:16mm;border-radius:2.4mm;background:{hx}"></div>
          <div><div class="t3" style="white-space:nowrap">{pant}</div><div class="cap" style="color:var(--brasa-tinta);font-weight:600">{papel}</div>
          <div class="tn" style="font-size:8pt;line-height:1.55;margin-top:1mm">CMYK {cmyk} · RGB {rgbv} · <b>{hx}</b></div></div></div>"""
    rules = [("Construção", "Degradê linear de duas paradas: Pantone 1505 C no início e Pantone 173 C no fim, da esquerda para a direita. Sem terceira cor e sem inversão."),
             ("Onde usar", "Superfícies amplas de interrupção: capas, aberturas de seção, painéis de evento, fundos de vídeo e peças editoriais."),
             ("Texto", f"Sempre em Carbono Profundo: {fmt(cr('#0C0500', '#F46C00'))}:1 no início e {fmt(cr('#0C0500', '#D04D27'))}:1 no fim, ambos AA. Branco fica entre {fmt(cr('#FFFFFF', '#F46C00'))}:1 e {fmt(cr('#FFFFFF', '#D04D27'))}:1 e reprova para texto comum."),
             ("Logotipo", "Sobre o degradê, use a versão monocromática Carbono. Nunca aplique o degradê no próprio logotipo."),
             ("Pantone 173 C", "Existe apenas como ponto final do degradê. Não é cor de apoio isolada.")]
    rr = "".join(f'<div style="display:grid;grid-template-columns:26mm 1fr;gap:3mm;padding:2mm 0;border-top:.25mm solid var(--fio)"><span class="t3" style="font-size:9pt">{a}</span><p style="font-size:8.6pt">{t}</p></div>' for a, t in rules)
    capa = f"""<div class="tile" style="height:52mm;background:{G};display:block;padding:5mm">
        <div style="font-size:5.6pt;font-weight:700;letter-spacing:.2em;color:#0C0500">ABERTURA DE SEÇÃO</div>
        <div style="font-family:InterD;font-size:17pt;font-weight:620;letter-spacing:-.035em;line-height:1.03;color:#0C0500;margin-top:3mm;width:70mm">Onde o futuro do crédito se encontra.</div>
        <div style="position:absolute;right:5mm;bottom:5mm">{logo(C["carbono-profundo"], w=20)}</div></div>"""
    b = f"""<div class="g12">
      <div style="grid-column:1/8">
        <div class="eb">Composição degradê</div><div class="t1" style="font-size:24pt">Da Brasa ao Pantone 173 C</div>
        <div class="sw mt3" style="height:62mm;background:{G};display:flex;justify-content:space-between;align-items:flex-end;padding:4mm 5mm">
          <span class="tn" style="font-size:8pt;font-weight:650;color:#0C0500">#F46C00 · 1505 C</span><span class="tn" style="font-size:8pt;font-weight:650;color:#0C0500">173 C · #D04D27</span></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm" class="mt3">
          {spec("Início", "PANTONE 1505 C", "0 · 71 · 100 · 0", "244 · 108 · 0", "#F46C00", "Cor primária")}
          {spec("Fim", "PANTONE 173 C", "13 · 84 · 100 · 3", "208 · 77 · 39", "#D04D27", "Só para degradê")}</div>
        <p class="cap mt2">CSS: <span class="mono" style="font-size:7.4pt">linear-gradient(90deg, #F46C00 0%, #D04D27 100%)</span></p></div>
      <div style="grid-column:8/13">
        <div class="mt1">{rr}</div>
        <div class="mt3">{capa}</div>
        <p class="note mt2">Cores conforme especificação da gestão da marca (novembro de 2026). As regras de uso são recomendação editorial desta edição.</p></div></div>"""
    return page(21, 3, b)

def sw(name, hx, role, h=26, txt=None, border=False, note=None):
    txt = txt or ("#0C0500" if lum(hx) > 0.18 else "#F6ECE6")
    cm = CMYK_IND.get(hx.upper(), "—")
    return f'''<div style="display:flex;flex-direction:column;gap:1.4mm">
      <div class="sw" style="height:{h}mm;background:{hx};{'border:.25mm solid var(--fio);' if border else ''}padding:2.4mm;display:flex;align-items:flex-end">
        <span style="font-size:7.6pt;font-weight:650;color:{txt}">{name}</span></div>
      <div class="tn" style="font-size:7.4pt;line-height:1.45"><b>{hx}</b> · RGB {" ".join(str(v) for v in rgb(hx))}<br><span class="soft">CMYK ind. {cm}</span><br>{role}{f"<br><span style='color:var(--brasa-tinta);font-weight:600'>{note}</span>" if note else ""}</div></div>'''


def p21():
    apoio = "".join([
        sw("Carbono Profundo", "#0C0500", "Fundo escuro principal: hero, rodapé, aberturas.", 34),
        sw("Creme", "#F9F1ED", "Fundo claro padrão das seções e páginas.", 34, border=True),
        sw("Tinta", "#231107", "Texto principal sobre superfícies claras.", 34),
        sw("Brasa Tinta", "#9D430B", "Texto de acento legível sobre fundo claro (5,81:1).", 34)])
    brasas = "".join([
        sw("Brasa Alta", "#FF8C45", "Acento sobre carbono; topo de gradiente do pilar ativo.", 18),
        sw("Brasa Profunda", "#C4560F", "Bordas, ícones e detalhe sobre claro. Nunca texto pequeno.", 18),
        f'''<div style="display:flex;flex-direction:column;gap:1.4mm"><div class="sw" style="height:18mm;background:linear-gradient(rgba(244,108,0,.12),rgba(244,108,0,.12)),#FFFFFF;border:.25mm solid var(--fio);padding:2.4mm;display:flex;align-items:flex-end"><span style="font-size:7.6pt;font-weight:650;color:#9D430B">Brasa Lavada</span></div>
        <div class="tn" style="font-size:7.4pt;line-height:1.45"><b>rgba(244,108,0,.12)</b><br><span class="soft">Sem CMYK: usar como transparência</span><br>Fundo de eyebrow e de ícone.</div></div>'''])
    neut = "".join([
        sw("Carbono", "#150903", "Degrau quase imperceptível sobre o Carbono Profundo.", 18),
        sw("Carbono Quente", "#261003", "Escuro alternativo, mais visível.", 18),
        sw("Papel", "#FFFFFF", "Superfície de card sobre Creme. Nunca fundo de seção inteira.", 18, border=True),
        sw("Creme de Contato", "#F4DFD2", "Exclusivo da seção de contato do site.", 18),
        sw("Tinta Suave", "#6B5548", "Texto secundário e legendas sobre claro.", 18),
        sw("Tinta Clara Suave", "#B09A8D", "Texto secundário sobre carbono.", 18)])
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Cores de apoio e neutras</div><div class="t1" style="font-size:24pt">Carbono e creme sustentam; a Brasa sinaliza</div></div>
      <p class="cap" style="max-width:100mm">O tamanho das amostras segue a hierarquia de uso. O CMYK é conversão indicativa (perfil FOGRA39, colorimétrico relativo), sujeita a perfil ICC do fornecedor e prova de cor. Os escuros são pretos ricos e exigem aprovação da gráfica.</p></div>
    <div class="t3 mt3">Institucionais de apoio</div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm" class="mt1">{apoio}</div>
    <div style="display:grid;grid-template-columns:3fr 6fr;gap:8mm" class="mt3">
      <div><div class="t3">Variações da Brasa · interface</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3mm" class="mt1">{brasas}</div></div>
      <div><div class="t3">Neutros de superfície e texto · interface</div><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:3mm" class="mt1">{neut}</div></div></div>
    <p class="note mt3"><b>Declarados no código, sem uso definido:</b> Carbono Claro #3A1C08 e Creme Fechado #F1E4DC. Não utilizar até que a gestão da marca defina seu papel. Fios de borda são sempre alfa sobre a superfície (Tinta a 5–10% no claro; branco a 5,5–10% no escuro), nunca cinza opaco.</p>'''
    return page(22, 3, b)


def p22():
    def bar(parts):
        return '<div style="display:flex;height:9mm;border-radius:2mm;overflow:hidden;box-shadow:0 0 0 .25mm rgba(35,17,7,.12)">' + "".join(
            f'<div style="flex:{p};background:{c}"></div>' for c, p in parts) + "</div>"
    def legend(parts):
        return '<div style="display:flex;gap:3mm;flex-wrap:wrap" class="mt1">' + "".join(f'<span class="cap tn"><span class="chip" style="background:{c}"></span> {n} {p}%</span>' for c, p, n in parts) + "</div>"
    claro = [("#F9F1ED", 62, "Creme"), ("#FFFFFF", 18, "Papel"), ("#231107", 14, "Tinta"), ("#F46C00", 4, "Brasa"), ("#9D430B", 2, "Brasa Tinta")]
    escuro = [("#0C0500", 70, "Carbono Profundo"), ("#261003", 14, "Carbono Quente"), ("#F6ECE6", 11, "Tinta Clara"), ("#F46C00", 5, "Brasa")]
    inter = [("#F46C00", 80, "Brasa"), ("#0C0500", 20, "Carbono Profundo")]
    comp_claro = f'''<div class="tile" style="height:62mm;background:#F9F1ED;border:.25mm solid var(--fio);display:block;padding:5mm">
        <div style="font-size:5pt;font-weight:700;letter-spacing:.2em;color:#9D430B">INFRAESTRUTURA</div>
        <div style="font-size:13pt;font-weight:620;letter-spacing:-.03em;line-height:1.05;margin-top:2mm;width:46mm">Da simulação à cobrança, em um único lugar.</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6mm;margin-top:4mm">{"".join('<div style="background:#fff;border-radius:2mm;height:14mm;border:.2mm solid rgba(35,17,7,.08)"></div>' for _ in range(2))}</div>
        <span class="pill" style="background:#F46C00;color:#0C0500;font-size:6pt;padding:1mm 2.6mm;margin-top:4mm">Fale com a UY3</span></div>'''
    comp_esc = f'''<div class="tile" style="height:62mm;background:#0C0500;display:block;padding:5mm">
        {logo(C["brasa"], w=12)}
        <div style="font-size:13pt;font-weight:620;letter-spacing:-.03em;line-height:1.05;margin-top:6mm;width:50mm;color:#F6ECE6">Tecnologia nascida no crédito.</div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6mm;margin-top:5mm">{"".join('<div style="background:#261003;border-radius:2mm;height:13mm;box-shadow:inset 0 .3mm 0 rgba(255,255,255,.1)"></div>' for _ in range(3))}</div></div>'''
    comp_int = f'''<div class="tile" style="height:62mm;background:#F46C00;display:block;padding:5mm">
        <div style="font-size:13pt;font-weight:620;letter-spacing:-.03em;line-height:1.05;width:56mm;color:#0C0500">Uma jornada. Sete etapas. Um único ambiente.</div>
        <div style="display:flex;gap:1.6mm;margin-top:9mm">{"".join(f'<div style="background:#F6853A;border-radius:1.6mm;height:8mm;flex:1;display:flex;align-items:center;justify-content:center;font-size:5pt;font-weight:650;color:#0C0500">{t}</div>' for t in ["Simulação","Proposta","Crédito","Cessão"])}</div></div>'''
    cols = [("Página clara", "Padrão para documentos, apresentações e seções do site.", comp_claro, claro),
            ("Página escura", "Aberturas, hero, eventos e vídeo. A Brasa ganha contraste.", comp_esc, escuro),
            ("Superfície de interrupção", "Fundo Brasa inteiro, raro e deliberado. Texto sempre em Carbono.", comp_int, inter)]
    cells = "".join(f'<div><div class="t3">{t}</div><p class="cap mt1" style="min-height:9mm">{d}</p><div class="mt1">{c}</div><div class="mt2">{bar([(x[0], x[1]) for x in parts])}</div>{legend(parts)}</div>' for t, d, c, parts in cols)
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Proporção cromática</div><div class="t1" style="font-size:24pt">Neutros dominam, a Brasa pontua</div></div>
      <p class="cap" style="max-width:104mm">“A Regra da Brasa Escassa” (DESIGN.md): o laranja marca estado, caminho e ação. Se aparece em elemento que não é nenhum dos três, virou decoração e deve sair. Os percentuais abaixo são <b>orientativos</b>, não norma.</p></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:7mm">{cells}</div>'''
    return page(23, 3, b)


def p23():
    pairs = [("#F9F1ED", "#231107", "Tinta sobre Creme"), ("#FFFFFF", "#231107", "Tinta sobre Papel"), ("#F9F1ED", "#6B5548", "Tinta Suave sobre Creme"),
             ("#F9F1ED", "#9D430B", "Brasa Tinta sobre Creme"), ("#0C0500", "#F6ECE6", "Tinta Clara sobre Carbono"), ("#0C0500", "#FF8C45", "Brasa Alta sobre Carbono"),
             ("#F46C00", "#0C0500", "Carbono sobre Brasa"), ("#0C0500", "#B09A8D", "Tinta Clara Suave sobre Carbono"),
             ("#F9F1ED", "#C4560F", "Brasa Profunda sobre Creme"), ("#0C0500", "#F46C00", "Brasa sobre Carbono"),
             ("#F46C00", "#FFFFFF", "Branco sobre Brasa"), ("#F9F1ED", "#F46C00", "Brasa sobre Creme")]
    def cls(r):
        if r >= 7: return True, "Preferencial"
        if r >= 4.5: return None, "Permitido"
        if r >= 3: return None, "Só texto grande"
        return False, "Evitar"
    cells = ""
    for bg, fg, n in pairs:
        r = cr(bg, fg)
        ok, t = cls(r)
        cells += f'''<div style="display:flex;flex-direction:column;gap:1.4mm">
          <div class="sw" style="height:22mm;background:{bg};{'border:.25mm solid var(--fio);' if bg in ('#F9F1ED','#FFFFFF') else ''}padding:3mm;display:flex;flex-direction:column;justify-content:space-between">
            <span style="color:{fg};font-size:13pt;font-weight:620;letter-spacing:-.02em">Aa Crédito</span><span style="color:{fg};font-size:7pt">Texto de 10 pt para leitura</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center"><span class="tn" style="font-size:8pt;font-weight:650">{fmt(r)}:1</span>{badge(ok, t)}</div>
          <span class="cap">{n}</span></div>'''
    b = f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12mm">
      <div><div class="eb">Combinações</div><div class="t1" style="font-size:24pt">Pares de fundo e texto</div></div>
      <p class="cap" style="max-width:116mm">Critério de contraste calculado (WCAG 2.x): <b>Preferencial</b> ≥ 7:1 (AAA); <b>Permitido</b> ≥ 4,5:1 (AA para qualquer texto); <b>Só texto grande</b> ≥ 3:1 (a partir de 18 pt, ou 14 pt em negrito); <b>Evitar</b> abaixo de 3:1. Texto sobre Brasa é sempre Carbono.</p></div>
    <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:6mm 4.5mm;margin-top:7mm">{cells}</div>'''
    return page(24, 3, b)


def p24():
    rows = [("Tinta", "#231107", "Creme", "#F9F1ED"), ("Tinta", "#231107", "Papel", "#FFFFFF"), ("Tinta Suave", "#6B5548", "Creme", "#F9F1ED"),
            ("Brasa Tinta", "#9D430B", "Creme", "#F9F1ED"), ("Brasa Profunda", "#C4560F", "Creme", "#F9F1ED"), ("Brasa", "#F46C00", "Creme", "#F9F1ED"),
            ("Tinta Clara", "#F6ECE6", "Carbono Profundo", "#0C0500"), ("Tinta Clara Suave", "#B09A8D", "Carbono Profundo", "#0C0500"),
            ("Brasa Alta", "#FF8C45", "Carbono Profundo", "#0C0500"), ("Carbono Profundo", "#0C0500", "Brasa", "#F46C00"),
            ("Branco", "#FFFFFF", "Brasa", "#F46C00"), ("Branco", "#FFFFFF", "Etapa da esteira", "#F6853A")]
    yn = lambda v: f'<span style="font-weight:700;color:{"#231107" if v else "#9D430B"}">{"Passa" if v else "Reprova"}</span>'
    tr = ""
    for fn, f, bn, bg in rows:
        r = cr(f, bg)
        tr += f'<tr><td><span class="chip" style="background:{f}"></span> {fn}</td><td><span class="chip" style="background:{bg}"></span> {bn}</td><td class="r"><b>{fmt(r)}:1</b></td><td>{yn(r>=4.5)}</td><td>{yn(r>=3)}</td><td>{yn(r>=3)}</td></tr>'
    b = f'''<div class="g12">
      <div style="grid-column:1/8">
        <div class="eb">Acessibilidade</div><div class="t1" style="font-size:22pt">Contraste calculado, não estimado</div>
        <table class="tb mt2"><thead><tr><th>Texto / elemento</th><th>Fundo</th><th class="r">Contraste</th><th>Texto normal 4,5:1</th><th>Texto grande 3:1</th><th>Componente 3:1</th></tr></thead><tbody>{tr}</tbody></table>
        <p class="cap mt1">Referência: WCAG nível AA. Luminância relativa sRGB calculada a partir dos valores HEX deste manual.</p></div>
      <div style="grid-column:8/13">
        <div class="t3">Cores funcionais de interface</div>
        <p class="mt1" style="font-size:8.8pt">O DESIGN.md documenta apenas o estado de <b>foco</b>: borda Brasa e anel de 3 px em Brasa a 14%. Estados de sucesso, alerta e erro <b>não têm tokens definidos</b> e não fazem parte da paleta institucional.</p>
        <div class="card mt2" style="padding:4mm">
          <div style="font-size:6pt;font-weight:700;letter-spacing:.2em;color:var(--ts)">E-MAIL CORPORATIVO</div>
          <div style="margin-top:1.6mm;border:.35mm solid #F46C00;box-shadow:0 0 0 .8mm rgba(244,108,0,.14);border-radius:2.6mm;padding:2.2mm 3mm;font-size:8.4pt">nome@empresa</div>
          <div style="display:flex;gap:1.6mm;align-items:center;margin-top:2mm;color:#9D430B;font-size:7.6pt;font-weight:600">{icon("alerta", 3.4, "#9D430B")} Informe um e-mail corporativo válido.</div></div>
        <p class="cap mt1">Foco documentado. A mensagem de erro é demonstrativa: ícone e texto carregam o sentido, nunca só a cor.</p>
        <p class="note mt3"><b>Divergências registradas no DESIGN.md:</b> o botão primário aparece com texto Carbono nos tokens e com texto branco na descrição do componente; as etapas da esteira (#F6853A) levam texto branco a 2,52:1; e o token Brasa ainda está em #F47626 e deve passar a #F46C00. Este manual adota a Regra do Carbono sobre Brasa nos dois casos. <b>Recomendação para validação:</b> definir tokens de sucesso, alerta e erro com contraste mínimo de 4,5:1 sobre Creme e Papel.</p></div></div>'''
    return page(25, 3, b)


PAGES = [p19, p20, p_grad, p21, p22, p23, p24]
