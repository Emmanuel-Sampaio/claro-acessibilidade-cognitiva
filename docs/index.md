---
title: Início
description: CLARO é um framework em português para times de produto aplicarem acessibilidade cognitiva e de aprendizagem no dia a dia.
hide:
  - toc
---

<div class="claro-hero" markdown>
<p class="claro-kicker">Tópicos em acessibilidade digital · v0.3.0</p>

# CLARO

<p class="claro-lede">Um framework de boas práticas para acessibilidade cognitiva e de aprendizagem. Ele traduz o W3C COGA e a WCAG 2.2 em decisões concretas de design, conteúdo e código — em português e no ritmo de uma sprint.</p>
</div>

[Ver os princípios](principios/index.md){ .md-button .md-button--primary }
[Perfis por dificuldade](perfis/index.md){ .md-button }
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
- O W3C COGA tem 8 objetivos e 58 padrões de projeto. É excelente — e longo demais para caber numa revisão de PR.
- Ferramentas automáticas encontram contraste, `alt` e rótulo. **Não encontram** texto confuso, fluxo longo, prazo curto ou erro incompreensível.

**A lacuna não é de norma. É de tradução.** O CLARO organiza o que já existe em cinco princípios fáceis de lembrar, cada um com práticas verificáveis e critérios de aceite. [Entenda o problema&nbsp;→](problema.md)

## Nove dificuldades, não diagnósticos

O público do CLARO é descrito pela **dificuldade que a pessoa encontra**, não pelo diagnóstico. Dificuldade de atenção, por exemplo, aparece em muitas condições diferentes e em qualquer pessoa cansada ou interrompida. Cada perfil traz barreiras, base normativa, um teste simples e **código pronto para adaptar**.

<div class="claro-cards">
  <a class="claro-card" href="perfis/atencao/"><span class="claro-num" aria-hidden="true">1</span><span class="claro-name">Atenção</span><span class="claro-desc">Foco, distrações e interrupções.</span></a>
  <a class="claro-card" href="perfis/memoria/"><span class="claro-num" aria-hidden="true">2</span><span class="claro-name">Memória</span><span class="claro-desc">Guardar e lembrar informações.</span></a>
  <a class="claro-card" href="perfis/leitura-e-linguagem/"><span class="claro-num" aria-hidden="true">3</span><span class="claro-name">Leitura e linguagem</span><span class="claro-desc">Texto, vocabulário e sentido figurado.</span></a>
  <a class="claro-card" href="perfis/numeros/"><span class="claro-num" aria-hidden="true">4</span><span class="claro-name">Números e cálculo</span><span class="claro-desc">Valores, datas, unidades e contas.</span></a>
  <a class="claro-card" href="perfis/funcoes-executivas/"><span class="claro-num" aria-hidden="true">5</span><span class="claro-name">Planejamento e organização</span><span class="claro-desc">Etapas, decisões e correção de erros.</span></a>
  <a class="claro-card" href="perfis/velocidade/"><span class="claro-num" aria-hidden="true">6</span><span class="claro-name">Velocidade de processamento</span><span class="claro-desc">Mais tempo para ler e decidir.</span></a>
  <a class="claro-card" href="perfis/percepcao/"><span class="claro-num" aria-hidden="true">7</span><span class="claro-name">Percepção</span><span class="claro-desc">Fundo, cor, espaçamento e excesso de estímulo.</span></a>
  <a class="claro-card" href="perfis/comunicacao-social/"><span class="claro-num" aria-hidden="true">8</span><span class="claro-name">Comunicação social</span><span class="claro-desc">Tom, intenção, regras implícitas e atendimento.</span></a>
  <a class="claro-card" href="perfis/fadiga-cognitiva/"><span class="claro-num" aria-hidden="true">9</span><span class="claro-name">Fadiga cognitiva</span><span class="claro-desc">Parar sem perder nada, decidir menos.</span></a>
</div>

## Para quem é

| Papel | Use o CLARO para… |
|---|---|
| Design | Revisar fluxos e telas antes do handoff |
| Conteúdo / UX writing | Reescrever textos, erros e instruções |
| Desenvolvimento | Transformar princípios em critérios de aceite e código |
| Produto | Priorizar barreiras cognitivas no backlog |
| QA | Verificar o que a ferramenta automática não vê |

## Como usar em 3 passos

1. **Escolha o ponto de partida.** Conhece o público? Comece pelo [perfil da dificuldade](perfis/index.md). Vai revisar uma tela? Comece pelos [princípios](principios/index.md).
2. **Adote o checklist.** São 30 itens prontos para entrar na *Definition of Done*, com prioridade por dificuldade.
3. **Meça.** Use a rubrica de 0 a 4 por princípio para ter linha de base e evolução.

!!! info "Status do projeto"
    Esta é a **versão 0.3.0**, que fecha a fase de revisão de literatura: [referências comentadas](literatura.md), três perfis novos e o [checklist](checklist.md) revisado com base na evidência. O checklist e a rubrica continuam em rascunho e serão validados na auditoria e nos testes com usuários. Veja o [roadmap](roadmap.md) e o [changelog](changelog.md).
