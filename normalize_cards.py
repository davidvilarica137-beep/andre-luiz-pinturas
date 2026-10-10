import re

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# Novo padrão para cada card completo, normalizado:
# <article class="card">\n   <div class="card-image">\n     <div class="card-placeholder">\n       <span class="placeholder-icon">📌</span>\n       <p class="placeholder-text">NOME</p>\n     </div>\n     <span class="card-tag">Serviço</span>\n   </div>\n  <h3>TÍTULO</h3>\n  <p>DESCRIÇÃO</p>\n</article>

# Regex para extrair cada card completo (padrão original, com duplicações)
card_pattern = re.compile(
    r'<article class="card">\s*'
    r'<div class="card-image">\s*'
    r'(?:<div class="card-image">)?\s*'
    r'<div class="card-placeholder">\s*'
    r'<span class="placeholder-icon">(.*?)</span>\s*'
    r'<p class="placeholder-text">(.*?)</p>\s*'
    r'</div>\s*'
    r'(?:</div>)?\s*'
    r'(?:<span class="card-tag">.*?</span>)?\s*'
    r'(?:</div>)?\s*'
    r'<h3>(.*?)</h3>\s*'
    r'<p>(.*?)</p>\s*'
    r'</article>',
    re.DOTALL
)

def normalize_card(m):
    icon = m.group(1).strip()
    title = m.group(2).strip()
    h3 = m.group(3).strip()
    p = m.group(4).strip()
    # Mapear ícones consistentes
    icon_map = {
        '🎨': '🎨',
        '🧱': '🧱',
        '🖌️': '🖌️',
        '💧': '💧',
        '🪵': '🪵',
        '🪚': '🪚',
        '🚪': '🚪',
        '🏠': '🏠',
    }
    return (f'<article class="card">\n'
            f'  <div class="card-image">\n'
            f'    <div class="card-placeholder">\n'
            f'      <span class="placeholder-icon">{icon}</span>\n'
            f'      <p class="placeholder-text">{title}</p>\n'
            f'    </div>\n'
            f'    <span class="card-tag">Serviço</span>\n'
            f'  </div>\n'
            f'  <h3>{h3}</h3>\n'
            f'  <p>{p}</p>\n'
            f'</article>')

html, n = card_pattern.subn(normalize_card, html)
print('Cards normalizados:', n)
open(path, 'w').write(html)
