import re

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# Remove o <div class="card-image"> vazio duplicado (linha intermediária)
# Padrão: <div class="card-image">\n<div class="card-image">\n<div class="card-placeholder">
# Para: <div class="card-placeholder">
html, n1 = re.subn(
    r'(<div class="card-placeholder">)',
    lambda m: m.group(1),
    html
)
# O padrão acima não remove o div vazio; vamos usar regex direto:
html, n2 = re.subn(
    r'<div class="card-image">\s*<div class="card-placeholder">',
    r'<div class="card-placeholder">',
    html
)
# Remove o </div> extra (abertura do card-image outer -> fechamento do inner)
html, n3 = re.subn(
    r'(<div class="card-placeholder">.*?</div>\s*</div>)(\s*<span class="card-tag">)',
    r'\1\2',
    html,
    flags=re.DOTALL
)

print('removido div vazio (n1):', n1, ' padrão (n2):', n2, ' padrão (n3):', n3)
open(path, 'w').write(html)
