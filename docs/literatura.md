---
title: Revisão de literatura
description: Referências comentadas que sustentam os perfis e o checklist do CLARO, o que a literatura confirma, o que ela contesta e o que mudou no framework por causa disso.
---

# Revisão de literatura

**A literatura sustenta a maior parte do CLARO, mas corrige três pontos e deixa claro que a evidência empírica sobre acessibilidade cognitiva na web ainda é pequena.** Esta página reúne as referências da v0.3.0, comentadas, e mostra o que mudou no framework por causa delas.

## Como a revisão foi feita

- **Tipo:** revisão narrativa, não sistemática. O objetivo é dar base a cada perfil e a cada item do checklist, não esgotar o tema.
- **Fontes:** documentos do W3C, legislação e normas brasileiras, e artigos revisados por pares localizados por busca em bases abertas e repositórios institucionais.
- **Critério de inclusão:** tratar de uma das [nove dificuldades](perfis/index.md), de interfaces digitais com pessoas com dificuldades cognitivas ou de um método de avaliação usado no projeto.
- **Verificação:** cada referência foi conferida na fonte (autor, ano, veículo e achado principal) antes de entrar aqui. Não há citação de segunda mão.
- **Período:** novembro de 2026.

## O que a literatura diz, em cinco achados

| # | Achado | Fonte | O que muda no CLARO |
|---|---|---|---|
| 1 | A evidência empírica é **pequena e às vezes contraditória**. Seguir diretrizes nem sempre remove a barreira. | Borg, Lantz e Gulliksen (2015) | Testar com pessoas reais é obrigatório, não opcional. Personalização (COGA, objetivo 8) ganha peso. |
| 2 | Em textos de leitura fácil, o que mais atrapalhou a compreensão foram **referências que obrigam a voltar no texto** e o **número de frases** — não o tamanho da frase nem a raridade da palavra. | Fajardo et al. (2014) | Item C1 do checklist revisado: além de frases curtas, repetir o nome em vez de usar pronomes que apontam para longe. |
| 3 | A memória de curto prazo guarda **cerca de 4 blocos**, não 7. | Cowan (2001) | Item L2 revisado: campos agrupados em blocos pequenos, com título. |
| 4 | Linhas longas são lidas um pouco mais rápido, mas **leitores preferem linhas médias** (~55 caracteres) e compreendem um pouco melhor. | Dyson (2004) | A recomendação de ~70 caracteres por linha se mantém, justificada por conforto e compreensão, não por velocidade. |
| 5 | Interrupções fazem as pessoas trabalharem **mais rápido, com mais estresse, frustração e esforço**. | Mark, Gudith e Klocke (2008) | Reforça os itens L4 e R1, e sustenta o novo perfil de fadiga cognitiva. |

!!! warning "A limitação mais importante"
    Quase todos os estudos empíricos citados têm amostras pequenas (de 16 a 94 participantes) e poucos usam grupo de controle. Eles apontam direções, não provam efeitos. É por isso que a fase de testes do CLARO compara a versão original com a ajustada, com as mesmas pessoas.

## Referências comentadas

### Normas, políticas e documentos técnicos

**W3C. *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA). Working Group Note, 2021.** <https://www.w3.org/TR/coga-usable/>
: A referência central do CLARO: 8 objetivos e 58 padrões de projeto. Descreve o público por funções cognitivas, não por diagnóstico — a mesma escolha dos [perfis](perfis/index.md). Não tem força de norma.

**W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. Recommendation, 2023.** <https://www.w3.org/TR/WCAG22/>
: Fonte dos critérios testáveis do checklist. Trouxe três critérios cognitivos novos (3.2.6, 3.3.7, 3.3.8), mas mantém boa parte da orientação cognitiva no nível AAA. Veja [WCAG 2.2 para cognição](normas/wcag.md).

**W3C. *Inaccessibility of CAPTCHA: Alternatives to Visual Turing Tests on the Web*. Working Group Note, 9 dez. 2019.** <https://www.w3.org/TR/2019/NOTE-turingtest-20191209/>
: Afirma que CAPTCHAs de caracteres são resolvidos com menos sucesso por pessoas com deficiências cognitivas e de aprendizagem, que CAPTCHAs de áudio causam sobrecarga cognitiva e que quebra-cabeças lógicos criam barreiras para quem tem dificuldade com linguagem ou números. Recomenda análise de risco, *honeypots* e verificação sem desafio interativo. Sustenta o item A2.

**Brasil. Lei nº 15.263, de 14 de novembro de 2025. Institui a Política Nacional de Linguagem Simples.** [Texto na Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/2025/lei-15263-14-novembro-2025-798293-publicacaooriginal-177011-pl.html)
: Vale para toda a administração pública. O art. 5º lista técnicas que coincidem com o princípio [Clareza](principios/clareza.md): ordem direta, frases curtas, uma ideia por parágrafo, palavras comuns, explicar termos técnicos, nome completo antes da sigla e **testar a compreensão com o público-alvo**. Cita expressamente pessoas com deficiência e remete à LBI. Torna parte do CLARO uma exigência legal no setor público.

