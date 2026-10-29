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

Para pessoas com TEA, previsibilidade é essencial: o mesmo botão precisa ter o mesmo nome e fazer a mesma coisa em todo o produto.

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

## Em código

Erro ligado ao campo, anunciado pelo leitor de tela e sem apagar o valor:

```html
<label for="cpf">CPF</label>
<input id="cpf" name="cpf" inputmode="numeric"
       aria-invalid="true"
       aria-describedby="cpf-erro" value="123456789">
<p id="cpf-erro" class="erro">
  O CPF tem 11 números. Você digitou 9.
</p>

<!-- Região de status para confirmações -->
<div role="status" id="status"></div>
```

```js
function validarCPF(campo) {
  const digitos = campo.value.replace(/\D/g, '');
  const erro = document.querySelector('#cpf-erro');
  if (digitos.length !== 11) {
    campo.setAttribute('aria-invalid', 'true');
    erro.textContent =
      `O CPF tem 11 números. Você digitou ${digitos.length}.`;
    return false;
  }
  campo.removeAttribute('aria-invalid');
  erro.textContent = '';
  return true;
}

// Depois de salvar:
document.querySelector('#status').textContent =
  'Cadastro salvo. Próximo passo: enviar documentos.';
```

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
