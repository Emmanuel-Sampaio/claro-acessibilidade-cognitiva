---
title: R · Ritmo
description: A pessoa controla o tempo — sem cronômetro, sem carrossel automático, sem autoplay, sem sessão que expira em silêncio.
---

<p class="claro-badge tone-r" data-letter="R">Princípio 4 de 5</p>

# Ritmo

**A pessoa usuária controla o tempo.** Sem cronômetro, sem carrossel automático, sem *autoplay*, sem sessão que expira em silêncio.

## O que é

Cada pessoa lê, decide e digita numa velocidade. Quem tem [velocidade de processamento](../perfis/velocidade.md) mais lenta precisa de mais tempo para ler e decidir. Quem tem [dificuldade de atenção](../perfis/atencao.md) perde o foco quando algo se move. Quando o produto impõe o tempo, ele exclui exatamente essas pessoas — e qualquer um que foi interrompido no meio da tarefa.

## Faça / Evite

=== "Faça"

    - Avise **antes** de a sessão expirar e ofereça mais tempo com um clique.
    - Diga no início quanto tempo a sessão dura.
    - Guarde o que foi preenchido se a sessão cair.
    - Dê botão de pausa a tudo que se move por mais de 5 segundos.
    - Respeite `prefers-reduced-motion`.
    - Deixe a pessoa avançar quando quiser — não por tempo.

=== "Evite"

    - Sessão de 5 minutos que cai sem aviso.
    - Carrossel que troca sozinho sem botão de pausa.
    - Vídeo ou áudio que começa a tocar sozinho.
    - Contagem regressiva de "oferta" para pressionar decisão.
    - Mensagem de sucesso que some antes de a pessoa terminar de ler.
    - Redirecionar automaticamente depois de alguns segundos.

## Antes e depois

| Antes | Depois |
|---|---|
| <span class="claro-before">Sessão cai em 5 minutos sem aviso</span> | **Aviso aos 4 minutos + botão "Preciso de mais tempo"** |
| <span class="claro-before">Carrossel de banners troca a cada 3 segundos</span> | **Banners estáticos, ou carrossel parado com setas** |
| <span class="claro-before">"Sucesso!" some em 2 segundos</span> | **Mensagem fica até a pessoa fechar ou seguir** |

## Por dificuldade

Ritmo atende principalmente estas dificuldades. O código está em cada perfil:

| Dificuldade | O que tem de código lá |
|---|---|
| [Velocidade de processamento](../perfis/velocidade.md) | aviso de sessão, mensagens que esperam, vídeo, layout estável |
| [Atenção](../perfis/atencao.md) | pausa no que se move, menos movimento |

## Base normativa

| Critério WCAG 2.2 | Nível | Relação |
|---|---|---|
| 2.2.1 Tempo ajustável (*Timing Adjustable*) | A | Desligar, ajustar ou estender limites de tempo |
| 2.2.2 Pausar, parar, ocultar (*Pause, Stop, Hide*) | A | Controle sobre conteúdo que se move ou atualiza |
| 2.2.3 Sem tempo (*No Timing*) | AAA | Tempo não é parte essencial da tarefa |
| 2.2.5 Nova autenticação (*Re-authenticating*) | AAA | Dados preservados ao logar de novo |
| 2.2.6 Tempo esgotado (*Timeouts*) | AAA | Avisar quanto tempo de inatividade causa perda de dados |
| 1.4.2 Controle de áudio (*Audio Control*) | A | Parar áudio que toca sozinho |

**COGA:** Objetivo 5 (manter o foco) e Objetivo 8 (adaptação e personalização).

## Como verificar

- [ ] Deixe a tela parada por 10 minutos. O que acontece?
- [ ] Tudo que se move tem botão de pausa?
- [ ] Com "reduzir movimento" ativado no sistema, as animações param?
- [ ] Mensagens importantes ficam na tela até a pessoa agir?

Itens completos no [checklist](../checklist.md#r-ritmo).
