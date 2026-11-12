import pikepdf
S="/tmp/claude-0/-home-claude/1ca3015c-558b-533c-93f8-815ce1894cd1/scratchpad"
src=f"{S}/out/Manual_de_Identidade_Visual_UY3.pdf"
pdf=pikepdf.open(src, allow_overwriting_input=True)
W,H=841.8898,595.2756
for pg in pdf.pages:
    x0,y0,x1,y1=[float(v) for v in pg.MediaBox]
    sx,sy=W/(x1-x0),H/(y1-y0)
    pg.contents_add(pikepdf.Stream(pdf,f"q {sx:.6f} 0 0 {sy:.6f} 0 0 cm".encode()),prepend=True)
    pg.contents_add(pikepdf.Stream(pdf,b"Q"),prepend=False)
    for k in ('/CropBox','/TrimBox','/BleedBox','/ArtBox'):
        if k in pg.obj: del pg.obj[k]
    pg.MediaBox=[0,0,W,H]
pdf.Root.Lang=pikepdf.String("pt-BR")
with pdf.open_metadata() as m:
    m['dc:title']="Manual de Identidade Visual · UY3"
    m['dc:creator']=["UY3 · Gestão da marca"]
    m['dc:description']="Manual de Identidade Visual da UY3 Sociedade de Crédito Direto S.A. Versão 1.0, novembro de 2026."
    m['dc:language']=["pt-BR"]
pdf.docinfo['/Title']="Manual de Identidade Visual · UY3"
pdf.docinfo['/Subject']="Versão 1.0 · Novembro 2026"
pdf.docinfo['/Author']="UY3 · Gestão da marca"
pdf.save(src)
print("ok")
