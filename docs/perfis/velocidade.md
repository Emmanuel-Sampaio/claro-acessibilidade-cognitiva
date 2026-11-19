---
title: Velocidade de processamento
description: Perfil de dificuldade de velocidade de processamento — precisar de mais tempo para ler, entender, decidir e responder.
---

<p class="claro-badge tone-p" data-letter="6">Perfil 6 de 9</p>

# Velocidade de processamento

**Precisar de mais tempo para ler, entender, decidir e responder.** A pessoa chega lá — só que no próprio ritmo.

Princípio mais ligado: [R · Ritmo](../principios/ritmo.md).

## Na prática

- A sessão expira enquanto a pessoa ainda está lendo.
- A mensagem de sucesso some antes de ela terminar de ler.
- O vídeo fala rápido demais e não tem transcrição.
- A página "pula" enquanto carrega e o botão muda de lugar na hora do toque.

!!! example "Uma cena"
    Fátima lê cada opção com calma antes de escolher. Na tela de pagamento, enquanto ela confere o valor pela segunda vez, a sessão expira sem aviso e o carrinho é esvaziado.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Sessão que expira em silêncio | Aviso antes, com "Preciso de mais tempo" |
| Mensagem que some sozinha | Mensagem que fica até a pessoa fechar ou seguir |
| Redirecionamento "em 3… 2… 1…" | Botão que a pessoa toca quando quiser |
| Vídeo rápido, sem texto | Legenda, transcrição e controle de velocidade |
| Layout que pula ao carregar | Espaço reservado para imagens e avisos |
| Contagem regressiva de oferta | Sem pressão de tempo artificial |

## Em código

### 1. Aviso antes de a sessão expirar

A WCAG pede pelo menos 20 segundos para a pessoa pedir mais tempo. Avisar 1 minuto antes é mais generoso.

```html
<dialog id="aviso-sessao" aria-labelledby="aviso-titulo">
  <h2 id="aviso-titulo">Sua sessão vai terminar em 1 minuto</h2>
  <p>O que você preencheu está salvo. Quer continuar?</p>
  <button id="mais-tempo">Preciso de mais tempo</button>
  <button id="sair">Sair agora</button>
</dialog>
```

```js
const DURACAO = 15 * 60 * 1000;   // sessão de 15 min
const AVISO_ANTES = 60 * 1000;    // avisa 1 min antes
const dialogo = document.querySelector('#aviso-sessao');
let timerAviso, timerFim;

function encerrarComRascunho() {
  // O rascunho já foi salvo (veja o perfil Memória).
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

### 2. Mensagem que espera a pessoa

```html
<div class="aviso aviso--sucesso" role="status">
  <p>Cadastro salvo. Próximo passo: enviar documentos.</p>
  <button type="button" class="fechar">Fechar aviso</button>
</div>
```

```js
// Sem setTimeout para esconder. Quem fecha é a pessoa.
document.querySelectorAll('.aviso .fechar').forEach((botao) => {
  botao.addEventListener('click', () => botao.closest('.aviso').remove());
});
```

### 3. Vídeo no ritmo de quem assiste

```html
<video controls preload="metadata" id="video-tutorial">
  <source src="tutorial.mp4" type="video/mp4">
  <track kind="captions" src="tutorial.pt.vtt" srclang="pt-BR" label="Português" default>
</video>

<div role="group" aria-label="Velocidade do vídeo">
  <button type="button" data-velocidade="0.75">Mais devagar</button>
  <button type="button" data-velocidade="1">Normal</button>
</div>

<details>
  <summary>Ler a transcrição</summary>
  <p><!-- texto completo do vídeo, dividido em parágrafos curtos --></p>
</details>
```

```js
const video = document.querySelector('#video-tutorial');
document.querySelectorAll('[data-velocidade]').forEach((botao) => {
  botao.addEventListener('click', () => {
    video.playbackRate = Number(botao.dataset.velocidade);
  });
});
```

### 4. Nada muda de lugar enquanto carrega

```html
<!-- Largura e altura reservam o espaço antes de a imagem chegar -->
<img src="produto.jpg" width="640" height="480" alt="Liquidificador branco de 2 litros">

<p role="status" class="carregando">Carregando seus pedidos…</p>
```

```css
img { max-width: 100%; height: auto; }

/* Reserve o espaço de avisos e anúncios para o conteúdo não pular */
.carregando, .area-aviso { min-height: 3rem; }
```

## Base normativa

**COGA** — Objetivo 4 (evitar erros) e Objetivo 8 (adaptação):
4.5.9 Evitar perda de dados e tempo esgotado · 4.9.1 A pessoa controla quando o conteúdo se move · 4.5.1 Controles e conteúdo não se movem sem aviso · 4.5.10 Dar retorno · 4.3.5 Dividir mídias em partes.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 2.2.1 Tempo ajustável | A | Desligar, ajustar ou estender limites de tempo |
| 2.2.2 Pausar, parar, ocultar | A | Controle sobre o que se move ou atualiza |
| 1.2.2 Legendas (gravadas) | A | Legenda em vídeos |
| 3.2.2 Em entrada | A | Nada muda de contexto só por preencher um campo |
| 2.2.3 Sem tempo | AAA | O tempo não é parte essencial da tarefa |
| 2.2.5 Nova autenticação | AAA | Dados preservados ao entrar de novo |
| 2.2.6 Tempo esgotado | AAA | Avisar quanto tempo de inatividade causa perda de dados |

## Como testar

- [ ] **Teste da calma:** faça a tarefa deixando cada tela parada por 2 minutos. Algo expira, some ou muda?
- [ ] No DevTools, simule rede e processador lentos. Algum botão muda de lugar enquanto a página carrega?
- [ ] Assista aos vídeos a 0,75x e com legenda. Existe transcrição?
- [ ] Procure `setTimeout` que esconde mensagens ou redireciona a página.