**ABNT. NBR 17225:2025 — Acessibilidade em conteúdo e aplicações web: requisitos.**
: Norma técnica brasileira baseada na WCAG 2.2. O mapeamento item a item com o checklist está previsto no [roadmap](roadmap.md).

**Washington Group on Disability Statistics. *Short Set on Functioning*.** [Especificação das perguntas](https://www.washingtongroup-disability.com/fileadmin/uploads/wg/Documents/Events/August_8-10_2017/WG-Short-Set-on-Functioning-Question-Specifications.pdf)
: Seis perguntas sobre dificuldade funcional, com quatro respostas (de "nenhuma dificuldade" a "não consegue de jeito nenhum"). Duas interessam ao CLARO: dificuldade para **lembrar ou se concentrar** e para **se comunicar**. É o modelo da triagem por dificuldade, sem laudo, usada na [avaliação](avaliacao.md).

### Visão geral do campo

**Friedman, M. G.; Bryen, D. N. Web accessibility design recommendations for people with cognitive disabilities. *Technology and Disability*, v. 19, n. 4, p. 205–212, 2007.** <https://content.iospress.com/articles/technology-and-disability/tad00242>
: Analisou 20 diretrizes, com 187 recomendações. As mais citadas: imagens e ícones junto com o texto (75% das diretrizes), texto claro e simples (70%), navegação e design consistentes (60%) e títulos e cabeçalhos (50%). É evidência de **consenso entre especialistas**, não de efeito medido.

**Borg, J.; Lantz, A.; Gulliksen, J. Accessibility to electronic communication for people with cognitive disabilities: a systematic search and review of empirical evidence. *Universal Access in the Information Society*, v. 14, n. 4, p. 547–562, 2015.** <https://link.springer.com/article/10.1007/s10209-014-0351-6>
: Revisão sistemática: 13 bases, 10.206 resultados, 29 estudos incluídos. Algumas medidas ajudaram (menos poluição visual na tela, mais espaçamento, fonte e cor personalizáveis, avisos em áudio). Os resultados às vezes se contradizem, e seguir diretrizes nem sempre removeu a barreira. Conclusão: evidência escassa, amostras pequenas, e as soluções precisam ser **ajustáveis pela pessoa**.

**Sweller, J. Cognitive load during problem solving: effects on learning. *Cognitive Science*, v. 12, n. 2, p. 257–285, 1988.**
: Origem da teoria da carga cognitiva: a memória de trabalho é limitada, e o que a interface obriga a pessoa a processar compete com a tarefa em si. É a base teórica de [Leveza](principios/leveza.md).

### Por dificuldade

#### Atenção

**Mark, G.; Gudith, D.; Klocke, U. The cost of interrupted work: more speed and stress. In: *CHI 2008*. ACM, 2008. p. 107–110.** <https://researchr.org/publication/MarkGK08>
: Com 48 participantes, pessoas interrompidas terminaram as tarefas mais rápido e sem perder qualidade, mas relataram mais estresse, frustração, pressão de tempo e esforço. Sustenta adiar notificações durante a tarefa ([perfil Atenção](perfis/atencao.md)) e o perfil de [fadiga cognitiva](perfis/fadiga-cognitiva.md).

#### Memória

**Cowan, N. The magical number 4 in short-term memory: a reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, v. 24, n. 1, p. 87–114, 2001.** <https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496>
: Revê o "número mágico 7" de Miller: o limite central fica em torno de **4 blocos** (de 3 a 5). Na interface, isso significa não pedir para a pessoa guardar um código de 6 dígitos de uma tela para outra e agrupar campos em blocos pequenos ([perfil Memória](perfis/memoria.md)).

#### Leitura e linguagem

**Fajardo, I.; Ávila, V.; Ferrer, A.; Tavares, G.; Gómez, M.; Hernández, A. Easy-to-read texts for students with intellectual disability: linguistic factors affecting comprehension. *Journal of Applied Research in Intellectual Disabilities*, v. 27, n. 3, p. 212–225, 2014.**
: Com 16 estudantes, textos de leitura fácil tiveram 87% de acerto em perguntas literais e 76% em inferenciais. O que mais atrapalhou: **referências que obrigam a voltar no texto** (pronomes e retomadas) e **número de frases**. Palavras por frase, frequência das palavras e índice de Flesch **não** tiveram efeito significativo. Amostra pequena, resultado preliminar — mas muda o checklist (item C1).

**Zorzi, M. et al. Extra-large letter spacing improves reading in dyslexia. *PNAS*, v. 109, n. 28, p. 11455–11459, 2012.** <https://ccnl.psy.unipd.it/publications/publications_folder/extra-large-letter-spacing-improves-reading-in-dyslexia/view>
: Com 94 crianças (54 italianas e 40 francesas), mais espaço entre letras e palavras aumentou a velocidade de leitura em cerca de 20% e reduziu os erros pela metade. Sustenta o critério 1.4.12 (deixar a pessoa aumentar o espaçamento) e o perfil de [percepção](perfis/percepcao.md).

**Dyson, M. C. How physical text layout affects reading from screen. *Behaviour & Information Technology*, v. 23, n. 6, p. 377–393, 2004.** <https://reading-pure-test.eprints-hosting.org/23344/>
: Revisão de estudos de leitura em tela. Linhas de 100 caracteres foram lidas mais rápido que as de 25, mas os leitores preferiram linhas médias (~55 caracteres), e um estudo achou melhor compreensão em 55. As amostras eram de universitários e usuários experientes, não de pessoas com dificuldade de leitura.

**Martins, T. B. F.; Ghiraldelo, C. M.; Nunes, M. G. V.; Oliveira Jr., O. N. *Readability formulas applied to textbooks in Brazilian Portuguese*. São Carlos: ICMSC-USP, 1996.** <https://repositorio.usp.br/item/000906089>
: Origem da adaptação do índice de Flesch ao português, segundo Aluisio et al. (2010, *Readability Assessment for Text Simplification*, workshop BEA5). É a ferramenta sugerida no teste do perfil de leitura — com a ressalva de Fajardo et al. de que o índice sozinho não previu compreensão.

#### Números e cálculo

**Peters, E.; Västfjäll, D.; Slovic, P.; Mertz, C. K.; Mazzocco, K.; Dickert, S. Numeracy and decision making. *Psychological Science*, v. 17, n. 5, p. 407–413, 2006.** <https://research.chalmers.se/en/publication/82667>
: Em quatro estudos, pessoas com menor habilidade numérica foram mais afetadas pela forma como o número é apresentado (efeito de enquadramento) e por informações irrelevantes, e o efeito não se explicava pela inteligência geral. Sustenta mostrar o total pronto, em reais, em vez de porcentagens soltas ([perfil Números](perfis/numeros.md)).

#### Planejamento e organização

**Diamond, A. Executive functions. *Annual Review of Psychology*, v. 64, p. 135–168, 2013.** <https://annualreviews.org/doi/pdf/10.1146/annurev-psych-113011-143750>
: Define as três funções executivas centrais: controle inibitório, memória de trabalho e flexibilidade cognitiva. Dá nome ao perfil [Planejamento e organização](perfis/funcoes-executivas.md).

#### Velocidade de processamento

**Salthouse, T. A. The processing-speed theory of adult age differences in cognition. *Psychological Review*, v. 103, n. 3, 1996.**
: Processamento mais lento prejudica a cognição por dois caminhos: falta de tempo para concluir as operações e perda das primeiras informações antes de as últimas ficarem prontas. Sustenta tirar limites de tempo e não fazer a informação sumir sozinha ([perfil Velocidade](perfis/velocidade.md)).

#### Fadiga cognitiva

**Boksem, M. A. S.; Tops, M. Mental fatigue: costs and benefits. *Brain Research Reviews*, v. 59, n. 1, p. 125–139, 2008.** <https://repository.tilburguniversity.edu/items/36be9bf7-fa00-413e-80f8-6f05e287aa6a>
: A fadiga mental aparece com trabalho cognitivo prolongado e está ligada a reações mais lentas, mais erros, pior planejamento e mais distração. Os autores a explicam como uma avaliação contínua de esforço contra recompensa. Sustenta o perfil de [fadiga cognitiva](perfis/fadiga-cognitiva.md): caminhos curtos, pausas sem perda e menos decisões.

### Métodos de avaliação

**Hart, S. G.; Staveland, L. E. Development of NASA-TLX (Task Load Index): results of empirical and theoretical research. *Advances in Psychology*, v. 52, p. 139–183, 1988.**
: Questionário de carga de trabalho em seis dimensões, usado na [avaliação](avaliacao.md). A adaptação para o público do CLARO (leitura em voz alta, escala visual) ainda precisa ser testada.

## Limitações desta revisão

- É narrativa: pode ter deixado de fora estudos relevantes. Uma busca sistemática fica para depois da v1.0.
- Há pouca pesquisa brasileira e em português sobre acessibilidade cognitiva na web. Esta é uma lacuna do campo, não só da revisão.
- Os perfis de [percepção](perfis/percepcao.md) e [comunicação social](perfis/comunicacao-social.md) se apoiam mais em normas e consenso do que em estudos empíricos.
