---
title: Antes e depois
description: Como cada princípio vira decisão — exemplos que cabem num critério de aceite e são verificáveis em revisão.
---

# Como o princípio vira decisão

Cada linha abaixo cabe num critério de aceite e é verificável em revisão.

| | Antes | Depois |
|---|---|---|
| **C** | <span class="claro-before">"Prossiga com a validação biométrica facial"</span> | **"Tire uma foto do seu rosto"** |
| **L** | <span class="claro-before">Formulário único com 32 campos</span> | **4 etapas de 8 campos, com barra de progresso** |
| **A** | <span class="claro-before">Código do SMS expira e o campo zera ao voltar</span> | **Colar permitido, campo preservado, 10 minutos** |
| **R** | <span class="claro-before">Sessão cai em 5 minutos sem aviso</span> | **Aviso aos 4 min + botão "Preciso de mais tempo"** |
| **O** | <span class="claro-before">"Erro 422: payload inválido"</span> | **"O CPF tem 11 dígitos. Você digitou 9."** |

!!! quote ""
    Nenhuma dessas mudanças exige tecnologia nova. Exige decisão — e alguém responsável por ela.

## Do exemplo ao critério de aceite

O jeito mais simples de levar o CLARO para a sprint é escrever o "depois" como critério de aceite da história.

=== "C · Clareza"

    ```gherkin
    Cenário: Instrução da captura de selfie
      Dado que estou na etapa de verificação de identidade
      Então vejo o título "Tire uma foto do seu rosto"
      E o texto não contém os termos "biometria", "validação" ou "facial"
      E o botão principal diz "Abrir câmera"
    ```

=== "L · Leveza"

    ```gherkin
    Cenário: Cadastro dividido em etapas
      Dado que inicio o cadastro
      Então vejo no máximo 8 campos por tela
      E vejo o texto "Etapa 1 de 4"
      E existe apenas um botão de ação principal
    ```

=== "A · Apoio à memória"

    ```gherkin
    Cenário: Voltar sem perder o código
      Dado que digitei o código recebido por SMS
      Quando volto para a etapa anterior e avanço de novo
      Então o código continua preenchido
      E consigo colar o código no campo
      E o código vale por 10 minutos
    ```

=== "R · Ritmo"

    ```gherkin
    Cenário: Aviso antes de a sessão expirar
      Dado que fiquei 4 minutos sem interagir
      Então vejo o aviso "Sua sessão vai terminar em 1 minuto"
      Quando clico em "Preciso de mais tempo"
      Então a sessão é renovada
      E nada do que preenchi é perdido
    ```

=== "O · Orientação"

    ```gherkin
    Cenário: CPF incompleto
      Dado que digitei 9 números no campo CPF
      Quando tento avançar
      Então vejo ao lado do campo "O CPF tem 11 dígitos. Você digitou 9."
      E o leitor de tela anuncia a mensagem
      E os 9 números continuam no campo
    ```

## Mais exemplos

| Princípio | Antes | Depois |
|---|---|---|
| C | <span class="claro-before">"Sua solicitação foi deferida"</span> | **"Seu pedido foi aprovado"** |
| C | <span class="claro-before">Botão "OK" no fim do formulário</span> | **"Enviar inscrição"** |
| L | <span class="claro-before">Pop-up de newsletter ao abrir o checkout</span> | **Nenhum pop-up durante a compra** |
| A | <span class="claro-before">CAPTCHA de distorção de letras</span> | **Verificação invisível ou login por link no e-mail** |
| A | <span class="claro-before">Chat de ajuda muda de canto em cada página</span> | **Botão "Ajuda" sempre no mesmo lugar do cabeçalho** |
| R | <span class="claro-before">"Redirecionando em 3… 2… 1…"</span> | **Botão "Continuar" que a pessoa clica quando quiser** |
| O | <span class="claro-before">Excluir conta sem confirmação</span> | **Tela de revisão + digitar "excluir" para confirmar** |
| O | <span class="claro-before">Lixeira que significa "excluir" numa tela e "arquivar" em outra</span> | **Mesmo ícone, mesmo nome, mesma ação em todo o produto** |
