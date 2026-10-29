---
title: Início
description: CLARO é um framework em português para times de produto aplicarem acessibilidade cognitiva e de aprendizagem no dia a dia.
hide:
  - toc
---

<div class="claro-hero" markdown>
<p class="claro-kicker">Tópicos em acessibilidade digital · v0.1.0</p>

# CLARO

<p class="claro-lede">Um framework de boas práticas para acessibilidade cognitiva e de aprendizagem. Ele traduz o W3C COGA e a WCAG 2.2 em decisões concretas de design, conteúdo e código — em português e no ritmo de uma sprint.</p>
</div>

[Ver os princípios](principios/index.md){ .md-button .md-button--primary }
[Abrir o checklist](checklist.md){ .md-button }
[Baixar o pitch (PDF)](assets/CLARO-pitch-acessibilidade-cognitiva.pdf){ .md-button }

## Cinco princípios, uma palavra

<div class="claro-acronym">
  <a class="claro-letter tone-c" href="principios/clareza/">
    <span class="claro-big" aria-hidden="true">C</span>
    <span class="claro-name">Clareza</span>
    <span class="claro-desc">Linguagem simples e direta. Uma ideia por vez.</span>
  </a>
  <a class="claro-letter tone-l" href="principios/leveza/">
    <span class="claro-big" aria-hidden="true">L</span>
    <span class="claro-name">Leveza</span>
    <span class="claro-desc">Uma tarefa por tela. Menos opções, menos ruído.</span>
  </a>
  <a class="claro-letter tone-a" href="principios/apoio-a-memoria/">
    <span class="claro-big" aria-hidden="true">A</span>
    <span class="claro-name">Apoio à memória</span>
    <span class="claro-desc">Nada de decorar. O que foi informado fica.</span>
  </a>
  <a class="claro-letter tone-r" href="principios/ritmo/">
    <span class="claro-big" aria-hidden="true">R</span>
    <span class="claro-name">Ritmo</span>
    <span class="claro-desc">Quem controla o tempo é a pessoa usuária.</span>
  </a>
  <a class="claro-letter tone-o" href="principios/orientacao/">
    <span class="claro-big" aria-hidden="true">O</span>
    <span class="claro-name">Orientação</span>
    <span class="claro-desc">Onde estou, o que fazer, como desfazer.</span>
  </a>
</div>

## Por que existe

A norma já existe. A prática, não.

- A WCAG 2.2 trouxe critérios cognitivos novos, mas boa parte da orientação cognitiva continua no nível AAA ou como recomendação não testável. Na prática, ela some do escopo.
- O W3C COGA tem 8 objetivos e mais de 100 padrões de projeto. É excelente — e longo demais para caber numa revisão de PR.
- Ferramentas automáticas encontram contraste, `alt` e rótulo. **Não encontram** texto confuso, fluxo longo, prazo curto ou erro incompreensível.

**A lacuna não é de norma. É de tradução.** O CLARO organiza o que já existe em cinco princípios fáceis de lembrar, cada um com práticas verificáveis e critérios de aceite. [Entenda o problema&nbsp;→](problema.md)

## Para quem é

| Papel | Use o CLARO para… |
|---|---|
| Design | Revisar fluxos e telas antes do handoff |
| Conteúdo / UX writing | Reescrever textos, erros e instruções |
| Desenvolvimento | Transformar princípios em critérios de aceite e código |
| Produto | Priorizar barreiras cognitivas no backlog |
| QA | Verificar o que a ferramenta automática não vê |

## Como usar em 3 passos

1. **Leia os princípios.** Cada página tem o que fazer, o que evitar e como verificar.
2. **Adote o checklist.** São 30 itens prontos para entrar na *Definition of Done*.
3. **Meça.** Use a rubrica de 0 a 4 por princípio para ter linha de base e evolução.

!!! info "Status do projeto"
    Esta é a **versão 0.1.0**: a proposta do framework, publicada junto com o pitch da disciplina. O checklist e a rubrica são rascunhos que serão validados na auditoria e nos testes com usuários. Veja o [roadmap](roadmap.md) e o [changelog](changelog.md).
