---
title: R · Ritmo
description: A pessoa controla o tempo — sem cronômetro, sem carrossel automático, sem autoplay, sem sessão que expira em silêncio.
---

<p class="claro-badge tone-r" data-letter="R">Princípio 4 de 5</p>

# Ritmo

**A pessoa usuária controla o tempo.** Sem cronômetro, sem carrossel automático, sem *autoplay*, sem sessão que expira em silêncio.

## O que é

Cada pessoa lê, decide e digita numa velocidade. Quem tem dislexia lê mais devagar. Quem tem TDAH perde o foco quando algo se move. Quem é mais velho processa com mais calma. Quando o produto impõe o tempo, ele exclui exatamente essas pessoas — e qualquer um que foi interrompido no meio da tarefa.

## Faça / Evite

=== "Faça"

    - Avise **antes** de a sessão expirar e ofereça mais tempo com um clique.
    - Diga no início quanto tempo a sessão dura.
    - Guarde o que foi preenchido se a sessão cair.
    - Dê botão de pausa a tudo que se move por mais de 5 segundos.
    - Respeite `prefers-reduced-motion`.
    - Deixe a pessoa avançar quando quiser — não por tempo.

=== "Evite"

    - Sessão de 5 minutos que cai sem aviso.
    - Carrossel que troca sozinho sem botão de pausa.
    - Vídeo ou áudio que começa a tocar sozinho.
    - Contagem regressiva de "oferta" para pressionar decisão.
    - Mensagem de sucesso que some antes de a pessoa terminar de ler.
    - Redirecionar automaticamente depois de alguns segundos.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">Sessão cai em 5 minutos sem aviso</span> | **Aviso aos 4 minutos + botão "Preciso de mais tempo"** |
| <span class="claro-before">Carrossel de banners troca a cada 3 segundos</span> | **Banners estáticos, ou carrossel parado com setas** |
| <span class="claro-before">"Sucesso!" some em 2 segundos</span> | **Mensagem fica até a pessoa fechar ou seguir** |

## Em código

Aviso de sessão com tempo de sobra para responder (a WCAG pede pelo menos 20 segundos):

```html
<dialog id="aviso-sessao" aria-labelledby="aviso-titulo">
  <h2 id="aviso-titulo">Sua sessão vai terminar em 1 minuto</h2>
  <p>O que você preencheu está salvo. Quer continuar?</p>
  <button id="mais-tempo">Preciso de mais tempo</button>
  <button id="sair">Sair agora</button>
</dialog>
```

```js
const DURACAO = 5 * 60 * 1000;      // sessão de 5 min
const AVISO_ANTES = 60 * 1000;      // avisa 1 min antes
const dialogo = document.querySelector('#aviso-sessao');
let timerAviso, timerFim;

function encerrarComRascunho() {
  // O rascunho já foi salvo (veja Apoio à memória).
  // Leve a pessoa ao login dizendo que nada se perdeu.
  location.assign('/entrar?motivo=sessao-expirada');
}

function iniciarSessao() {
  clearTimeout(timerAviso);
  clearTimeout(timerFim);
  timerAviso = setTimeout(() => dialogo.showModal(), DURACAO - AVISO_ANTES);
  timerFim = setTimeout(encerrarComRascunho, DURACAO);
}

document.querySelector('#mais-tempo').addEventListener('click', async () => {
  await fetch('/api/sessao/renovar', { method: 'POST' });
  dialogo.close();
  iniciarSessao();
});

iniciarSessao();
```

E nada de movimento para quem pediu menos movimento:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
  }
}
```

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 2.2.1 Tempo ajustável (*Timing Adjustable*) | A | Desligar, ajustar ou estender limites de tempo |
| 2.2.2 Pausar, parar, ocultar (*Pause, Stop, Hide*) | A | Controle sobre conteúdo que se move ou atualiza |
| 2.2.3 Sem tempo (*No Timing*) | AAA | Tempo não é parte essencial da tarefa |
| 2.2.5 Nova autenticação (*Re-authenticating*) | AAA | Dados preservados ao logar de novo |
| 2.2.6 Tempo esgotado (*Timeouts*) | AAA | Avisar quanto tempo de inatividade causa perda de dados |
| 1.4.2 Controle de áudio (*Audio Control*) | A | Parar áudio que toca sozinho |

**COGA:** Objetivo 5 (manter o foco) e Objetivo 8 (adaptação e personalização).

## Como verificar

- [ ] Deixe a tela parada por 10 minutos. O que acontece?
- [ ] Tudo que se move tem botão de pausa?
- [ ] Com "reduzir movimento" ativado no sistema, as animações param?
- [ ] Mensagens importantes ficam na tela até a pessoa agir?

Itens completos no [checklist](../checklist.md#r-ritmo).
