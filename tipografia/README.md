# Tipografia · Inter

A UY3 usa **uma família só: Inter**. Não existe fonte de display separada. A personalidade vem do tratamento: tracking negativo nos títulos, peso 620 e alternativas de glifo ativadas.

← [Voltar ao README principal](../README.md) · 📄 [Manual, capítulo 04 (páginas 26–31)](../manual/Manual_de_Identidade_Visual_UY3_v1.0.pdf)

## Links oficiais

- Site: <https://rsms.me/inter/>
- Repositório: <https://github.com/rsms/inter>
- Versão incluída neste repositório: **Inter 4.1** · <https://github.com/rsms/inter/releases/tag/v4.1>
- Licença: SIL Open Font License 1.1 ([`inter/LICENSE.txt`](inter/LICENSE.txt)). Permite uso comercial e incorporação em PDF.

## Arquivos em `inter/`

| Caminho | Conteúdo | Quando usar |
|---|---|---|
| [`InterVariable.ttf`](inter/InterVariable.ttf) · [`InterVariable-Italic.ttf`](inter/InterVariable-Italic.ttf) | Fonte variável (pesos 100–900 e tamanho óptico) | **Recomendado** em design e desktop: único formato com o peso 620 |
| [`Inter.ttc`](inter/Inter.ttc) | Coleção estática completa | Softwares sem suporte a fontes variáveis |
| [`web/`](inter/web/) | WOFF2 variáveis e estáticos + `inter.css` | Sites e aplicações |
| [`extras/otf`](inter/extras/otf/) · [`extras/ttf`](inter/extras/ttf/) | Estáticos individuais OTF e TTF | Office, ferramentas legadas |
| [`extras/woff-hinted`](inter/extras/woff-hinted/) | WOFF2 com hinting | Telas de baixa resolução no Windows |
| [`help.txt`](inter/help.txt) | Guia oficial de instalação | — |

## Pesos em uso

| Peso | Uso |
|---|---|
| 400 Regular | Corpo, lede, legendas, tabelas |
| 600 SemiBold | Title, subtitle, botões. Substitui o 620 onde não há fonte variável |
| 620 (variável) | Display e headline |
| 700 Bold | Label em caixa alta (tracking +0,22em) |

## Uso na web

```css
@font-face {
  font-family: "Inter";
  src: url("tipografia/inter/web/InterVariable.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}

body {
  font-family: Inter, "Segoe UI", system-ui, -apple-system, sans-serif;
  font-feature-settings: "cv05" 1, "cv11" 1, "ss03" 1;
}

h1 { font-weight: 620; letter-spacing: -0.045em; line-height: 1.03; }
td.valor { font-feature-settings: "tnum" 1; }
```

## Alternativas de glifo

| Recurso | Efeito |
|---|---|
| `cv11` | “a” de um andar |
| `cv05` | “l” com cauda |
| `ss03` | Aspas e vírgulas arredondadas |
| `tnum` | Numerais tabulares para tabelas e valores |
