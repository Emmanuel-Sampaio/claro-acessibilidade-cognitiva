---
title: Leitura e linguagem
description: Perfil de dificuldade de leitura e linguagem — decodificar palavras, entender frases longas, vocabulário técnico e sentido figurado.
---

<p class="claro-badge tone-p" data-letter="3">Perfil 3 de 9</p>

# Leitura e linguagem

**Dificuldade para decodificar palavras, entender frases longas ou técnicas e interpretar sentido figurado, ironia ou o que está implícito.**

Princípio mais ligado: [C · Clareza](../principios/clareza.md).

## Na prática

- Ler cansa. Blocos densos de texto são pulados — junto com a informação importante.
- Jargão, siglas e palavras raras param a leitura.
- Metáfora e ironia são lidas ao pé da letra: "seu carrinho está pegando fogo" não vira "promoção".
- Fonte apertada, linhas longas e texto justificado fazem o olho perder a linha.
- Ícone sem texto é um enigma.

!!! example "Uma cena"
    Lia lê devagar e relê frases longas. A tela diz: "Proceda à anexação do comprovante de residência atualizado". Ela não sabe se "atualizado" quer dizer deste mês ou deste ano, e não encontra onde fica o botão de anexar.

## Barreira → o que ajuda

| Barreira | O que ajuda |
|---|---|
| Frases longas e voz passiva | Frases curtas, voz ativa, uma ideia por frase |
| Jargão e siglas | Palavra do dia a dia; sigla explicada na primeira vez |
| Implícito ("atualizado") | Dizer o que se quer: "dos últimos 3 meses" |
| Metáfora, ironia, trocadilho | Linguagem literal em instruções e erros |
| Linhas longas, texto justificado | Até ~70 caracteres por linha, alinhado à esquerda |
| Ícone sozinho | Ícone **com** texto |
| Documento longo | Resumo no topo |

## Em código

### 1. Texto que o olho consegue seguir

```css
.conteudo {
  max-width: 70ch;            /* linhas curtas */
  font-size: 1.125rem;
  line-height: 1.6;
  text-align: left;           /* nunca justify */
}
.conteudo p + p { margin-top: 1em; }

/* Deixe a pessoa aumentar espaçamentos sem quebrar o layout:
   use min-height, nunca height fixa, em caixas com texto */
.cartao { min-height: 8rem; }
```

### 2. Termo difícil explicado ali mesmo

```html
<p>
  Envie o <abbr title="Documento Auxiliar da Nota Fiscal Eletrônica">DANFE</abbr>
  junto com a foto do produto.
</p>
<details class="explica">
  <summary>O que é o DANFE?</summary>
  <p>É a folha impressa que vem dentro da caixa do produto, junto com a nota fiscal.</p>
</details>
```

### 3. Ícone sempre acompanhado de texto

```html
<!-- Evite: só o ícone, com o nome escondido -->
<button type="button" aria-label="Excluir"><svg aria-hidden="true">…</svg></button>

<!-- Prefira: ícone + palavra visível -->
<button type="button">
  <svg aria-hidden="true" focusable="false">…</svg>
  Excluir arquivo
</button>
```

### 4. Resumo antes do texto longo

```html
<section aria-labelledby="resumo">
  <h2 id="resumo">Resumo</h2>
  <ul>
    <li>Prazo: até 30 de novembro.</li>
    <li>Você precisa de: RG e comprovante de residência dos últimos 3 meses.</li>
    <li>Custo: gratuito.</li>
  </ul>
</section>

<!-- Palavra estrangeira sem tradução boa? Marque o idioma
     para o leitor de tela pronunciar certo. -->
<p>Ative o <span lang="en">Bluetooth</span> do celular.</p>
```

### Reescrita: antes e depois

| Antes | Depois |
|---|---|
| "Proceda à anexação do comprovante de residência atualizado" | "Envie uma conta de luz, água ou telefone dos últimos 3 meses" |
| "Sua solicitação foi deferida" | "Seu pedido foi aprovado" |
| "Não deixe de não esquecer o documento" | "Leve o documento" |
| "Seu carrinho está pegando fogo! 🔥" | "Os itens do seu carrinho estão com desconto até sexta" |

## Base normativa

**COGA** — Objetivo 3 (conteúdo claro) e Objetivo 1 (entender o que as coisas são):
4.4.1 Palavras claras · 4.4.2 Tempo verbal e voz simples · 4.4.3 Sem dupla negação nem orações encaixadas · 4.4.4 Linguagem literal · 4.4.5 Texto sucinto · 4.4.8 Resumo de documentos longos · 4.4.9 Uma instrução por vez · 4.4.10 Espaço em branco · 4.4.12 Explicar o que está implícito · 4.2.7 Ícones que ajudam · 4.8.2 Alternativa para conteúdo complexo.

| Critério WCAG 2.2 | Nível | O que pede |
|---|---|---|
| 2.4.6 Cabeçalhos e rótulos | AA | Títulos e rótulos descrevem o propósito |
| 1.4.12 Espaçamento de texto | AA | Nada quebra quando a pessoa aumenta espaçamentos |
| 3.1.2 Idioma de partes | AA | Trechos em outro idioma marcados |
| 1.4.8 Apresentação visual | AAA | Linhas curtas, sem justificar, espaçamento adequado |
| 3.1.3 Palavras incomuns | AAA | Jargão e expressões explicados |
| 3.1.4 Abreviaturas | AAA | Siglas expandidas |
| 3.1.5 Nível de leitura | AAA | Texto acessível a quem tem ensino fundamental |

## Como testar

- [ ] Ouça o texto num leitor de voz (o do próprio celular serve). Você tropeça em alguma frase?
- [ ] Cole o texto num índice de legibilidade adaptado ao português (Flesch). Ele é de nível fundamental?
- [ ] Peça a alguém de fora do projeto que explique com as próprias palavras o que a tela pede.
- [ ] Procure ícones sem texto, siglas sem explicação e frases com mais de 20 palavras.
