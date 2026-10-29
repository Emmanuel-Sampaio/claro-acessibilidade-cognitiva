---
title: Checklist de 30 itens
description: Seis itens por princípio, prontos para virar Definition of Done do time.
---

# Checklist CLARO

Trinta itens, seis por princípio, escritos para caber na *Definition of Done* do time. Cada item é verificável por uma pessoa em revisão — sem ferramenta especial.

!!! warning "Rascunho v0.1"
    Esta é a primeira versão do checklist. Ela será revisada depois da auditoria dos 5 serviços e dos testes com usuários (veja o [roadmap](roadmap.md)). Sugestões são bem-vindas pelas *issues* do repositório.

??? tip "Como adotar no time"
    1. Copie os itens para o modelo de PR ou para a descrição da história.
    2. Comece pelos itens com critério de nível **A** e **AA** — eles também são exigência legal.
    3. Inclua os demais aos poucos, um princípio por sprint.
    4. Marque "não se aplica" quando a tela não tiver aquele elemento — e diga por quê.

## C · Clareza

- [ ] **C1.** Frases curtas (até ~20 palavras) e uma ideia por parágrafo.
- [ ] **C2.** Instruções e erros sem metáfora, ironia ou expressão idiomática.
- [ ] **C3.** Siglas e termos técnicos explicados na primeira vez que aparecem. <small>(3.1.3, 3.1.4 · AAA)</small>
- [ ] **C4.** Botões e links dizem a ação ou o destino — nada de "OK" ou "Clique aqui". <small>(2.4.6 · AA)</small>
- [ ] **C5.** Instrução visível antes do campo, não só no *placeholder*. <small>(3.3.2 · A)</small>
- [ ] **C6.** Texto principal legível por quem tem ensino fundamental, ou versão simplificada disponível. <small>(3.1.5 · AAA)</small>

## L · Leveza

- [ ] **L1.** Cada tela tem uma tarefa principal e uma única ação primária em destaque.
- [ ] **L2.** Formulários longos divididos em etapas de até ~8 campos, com progresso em texto.
- [ ] **L3.** Só se pedem dados necessários; campos opcionais estão marcados.
- [ ] **L4.** Nenhum pop-up, banner ou animação compete com a tarefa principal.
- [ ] **L5.** Conteúdo dividido em seções com títulos descritivos. <small>(2.4.10 · AAA)</small>
- [ ] **L6.** Nada muda de contexto (nova aba, envio, redirecionamento) sem ação da pessoa. <small>(3.2.5 · AAA)</small>

## A · Apoio à memória

- [ ] **A1.** Dados já informados no mesmo processo vêm preenchidos ou disponíveis para seleção. <small>(3.3.7 · A)</small>
- [ ] **A2.** Login sem teste cognitivo: colar senha e gerenciador de senhas funcionam; CAPTCHA tem alternativa. <small>(3.3.8 · AA)</small>
- [ ] **A3.** Códigos de verificação podem ser colados e ficam válidos por tempo suficiente (ex.: 10 min).
- [ ] **A4.** Ajuda (contato, chat, dúvidas) fica no mesmo lugar em todas as páginas. <small>(3.2.6 · A)</small>
- [ ] **A5.** Campos de dados pessoais usam `autocomplete` correto. <small>(1.3.5 · AA)</small>
- [ ] **A6.** Voltar uma etapa ou recarregar não apaga o que foi preenchido.

## R · Ritmo

- [ ] **R1.** Todo limite de tempo pode ser desligado, ajustado ou estendido. <small>(2.2.1 · A)</small>
- [ ] **R2.** Aviso antes de a sessão expirar, com pelo menos 20 s para pedir mais tempo. <small>(2.2.1 · A)</small>
- [ ] **R3.** Carrossel e conteúdo em movimento têm pausa — ou não se movem sozinhos. <small>(2.2.2 · A)</small>
- [ ] **R4.** Se a sessão cair, os dados são preservados e a duração da sessão foi informada. <small>(2.2.5, 2.2.6 · AAA)</small>
- [ ] **R5.** Áudio e vídeo não tocam sozinhos. <small>(1.4.2 · A)</small>
- [ ] **R6.** Animações param quando o sistema pede menos movimento (`prefers-reduced-motion`).

## O · Orientação

- [ ] **O1.** Título da página e cabeçalho dizem onde a pessoa está; etapa atual indicada. <small>(2.4.2 · A, 2.4.8 · AAA)</small>
- [ ] **O2.** Erro em linguagem humana, ao lado do campo, dizendo como corrigir. <small>(3.3.1 · A, 3.3.3 · AA)</small>
- [ ] **O3.** Erros e confirmações são anunciados por leitor de tela. <small>(4.1.3 · AA)</small>
- [ ] **O4.** Ações importantes ou destrutivas podem ser revisadas, confirmadas ou desfeitas. <small>(3.3.4 · AA)</small>
- [ ] **O5.** Componentes com a mesma função têm o mesmo nome e comportamento em todo o produto. <small>(3.2.4 · AA)</small>
- [ ] **O6.** Depois de cada ação, a pessoa vê o resultado e o próximo passo.

## Versão para copiar

Para colar num modelo de *pull request* ou numa história:

```markdown
### Checklist CLARO
- [ ] C — Textos curtos, sem jargão, botões com verbo de ação, instrução visível
- [ ] L — Uma ação principal, etapas curtas com progresso, sem pop-up na tarefa
- [ ] A — Nada pedido duas vezes, colar permitido, ajuda no mesmo lugar, autocomplete
- [ ] R — Sem tempo limite silencioso, pausa no que se move, sem autoplay
- [ ] O — Erro diz como corrigir, anunciado ao leitor de tela, ações podem ser desfeitas
```
