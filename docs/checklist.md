---
title: Checklist de 30 itens
description: Seis itens por princípio, prontos para virar Definition of Done do time.
---

# Checklist CLARO

Trinta itens, seis por princípio, escritos para caber na *Definition of Done* do time. Cada item é verificável por uma pessoa em revisão — sem ferramenta especial.

!!! warning "Rascunho v0.3"
    Terceira versão do checklist, revisada com base na [revisão de literatura](literatura.md). Ela ainda será validada na auditoria dos 5 serviços e no teste piloto, antes da versão 1.0 em 3 de dezembro de 2026 (veja o [roadmap](roadmap.md)). Sugestões são bem-vindas pelas *issues* do repositório.

??? info "O que mudou na v0.3 e por quê"
    | Item | Mudança | Motivo |
    |---|---|---|
    | C1 | Repetir o nome em vez de pronomes que obrigam a voltar no texto | Retomadas foram o fator que mais atrapalhou a compreensão literal em [Fajardo et al. (2014)](literatura.md#leitura-e-linguagem) |
    | C2 | Inclui emoji no lugar de palavras | Novo perfil [Comunicação social](perfis/comunicacao-social.md) |
    | C6 | Legibilidade conferida com pessoas do público; linhas de até ~70 caracteres; espaçamento ajustável | Índice de legibilidade sozinho não previu compreensão (Fajardo et al.); Lei 15.263/2025 exige teste com o público; [Dyson (2004)](literatura.md#leitura-e-linguagem) e [Zorzi et al. (2012)](literatura.md#leitura-e-linguagem) |
    | L2 | Campos agrupados em blocos pequenos | A memória de curto prazo guarda cerca de 4 itens ([Cowan, 2001](literatura.md#memoria)) |
    | L5 | Inclui saber quanto falta durante a tarefa | Novo perfil [Fadiga cognitiva](perfis/fadiga-cognitiva.md) |
    | A4 | Ajuda inclui um canal por escrito com uma pessoa | Novo perfil [Comunicação social](perfis/comunicacao-social.md) |
    | A6 | Tarefas longas têm "salvar e continuar depois" | Novo perfil [Fadiga cognitiva](perfis/fadiga-cognitiva.md) |
    | R6 | Nada pisca mais de 3 vezes por segundo | Novo perfil [Percepção](perfis/percepcao.md) |
    | O3 | Status indicado por texto ou ícone, nunca só por cor | Novo perfil [Percepção](perfis/percepcao.md) |
    | O5 | Mudanças de interface avisadas antes | Novo perfil [Comunicação social](perfis/comunicacao-social.md) |

??? tip "Como adotar no time"
    1. Copie os itens para o modelo de PR ou para a descrição da história.
    2. Comece pelos itens com critério de nível **A** e **AA** — eles também são exigência legal.
    3. Inclua os demais aos poucos, um princípio por sprint.
    4. Marque "não se aplica" quando a tela não tiver aquele elemento — e diga por quê.

## Por dificuldade

Se o seu público tem uma dificuldade específica, comece por estes itens:

| Dificuldade | Itens prioritários |
|---|---|
| [Atenção](perfis/atencao.md) | L1 · L4 · L6 · R3 · R5 · R6 |
| [Memória](perfis/memoria.md) | C5 · A1 · A2 · A4 · A5 · A6 |
| [Leitura e linguagem](perfis/leitura-e-linguagem.md) | C1 · C2 · C3 · C4 · C6 |
| [Números e cálculo](perfis/numeros.md) | C5 · A3 · O2 · O4 |
| [Planejamento e organização](perfis/funcoes-executivas.md) | L2 · L5 · O1 · O2 · O4 · O6 |
| [Velocidade de processamento](perfis/velocidade.md) | R1 · R2 · R3 · R4 · R5 |
| [Percepção](perfis/percepcao.md) | C6 · L4 · R5 · R6 · O3 |
| [Comunicação social](perfis/comunicacao-social.md) | C2 · C3 · A4 · O5 · O6 |
| [Fadiga cognitiva](perfis/fadiga-cognitiva.md) | L2 · L3 · L5 · A6 · R4 · O4 |

## C · Clareza

- [ ] **C1.** Frases curtas (até ~20 palavras), uma ideia por parágrafo, conteúdo em seções com títulos e o nome repetido em vez de pronomes que obrigam a voltar no texto. <small>(2.4.10 · AAA)</small>
- [ ] **C2.** Instruções, erros e status sem metáfora, ironia, expressão idiomática ou emoji no lugar de palavras.
- [ ] **C3.** Siglas e termos técnicos explicados na primeira vez que aparecem. <small>(3.1.3, 3.1.4 · AAA)</small>
- [ ] **C4.** Botões e links dizem a ação ou o destino — nada de "OK" ou "Clique aqui". <small>(2.4.6 · AA)</small>
- [ ] **C5.** Instrução visível antes do campo, não só no *placeholder*. <small>(3.3.2 · A)</small>
- [ ] **C6.** Texto legível: nível de ensino fundamental conferido com pessoas do público (não só com índice), linhas de até ~70 caracteres e espaçamento que pode ser aumentado sem quebrar o layout. <small>(1.4.12 · AA, 3.1.5 · AAA)</small>

## L · Leveza

- [ ] **L1.** Cada tela tem uma tarefa principal e uma única ação primária em destaque.
- [ ] **L2.** Formulários longos divididos em etapas de até ~8 campos, agrupados em blocos pequenos com título, e progresso em texto.
- [ ] **L3.** Só se pedem dados necessários; campos opcionais estão marcados.
- [ ] **L4.** Nenhum pop-up, banner ou animação compete com a tarefa principal.
- [ ] **L5.** Antes de começar, a pessoa sabe do que vai precisar e quanto tempo a tarefa leva; durante, sabe quanto falta.
- [ ] **L6.** Nada muda de contexto (nova aba, envio, redirecionamento) sem ação da pessoa. <small>(3.2.5 · AAA)</small>

## A · Apoio à memória

- [ ] **A1.** Dados já informados no mesmo processo vêm preenchidos ou disponíveis para seleção. <small>(3.3.7 · A)</small>
- [ ] **A2.** Login sem teste cognitivo: colar senha e código funciona, o gerenciador de senhas preenche e o CAPTCHA tem alternativa. <small>(3.3.8 · AA)</small>
- [ ] **A3.** O sistema faz as contas: total com todas as taxas desde o início, parcelado com o valor total, prazos com data e dia da semana.
- [ ] **A4.** Ajuda — incluindo um canal por escrito com uma pessoa — fica no mesmo lugar em todas as páginas. <small>(3.2.6 · A)</small>
- [ ] **A5.** Campos de dados pessoais usam `autocomplete` correto. <small>(1.3.5 · AA)</small>
- [ ] **A6.** Voltar uma etapa, recarregar ou parar no meio não apaga o que foi preenchido; tarefas longas têm "salvar e continuar depois".

## R · Ritmo

- [ ] **R1.** Todo limite de tempo pode ser desligado, ajustado ou estendido — inclusive mensagens que somem sozinhas. <small>(2.2.1 · A)</small>
- [ ] **R2.** Aviso antes de a sessão expirar, com pelo menos 20 s para pedir mais tempo. <small>(2.2.1 · A)</small>
- [ ] **R3.** Carrossel e conteúdo em movimento têm pausa — ou não se movem sozinhos. <small>(2.2.2 · A)</small>
- [ ] **R4.** Se a sessão cair, os dados são preservados e a duração da sessão foi informada. <small>(2.2.5, 2.2.6 · AAA)</small>
- [ ] **R5.** Áudio e vídeo não tocam sozinhos; vídeos têm legenda e transcrição. <small>(1.4.2, 1.2.2 · A)</small>
- [ ] **R6.** Animações param quando o sistema pede menos movimento (`prefers-reduced-motion`), e nada pisca mais de 3 vezes por segundo. <small>(2.3.1 · A)</small>

## O · Orientação

- [ ] **O1.** Título da página e cabeçalho dizem onde a pessoa está; etapa atual indicada. <small>(2.4.2 · A, 2.4.8 · AAA)</small>
- [ ] **O2.** Erro em linguagem humana, ao lado do campo, dizendo como corrigir; formatos comuns de entrada são aceitos. <small>(3.3.1 · A, 3.3.3 · AA)</small>
- [ ] **O3.** Erros e confirmações são anunciados por leitor de tela e indicados por texto ou ícone, nunca só por cor. <small>(1.4.1 · A, 4.1.3 · AA)</small>
- [ ] **O4.** Ações importantes ou destrutivas podem ser revisadas, confirmadas ou desfeitas. <small>(3.3.4 · AA)</small>
- [ ] **O5.** Componentes com a mesma função têm o mesmo nome e comportamento em todo o produto, e mudanças de interface são avisadas antes. <small>(3.2.4 · AA)</small>
- [ ] **O6.** Depois de cada ação, a pessoa vê o resultado e o próximo passo.

## Base de evidência

Cada item com a norma, o padrão do COGA e o estudo que o sustentam. Os estudos estão comentados na [revisão de literatura](literatura.md).

| Item | WCAG 2.2 ou lei | COGA | Literatura |
|---|---|---|---|
| C1 | 2.4.10 · Lei 15.263, art. 5º | 4.4.3 · 4.4.5 | Fajardo et al. 2014; Friedman e Bryen 2007 |
| C2 | Lei 15.263, art. 5º | 4.4.4 · 4.4.12 | Fajardo et al. 2014 |
| C3 | 3.1.3 · 3.1.4 · Lei 15.263, art. 5º | 4.4.1 | – |
| C4 | 2.4.6 | 4.2.5 | Friedman e Bryen 2007 |
| C5 | 3.3.2 | 4.5.6 | – |
| C6 | 1.4.12 · 3.1.5 · 1.4.8 · Lei 15.263, art. 5º | 4.4.10 | Zorzi et al. 2012; Dyson 2004; Fajardo et al. 2014 |
| L1 | – | 4.3.4 · 4.6.3 | Sweller 1988 |
| L2 | – | 4.6.2 | Cowan 2001 |
| L3 | – | 4.6.3 | – |
| L4 | 2.2.4 | 4.6.1 | Mark et al. 2008; Borg et al. 2015 |
| L5 | – | 4.6.4 | Boksem e Tops 2008 |
| L6 | 3.2.2 · 3.2.5 | 4.5.1 | – |
| A1 | 3.3.7 | 4.7.5 | – |
| A2 | 3.3.8 | 4.7.1 · 4.7.2 | W3C, *Inaccessibility of CAPTCHA* 2019 |
| A3 | – | 4.4.13 · 4.5.3 · 4.7.5 | Peters et al. 2006 |
| A4 | 3.2.6 | 4.8.1 · 4.8.5 | – |
| A5 | 1.3.5 | – | – |
| A6 | 2.2.5 | 4.5.9 | Boksem e Tops 2008 |
| R1 | 2.2.1 | 4.5.9 | Salthouse 1996 |
| R2 | 2.2.1 · 2.2.6 | 4.5.9 | Salthouse 1996 |
| R3 | 2.2.2 | 4.9.1 | – |
| R4 | 2.2.5 · 2.2.6 | 4.5.9 | – |
| R5 | 1.2.2 · 1.4.2 | 4.3.5 | – |
| R6 | 2.3.1 · 2.3.3 | 4.9.1 | – |
| O1 | 2.4.2 · 2.4.8 | 4.2.1 · 4.2.4 | Friedman e Bryen 2007 |
| O2 | 3.3.1 · 3.3.3 | 4.5.5 · 4.5.8 | – |
| O3 | 1.4.1 · 4.1.3 | 4.5.10 | – |
| O4 | 3.3.4 | 4.5.2 · 4.5.5 | – |
| O5 | 3.2.3 · 3.2.4 | 4.2.3 · 4.9.4 | Friedman e Bryen 2007 |
| O6 | – | 4.5.10 · 4.8.3 | – |

!!! abstract "O que a tabela mostra"
    Todos os 30 itens têm base em pelo menos uma norma ou padrão do COGA, e 15 citam a literatura. Mas só **5** se apoiam em experimentos com pessoas usando texto ou interface (C1, C2, C6, L4 e A3). Os outros 10 citam teoria (Sweller, Cowan, Salthouse), revisões (Boksem e Tops), documentos técnicos (W3C) ou consenso de diretrizes (Friedman e Bryen). É por isso que a [fase de testes](avaliacao.md) existe: para medir o efeito dos itens, não só supor.

## Versão para copiar

Para colar num modelo de *pull request* ou numa história:

```markdown
### Checklist CLARO
- [ ] C — Textos curtos e literais, sem jargão nem emoji no lugar de palavras, botões com verbo de ação, instrução visível
- [ ] L — Uma ação principal, "antes de começar", etapas curtas com progresso, sem pop-up na tarefa
- [ ] A — Nada pedido duas vezes, colar permitido, sistema faz as contas, ajuda por escrito no mesmo lugar, salvar e continuar depois
- [ ] R — Sem tempo limite silencioso, pausa no que se move, sem autoplay, nada piscando
- [ ] O — Erro diz como corrigir, não depende só de cor, anunciado ao leitor de tela, ações podem ser desfeitas
```
