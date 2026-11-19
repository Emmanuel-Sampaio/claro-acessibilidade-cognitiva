---
title: Avaliação
description: Como sabemos que funciona — auditoria com dois avaliadores, teste piloto, iteração, rubrica de 0 a 4 e o estudo completo planejado.
---

# Como sabemos que funciona

Três fases até a entrega final, em 3 de dezembro de 2026, e um estudo completo depois da disciplina.

<div class="claro-timeline">
  <div><strong>01 · Auditoria</strong>5 serviços, 2 avaliadores · até 25/11</div>
  <div><strong>02 · Teste piloto</strong>3 a 5 colegas, original × ajustada · até 01/12</div>
  <div><strong>03 · Iteração</strong>O que falhou volta para o checklist · 02/12</div>
  <div><strong>Guia v1.0</strong>Entrega final · 03/12</div>
</div>

## Fase 01 · Auditoria (até 25/11)

Auditoria CLARO em **5 serviços digitais brasileiros de alto uso**, feita por **dois avaliadores de forma independente**. Onde as notas divergirem em mais de 1 ponto, os dois revisam a evidência juntos e registram o motivo da divergência — isso também mostra quais itens do checklist estão ambíguos.

| Categoria | Tarefa sugerida para auditar |
|---|---|
| gov.br | Entrar na conta e emitir um documento |
| Matrícula escolar | Fazer a inscrição de um estudante |
| Agendamento de saúde | Marcar uma consulta |
| Banco | Fazer um Pix para um contato novo |
| E-commerce | Comprar um produto como visitante |

Cada serviço recebe uma **nota de 0 a 4 por princípio**, com evidência em print.

### Rubrica de pontuação

| Nota | Nível | Descrição | Referência no checklist |
|---|---|---|---|
| **4** | Exemplar | Todos os itens atendidos, com evidência | 6 de 6 itens |
| **3** | Bom | Atritos pontuais, nenhum impede a tarefa | 5 de 6 itens |
| **2** | Parcial | Atritos frequentes; a tarefa exige esforço extra | 3 ou 4 itens |
| **1** | Grave | A tarefa só é concluída com ajuda ou muita persistência | 1 ou 2 itens |
| **0** | Bloqueante | A tarefa não pode ser concluída por causa deste princípio | 0 itens, ou qualquer bloqueio |

!!! note "Regra do bloqueio"
    Uma única barreira que impede a conclusão da tarefa zera a nota daquele princípio, não importa quantos itens estejam atendidos.

**Kit de avaliação:** [baixe o modelo de planilha (CSV)](assets/kit-avaliacao-claro.csv). Abre no Excel, no Google Planilhas ou no LibreOffice.

## Fase 02 · Teste piloto (até 01/12)

**3 a 5 colegas voluntários** fazem a mesma tarefa na **versão original** de um dos serviços auditados e numa **versão ajustada** pelo CLARO (um protótipo em HTML), alternando a ordem entre as pessoas.

O piloto **não pretende provar a hipótese**: com poucas pessoas e sem seleção por dificuldade, ele testa o procedimento — o roteiro, o protótipo, as métricas e o tempo de cada sessão — para que o estudo completo comece sem surpresas.

- Sem nome, sem dados de saúde e sem perguntas sobre dificuldades ou diagnósticos.
- Consentimento por escrito, num termo curto em linguagem simples.
- Antes de começar, confirmar com o professor da disciplina se o piloto precisa passar pelo Comitê de Ética.

As métricas são as mesmas do estudo completo (tabela abaixo).

## Depois da disciplina: estudo completo

**12 participantes** executam a mesma tarefa na **versão original** e na **versão ajustada** pelo CLARO, depois da aprovação do Comitê de Ética em Pesquisa.

A seleção é feita pela **dificuldade relatada**, não por diagnóstico, com pelo menos uma pessoa para cada um dos [nove perfis](perfis/index.md). Ninguém precisa apresentar laudo. A triagem segue o modelo das perguntas do [Grupo de Washington](literatura.md#normas-politicas-e-documentos-tecnicos) — as mesmas que inspiram o Censo — com respostas de "nenhuma dificuldade" a "não consegue de jeito nenhum" (por exemplo: "Você tem dificuldade para lembrar ou se concentrar?"). Como uma pessoa costuma ter mais de uma dificuldade, os resultados também são analisados por perfil.

| Métrica | Como medir | Direção esperada |
|---|---|---|
| Taxa de conclusão | Concluiu a tarefa sem ajuda? | ↑ |
| Tempo | Do início da tarefa até a conclusão | ↓ |
| Erros | Ações erradas ou corrigidas | ↓ |
| Pedidos de ajuda | Quantas vezes pediu ajuda à pessoa moderadora | ↓ |
| Carga cognitiva percebida | Questionário NASA-TLX após cada versão | ↓ |

??? info "Sobre o NASA-TLX"
    O NASA Task Load Index é um questionário de carga de trabalho com seis dimensões: demanda mental, demanda física, demanda temporal, desempenho, esforço e frustração. É amplamente usado em estudos de usabilidade e fatores humanos. Para este público, recomenda-se ler as perguntas em voz alta e usar uma escala visual.

!!! warning "Ética em pesquisa"
    Pesquisa com pessoas exige Termo de Consentimento Livre e Esclarecido em linguagem simples e, quando aplicável, aprovação do Comitê de Ética em Pesquisa da instituição. Alternar a ordem das versões entre participantes ajuda a reduzir o efeito de aprendizado.

## Fase 03 · Iteração e entrega final (02/12 e 03/12)

O que falhou na auditoria e no piloto volta para o checklist e para a rubrica. Depois disso, publicação da **versão 1.0** do guia, com licença aberta e exemplos de código, na entrega final de **3 de dezembro de 2026**.

## Hipótese a testar

!!! abstract "Hipótese"
    Aplicar o CLARO **reduz tempo de conclusão e abandono** para quem tem dificuldades cognitivas **sem prejudicar** quem não tem.

É o mesmo efeito da rampa na calçada: feita para a cadeira de rodas, serve ao carrinho de bebê, à mala de viagem e a quem está com o pé machucado.
