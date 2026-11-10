---
title: Planejamento e organização
description: Perfil de dificuldade de funções executivas — planejar, seguir etapas em ordem, tomar decisões e corrigir o rumo quando algo dá errado.
---

<p class="claro-badge tone-p" data-letter="5">Perfil 5 de 6</p>

# Planejamento e organização

**Dificuldade para planejar uma tarefa, seguir etapas em ordem, escolher entre opções e corrigir o rumo quando algo dá errado.** Na literatura, essas habilidades se chamam *funções executivas*.

Princípios mais ligados: [L · Leveza](../principios/leveza.md) e [O · Orientação](../principios/orientacao.md).

## Na prática

- A pessoa começa sem saber do que vai precisar — e trava na etapa 4.
- Muitas opções sem uma recomendação paralisam a decisão.
- Um erro sem explicação vira um beco sem saída.
- Medo de errar de forma irreversível faz a pessoa não concluir.

!!! example "Uma cena"
    Bruna começa a renovar a matrícula, chega à etapa 4 e descobre que precisa de um documento que não está com ela. Não há aviso de que o que ela preencheu fica salvo, então ela fecha a página — e precisa recomeçar do zero no dia seguinte.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Não saber o que vai precisar | "Antes de começar": lista de documentos e tempo estimado |
| Não saber quantas etapas faltam | Etapas numeradas, com a atual destacada |
| Muitas opções equivalentes | Poucas opções, com uma recomendada e as consequências de cada uma |
| Erro genérico | Erro que diz o que aconteceu e como resolver |
| Medo de ação irreversível | Revisão antes de enviar e opção de desfazer |
| Travou e não sabe o que fazer | Ajuda humana fácil de achar |

## Em código

### 1. "Antes de começar"

```html
<section aria-labelledby="antes">
  <h2 id="antes">Antes de começar</h2>
  <p>Leva cerca de 10 minutos. Você pode parar e continuar depois: salvamos tudo.</p>
  <p>Tenha em mãos:</p>
  <ul>
    <li>Documento com foto (RG ou CNH)</li>
    <li>Comprovante de residência dos últimos 3 meses</li>
  </ul>
  <a class="botao" href="/matricula/etapa-1">Começar</a>
</section>
```

### 2. Etapas visíveis

```html
<nav aria-label="Etapas da matrícula">
  <ol class="etapas">
    <li><a href="/matricula/etapa-1">Dados do estudante</a></li>
    <li aria-current="step">Endereço</li>
    <li>Documentos</li>
    <li>Revisão</li>
  </ol>
</nav>
<h1>Endereço <span class="progresso">(etapa 2 de 4)</span></h1>
```

### 3. Erro que diz como resolver

```html
<label for="cpf">CPF</label>
<input id="cpf" name="cpf" inputmode="numeric" aria-describedby="cpf-erro">
<p id="cpf-erro" class="erro"></p>
```

```js
function validarCPF(campo) {
  const digitos = campo.value.replace(/\D/g, '');
  const erro = document.querySelector('#cpf-erro');

  if (digitos.length !== 11) {
    campo.setAttribute('aria-invalid', 'true');
    // O que aconteceu + como resolver. O valor digitado continua no campo.
    erro.textContent = `O CPF tem 11 números. Você digitou ${digitos.length}.`;
    return false;
  }
  campo.removeAttribute('aria-invalid');
  erro.textContent = '';
  return true;
}
```

### 4. Revisar antes, desfazer depois

```html
<h2>Revise antes de enviar</h2>
<dl class="revisao">
  <dt>Endereço</dt>
  <dd>Rua A, 100 — Fortaleza/CE <a href="/matricula/etapa-2">Editar endereço</a></dd>
  <dt>Documentos</dt>
  <dd>RG, comprovante de residência <a href="/matricula/etapa-3">Editar documentos</a></dd>
</dl>
<button type="submit">Enviar matrícula</button>

<div role="status" id="aviso"></div>
```

```js
// Em vez de "Tem certeza?", mova para a lixeira e ofereça desfazer
function moverParaLixeira(item) {
  api.moverParaLixeira(item.dataset.id);
  item.hidden = true;

  const desfazer = document.createElement('button');
  desfazer.type = 'button';
  desfazer.textContent = 'Desfazer';
  desfazer.addEventListener('click', async () => {
    await api.restaurar(item.dataset.id);
    item.hidden = false;
    aviso.textContent = `"${item.dataset.nome}" voltou para a lista.`;
  });

  aviso.replaceChildren(`"${item.dataset.nome}" foi para a lixeira. `, desfazer);
}
```

## Base normativa

**COGA** — Objetivo 1 (entender como usar), Objetivo 4 (evitar e corrigir erros) e Objetivo 7 (ajuda):
4.2.4 Cada etapa clara · 4.5.7 Instruções passo a passo · 4.6.4 Informar o necessário para se preparar · 4.6.2 Caminhos críticos curtos · 4.5.2 Deixar voltar · 4.5.5 Desfazer erros com facilidade · 4.8.3 Dizer resultados e desvantagens de cada opção · 4.8.1 Ajuda humana.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 3.3.1 Identificação do erro | A | Erro descrito em texto |
| 3.3.3 Sugestão de erro | AA | Dizer como corrigir |
| 3.3.4 Prevenção de erros (jurídico, financeiro, dados) | AA | Revisar, confirmar ou desfazer |
| 4.1.3 Mensagens de status | AA | Resultados anunciados sem mover o foco |
| 2.4.8 Localização | AAA | Saber onde está no processo |
| 3.3.5 Ajuda | AAA | Ajuda contextual disponível |
| 3.3.6 Prevenção de erros (todos) | AAA | Revisar ou desfazer qualquer envio |

## Como testar

- [ ] Leia só a primeira tela. Dá para saber do que você vai precisar e quanto tempo leva?
- [ ] Erre de propósito em cada campo. Cada mensagem diz como resolver?
- [ ] Peça a alguém de fora que faça a tarefa sem ajuda. Conte quantas vezes a pessoa volta atrás ou hesita.
- [ ] Existe alguma ação sem revisão e sem desfazer?
