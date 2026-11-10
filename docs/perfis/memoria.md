---
title: Memória
description: Perfil de dificuldade de memória — guardar uma informação por alguns segundos (memória de trabalho) ou lembrar dela depois (memória de longo prazo).
---

<p class="claro-badge tone-p" data-letter="2">Perfil 2 de 6</p>

# Memória

**Dificuldade para guardar uma informação por alguns segundos enquanto faz outra coisa (memória de trabalho) ou para lembrar dela depois (memória de longo prazo).**

Princípios mais ligados: [A · Apoio à memória](../principios/apoio-a-memoria.md) e [O · Orientação](../principios/orientacao.md).

## Na prática

- Copiar um código de uma tela para outra é uma corrida contra o esquecimento.
- Senhas, perguntas de segurança e caminhos de menu viram barreira.
- A instrução que estava no campo some quando a pessoa começa a digitar — e ela não lembra o que era.
- Voltar uma etapa e encontrar tudo em branco faz a pessoa desistir.

!!! example "Uma cena"
    José recebe um código por SMS, troca de aplicativo para ler e volta. A página recarregou e o campo está vazio. Quando ele volta ao SMS, já não lembra se o código era 482913 ou 482193.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Colar bloqueado em senha e código | Colar sempre permitido; gerenciador de senhas funcionando |
| Instrução só no *placeholder* | Instrução visível, ligada ao campo |
| Mesmo dado pedido duas vezes | Reaproveitar o que já foi informado |
| Formulário que zera ao voltar | Rascunho salvo a cada alteração |
| Número de protocolo para anotar | Botão de copiar e opção de receber por e-mail |
| Login que depende de lembrar | Link de acesso por e-mail, chave de acesso (*passkey*) ou gerenciador de senhas |
| Ajuda que muda de lugar | Ajuda sempre no mesmo lugar |

## Em código

### 1. Deixe o navegador lembrar pela pessoa

```html
<label for="nome">Nome completo</label>
<input id="nome" autocomplete="name">

<label for="email">E-mail</label>
<input id="email" type="email" autocomplete="email">

<label for="senha">Senha</label>
<input id="senha" type="password" autocomplete="current-password">

<!-- O celular sugere o código do SMS e colar funciona.
     Nunca use onpaste="return false". -->
<label for="codigo">Código de 6 números enviado por SMS</label>
<input id="codigo" inputmode="numeric" autocomplete="one-time-code" maxlength="6">
```

### 2. Instrução que não some

```html
<label for="cpf">CPF</label>
<p id="cpf-ajuda" class="ajuda">Só os 11 números. Exemplo: 12345678901.</p>
<input id="cpf" name="cpf" inputmode="numeric" aria-describedby="cpf-ajuda">
```

### 3. Rascunho que sobrevive a voltar e recarregar

```js
const form = document.querySelector('#cadastro');
const CHAVE = 'cadastro-rascunho';

// Restaura o que a pessoa já tinha digitado
try {
  const salvo = JSON.parse(sessionStorage.getItem(CHAVE) || '{}');
  for (const [nome, valor] of Object.entries(salvo)) {
    if (form.elements[nome]) form.elements[nome].value = valor;
  }
} catch { /* sem armazenamento: segue normal */ }

// Salva a cada alteração (nunca senhas)
form.addEventListener('input', () => {
  const dados = {};
  for (const campo of form.elements) {
    if (campo.name && campo.type !== 'password') dados[campo.name] = campo.value;
  }
  try { sessionStorage.setItem(CHAVE, JSON.stringify(dados)); } catch {}
});
```

### 4. O sistema guarda o número, não a pessoa

```html
<p>Número do protocolo: <strong id="protocolo">2026-000123</strong></p>
<button type="button" data-copiar="protocolo">Copiar número</button>
<a href="/protocolo/2026-000123/enviar">Receber por e-mail</a>
<p role="status" id="copiado"></p>
```

```js
document.querySelectorAll('[data-copiar]').forEach((botao) => {
  botao.addEventListener('click', async () => {
    const texto = document.getElementById(botao.dataset.copiar).textContent;
    await navigator.clipboard.writeText(texto);
    document.querySelector('#copiado').textContent = 'Número copiado.';
  });
});
```

## Base normativa

**COGA** — Objetivo 6 (processos que não dependem da memória) e Objetivo 7 (ajuda e suporte):
4.7.1 Login que não depende de memória · 4.7.2 Login simples, em uma etapa · 4.7.5 Não depender de cálculo nem de decorar · 4.5.6 Rótulos claros e visíveis · 4.5.9 Evitar perda de dados e tempo esgotado · 4.8.7 Oferecer lembretes.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 3.3.7 Entrada redundante | A | Não pedir de novo o que já foi informado |
| 3.2.6 Ajuda consistente | A | Ajuda no mesmo lugar relativo |
| 3.3.2 Rótulos ou instruções | A | Instrução visível para entrada de dados |
| 3.3.8 Autenticação acessível (mínimo) | AA | Login sem teste cognitivo |
| 1.3.5 Identificar o propósito da entrada | AA | `autocomplete` em dados pessoais |
| 3.3.9 Autenticação acessível (aprimorado) | AAA | Sem exceção de reconhecimento de objetos |
| 2.2.5 Nova autenticação | AAA | Dados preservados ao entrar de novo |

## Como testar

- [ ] **Teste do intervalo:** pare no meio da tarefa por 10 minutos, faça outra coisa e volte. O que você precisou lembrar?
- [ ] Percorra o fluxo inteiro anotando cada dado pedido. Algum aparece duas vezes?
- [ ] Cole a senha e o código. Funciona? O gerenciador de senhas preenche?
- [ ] Volte uma etapa e recarregue a página. O que foi digitado continua lá?
