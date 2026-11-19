---
title: Números e cálculo
description: Perfil de dificuldade com números — entender valores, datas, horários e unidades, e fazer contas de cabeça.
---

<p class="claro-badge tone-p" data-letter="4">Perfil 4 de 9</p>

# Números e cálculo

**Dificuldade para entender valores, porcentagens, datas, horários e unidades, e para fazer contas de cabeça.**

Princípios mais ligados: [C · Clareza](../principios/clareza.md) e [A · Apoio à memória](../principios/apoio-a-memoria.md).

## Na prática

- "12x de R$ 49,90" não vira "R$ 598,80" na cabeça da pessoa.
- Porcentagem solta ("juros de 2,99% a.m.") não diz quanto ela vai pagar.
- "Vence em 15/11" exige saber que dia é hoje e contar.
- Campo de valor que só aceita um formato ("1234.56") recusa o jeito que a pessoa escreve.
- Taxa que aparece só no fim do pagamento parece pegadinha.

!!! example "Uma cena"
    Carlos vê "12x de R$ 49,90" e escolhe parcelar. Ele não percebe que o total é R$ 598,80, ou seja, R$ 98,90 a mais do que o preço à vista, de R$ 499,90.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| A pessoa precisa fazer a conta | O sistema faz a conta e mostra o resultado |
| Taxas reveladas no fim | Total com todas as taxas desde o início |
| Data solta | Data relativa **e** absoluta: "amanhã (sexta, 14 de novembro)" |
| Porcentagem solta | Valor em reais ao lado da porcentagem |
| Formato rígido de entrada | Aceitar vários formatos e mostrar como foi entendido |
| Unidade ou medida pouco comum | Unidade familiar, escrita por extenso |

## Em código

### 1. O sistema faz a conta

Trabalhe em centavos (números inteiros) e mostre o total, com cada taxa por nome.

```js
const real = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' });

const itens = [
  { nome: 'Produto',         centavos: 49990 },
  { nome: 'Frete',           centavos: 1500 },
  { nome: 'Taxa de serviço', centavos: 390 },
];
const total = itens.reduce((soma, item) => soma + item.centavos, 0);

resumo.textContent = `Você vai pagar ${real.format(total / 100)} no total.`;
// "Você vai pagar R$ 518,80 no total."
```

```js
// Parcelado: sempre o total e a diferença para o à vista
function textoParcelas(parcelas, valorParcelaCentavos, aVistaCentavos) {
  const total = parcelas * valorParcelaCentavos;
  const diferenca = total - aVistaCentavos;
  let texto = `${parcelas} parcelas de ${real.format(valorParcelaCentavos / 100)}. ` +
              `Total: ${real.format(total / 100)}.`;
  if (diferenca > 0) texto += ` São ${real.format(diferenca / 100)} a mais do que à vista.`;
  return texto;
}
// textoParcelas(12, 4990, 49990)
// "12 parcelas de R$ 49,90. Total: R$ 598,80. São R$ 98,90 a mais do que à vista."
```

### 2. Prazo que não exige contar no calendário

```js
function textoPrazo(vencimento) {
  const hoje = new Date();
  hoje.setHours(0, 0, 0, 0);
  const dia = new Date(vencimento);
  dia.setHours(0, 0, 0, 0);

  const dias = Math.round((dia - hoje) / 86_400_000);
  const relativo = new Intl.RelativeTimeFormat('pt-BR', { numeric: 'auto' }).format(dias, 'day');
  const absoluto = new Intl.DateTimeFormat('pt-BR', {
    weekday: 'long', day: 'numeric', month: 'long',
  }).format(dia);

  return `Vence ${relativo} (${absoluto}).`;
}
// "Vence amanhã (sexta-feira, 14 de novembro)."
// "Vence em 5 dias (terça-feira, 18 de novembro)."
```

### 3. Aceitar o jeito que a pessoa escreve — e mostrar como entendeu

```js
// Aceita "1.234,56", "1234,56", "1234.56" e "R$ 50". Devolve centavos.
function lerValor(texto) {
  let t = texto.replace(/[^\d,.]/g, '');
  if (t.includes(',')) t = t.replace(/\./g, '').replace(',', '.');
  const n = Number(t);
  return Number.isFinite(n) && t !== '' ? Math.round(n * 100) : null;
}

campoValor.addEventListener('change', () => {
  const centavos = lerValor(campoValor.value);
  confirmacao.textContent = centavos === null
    ? 'Digite só o valor. Exemplo: 150,00.'
    : `Valor: ${real.format(centavos / 100)}. Está certo?`;
});

// CPF e telefone: aceite com ou sem pontos, traços e espaços
const soNumeros = (texto) => texto.replace(/\D/g, '');
```

### 4. Progresso em fração, não só em porcentagem

```html
<p id="progresso-texto">Etapa 3 de 5</p>
<progress max="5" value="3" aria-labelledby="progresso-texto"></progress>
```

## Base normativa

**COGA** — o tema aparece em vários objetivos:
4.4.13 Alternativas para conceitos numéricos · 4.7.5 Não depender de cálculo nem de decorar · 4.5.12 Unidades e medidas familiares · 4.5.3 Avisar taxas e custos no início · 4.5.8 Aceitar diferentes formatos de entrada.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 3.3.2 Rótulos ou instruções | A | Dizer o formato esperado |
| 3.3.3 Sugestão de erro | AA | Dizer como corrigir um valor inválido |
| 3.3.4 Prevenção de erros (financeiro) | AA | Revisar e confirmar antes de pagar |

!!! warning "Aqui a WCAG quase não chega"
    Nenhum critério da WCAG trata de cálculo, porcentagem ou datas relativas. Toda a orientação deste perfil vem do COGA — é o tipo de lacuna que o CLARO existe para cobrir.

## Como testar

- [ ] **Teste sem calculadora:** faça a tarefa sem papel nem calculadora. Você soube quanto ia pagar e até quando?
- [ ] Todo valor parcelado mostra o total? Toda porcentagem tem o valor em reais ao lado?
- [ ] Digite o valor de três jeitos diferentes. Todos são aceitos?
- [ ] Alguma taxa aparece só na última tela?
