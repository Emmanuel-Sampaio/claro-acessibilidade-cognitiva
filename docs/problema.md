---
title: O problema
description: Por que barreiras cognitivas quase nunca entram no backlog, e quem é afetado por elas.
---

# O problema

## A web está ficando mais difícil de usar

E piora justamente onde ninguém mede.

<div class="claro-stats">
  <div class="claro-stat"><strong>95,9%</strong><span>das home pages do top 1 milhão têm falhas de WCAG detectáveis. Em 2025 eram 94,8%.</span></div>
  <div class="claro-stat"><strong>56,1</strong><span>erros por página, em média. Alta de cerca de 10% em um ano.</span></div>
  <div class="claro-stat"><strong>1.437</strong><span>elementos por página, em média. Alta de 22,5% em um ano — quase o dobro de 2019.</span></div>
</div>

<small>Fonte: WebAIM Million 2026, análise automatizada das 1.000.000 de home pages mais acessadas.</small>

### E isso é só o que o robô enxerga

Testes automatizados encontram contraste, texto alternativo e rótulo de campo. Eles **não encontram**:

- texto confuso ou cheio de jargão;
- fluxo longo demais;
- prazo curto ou sessão que expira sem aviso;
- erro que ninguém entende;
- passo que exige decorar um código.

As barreiras cognitivas são invisíveis para as ferramentas. Por isso quase nunca entram no backlog.

## Não é um público pequeno

Transtornos cognitivos e de aprendizagem atravessam toda a população.

| Público | O que é mais afetado | Barreiras típicas |
|---|---|---|
| **TDAH** | Atenção sustentada, foco, impulsividade | Ruído visual, fluxos longos |
| **Dislexia e discalculia** | Leitura e números | Texto denso, fonte apertada, prazo |
| **Deficiência intelectual** | Abstração, memória de trabalho | Jargão, etapas encadeadas |
| **TEA** | Linguagem literal, previsibilidade | Metáfora, ironia, mudança de padrão |
| **Envelhecimento** | Memória, velocidade de processamento | Tudo acima — e é o grupo que mais cresce no Brasil |
| **Situacional** | Qualquer pessoa, algum dia | Cansaço, pressa, dor, luto, estresse, segunda língua |

<div class="claro-stats">
  <div class="claro-stat"><strong>14,4 mi</strong><span>pessoas com deficiência no Brasil (7,3% da população de 2 anos ou mais).</span></div>
  <div class="claro-stat"><strong>2,4 mi</strong><span>pessoas com diagnóstico de TEA.</span></div>
  <div class="claro-stat"><strong>27,5%</strong><span>das pessoas com 70 anos ou mais têm alguma deficiência.</span></div>
</div>

<small>Fonte: IBGE, Censo Demográfico 2022 (resultados da amostra, divulgados em 2025). Segundo o mesmo levantamento, 63,1% das pessoas com deficiência de 25 anos ou mais não concluíram o ensino fundamental — mais um motivo para linguagem simples.</small>

## A norma existe. A prática, não.

=== "O que já temos"

    - A **WCAG 2.2** trouxe critérios cognitivos: Ajuda Consistente (3.2.6), Entrada Redundante (3.3.7) e Autenticação Acessível (3.3.8).
    - O **W3C COGA** — *Making Content Usable for People with Cognitive and Learning Disabilities* — tem 8 objetivos e mais de 100 padrões de projeto.
    - A **LBI** (Lei 13.146/2015) e o **eMAG** obrigam acessibilidade no setor público.

=== "O que ainda falta"

    - A maior parte da orientação cognitiva vive no nível **AAA** ou como recomendação não testável. Ela some do escopo do projeto.
    - Não há checklist operacional **em português** que caiba na rotina de sprint.
    - Nenhuma ferramenta automatizada avalia **carga cognitiva**. Sem métrica, não vira prioridade.

!!! quote "A tese do CLARO"
    A lacuna não é de norma. É de tradução. O framework organiza o que já existe — ele não substitui a WCAG nem o COGA.

[Conheça os cinco princípios →](principios/index.md){ .md-button .md-button--primary }
