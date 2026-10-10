import re

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# Remove o div card-image duplicado: <div class="card-image">\n<div class="card-image">\n<div class="card-placeholder">
html, n1 = re.subn(
    r'<div class="card-image">\s*<div class="card-placeholder">',
    r'<div class="card-placeholder">',
    html
)

# Remove o </div> extra que fechava o card-image interno (deixa o tag card-tag fora)
html, n2 = re.subn(
    r'(<div class="card-placeholder">.*?</div>\s*</div>)(\s*<span class="card-tag">)',
    r'\1\2',
    html,
    flags=re.DOTALL
)

print('removido div vazio (n1):', n1, '| remoção </div> extra (n2):', n2)
open(path, 'w').write(html)
