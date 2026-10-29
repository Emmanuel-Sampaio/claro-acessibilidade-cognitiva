---
title: C · Clareza
description: Linguagem simples e direta — frases curtas, uma ideia por parágrafo, sem metáfora, ironia ou jargão.
---

<p class="claro-badge tone-c" data-letter="C">Princípio 1 de 5</p>

# Clareza

**Linguagem simples e direta.** Frases curtas, uma ideia por parágrafo, sem metáfora, ironia ou jargão. Se precisa de termo técnico, explique na primeira vez.

## O que é

Clareza é a pessoa entender **na primeira leitura**, mesmo cansada, com pressa ou lendo numa segunda língua. Texto é interface: um rótulo ambíguo bloqueia tanto quanto um botão quebrado.

## Faça / Evite

=== "Faça"

    - Frases curtas — mire em até 20 palavras.
    - Uma ideia por parágrafo.
    - Verbos de ação em botões: **Enviar documento**, **Pagar boleto**.
    - Explique sigla e termo técnico na primeira vez que aparecem.
    - Escreva a instrução **antes** do campo, em texto visível.
    - Use palavras do dia a dia da pessoa, não do sistema.

=== "Evite"

    - Metáfora, ironia e expressão idiomática em instruções.
    - Jargão interno: "validação biométrica", "payload", "protocolo".
    - Botões genéricos: **OK**, **Prosseguir**, **Clique aqui**.
    - Instrução só no *placeholder* — ela some quando a pessoa digita.
    - Voz passiva e dupla negação: "não deixe de não preencher…".
    - Parágrafos longos com várias condições encadeadas.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">"Prossiga com a validação biométrica facial"</span> | **"Tire uma foto do seu rosto"** |
| <span class="claro-before">"Informe o identificador do contribuinte"</span> | **"Digite seu CPF"** |
| <span class="claro-before">"Clique aqui"</span> | **"Baixar comprovante (PDF)"** |

## Em código

Instrução visível, ligada ao campo, e sigla explicada:

```html
<label for="cpf">CPF</label>
<p id="cpf-ajuda">Só os 11 números. Exemplo: 12345678901.</p>
<input id="cpf" name="cpf" inputmode="numeric"
       autocomplete="off" aria-describedby="cpf-ajuda">

<p>
  O <abbr title="Cadastro de Pessoas Físicas">CPF</abbr>
  é o número que aparece no seu documento.
</p>
```

!!! note "Por que não só o placeholder?"
    O texto do *placeholder* desaparece quando a pessoa começa a digitar. Quem tem memória de trabalho limitada perde a instrução no meio da tarefa.

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 2.4.6 Cabeçalhos e rótulos (*Headings and Labels*) | AA | Rótulos descrevem o propósito |
| 3.3.2 Rótulos ou instruções (*Labels or Instructions*) | A | Instrução visível para entrada de dados |
| 3.1.3 Palavras incomuns (*Unusual Words*) | AAA | Jargão e expressões explicados |
| 3.1.4 Abreviaturas (*Abbreviations*) | AAA | Siglas expandidas |
| 3.1.5 Nível de leitura (*Reading Level*) | AAA | Texto acessível a quem tem ensino fundamental |

**COGA:** Objetivo 3 (conteúdo claro e compreensível) e Objetivo 1 (entender o que as coisas são e como usá-las).

## Como verificar

- [ ] Leia o texto em voz alta. Tropeçou? Reescreva.
- [ ] Algum botão diz só "OK", "Continuar" ou "Clique aqui"?
- [ ] Toda sigla aparece por extenso na primeira vez?
- [ ] A instrução continua visível enquanto a pessoa digita?
- [ ] Um colega de outra área entende sem perguntar nada?

Itens completos no [checklist](../checklist.md#c-clareza).
