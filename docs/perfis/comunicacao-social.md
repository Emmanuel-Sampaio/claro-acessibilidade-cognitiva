---
title: Comunicação social
description: Perfil de dificuldade de comunicação social — entender tom, intenção e regras implícitas, lidar com mudanças inesperadas e se comunicar com o serviço.
---

<p class="claro-badge tone-p" data-letter="8">Perfil 8 de 9</p>

# Comunicação social

**Dificuldade para entender tom, intenção e regras que ninguém diz em voz alta, lidar com mudanças inesperadas e se comunicar com o serviço — perguntar, reclamar, pedir ajuda.**

Princípios mais ligados: [C · Clareza](../principios/clareza.md) e [O · Orientação](../principios/orientacao.md).

!!! note "Como este perfil se diferencia de Leitura e linguagem"
    [Leitura e linguagem](leitura-e-linguagem.md) trata de **decodificar e entender o texto**. Este perfil trata da **interação**: o que a mensagem quer dizer além das palavras, o que o serviço espera da pessoa, e como ela consegue falar com alguém. Aparece em quem tem dificuldade com o implícito, em quem usa o português como segunda língua, em quem vem de outra cultura, em quem tem ansiedade social — e em qualquer pessoa diante de um atendimento confuso.

## Na prática

- "Ops! Algo deu errado 😅" não diz se o pagamento foi feito ou não.
- O chatbot responde com ironia ou com uma pergunta aberta demais ("Como posso te ajudar hoje?").
- O único canal de atendimento é o telefone.
- A tela mudou de layout de um dia para o outro, sem aviso.
- Regras implícitas: "o prazo é até sexta" — sexta inclusive? até que horas?

!!! example "Uma cena"
    Ana tenta remarcar uma consulta pelo chat. O robô responde "Hmm, não entendi 🤔 Pode reformular?" três vezes. Não há botão para falar com uma pessoa, e ligar por telefone é o que ela mais quer evitar. Ela desiste e perde a consulta.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Mensagem com tom ambíguo ou só emoji | Mensagem literal: o que aconteceu, o que a pessoa precisa fazer |
| Chatbot que não entende e não dá saída | Opções em botões e "Falar com uma pessoa" sempre visível |
| Atendimento só por telefone | Um canal por escrito (formulário, e-mail ou chat com pessoa) |
| Mudança de interface sem aviso | Aviso antes, com o que muda e a opção de usar a versão antiga por um tempo |
| Regra implícita ("até sexta") | Regra completa: "até sexta-feira, 21/11, às 23h59" |
| Mesma ação com nomes diferentes | Mesmo nome, mesmo ícone, mesmo lugar em todo o produto |

## Em código

### 1. Status que diz o que aconteceu e o que fazer

```js
// Uma mensagem por situação, sempre com duas partes:
// o que aconteceu + o que a pessoa faz agora
const MENSAGENS = {
  pago:        { texto: 'Pagamento aprovado. Você não precisa fazer mais nada.', tipo: 'sucesso' },
  recusado:    { texto: 'Pagamento recusado pelo banco. Nada foi cobrado. Tente outro cartão ou pague com Pix.', tipo: 'erro' },
  processando: { texto: 'Pagamento em análise. Avisaremos por e-mail em até 2 horas. Não pague de novo.', tipo: 'aviso' },
};

function mostrarStatus(codigo) {
  const m = MENSAGENS[codigo] ?? {
    texto: 'Não conseguimos confirmar o pagamento. Nada foi cobrado. Fale com o atendimento.',
    tipo: 'erro',
  };
  const caixa = document.querySelector('#status-pagamento');   // role="status"
  caixa.className = `mensagem mensagem--${m.tipo}`;
  caixa.textContent = m.texto;
}
```

### 2. Chat com saída para uma pessoa

