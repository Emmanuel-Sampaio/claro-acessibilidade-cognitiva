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

Dificuldades cognitivas atravessam toda a população — com ou sem diagnóstico, de forma permanente ou passageira. Por isso o CLARO olha para a **dificuldade**, não para o laudo.

| Dificuldade | Como aparece na interface | Barreiras típicas |
|---|---|---|
| [**Atenção**](perfis/atencao.md) | Perde o foco com o que se move; se perde depois de uma interrupção | Pop-ups, carrosséis, fluxos longos |
| [**Memória**](perfis/memoria.md) | Esquece o código entre uma tela e outra; não lembra senhas | Colar bloqueado, dado pedido duas vezes |
| [**Leitura e linguagem**](perfis/leitura-e-linguagem.md) | Cansa com blocos de texto; lê metáfora ao pé da letra | Jargão, frases longas, ícone sem texto |
| [**Números e cálculo**](perfis/numeros.md) | Não converte "12x de R$ 49,90" no total | Contas de cabeça, taxas escondidas |
| [**Planejamento e organização**](perfis/funcoes-executivas.md) | Começa sem saber do que vai precisar; trava em erros | Etapas sem fim visível, erro genérico |
| [**Velocidade de processamento**](perfis/velocidade.md) | Precisa de mais tempo para ler e decidir | Sessão que expira, mensagem que some |

!!! info "Uma dificuldade, muitas origens"
    A mesma dificuldade de atenção pode vir de condições muito diferentes, de nenhuma condição diagnosticada, ou simplesmente de cansaço, dor, luto, estresse, pressa ou de estar usando o celular com uma criança no colo. Ninguém está livre de precisar disso algum dia.

<div class="claro-stats">
  <div class="claro-stat"><strong>14,4 mi</strong><span>pessoas com deficiência no Brasil (7,3% da população de 2 anos ou mais).</span></div>
  <div class="claro-stat"><strong>1,4 mi</strong><span>com limitação em funções mentais que afeta comunicação, cuidados pessoais, trabalho ou estudo.</span></div>
  <div class="claro-stat"><strong>27,5%</strong><span>das pessoas com 70 anos ou mais têm alguma deficiência.</span></div>
</div>

<small>Fonte: IBGE, Censo Demográfico 2022 (resultados da amostra, divulgados em 2025). O Censo identifica deficiência por **dificuldade funcional** autodeclarada, não por laudo — a mesma lógica dos perfis do CLARO. Segundo o mesmo levantamento, 63,1% das pessoas com deficiência de 25 anos ou mais não concluíram o ensino fundamental — mais um motivo para linguagem simples.</small>

## A norma existe. A prática, não.

=== "O que já temos"

    - A **WCAG 2.2** trouxe critérios cognitivos: Ajuda Consistente (3.2.6), Entrada Redundante (3.3.7) e Autenticação Acessível (3.3.8).
    - O **W3C COGA** — *Making Content Usable for People with Cognitive and Learning Disabilities* — tem 8 objetivos e 58 padrões de projeto.
    - A **LBI** (Lei 13.146/2015) e o **eMAG** obrigam acessibilidade no setor público.

=== "O que ainda falta"

    - A maior parte da orientação cognitiva vive no nível **AAA** ou como recomendação não testável. Ela some do escopo do projeto.
    - Não há checklist operacional **em português** que caiba na rotina de sprint.
    - Nenhuma ferramenta automatizada avalia **carga cognitiva**. Sem métrica, não vira prioridade.

!!! quote "A tese do CLARO"
    A lacuna não é de norma. É de tradução. O framework organiza o que já existe — ele não substitui a WCAG nem o COGA.

[Conheça os cinco princípios →](principios/index.md){ .md-button .md-button--primary }
