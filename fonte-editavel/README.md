# Fonte editável do manual

← [Voltar ao README principal](../README.md)

O manual foi diagramado em HTML/CSS e exportado para PDF pelo Chrome. Esta pasta contém tudo o que é necessário para editar e regenerar o documento.

| Caminho | Conteúdo |
|---|---|
| [`Manual_de_Identidade_Visual_UY3.html`](Manual_de_Identidade_Visual_UY3.html) | HTML-fonte completo (41 páginas A4 paisagem) |
| [`fonts/`](fonts/) | Instâncias estáticas da Inter 4.1 usadas no PDF (400, 500, 600, 620, 650, 700, 800, Display 620 e Itálico), sob a licença OFL |
| [`img/`](img/) | Rasterizações do logotipo usadas no teste de tamanho mínimo |
| [`build/`](build/) | Scripts Python que geram o HTML, o PDF e os arquivos do logotipo |

## Exportar o PDF

**Pelo navegador**
1. Abra o HTML no Google Chrome.
2. Imprima em papel A4, orientação paisagem, com margens nenhuma e “gráficos de fundo” ativado.

**Pela linha de comando**

```bash
google-chrome --headless=new --no-pdf-header-footer --export-tagged-pdf \
  --print-to-pdf=Manual_de_Identidade_Visual_UY3.pdf Manual_de_Identidade_Visual_UY3.html
```

## Scripts

- `base.py`: tokens, path vetorial do logotipo, ícones e CSS.
- `ch12.py`, `ch3.py`, `ch4.py`, `ch56.py`: páginas por capítulo.
- `build.py`: monta o HTML e imprime o PDF.
- `finalize.py`: ajusta o formato exato (297 × 210 mm) e os metadados.
- `overflow.py`: verifica se algum elemento escapa da área útil.
- `assets.py`: gera os logotipos em SVG, PDF (RGB, CMYK, Pantone) e PNG.

Os scripts usam o caminho absoluto do ambiente original na variável `S` de `base.py`. Ajuste esse caminho antes de rodar. Dependências: Python 3, `fonttools`, `pikepdf`, `playwright`, Google Chrome e `poppler-utils`.