```html
<section aria-labelledby="chat-titulo">
  <h2 id="chat-titulo">Atendimento</h2>
  <p>Escolha uma opção ou escreva sua dúvida.</p>
  <div role="group" aria-label="Assuntos mais comuns">
    <button type="button" data-assunto="remarcar">Remarcar consulta</button>
    <button type="button" data-assunto="cancelar">Cancelar consulta</button>
    <button type="button" data-assunto="resultado">Ver resultado de exame</button>
  </div>
  <div id="conversa" role="log" aria-live="polite"></div>
  <!-- Sempre visível, desde a primeira mensagem -->
  <a class="botao" href="/atendimento/pessoa">Falar com uma pessoa (por escrito)</a>
</section>
```

```js
// Depois de 2 respostas sem entender, o próprio robô oferece a pessoa
let semEntender = 0;
function respostaDoRobo(entendeu, texto) {
  if (entendeu) { semEntender = 0; return texto; }
  semEntender += 1;
  return semEntender >= 2
    ? 'Não entendi. Vou passar sua conversa para uma pessoa da equipe. Ela responde por aqui em até 1 hora.'
    : 'Não entendi. Escolha um dos assuntos acima ou escreva de outro jeito.';
}
```

### 3. Avisar antes de mudar

```html
<aside class="aviso" aria-labelledby="mudanca-titulo">
  <h2 id="mudanca-titulo">A tela de pagamento vai mudar em 1º de dezembro</h2>
  <p>Os botões continuam com os mesmos nomes. O que muda: o resumo do pedido passa para o topo.</p>
  <a href="/pagamento?versao=nova">Experimentar a nova tela agora</a>
  <p>Até 31 de dezembro, você pode voltar para a tela antiga em Configurações.</p>
</aside>
```

### 4. Emoji e ícone nunca sozinhos

```html
<!-- O leitor de tela lê o nome, e a palavra visível tira a dúvida de todos -->
<p>
  <span role="img" aria-label="Aprovado">✅</span> Aprovado
</p>

<!-- Prazo completo, sem regra implícita -->
<p>Envie até <time datetime="2026-11-21T23:59">sexta-feira, 21 de novembro, às 23h59</time>.</p>
```

## Base normativa

**COGA** — Objetivo 3 (conteúdo claro), Objetivo 6 (memória) e Objetivo 7 (ajuda):
4.4.4 Linguagem literal · 4.4.12 Explicar o conteúdo implícito · 4.8.1 Ajuda humana · 4.8.5 Facilitar encontrar ajuda · 4.7.4 Permitir evitar menus de voz · 4.2.2 Hierarquia e design familiares · 4.9.4 Interface personalizada e familiar.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 1.1.1 Conteúdo não textual | A | Emoji e ícone com alternativa em texto |
| 3.2.6 Ajuda consistente | A | Contato e ajuda no mesmo lugar |
| 3.2.3 Navegação consistente | AA | Menus no mesmo lugar e na mesma ordem |
| 3.2.4 Identificação consistente | AA | Mesma função, mesmo nome |
| 3.1.3 Palavras incomuns | AAA | Expressões e jargão explicados |
| 3.3.5 Ajuda | AAA | Ajuda contextual disponível |

**Literatura:** perguntas que exigem inferência tiveram menos acertos (76%) que as literais (87%) em textos de leitura fácil ([Fajardo et al., 2014](../literatura.md#leitura-e-linguagem)). A Lei 15.263/2025 pede ordem direta, palavras comuns e teste com o público ([Lei de Linguagem Simples](../literatura.md#normas-politicas-e-documentos-tecnicos)). O Grupo de Washington inclui a dificuldade de se comunicar entre as seis perguntas básicas de funcionalidade.

## Como testar

- [ ] Leia cada mensagem de erro e de status sem emoji. Ela ainda diz o que aconteceu e o que fazer?
- [ ] Tente resolver o problema mais comum do serviço **sem telefone**. É possível?
- [ ] No chat, escreva algo que o robô não entende. Em quantas mensagens aparece uma pessoa?
- [ ] Procure prazos e regras com informação faltando: dia da semana, data, horário, "inclusive".
