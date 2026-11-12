# Relatório técnico · Manual de Identidade Visual UY3

**Edição:** Versão 1.0 · Novembro 2026
**Entregável:** `Manual_de_Identidade_Visual_UY3.pdf`, com 41 páginas A4 paisagem (297 × 210 mm)
**Data do relatório:** 12/11/2026 (revisado no mesmo dia: cor Pantone 1505 C, degradê e repositório)

Este relatório registra de onde vem cada regra do manual, o que foi verificado e o que ainda depende de aprovação. Ele acompanha o PDF e não o substitui.

---

## 1. Arquivos analisados

| Arquivo | Origem | Uso no manual |
|---|---|---|
| `logo UY3-.pdf` | Projeto UY3 Marketing | Fonte de verdade do desenho do logotipo |
| Especificação de cor (print enviado em 12/11/2026) | Gestão da marca | Pantone 1505 C (cor primária) e 173 C (degradê) |
| `DESIGN.md` | Projeto UY3 Marketing | Paleta, tipografia, componentes, regras nomeadas |
| `UY3_Knowledge_Base_2026-08-13.md` | Projeto | Razão social, CNPJ, missão, tom de voz |
| `UY3_Tecnologia_Site.md` | Projeto | Textos de referência (banco de frases do site) |
| `260813_UY3_MngmntPresentation.pptx` | Projeto | Contexto: esteira de crédito. **Nenhum dado interno publicado** |
| `prompt_manual_identidade_visual_scd.md` | Anexo da conversa | Roteiro editorial e critérios de validação |
| PDFs de referência (BNP Paribas, Deutsche Bank etc.) | **Não fornecidos** | A direção editorial seguiu a descrição do prompt |

## 2. Auditoria do logotipo

- **Arquivo:** Adobe Illustrator 29.5 (Windows), PDF/X-4, criado em 14/05/2025, com uma página A4 e uma única forma vetorial composta.
- **Preenchimento:** DeviceCMYK **0 / 66,8 / 96,5 / 0**. Intenção de saída: **CGATS TR 001** (SWOP).
- **Caixa delimitadora:** 622,43 × 329,32 pt. Proporção **1,890 : 1**.
- **Medidas observadas:** haste do U 55,71 un.; haste do Y 55,41 un.; módulo X ≈ 55,6 un. (16,9% da altura). Todos os cortes diagonais estão a 45°. Intervalos entre caracteres de 0,62X a 0,65X.
- **Versões existentes:** apenas a assinatura horizontal em Brasa. Por decisão da gestão da marca, não haverá versão vertical, reduzida, símbolo isolado nem descritor.
- **Integridade:** o SVG extraído foi comparado ao original rasterizado a 144 dpi, com 0,116% de pixels divergentes, todos na borda de antialiasing.

### Cor do logotipo (atualizada em 12/11/2026)
O vetor original está em CMYK 0 / 66,8 / 96,5 / 0, equivalente a #F47626 pelo perfil CGATS TR 001, o mesmo valor do token Brasa do `DESIGN.md`. A gestão da marca definiu uma nova especificação: **Pantone 1505 C · CMYK 0 / 71 / 100 / 0 · RGB 244 108 0 · #F46C00**. O manual e os arquivos oficiais do logotipo da v1.0 usam os novos valores. O arquivo original e os tokens do site ficam desatualizados e devem ser substituídos.

## 3. Matriz de procedência

