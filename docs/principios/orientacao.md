---
title: O · Orientação
description: Onde estou, o que fazer agora, o que deu errado e como desfazer — erro em linguagem humana, com o caminho da correção.
---

<p class="claro-badge tone-o" data-letter="O">Princípio 5 de 5</p>

# Orientação

**Onde estou, o que fazer agora, o que deu errado e como desfazer.** Erro em linguagem humana, com o caminho da correção.

## O que é

Orientação responde a quatro perguntas que a pessoa faz o tempo todo, mesmo sem perceber:

1. **Onde estou?** — título, etapa, caminho.
2. **O que faço agora?** — próxima ação clara.
3. **O que deu errado?** — erro específico, perto de onde aconteceu.
4. **Como desfaço?** — voltar, editar, cancelar sem medo.

Previsibilidade reduz o esforço de todo mundo, e é essencial para quem tem dificuldade de [planejamento](../perfis/funcoes-executivas.md) ou de [memória](../perfis/memoria.md): o mesmo botão precisa ter o mesmo nome e fazer a mesma coisa em todo o produto.

## Faça / Evite

=== "Faça"

    - Título da página que diz onde a pessoa está.
    - Mensagem de erro que diz **o que** está errado e **como** corrigir.
    - Erro ao lado do campo, e um resumo no topo em formulários longos.
    - Tela de revisão antes de enviar dados importantes.
    - Opção de desfazer ou cancelar depois de ações destrutivas.
    - Confirmação clara do que aconteceu e do próximo passo.

=== "Evite"

    - Códigos técnicos: "Erro 422", "Falha inesperada".
    - Erro só em vermelho, sem texto.
    - Mensagem genérica no topo sem dizer qual campo.
    - Apagar o que a pessoa digitou quando há erro.
    - O mesmo ícone com significados diferentes em telas diferentes.
    - Ações irreversíveis sem confirmação.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">"Erro 422: payload inválido"</span> | **"O CPF tem 11 dígitos. Você digitou 9."** |
| <span class="claro-before">"Dados inválidos"</span> | **"A data de nascimento precisa estar no formato dia/mês/ano. Exemplo: 07/03/1990."** |
| <span class="claro-before">Excluir sem confirmação</span> | **"Arquivo excluído. Desfazer"** por 30 segundos, ou confirmação antes |

## Por dificuldade

Orientação atende principalmente estas dificuldades. O código está em cada perfil:

| Dificuldade | O que tem de código lá |
|---|---|
| [Planejamento e organização](../perfis/funcoes-executivas.md) | etapas, erro que diz como resolver, revisão e desfazer |
| [Memória](../perfis/memoria.md) | ajuda no mesmo lugar, protocolo guardado pelo sistema |
| [Comunicação social](../perfis/comunicacao-social.md) | chat com saída para uma pessoa, aviso antes de mudar |

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 3.3.1 Identificação do erro (*Error Identification*) | A | Erro descrito em texto |
| 3.3.3 Sugestão de erro (*Error Suggestion*) | AA | Dizer como corrigir |
| 3.3.4 Prevenção de erros (*Error Prevention (Legal, Financial, Data)*) | AA | Revisar, confirmar ou desfazer |
| 2.4.8 Localização (*Location*) | AAA | Saber onde está no conjunto de páginas |
| 3.2.4 Identificação consistente (*Consistent Identification*) | AA | Mesma função, mesmo nome |
| 4.1.3 Mensagens de status (*Status Messages*) | AA | Confirmações anunciadas sem mover o foco |

**COGA:** Objetivo 4 (evitar erros e saber corrigi-los) e Objetivo 2 (encontrar o que precisa).

## Como verificar

- [ ] Erre de propósito em cada campo. A mensagem diz como corrigir?
- [ ] O valor digitado continua no campo depois do erro?
- [ ] Com leitor de tela, o erro e a confirmação são anunciados?
- [ ] Toda ação destrutiva tem confirmação ou desfazer?

Itens completos no [checklist](../checklist.md#o-orientacao).
