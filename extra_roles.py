import re

from docutils import nodes


def setup(app):
    app.add_role('fa', fa)
    app.add_role('pypas', pypas)


def fa(name, rawtext, text, lineno, inliner, options={}, content=[]):
    m = re.match(r'((?P<style>[rsb]):)?(?P<icon>[^#]+)(#(?P<color>\w+))?', text)
    match m['style']:
        case 'r':
            style = 'regular'
        case 'b':
            style = 'brands'
        case _:
            style = 'solid'
    icon = m['icon']
    if color := m['color']:
        color = color if color.isalpha() else f'#{color}'
        html_style = f'style="color: {color}"'
    else:
        html_style = ''
    html = f'<i class="fa-{style} fa-{icon}" {html_style}></i>'
    node = nodes.raw('', html, format='html')
    return [node], []


def pypas(name, rawtext, text, lineno, inliner, options={}, content=[]):
    ENLARGE_SYMBOL = '!'
    exercise = text.rstrip(ENLARGE_SYMBOL)
    style = 'font-size: larger' if text.endswith(ENLARGE_SYMBOL) else ''
    html = f'<a href="https://pypas.es">pypas</a>: <b><tt style="{style}">{exercise}</tt></b>'
    node = nodes.raw('', html, format='html')
    return [node], []
