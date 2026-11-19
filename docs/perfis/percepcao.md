---
title: Percepção
description: Perfil de dificuldade de percepção — separar o que importa do fundo, achar um elemento na tela, perceber diferenças sutis e lidar com excesso de estímulo visual ou sonoro.
---

<p class="claro-badge tone-p" data-letter="7">Perfil 7 de 9</p>

# Percepção

**Dificuldade para separar o que importa do fundo, achar um elemento na tela, perceber diferenças sutis de cor ou forma e lidar com excesso de estímulo visual ou sonoro.** Aqui o problema não é enxergar ou ouvir, e sim processar o que chega.

Princípios mais ligados: [L · Leveza](../principios/leveza.md) e [C · Clareza](../principios/clareza.md).

## Na prática

- Letras muito juntas "se embaralham"; a linha seguinte se confunde com a atual.
- Um aviso que só muda de cor passa despercebido.
- Fundo com textura, imagem atrás do texto ou muitas caixas com bordas iguais escondem o que importa.
- Luz piscando, som de fundo e vídeo começando sozinho viram sobrecarga — a pessoa sai da página.
- Instruções do tipo "clique no botão verde à direita" não ajudam quem não percebe bem cor ou posição.

!!! example "Uma cena"
    Paulo preenche um formulário e erra o CEP. O campo fica com a borda vermelha, mais nada. Ele não percebe a diferença, clica em "Continuar" três vezes e acha que o site travou.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Informação só na cor | Cor **e** ícone **e** texto |
| Instrução por posição ou forma ("botão redondo à direita") | Instrução pelo nome do botão |
| Texto sobre imagem ou fundo com textura | Fundo liso, contraste de pelo menos 4,5:1 |
| Letras e linhas apertadas | Espaçamento que a pessoa pode aumentar sem quebrar o layout |
| Muitos blocos com o mesmo peso visual | Grupos claros, com espaço entre eles e título |
| Luz piscando, som de fundo, vídeo que começa sozinho | Nada pisca; som só quando a pessoa pede |

## Em código

### 1. Status que não depende só da cor

```html
<!-- Evite: só a borda vermelha -->
<input id="cep" class="erro">

<!-- Prefira: ícone + texto + ligação com o campo -->
<label for="cep">CEP</label>
<input id="cep" aria-invalid="true" aria-describedby="cep-erro">
<p id="cep-erro" class="mensagem mensagem--erro">
  <svg aria-hidden="true" focusable="false"><!-- ícone de alerta --></svg>
  O CEP tem 8 números. Você digitou 7.
</p>
```

```css
.mensagem--erro {
  color: #8a1c1c;                      /* contraste de 9:1 sobre branco */
  border-left: 4px solid currentColor; /* forma, além da cor */
  padding-left: 0.5rem;
  font-weight: 600;
}
```

### 2. Grupos que o olho separa sem esforço

```css
/* Espaço entre grupos maior que o espaço dentro do grupo */
.grupo { padding: 1rem; border: 1px solid #c7d5d9; border-radius: 8px; }
.grupo + .grupo { margin-top: 2rem; }
.grupo > * + * { margin-top: 0.75rem; }

/* Texto nunca sobre imagem ou textura */
.texto { background: #ffffff; color: #1b2528; }

/* Quem pede mais contraste no sistema recebe bordas mais fortes */
@media (prefers-contrast: more) {
  .grupo { border: 2px solid #1b2528; }
}
```

```html
<fieldset class="grupo">
  <legend>Endereço de entrega</legend>
  <!-- campos do endereço -->
</fieldset>
```

### 3. Espaçamento que pode crescer

A pessoa (ou uma extensão do navegador) deve poder aumentar o espaço entre letras, palavras e linhas sem que nada se sobreponha.

```css
.conteudo {
  line-height: 1.6;
  letter-spacing: 0.01em;
  word-spacing: 0.05em;
}
/* Caixas com texto crescem com o conteúdo: nunca altura fixa */
.cartao { min-height: 6rem; overflow: visible; }
```

### 4. Nada pisca, nada toca sozinho

```css
/* Evite qualquer coisa assim — mais de 3 piscadas por segundo pode até causar crises */
.alerta-piscando { animation: piscar 0.2s infinite; }

/* Prefira: destaque parado */
.alerta { border: 2px solid #b4461a; background: #fff4ee; }
```

```html
<!-- Vídeo começa parado, com legenda; sem música de fundo por cima da fala -->
<video controls preload="metadata">
  <source src="tutorial.mp4" type="video/mp4">
  <track kind="captions" src="tutorial.pt.vtt" srclang="pt-BR" label="Português" default>
</video>
```

## Base normativa

**COGA** — Objetivo 3 (conteúdo claro) e Objetivo 1 (entender o que as coisas são):
4.4.11 Conteúdo que não fica encoberto pelo fundo · 4.4.10 Espaço em branco · 4.2.3 Design visual consistente · 4.2.7 Ícones que ajudam · 4.3.3 Estrutura de página clara · 4.9.1 A pessoa controla quando o conteúdo se move.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 1.3.3 Características sensoriais | A | Instruções não dependem só de forma, posição ou som |
| 1.4.1 Uso de cor | A | Cor nunca é o único jeito de passar a informação |
| 2.3.1 Três flashes ou abaixo do limite | A | Nada pisca mais de 3 vezes por segundo |
| 1.4.3 Contraste (mínimo) | AA | Texto com contraste de pelo menos 4,5:1 |
| 1.4.11 Contraste não textual | AA | Bordas e ícones importantes com contraste de 3:1 |
| 1.4.12 Espaçamento de texto | AA | Aumentar espaçamentos não quebra o conteúdo |
| 1.4.7 Som de fundo baixo ou ausente | AAA | Fala gravada sem som de fundo competindo |
| 1.4.8 Apresentação visual | AAA | Linhas curtas, espaçamento adequado, cores ajustáveis |

**Literatura:** espaço extra entre letras e palavras aumentou em cerca de 20% a velocidade de leitura e reduziu os erros pela metade em crianças com dificuldade de leitura ([Zorzi et al., 2012](../literatura.md#leitura-e-linguagem)). Menos poluição visual e fonte e cores personalizáveis ajudaram na revisão de [Borg, Lantz e Gulliksen (2015)](../literatura.md#visao-geral-do-campo).

## Como testar

- [ ] **Teste em tons de cinza:** ative o filtro de tons de cinza do celular. Algum erro, status ou gráfico perdeu o sentido?
- [ ] Use um *bookmarklet* de espaçamento de texto (WCAG 1.4.12). Algo se sobrepõe ou some?
- [ ] Procure instruções que dependem de cor, forma ou posição.
- [ ] Abra a página com o som do computador ligado. Algo toca ou pisca sem você pedir?
