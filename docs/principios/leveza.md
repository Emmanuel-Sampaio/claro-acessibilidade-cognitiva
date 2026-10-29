---
title: L · Leveza
description: Uma tarefa por tela — menos opções, menos campos, menos ruído visual, processos longos divididos em etapas curtas.
---

<p class="claro-badge tone-l" data-letter="L">Princípio 2 de 5</p>

# Leveza

**Uma tarefa por tela.** Menos opções, menos campos, menos ruído visual. Divida processos longos em etapas curtas com progresso visível.

## O que é

Atenção e memória de trabalho são recursos limitados — para todo mundo, e bem mais para quem tem TDAH, deficiência intelectual ou está sob estresse. Cada elemento extra na tela cobra um pouco desse recurso. Leveza é gastar a atenção da pessoa só com o que importa para a tarefa atual.

## Faça / Evite

=== "Faça"

    - Uma ação principal por tela, visualmente destacada.
    - Etapas curtas (até ~8 campos) com indicação "Etapa 2 de 4".
    - Peça só o necessário. Se é opcional, pergunte se precisa mesmo.
    - Agrupe campos relacionados sob títulos descritivos.
    - Espaço em branco generoso entre blocos.
    - Mostre opções avançadas só quando a pessoa pedir.

=== "Evite"

    - Formulário único com dezenas de campos.
    - Pop-up, banner de oferta ou chat abrindo no meio da tarefa.
    - Várias ações com o mesmo peso visual competindo entre si.
    - Menus com dezenas de itens no mesmo nível.
    - Abrir nova aba ou enviar o formulário sem a pessoa pedir.
    - Animações decorativas perto do conteúdo principal.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">Formulário único com 32 campos</span> | **4 etapas de 8 campos, com barra de progresso** |
| <span class="claro-before">Tela de pagamento com banner de cartão, cupom e chat abertos</span> | **Só o resumo do pedido e o botão Pagar; cupom em link discreto** |

## Em código

Indicador de etapas que funciona para quem enxerga e para quem usa leitor de tela:

```html
<nav aria-label="Etapas do cadastro">
  <ol class="etapas">
    <li>Dados pessoais</li>
    <li aria-current="step">Endereço</li>
    <li>Documentos</li>
    <li>Revisão</li>
  </ol>
</nav>

<h1>Endereço <span class="progresso">(etapa 2 de 4)</span></h1>
```

!!! tip "Leveza não é esconder"
    Dividir em etapas só ajuda se a pessoa sabe quantas faltam e consegue voltar sem perder nada. Veja [Apoio à memória](apoio-a-memoria.md) e [Orientação](orientacao.md).

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 2.4.10 Cabeçalhos de seção (*Section Headings*) | AAA | Conteúdo organizado em blocos com título |
| 3.2.5 Mudança mediante solicitação (*Change on Request*) | AAA | Nada muda de contexto sem ação da pessoa |
| 3.2.3 Navegação consistente (*Consistent Navigation*) | AA | Menus no mesmo lugar e na mesma ordem |
| 2.4.5 Várias formas (*Multiple Ways*) | AA | Busca e navegação para achar o conteúdo |

**COGA:** Objetivo 5 (manter o foco), Objetivo 2 (encontrar o que precisa) e Objetivo 8 (adaptação e personalização).

!!! warning "A lacuna aparece aqui"
    Quase nada de Leveza é testável pela WCAG em nível A ou AA. Não existe critério que diga "no máximo X campos por tela". É exatamente o tipo de orientação que some do escopo — e que o CLARO transforma em critério de aceite do time.

## Como verificar

- [ ] Qual é a ação principal desta tela? Ela é a mais visível?
- [ ] Algum campo pode sair sem prejuízo para o processo?
- [ ] O progresso aparece em texto, não só em cor?
- [ ] Algo aparece, pisca ou se move sem a pessoa pedir?

Itens completos no [checklist](../checklist.md#l-leveza).
