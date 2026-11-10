---
title: Checklist de 30 itens
description: Seis itens por princípio, prontos para virar Definition of Done do time.
---

# Checklist CLARO

Trinta itens, seis por princípio, escritos para caber na *Definition of Done* do time. Cada item é verificável por uma pessoa em revisão — sem ferramenta especial.

!!! warning "Rascunho v0.2"
    Esta é a segunda versão do checklist, agora ligada aos perfis por dificuldade. Ela será revisada depois da auditoria dos 5 serviços e dos testes com usuários (veja o [roadmap](roadmap.md)). Sugestões são bem-vindas pelas *issues* do repositório.

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

## C · Clareza

- [ ] **C1.** Frases curtas (até ~20 palavras), uma ideia por parágrafo e conteúdo dividido em seções com títulos. <small>(2.4.10 · AAA)</small>
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
- [ ] **L5.** Antes de começar, a pessoa sabe do que vai precisar e quanto tempo a tarefa leva.
- [ ] **L6.** Nada muda de contexto (nova aba, envio, redirecionamento) sem ação da pessoa. <small>(3.2.5 · AAA)</small>

## A · Apoio à memória

- [ ] **A1.** Dados já informados no mesmo processo vêm preenchidos ou disponíveis para seleção. <small>(3.3.7 · A)</small>
- [ ] **A2.** Login sem teste cognitivo: colar senha e código funciona, o gerenciador de senhas preenche e o CAPTCHA tem alternativa. <small>(3.3.8 · AA)</small>
- [ ] **A3.** O sistema faz as contas: total com todas as taxas desde o início, parcelado com o valor total, prazos com data e dia da semana.
- [ ] **A4.** Ajuda (contato, chat, dúvidas) fica no mesmo lugar em todas as páginas. <small>(3.2.6 · A)</small>
- [ ] **A5.** Campos de dados pessoais usam `autocomplete` correto. <small>(1.3.5 · AA)</small>
- [ ] **A6.** Voltar uma etapa ou recarregar não apaga o que foi preenchido.

## R · Ritmo

- [ ] **R1.** Todo limite de tempo pode ser desligado, ajustado ou estendido — inclusive mensagens que somem sozinhas. <small>(2.2.1 · A)</small>
- [ ] **R2.** Aviso antes de a sessão expirar, com pelo menos 20 s para pedir mais tempo. <small>(2.2.1 · A)</small>
- [ ] **R3.** Carrossel e conteúdo em movimento têm pausa — ou não se movem sozinhos. <small>(2.2.2 · A)</small>
- [ ] **R4.** Se a sessão cair, os dados são preservados e a duração da sessão foi informada. <small>(2.2.5, 2.2.6 · AAA)</small>
- [ ] **R5.** Áudio e vídeo não tocam sozinhos; vídeos têm legenda e transcrição. <small>(1.4.2, 1.2.2 · A)</small>
- [ ] **R6.** Animações param quando o sistema pede menos movimento (`prefers-reduced-motion`).

## O · Orientação

- [ ] **O1.** Título da página e cabeçalho dizem onde a pessoa está; etapa atual indicada. <small>(2.4.2 · A, 2.4.8 · AAA)</small>
- [ ] **O2.** Erro em linguagem humana, ao lado do campo, dizendo como corrigir; formatos comuns de entrada são aceitos. <small>(3.3.1 · A, 3.3.3 · AA)</small>
- [ ] **O3.** Erros e confirmações são anunciados por leitor de tela. <small>(4.1.3 · AA)</small>
- [ ] **O4.** Ações importantes ou destrutivas podem ser revisadas, confirmadas ou desfeitas. <small>(3.3.4 · AA)</small>
- [ ] **O5.** Componentes com a mesma função têm o mesmo nome e comportamento em todo o produto. <small>(3.2.4 · AA)</small>
- [ ] **O6.** Depois de cada ação, a pessoa vê o resultado e o próximo passo.

## Versão para copiar

Para colar num modelo de *pull request* ou numa história:

```markdown
### Checklist CLARO
- [ ] C — Textos curtos, sem jargão, botões com verbo de ação, instrução visível
- [ ] L — Uma ação principal, "antes de começar", etapas curtas com progresso, sem pop-up na tarefa
- [ ] A — Nada pedido duas vezes, colar permitido, sistema faz as contas, ajuda no mesmo lugar, autocomplete
- [ ] R — Sem tempo limite silencioso, pausa no que se move, sem autoplay
- [ ] O — Erro diz como corrigir, anunciado ao leitor de tela, ações podem ser desfeitas
```