| Elemento | Valor ou regra | Fonte | Situação | Observação |
|---|---|---|---|---|
| Logotipo | Assinatura horizontal “UY3” | `logo UY3-.pdf` | **Confirmado** | Reproduzido do vetor, sem redesenho |
| Versão negativa | Mesmo vetor em #FFFFFF | Decisão da gestão da marca (12/11/2026) | **Confirmado nesta edição** | Recoloração autorizada |
| Versão monocromática | Mesmo vetor em #0C0500 | Decisão da gestão da marca (12/11/2026) | **Confirmado nesta edição** | Única versão sobre Brasa |
| Vertical, reduzida, símbolo | — | Decisão da gestão da marca (12/11/2026) | **Não existirão** | Removidos do manual; letras isoladas não podem ser usadas como ícone |
| Cor principal | Brasa · Pantone 1505 C · CMYK 0/71/100/0 · RGB 244 108 0 · #F46C00 | Especificação da gestão da marca (12/11/2026) | **Confirmado** | Substitui #F47626 e o CMYK 0/66,8/96,5/0 |
| Composição degradê | Linear de 1505 C (#F46C00) a 173 C (#D04D27 · CMYK 13/84/100/3 · RGB 208 77 39) | Especificação da gestão da marca (12/11/2026) | **Confirmado** | Regras de uso recomendadas (página 21) |
| Pantone 173 C isolado | — | — | Não é cor de apoio | Só como ponto final do degradê |
| Brasa Lavada | rgba(244,108,0,.12) | `DESIGN.md`, atualizada para a nova Brasa | **Inferido** | Mesma opacidade do token original |
| Neutros e variações da Brasa | 15 tokens HEX/RGBA | `DESIGN.md` | **Confirmado** | Carbono Claro e Creme Fechado sem uso definido |
| CMYK dos demais tons | Valores indicativos | Calculado (FOGRA39, colorimétrico relativo) | **Inferido** | Sujeito a perfil ICC e prova de cor |
| Contrastes | Todos os valores publicados | Calculado (WCAG 2.x, sRGB) | **Confirmado por cálculo** | Ver seção 5 |
| Tipografia | Inter, família única; pesos 400/600/620/700; cv05, cv11, ss03 | `DESIGN.md` | **Confirmado** | Inter 4.1, OFL 1.1, incorporada |
| Fallback e mono | Segoe UI/system-ui; ui-monospace só na janela de código | `DESIGN.md` | **Confirmado** | — |
| Hierarquia digital | Display, Headline, Title, Subtitle, Lede, Body, Label, Code | `DESIGN.md` | **Confirmado** | — |
| Hierarquia A4 | Tamanhos em pt para impressão | Este manual | **Recomendado** | — |
| Componentes, raios, sombras, ícones, esteira | Casca dupla, pill, traço 1,5–1,8 etc. | `DESIGN.md` | **Confirmado** | — |
| Grid de documentos | 12 colunas, margens 16/22/17 mm | Este manual | **Recomendado** | O site usa container centrado |
| Área de proteção | 1X (haste do U) em todos os lados | Este manual | **Recomendado** | O arquivo original não define |
| Tamanho mínimo | 6 mm impresso; 24 px digital (32 px recomendado) | Teste de rasterização do original | **Recomendado / provisório** | Validar em prova de impressão |
| Assinatura conjunta | 2X de distância, separador de 1 px a 25% | Este manual | **Recomendado** | — |
| Pares de personalidade | Experiente / técnica / ágil / tecnológica / regulada | Guia de Tom de Voz (via base de conhecimento) | **Confirmado** | A tradução visual é direção de arte |
| Palavras de direção | Precisão, Consistência, Calor contido | Este manual | **Recomendado** | Não são valores institucionais |
| Razão social e CNPJ | UY3 Sociedade de Crédito Direto S.A. · 39.587.424/0001-30 | Site institucional (base de conhecimento) | **Confirmado** | Usados só no papel timbrado |
| Missão | Descentralizar e democratizar o acesso ao crédito no Brasil | Site institucional | **Confirmado** | — |
| Restrições de imagem e linguagem | Sem dinheiro como imagem; não usar “banco”; não expor stack | Diretrizes editoriais do projeto | **Confirmado** | — |
| Cores de sucesso, alerta e erro | — | Ausentes no `DESIGN.md` | **A definir** | Recomendação: mínimo de 4,5:1 sobre Creme e Papel |
| Fotografia | Princípios e molduras conceituais | `DESIGN.md` + projeto | **Recomendado** | Sem banco de imagens aprovado |

## 4. Divergências encontradas no `DESIGN.md`

0. **Token Brasa desatualizado.** O `DESIGN.md` define a Brasa como #F47626 e a Brasa Lavada como rgba(244,118,38,.12). Ambos devem passar à nova especificação (#F46C00).
1. **Texto do botão primário.** Os tokens definem texto Carbono Profundo; a descrição do componente fala em “texto branco”, e o hover também usa branco. O manual adota **Carbono sobre Brasa** (branco sobre Brasa = 3,00:1, reprova AA para texto comum).
2. **Etapas da esteira (`rail-step`).** O fundo #F6853A com texto branco dá **2,52:1** e reprova. O manual mostra a esteira com texto Carbono.
3. **Eyebrow.** O token usa Brasa Profunda sobre Brasa Lavada (3,56:1 sobre Creme, reprova para texto de 10 px); a descrição indica Brasa Tinta (5,15:1, passa). O manual adota **Brasa Tinta**.
4. **Contraste declarado.** O `DESIGN.md` informa “Carbono sobre Brasa = 6,24:1”. Com a nova Brasa, o cálculo dá 6,74:1 com Carbono Profundo, 6,52:1 com Carbono e 6,05:1 com Tinta. A regra se mantém válida; o número deve ser corrigido no documento.

## 5. Contrastes calculados (amostra)

| Par | Contraste | AA texto normal |
|---|---|---|
| Tinta sobre Creme | 16,31:1 | Passa |
| Tinta Suave sobre Creme | 6,24:1 | Passa |
| Brasa Tinta sobre Creme | 5,81:1 | Passa |
| Brasa Profunda sobre Creme | 4,02:1 | Reprova (só texto grande) |
| Brasa sobre Creme | 2,69:1 | Reprova |
| Brasa sobre Papel | 3,00:1 | Reprova (só texto grande) |
| Brasa sobre Carbono Profundo | 6,74:1 | Passa |
| Brasa Alta sobre Carbono Profundo | 8,76:1 | Passa |
| Carbono Profundo sobre Brasa | 6,74:1 | Passa |
| Branco sobre Brasa | 3,00:1 | Reprova (só texto grande) |
| Carbono Profundo sobre 173 C (fim do degradê) | 4,60:1 | Passa |
| Branco sobre 173 C | 4,40:1 | Reprova |

Os logotipos são isentos dos critérios da WCAG, mas a Brasa sobre fundo claro fica no limite de 3:1 (Papel) ou abaixo (Creme). Por isso o manual exige os tamanhos mínimos e trata o Carbono como fundo de maior contraste.

## 6. Verificações realizadas no PDF final

- 41 páginas, todas com **841,89 × 595,28 pt (297 × 210 mm)**, conferidas página a página.
- Texto selecionável e pesquisável; PDF marcado (tagged); idioma pt-BR; título e metadados preenchidos.
- Fontes incorporadas como CID TrueType em subconjunto (Inter 400, 500, 600, 620, 650, 700 e 800, Display 620, Itálico e DejaVu Sans Mono para código). Nenhuma fonte Type 3.
- Logotipo vetorial em todas as páginas, a partir do path original, na nova cor #F46C00.
- Busca no HTML-fonte: o valor antigo #F47626 só aparece em duas menções textuais à especificação anterior.
- Numeração de rodapé conferida por extração de texto nas páginas 2 a 41; sumário sincronizado com a paginação.
- Verificação automática de vazamento: nenhum elemento ultrapassa a área útil.
- Revisão visual de todas as páginas a 72 dpi, com correção e nova exportação das páginas 4, 9, 10, 13, 14, 16, 18, 21, 26, 29, 32, 33, 35, 36, 37 e 38.

## 7. Limitações

- Os PDFs de referência de outras instituições não estavam disponíveis. Nenhum elemento deles foi usado.
- Não há banco de imagens aprovado. As páginas de fotografia usam molduras tonais rotuladas como conceituais.
- CMYK de cores além da Brasa e do Pantone 173 C é indicativo (FOGRA39). Os escuros resultam em pretos ricos com cobertura alta e precisam de validação da gráfica.
- O PDF foi preparado para tela. Uma versão de impressão (sangria, marcas de corte, perfil do fornecedor) não foi gerada.
- O peso 620 depende da Inter variável. Em Office e e-mail, usar SemiBold 600.

## 8. Propostas para validação da gestão da marca

1. Área de proteção de 1X e tamanhos mínimos provisórios (6 mm / 24 px).
2. Regras de assinatura conjunta (2X e separador).
3. Grid de 12 colunas e tamanhos tipográficos para A4.
4. Tokens funcionais de sucesso, alerta e erro.
5. Correção das divergências do `DESIGN.md` (seção 4), começando pelo token Brasa.
6. Favicon: abaixo de 24 px o logotipo fica sob o mínimo testado. Como não haverá símbolo, definir o tratamento desse caso de exceção.
7. Banco de imagens e prova de cor do Pantone 1505 C e da quadricromia equivalente.
8. Regras de uso da composição degradê (página 21).
9. Versão monocromática para impressão: o Carbono em CMYK resulta em preto rico (66/66/51/100); avaliar a necessidade de uma versão 100% K.

## 9. Ativos entregues

- `Manual_de_Identidade_Visual_UY3.pdf`
- Logotipo em SVG: principal Brasa, negativo branco e mono Carbono
- Logotipo em PDF: principal em RGB, CMYK e Pantone 1505 C (cor especial com alternativa CMYK), negativo em RGB, mono em RGB e CMYK
- Logotipo em PNG transparente, com 2000 px de largura, nas três cores
- Repositório `agenciatweed/brand-guidelines-uy3` com o manual, os ativos, os tokens, a fonte Inter e o arquivo-fonte
- O arquivo original `logo UY3-.pdf` (cor anterior) não foi redistribuído.
