"""Ajustes de acessibilidade no HTML gerado pelo MkDocs.

Dá um nome acessível a cada caixa de seleção do checklist,
usando o texto do próprio item da lista.
"""
import re
from html import unescape

_ITEM = re.compile(
    r'(<li class="task-list-item">\s*<label class="task-list-control">\s*<input type="checkbox")'
    r'([^>]*>.*?</label>)(.*?)(?=</li>|<ul|<ol)',
    re.S,
)


def _label(match):
    texto = unescape(re.sub(r"<[^>]+>", "", match.group(3)))
    texto = re.sub(r"\s+", " ", texto).strip().replace('"', "&quot;")
    return f'{match.group(1)} aria-label="{texto}"{match.group(2)}{match.group(3)}'


def on_page_content(html, **kwargs):
    return _ITEM.sub(_label, html)
