---
title: Fadiga cognitiva
description: Perfil de fadiga cognitiva — energia mental que acaba antes da tarefa; precisa parar sem perder nada, decidir menos e saber quanto falta.
---

<p class="claro-badge tone-p" data-letter="9">Perfil 9 de 9</p>

# Fadiga cognitiva

**A energia mental acaba antes da tarefa.** A pessoa começa bem, mas a atenção, a memória e a paciência caem com o tempo — e, quando caem, os erros aumentam. Precisa parar sem perder nada, decidir menos e saber quanto falta.

Princípios mais ligados: [L · Leveza](../principios/leveza.md) e [A · Apoio à memória](../principios/apoio-a-memoria.md).

!!! note "Por que um perfil próprio"
    Fadiga cognitiva **amplifica** as outras dificuldades: quem está esgotado passa a ter dificuldade de atenção, de memória e de velocidade. Ela aparece depois de doenças, com dor crônica, sono ruim, sobrecarga de trabalho, cuidado de outra pessoa, luto — e varia ao longo do dia. A mesma pessoa que fez o cadastro de manhã pode não conseguir à noite.

## Na prática

- Formulários longos são abandonados no meio, e voltar significa recomeçar.
- Cada decisão (plano, opção, configuração) gasta energia que já está no fim.
- Sem saber quanto falta, a pessoa não sabe se vale a pena continuar agora.
- Erros aumentam no fim de tarefas longas — justamente onde ficam pagamento e confirmação.

!!! example "Uma cena"
    Marcos faz o pedido de um benefício à noite, depois do trabalho. Na etapa 6 de um formulário sem fim visível, o cansaço vence. Não há como salvar. No dia seguinte, ele precisa preencher tudo de novo — e erra o número da conta.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Não dá para parar no meio | "Salvar e continuar depois", com link enviado por e-mail |
| Não se sabe quanto falta | Etapas restantes e tempo estimado |
| Muitas decisões | Opção recomendada já marcada; opcionais podem ficar para depois |
| Tudo detalhado de uma vez | Resumo primeiro, detalhes só se a pessoa pedir |
| Passos críticos no fim da tarefa longa | Revisão clara antes de confirmar; caminho mais curto possível |

## Em código

### 1. Salvar e continuar depois

```html
<form id="pedido">
  <!-- campos da etapa -->
  <button type="submit">Continuar</button>
  <button type="button" id="salvar-depois">Salvar e continuar depois</button>
</form>
<p role="status" id="salvo"></p>
```

```js
document.querySelector('#salvar-depois').addEventListener('click', async () => {
  const dados = Object.fromEntries(new FormData(document.querySelector('#pedido')));
  // O servidor guarda o rascunho e envia o link por e-mail (vale por 30 dias)
  const resposta = await fetch('/api/rascunhos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  });
  const { validoAte } = await resposta.json();
  document.querySelector('#salvo').textContent =
    `Pronto. Enviamos um link para o seu e-mail. Você pode continuar até ${validoAte}.`;
});
```

### 2. Quanto falta, em etapas e em minutos

```js
// Tempo médio de cada etapa, medido em uso real (em minutos)
const ETAPAS = [
  { nome: 'Seus dados', minutos: 3 },
  { nome: 'Endereço', minutos: 2 },
  { nome: 'Documentos', minutos: 4 },
  { nome: 'Revisão', minutos: 1 },
];

function textoRestante(etapaAtual) {          // etapaAtual começa em 1
  const faltam = ETAPAS.slice(etapaAtual);
  if (faltam.length === 0) return 'Esta é a última etapa.';
  const minutos = faltam.reduce((soma, e) => soma + e.minutos, 0);
  const etapas = faltam.length === 1 ? '1 etapa' : `${faltam.length} etapas`;
  return `Depois desta, faltam ${etapas}: cerca de ${minutos} minutos.`;
}
// textoRestante(2) → "Depois desta, faltam 2 etapas: cerca de 5 minutos."
```

### 3. Menos decisões agora

```html
<fieldset>
  <legend>Como quer receber os avisos?</legend>
  <!-- A opção mais comum já vem marcada e diz por quê -->
  <label><input type="radio" name="aviso" value="email" checked>
    E-mail (recomendado: chega com o link direto)</label>
  <label><input type="radio" name="aviso" value="sms"> SMS</label>
</fieldset>

<details>
  <summary>Informações opcionais (pode preencher depois)</summary>
  <!-- campos que não são necessários agora -->
</details>
```

### 4. Resumo primeiro, detalhes se a pessoa pedir

```html
<section aria-labelledby="resumo-beneficio">
  <h2 id="resumo-beneficio">Seu pedido em 3 linhas</h2>
  <ul>
    <li>Valor: R$ 600,00 por mês.</li>
    <li>Primeiro pagamento: até 10 de dezembro.</li>
    <li>Você não precisa fazer mais nada agora.</li>
  </ul>
  <details>
    <summary>Ver todas as regras do benefício</summary>
    <!-- texto completo -->
  </details>
</section>
```

## Base normativa

**COGA** — Objetivo 5 (foco), Objetivo 4 (erros) e Objetivo 8 (adaptação):
4.6.2 Caminhos críticos curtos · 4.6.3 Evitar conteúdo demais · 4.6.4 Informar o necessário para se preparar · 4.5.9 Evitar perda de dados e tempo esgotado · 4.8.3 Dizer resultados e desvantagens de cada opção · 4.8.7 Oferecer lembretes · 4.9.3 Apoiar a simplificação.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 2.2.1 Tempo ajustável | A | Limites de tempo podem ser estendidos |
| 3.3.7 Entrada redundante | A | Não pedir de novo o que já foi informado |
| 2.4.5 Várias formas | AA | Mais de um caminho até o conteúdo |
| 3.3.4 Prevenção de erros (jurídico, financeiro, dados) | AA | Revisar antes de confirmar |
| 2.2.5 Nova autenticação | AAA | Dados preservados ao entrar de novo |
| 2.2.6 Tempo esgotado | AAA | Avisar quanto tempo de inatividade causa perda de dados |

**Literatura:** fadiga mental está ligada a reações mais lentas, mais erros, pior planejamento e mais distração ([Boksem e Tops, 2008](../literatura.md#fadiga-cognitiva)). Interrupções aumentam estresse, frustração e esforço, mesmo quando a tarefa termina mais rápido ([Mark, Gudith e Klocke, 2008](../literatura.md#atencao)).

## Como testar

- [ ] **Teste do fim do dia:** faça a tarefa inteira à noite, cansado. Onde você errou ou quis desistir?
- [ ] Pare no meio e feche o navegador. Dá para continuar de onde parou?
- [ ] Conte as decisões que a tarefa exige. Quais poderiam ter uma opção recomendada?
- [ ] Em cada etapa, você sabe quanto falta?
