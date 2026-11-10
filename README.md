# CLARO

**Framework de boas práticas para acessibilidade cognitiva e de aprendizagem.**

Um guia operacional em português para times de produto traduzirem o W3C COGA e a WCAG 2.2 em decisões concretas de design, conteúdo e código.

📖 **Documentação:** <https://emmanuel-sampaio.github.io/claro-acessibilidade-cognitiva/>

| | Princípio | Em uma frase |
|---|---|---|
| **C** | Clareza | Linguagem simples e direta. |
| **L** | Leveza | Uma tarefa por tela. |
| **A** | Apoio à memória | Nada de decorar. |
| **R** | Ritmo | A pessoa controla o tempo. |
| **O** | Orientação | Onde estou, o que fazer, como desfazer. |

## Seis perfis por dificuldade

Atenção · Memória · Leitura e linguagem · Números e cálculo · Planejamento e organização · Velocidade de processamento — cada um com barreiras, base normativa (WCAG 2.2 + COGA), teste e código.

## O que tem aqui

- `docs/` — conteúdo do site em Markdown
- `docs/perfis/` — perfis por dificuldade, com código
- `docs/normas/` — WCAG 2.2, COGA e matriz normativa
- `docs/checklist.md` — checklist de 30 itens (rascunho v0.2)
- `docs/avaliacao.md` — método de avaliação e rubrica de 0 a 4
- `docs/assets/` — pitch em PDF e modelo de planilha de avaliação
- `mkdocs.yml` — configuração do site (MkDocs + Material)

## Rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Abra <http://127.0.0.1:8000>. O site recarrega ao salvar qualquer arquivo em `docs/`.

## Publicação

Cada push na branch `main` publica o site no GitHub Pages pelo workflow `.github/workflows/deploy.yml`.

## Status

Versão **0.2.0** — perfis por dificuldade e normas reestruturadas. Projeto iniciado com o pitch da disciplina *Tópicos em Acessibilidade Digital* (UFC, 2026.2). Veja o [CHANGELOG](CHANGELOG.md).

## Licença

- Conteúdo: [CC BY 4.0](LICENSE)
- Exemplos de código: MIT

Autoria: Emmanuel Sampaio · Universidade Federal do Ceará
