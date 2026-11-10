# Changelog

Todas as mudanças relevantes do CLARO ficam registradas aqui. O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as versões seguem o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

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

[0.2.0]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.2.0
[0.1.0]: https://github.com/Emmanuel-Sampaio/claro-acessibilidade-cognitiva/releases/tag/v0.1.0
