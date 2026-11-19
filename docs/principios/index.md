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
4. **Por dificuldade** — quais perfis o princípio atende, com link para o código de cada um.
5. **Base normativa** — critérios da WCAG 2.2 e objetivos do COGA.
6. **Como verificar** — o que olhar na revisão.

## Princípios e perfis

Os **princípios** dizem *o que fazer*. Os [perfis por dificuldade](../perfis/index.md) dizem *para quem* e trazem o código. Os dois se cruzam:

| Princípio | Atende principalmente |
|---|---|
| **C** Clareza | [Leitura e linguagem](../perfis/leitura-e-linguagem.md) · [Números e cálculo](../perfis/numeros.md) · [Percepção](../perfis/percepcao.md) · [Comunicação social](../perfis/comunicacao-social.md) |
| **L** Leveza | [Atenção](../perfis/atencao.md) · [Planejamento e organização](../perfis/funcoes-executivas.md) · [Percepção](../perfis/percepcao.md) · [Fadiga cognitiva](../perfis/fadiga-cognitiva.md) |
| **A** Apoio à memória | [Memória](../perfis/memoria.md) · [Números e cálculo](../perfis/numeros.md) · [Fadiga cognitiva](../perfis/fadiga-cognitiva.md) |
| **R** Ritmo | [Velocidade de processamento](../perfis/velocidade.md) · [Atenção](../perfis/atencao.md) |
| **O** Orientação | [Planejamento e organização](../perfis/funcoes-executivas.md) · [Memória](../perfis/memoria.md) · [Comunicação social](../perfis/comunicacao-social.md) |

## Base normativa

O CLARO não cria requisitos novos: cada princípio agrupa critérios da WCAG 2.2 e padrões do W3C COGA. A relação completa está na seção [Normas](../normas/index.md), e a tabela princípio × critério na [matriz normativa](../normas/matriz.md#por-principio).

!!! tip "Repare nos níveis"
    Muitos critérios ligados aos princípios são **AAA** (3.1.5, 2.4.8, 2.2.6, 3.3.9…). Projetos costumam mirar só no AA, e é aí que a acessibilidade cognitiva some. O CLARO trata esses critérios como prática recomendada do time, mesmo quando não são exigência legal.
