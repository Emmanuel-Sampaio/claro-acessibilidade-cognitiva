---
title: Os cinco princípios
description: Clareza, Leveza, Apoio à memória, Ritmo e Orientação — e como cada um se conecta à WCAG 2.2 e ao W3C COGA.
---

# Os cinco princípios

O acrônimo é a interface do framework. Ele precisa caber na cabeça de quem decide — numa reunião de refinamento, numa revisão de tela, num PR.

| | Princípio | Em uma frase | Pergunta de revisão |
|---|---|---|---|
| **C** | [Clareza](clareza.md) | Linguagem simples e direta. | Uma pessoa cansada entende isso na primeira leitura? |
| **L** | [Leveza](leveza.md) | Uma tarefa por tela. | O que dá para tirar desta tela sem perder nada? |
| **A** | [Apoio à memória](apoio-a-memoria.md) | Nada de decorar. | Pedimos para a pessoa lembrar ou redigitar algo? |
| **R** | [Ritmo](ritmo.md) | A pessoa controla o tempo. | Algo acontece sozinho, some ou expira? |
| **O** | [Orientação](orientacao.md) | Onde estou, o que fazer, como desfazer. | Se der errado, a pessoa sabe o que fazer? |

## Como cada página está organizada

Todas as páginas de princípio seguem a mesma estrutura — previsibilidade também é acessibilidade:

1. **O que é** — a ideia em poucas linhas.
2. **Faça / Evite** — práticas concretas.
3. **Antes e depois** — um exemplo real de decisão.
4. **Em código** — um trecho de HTML ou JavaScript.
5. **Base normativa** — critérios da WCAG 2.2 e objetivos do COGA.
6. **Como verificar** — o que olhar na revisão.

## Mapa normativo

O CLARO não cria requisitos novos. Cada princípio agrupa critérios da WCAG 2.2 e objetivos do W3C COGA.

| Princípio | WCAG 2.2 (principais) | Objetivos COGA |
|---|---|---|
| **C** Clareza | 2.4.6 · 3.3.2 · 3.1.3 · 3.1.4 · 3.1.5 | 1 · 3 |
| **L** Leveza | 2.4.10 · 3.2.5 · 3.2.3 · 2.4.5 | 2 · 5 · 8 |
| **A** Apoio à memória | 3.3.7 · 3.3.8 · 3.3.9 · 3.2.6 · 1.3.5 | 6 · 7 |
| **R** Ritmo | 2.2.1 · 2.2.2 · 2.2.3 · 2.2.5 · 2.2.6 · 1.4.2 | 5 · 8 |
| **O** Orientação | 3.3.1 · 3.3.3 · 3.3.4 · 2.4.8 · 3.2.4 · 4.1.3 | 2 · 4 |

??? info "Os 8 objetivos do W3C COGA"
    1. Ajudar a pessoa a entender o que as coisas são e como usá-las.
    2. Ajudar a pessoa a encontrar o que precisa.
    3. Usar conteúdo claro e compreensível.
    4. Ajudar a pessoa a evitar erros e a saber corrigi-los.
    5. Ajudar a pessoa a manter o foco.
    6. Garantir que os processos não dependam da memória.
    7. Oferecer ajuda e suporte.
    8. Apoiar adaptação e personalização.

    Tradução livre de *Making Content Usable for People with Cognitive and Learning Disabilities* (W3C).

!!! tip "Repare nos níveis"
    Muitos critérios do mapa são **AAA** (3.1.5, 2.4.8, 2.2.6, 3.3.9…). Projetos costumam mirar só no AA, e é aí que a acessibilidade cognitiva some. O CLARO trata esses critérios como prática recomendada do time, mesmo quando não são exigência legal.
