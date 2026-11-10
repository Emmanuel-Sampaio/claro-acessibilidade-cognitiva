---
title: A · Apoio à memória
description: Nada de decorar — dados já informados persistem, códigos não migram de tela, a ajuda fica sempre no mesmo lugar.
---

<p class="claro-badge tone-a" data-letter="A">Princípio 3 de 5</p>

# Apoio à memória

**Nada de decorar.** Dados já informados persistem, o código não migra de tela, a ajuda fica sempre no mesmo lugar.

## O que é

Toda vez que o produto pede para a pessoa **lembrar**, **copiar à mão** ou **redigitar** algo, ele transfere trabalho do sistema para a memória dela. Para quem tem [dificuldade de memória](../perfis/memoria.md) — por qualquer motivo, permanente ou passageiro —, esse é um dos pontos de abandono mais comuns.

A WCAG 2.2 trouxe três critérios novos exatamente aqui: 3.2.6, 3.3.7 e 3.3.8.

## Faça / Evite

=== "Faça"

    - Reaproveite o que já foi informado no mesmo processo.
    - Permita **colar** senhas e códigos.
    - Deixe o gerenciador de senhas funcionar.
    - Use `autocomplete` nos campos de dados pessoais.
    - Mantenha o que foi preenchido ao voltar uma etapa.
    - Ajuda (contato, chat, dúvidas) sempre no mesmo lugar.

=== "Evite"

    - Pedir o mesmo endereço duas vezes no mesmo fluxo.
    - Bloquear colar no campo de senha ou de confirmação de e-mail.
    - CAPTCHA de quebra-cabeça, transcrição ou cálculo sem alternativa.
    - Código que precisa ser decorado numa tela e digitado em outra.
    - Apagar o formulário quando a pessoa volta ou erra.
    - Ajuda que muda de posição em cada página.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">Código do SMS expira e o campo zera ao voltar</span> | **Colar permitido, campo preservado, validade de 10 minutos** |
| <span class="claro-before">"Repita seu e-mail" com colar bloqueado</span> | **Um campo de e-mail, com confirmação por link** |
| <span class="claro-before">Endereço de entrega e de cobrança digitados duas vezes</span> | **Caixa "Usar o mesmo endereço da entrega" marcada por padrão** |

## Por dificuldade

Apoio à memória atende principalmente estas dificuldades. O código está em cada perfil:

| Dificuldade | O que tem de código lá |
|---|---|
| [Memória](../perfis/memoria.md) | autocomplete, colar código, rascunho, copiar protocolo |
| [Números e cálculo](../perfis/numeros.md) | o sistema faz a conta pela pessoa |

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 3.3.7 Entrada redundante (*Redundant Entry*) | A | Não pedir de novo o que já foi informado |
| 3.3.8 Autenticação acessível — mínimo (*Accessible Authentication (Minimum)*) | AA | Login sem teste cognitivo |
| 3.3.9 Autenticação acessível — aprimorado (*Accessible Authentication (Enhanced)*) | AAA | Sem exceções de reconhecimento de objetos |
| 3.2.6 Ajuda consistente (*Consistent Help*) | A | Ajuda no mesmo lugar relativo |
| 1.3.5 Identificar o propósito da entrada (*Identify Input Purpose*) | AA | `autocomplete` em dados pessoais |

**COGA:** Objetivo 6 (processos que não dependem da memória) e Objetivo 7 (ajuda e suporte).

## Como verificar

- [ ] Percorra o fluxo inteiro: algum dado foi pedido duas vezes?
- [ ] Dá para colar no campo de senha e no de código?
- [ ] Volte uma etapa: o que foi digitado continua lá?
- [ ] O link de ajuda está no mesmo lugar em todas as telas?

Itens completos no [checklist](../checklist.md#a-apoio-a-memoria).
