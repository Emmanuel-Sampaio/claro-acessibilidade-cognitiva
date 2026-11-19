---
title: Atenção
description: Perfil de dificuldade de atenção — manter o foco, filtrar distrações e retomar a tarefa depois de uma interrupção.
---

<p class="claro-badge tone-p" data-letter="1">Perfil 1 de 9</p>

# Atenção

**Dificuldade para manter o foco numa tarefa, filtrar o que não importa e retomar depois de uma interrupção.**

Princípios mais ligados: [L · Leveza](../principios/leveza.md) e [R · Ritmo](../principios/ritmo.md).

## Na prática

- Qualquer coisa que se mexe, pisca ou aparece puxa o olhar — e leva a tarefa junto.
- Depois de uma interrupção, a pessoa não sabe mais em que ponto estava.
- Telas com muitas opções do mesmo peso fazem a pessoa "passear" sem decidir.
- Fluxos longos perdem a pessoa no meio do caminho.

!!! example "Uma cena"
    Rita preenche um cadastro no ônibus. Um banner de oferta abre por cima do formulário. Ela fecha o banner, perde o campo em que estava e começa a digitar o endereço no campo errado.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Carrossel que troca sozinho | Conteúdo parado; se girar, botão de pausa e parada ao interagir |
| Pop-up, chat ou notificação no meio da tarefa | Adiar o que não é urgente até a tarefa terminar |
| Animações decorativas | Respeitar "reduzir movimento"; animar só o que dá retorno à ação |
| Mudança de etapa sem aviso | Levar o foco para o título da nova etapa |
| Voltar e não saber onde parou | Guardar o ponto e oferecer "Continuar de onde parei" |
| Várias ações com o mesmo destaque | Uma ação principal por tela |

## Em código

### 1. Carrossel que não compete com a tarefa

O melhor carrossel é o que não gira sozinho. Se precisar girar, ele para quando a pessoa interage, tem botão de pausa e respeita "reduzir movimento".

```html
<section class="carrossel" aria-roledescription="carrossel" aria-label="Novidades">
  <button type="button" class="pausar">Pausar</button>
  <div class="slides"><!-- slides --></div>
</section>
```

```js
const carrossel = document.querySelector('.carrossel');
const botao = carrossel.querySelector('.pausar');
const menosMovimento = matchMedia('(prefers-reduced-motion: reduce)').matches;
let timer = null;

function girar() {
  if (menosMovimento) return;                // não gira para quem pediu menos movimento
  timer = setInterval(proximoSlide, 7000);
  botao.textContent = 'Pausar';
}
function pausar() {
  clearInterval(timer);
  timer = null;
  botao.textContent = 'Continuar';
}

botao.addEventListener('click', () => (timer ? pausar() : girar()));
// Parou de girar quando a pessoa chega perto — e só volta se ela pedir
carrossel.addEventListener('mouseenter', pausar);
carrossel.addEventListener('focusin', pausar);

girar();
```

### 2. Adiar o que não é urgente

Avisos de marketing, dicas e "novidades" esperam a tarefa acabar. Só o que é urgente interrompe.

```html
<div role="status" id="avisos"></div>
```

```js
const form = document.querySelector('#cadastro');
const avisos = document.querySelector('#avisos');
const fila = [];
let emTarefa = false;

form.addEventListener('focusin', () => { emTarefa = true; });
form.addEventListener('submit', () => {
  emTarefa = false;
  fila.splice(0).forEach(mostrar);           // entrega o que ficou esperando
});

function notificar(texto, { urgente = false } = {}) {
  if (urgente || !emTarefa) mostrar(texto);
  else fila.push(texto);
}
function mostrar(texto) {
  avisos.textContent = texto;
}
```

### 3. Menos movimento

```css
/* Nada se mexe para quem pediu menos movimento */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Para todo mundo: animação só como resposta a uma ação, curta e sem loop */
.botao:active { transform: scale(0.98); transition: transform 80ms; }
```

### 4. Retomar depois da interrupção

Ao trocar de etapa, o foco vai para o título — a atenção chega onde está o conteúdo novo. E o produto guarda onde a pessoa parou.

```html
<h1 id="titulo-etapa" tabindex="-1">Endereço (etapa 2 de 4)</h1>
```

```js
function irParaEtapa(numero) {
  mostrarEtapa(numero);
  document.querySelector('#titulo-etapa').focus();
  try { localStorage.setItem('cadastro-etapa', String(numero)); } catch {}
}

// Ao voltar para a página
let etapaSalva = null;
try { etapaSalva = localStorage.getItem('cadastro-etapa'); } catch {}
if (etapaSalva) {
  document.querySelector('#retomar').hidden = false;   // "Continuar de onde parei (etapa 2)"
}
```

## Base normativa

**COGA** — Objetivo 5 (manter o foco) e Objetivo 8 (adaptação):
4.6.1 Limitar interrupções · 4.6.2 Caminhos críticos curtos · 4.6.3 Evitar conteúdo demais · 4.9.1 A pessoa controla quando o conteúdo se move · 4.5.1 Controles e conteúdo não se movem sem aviso · 4.3.4 Ações importantes fáceis de achar.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 2.2.2 Pausar, parar, ocultar | A | Pausa para o que se move por mais de 5 s |
| 1.4.2 Controle de áudio | A | Parar áudio que toca sozinho |
| 2.4.3 Ordem do foco | A | O foco segue uma ordem que faz sentido |
| 2.4.11 Foco não encoberto (mínimo) | AA | Nada cobre o elemento em foco |
| 2.2.4 Interrupções | AAA | Interrupções podem ser adiadas ou suprimidas |
| 2.3.3 Animação a partir de interações | AAA | Animações de interação podem ser desligadas |
| 3.2.5 Mudança mediante solicitação | AAA | Nada muda de contexto sem a pessoa pedir |

## Como testar

- [ ] **Teste da interrupção:** no meio da tarefa, saia por 2 minutos (atenda o celular) e volte. Você sabe onde estava?
- [ ] Aperte os olhos até a tela ficar borrada. A ação principal ainda é a coisa mais visível?
- [ ] Conte o que se move, pisca ou aparece sozinho. O número ideal é zero.
- [ ] Ative "reduzir movimento" no sistema e repita a tarefa.
