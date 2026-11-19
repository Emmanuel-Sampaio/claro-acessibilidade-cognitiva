# Changelog

Todas as mudanças relevantes do CLARO ficam registradas aqui. O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as versões seguem o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.3.1] — 2026-11-19

### Alterado

- Cronograma ajustado para a entrega final em 3 de dezembro de 2026: auditoria com dois avaliadores até 25/11, teste piloto com 3 a 5 colegas até 01/12 e versão 1.0 em 03/12.
- O estudo completo com 12 participantes, que depende do Comitê de Ética, passa a ser trabalho futuro, depois da disciplina.

## [0.3.0] — 2026-11-19

Fecha a fase de revisão de literatura: o CLARO passa a ter base bibliográfica verificada, três perfis novos e um checklist revisado com a evidência.

### Adicionado

- **Revisão de literatura**: revisão narrativa com 20 referências comentadas (normas, legislação e estudos), todas conferidas na fonte; cinco achados principais e o que muda no framework por causa de cada um.
- **Três perfis novos**, com código: Percepção, Comunicação social e Fadiga cognitiva. O framework passa de 6 para 9 perfis.
- **Base de evidência do checklist**: cada item ligado à norma, ao padrão do COGA e ao estudo que o sustenta.
- Lei nº 15.263/2025 (Política Nacional de Linguagem Simples) e as perguntas do Grupo de Washington como referências.
- Página WCAG 2.2 para cognição: 46 critérios (16 A · 14 AA · 16 AAA), antes 38.

### Alterado

- Checklist v0.3: itens C1, C2, C6, L2, L5, A4, A6, R6, O3 e O5 revisados (o motivo de cada mudança está na página do checklist).
- Avaliação: triagem pelo modelo do Grupo de Washington e pelo menos um participante por perfil.
- Matriz normativa, páginas de princípio e página inicial atualizadas com os novos perfis.

## [0.2.0] — 2026-11-10

O público passa a ser descrito por **dificuldade funcional**, não por diagnóstico, e a parte normativa ganha uma seção própria.

### Adicionado

- **Perfis por dificuldade**: Atenção, Memória, Leitura e linguagem, Números e cálculo, Planejamento e organização (funções executivas) e Velocidade de processamento. Cada perfil traz barreiras, uma cena de exemplo, base normativa, um teste simples e código em HTML, CSS e JavaScript.
- Código novo: notificações adiadas durante a tarefa, retomar de onde parou, copiar protocolo, glossário inline, total com taxas, prazos com data relativa, entrada de valores em vários formatos, "Antes de começar", revisão com desfazer, vídeo com controle de velocidade e layout estável.
- **Seção Normas**: como WCAG 2.2 e COGA se relacionam; critérios da WCAG para cognição por nível (A, AA, AAA); os 8 objetivos e 58 padrões do COGA traduzidos; matriz dificuldade × princípio × COGA × WCAG × checklist.
- Prioridade do checklist por dificuldade.
- ABNT NBR 17225:2025 nas referências.

### Alterado

- Páginas de princípio: o código foi para os perfis, e cada princípio aponta para as dificuldades que atende.
- "O problema": a tabela de público passa a ser por dificuldade, e o dado do Censo usado é o de limitação em funções mentais.
- Avaliação: participantes selecionados por dificuldade relatada, sem exigência de laudo.
- Checklist v0.2: C1 inclui seções com título; L5 vira "Antes de começar"; A2 inclui colar código; A3 vira "o sistema faz as contas"; R1, R5 e O2 ampliados.

### Corrigido

- Número de padrões do COGA: são 58, não "mais de 100".

## [0.1.0] — 2026-10-29

Primeira versão pública: a proposta do framework, publicada junto com o pitch da disciplina.

### Adicionado

- Site de documentação com os cinco princípios: **C**lareza, **L**eveza, **A**poio à memória, **R**itmo e **O**rientação.
- Página para cada princípio com Faça/Evite, exemplos antes e depois, trechos de código e base normativa (WCAG 2.2 e W3C COGA).
- Mapa normativo ligando cada princípio aos critérios da WCAG 2.2 e aos 8 objetivos do COGA.
- Exemplos antes/depois escritos como critérios de aceite (Gherkin).
- Checklist de 30 itens (rascunho), pronto para *Definition of Done*.
- Método de avaliação em 3 fases e rubrica de 0 a 4 por princípio (rascunho).
- Modelo de planilha de avaliação (CSV).
- Roadmap de 12 semanas e versões planejadas até a v1.0.0.
- Pitch original em PDF.

[0.3.1]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.3.1
[0.3.0]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.3.0
[0.2.0]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.2.0
[0.1.0]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.1.0
