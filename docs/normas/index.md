---
title: WCAG 2.2 e COGA
description: Como a WCAG 2.2 e o W3C COGA se relacionam, o que cada um exige ou recomenda e como o CLARO usa os dois.
---

# WCAG 2.2 e COGA: como se encaixam

São dois documentos do W3C com papéis diferentes. Entender a diferença é o primeiro passo para não deixar a acessibilidade cognitiva de fora do escopo.

<div class="claro-compare" markdown>

<div markdown>

### WCAG 2.2

**O que é:** a norma técnica de acessibilidade web. Uma *Recommendation* do W3C.

**Formato:** critérios de sucesso **testáveis** — passa ou não passa.

**Níveis:** A (mínimo), AA (o que leis e contratos costumam exigir) e AAA (mais exigente).

**Peso:** é a base de leis e normas no mundo todo. No Brasil, inspira a ABNT NBR 17225 (2025) e o eMAG.

**Limite:** cognição é difícil de testar com "passa ou não passa". Por isso, grande parte do que importa está no **AAA** ou ficou de fora.

[Critérios da WCAG para cognição →](wcag.md)

</div>

<div markdown>

### W3C COGA

**O que é:** *Making Content Usable for People with Cognitive and Learning Disabilities*. Uma *Working Group Note* do W3C (2021).

**Formato:** **8 objetivos** e **58 padrões de projeto**, com exemplos do que fazer e do que evitar.

**Níveis:** não tem. É orientação, não requisito.

**Peso:** não é exigido para conformidade com a WCAG. É a referência mais completa sobre acessibilidade cognitiva.

**Limite:** extenso e pouco operacional para a rotina de uma sprint.

[Objetivos e padrões do COGA →](coga.md)

</div>

</div>

## O que cada um cobre

| | WCAG 2.2 A/AA | WCAG 2.2 AAA | COGA |
|---|---|---|---|
| Login sem decorar senha | ✓ 3.3.8 | ✓ 3.3.9 | ✓ 4.7.1 |
| Não pedir o mesmo dado duas vezes | ✓ 3.3.7 | – | ✓ 4.7.5 |
| Ajuda no mesmo lugar | ✓ 3.2.6 | – | ✓ 4.8.5 |
| Erro que diz como corrigir | ✓ 3.3.3 | – | ✓ 4.5.5 |
| Linguagem simples | – | ✓ 3.1.5 | ✓ 4.4.1 |
| Explicar jargão e siglas | – | ✓ 3.1.3 · 3.1.4 | ✓ 4.4.1 |
| Adiar interrupções | – | ✓ 2.2.4 | ✓ 4.6.1 |
| Uma tarefa por tela, poucos campos | – | – | ✓ 4.6.3 |
| Mostrar o total em vez de pedir a conta | – | – | ✓ 4.7.5 · 4.4.13 |
| Dizer antes do que a pessoa vai precisar | – | – | ✓ 4.6.4 |
| Linguagem literal, sem metáfora | – | – | ✓ 4.4.4 |

!!! warning "A lacuna em uma frase"
    Quem mira só no nível AA — que é o que a maioria dos projetos faz — fica com **4 das 11 linhas** acima. O resto depende de o time decidir adotar.

## Como o CLARO usa os dois

<div class="claro-flow" role="list" aria-label="Como o CLARO usa a WCAG e o COGA">
  <div class="claro-flow-row" role="listitem">
    <div><strong>W3C COGA</strong><span>8 objetivos · 58 padrões</span></div>
    <div><strong>WCAG 2.2</strong><span>critérios testáveis A · AA · AAA</span></div>
  </div>
  <p class="claro-flow-arrow" aria-hidden="true">↓ o CLARO organiza em duas visões ↓</p>
  <div class="claro-flow-row" role="listitem">
    <div><strong>5 princípios</strong><span>o que fazer: Clareza · Leveza · Apoio à memória · Ritmo · Orientação</span></div>
    <div><strong>9 perfis</strong><span>para que dificuldade: Atenção · Memória · Leitura · Números · Planejamento · Velocidade · Percepção · Comunicação social · Fadiga</span></div>
  </div>
  <p class="claro-flow-arrow" aria-hidden="true">↓</p>
  <div class="claro-flow-row claro-flow-one" role="listitem">
    <div><strong>Checklist de 30 itens + rubrica 0–4</strong><span>o que se verifica na revisão e na auditoria</span></div>
  </div>
</div>

1. **Os princípios** agrupam os padrões do COGA em cinco decisões fáceis de lembrar.
2. **Os perfis** mostram, para cada dificuldade funcional, quais padrões e critérios importam mais — com código.
3. **O checklist** transforma tudo em itens verificáveis. Itens com critério WCAG trazem o número e o nível; os demais vêm do COGA.

A ligação completa entre as três visões está na [matriz normativa](matriz.md).

## No Brasil

| Referência | O que é | Relação com a cognição |
|---|---|---|
| **LBI** (Lei 13.146/2015) | Lei Brasileira de Inclusão | Obriga acessibilidade em sites de empresas e órgãos públicos |
| **ABNT NBR 17225** (2025) | Norma técnica de acessibilidade web, baseada na WCAG 2.2 | Divide as orientações entre requisitos e recomendações |
| **eMAG** | Modelo de acessibilidade do governo federal | Referência histórica para o setor público |
