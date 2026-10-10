import re

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# --- Etapa 1: limpar divs duplicadas no card-image ---
# Casos encontrados:
#  a) <div class="card-image">\n<div class="card-placeholder">  ->  <div class="card-placeholder">
#  b) <div class="card-image">\n<div class="card-image">\n<div class="card-placeholder"> -> <div class="card-placeholder">
html, n1 = re.subn(
    r'<div class="card-image">\s*<div class="card-placeholder">',
    r'<div class="card-placeholder">',
    html
)
html, n2 = re.subn(
    r'<div class="card-image">\s*<div class="card-image">\s*<div class="card-placeholder">',
    r'<div class="card-placeholder">',
    html
)

# --- Etapa 2: remover o </div> extra (fechamento do card-image interno)
# Padrão: <div class="card-placeholder">...</div></div><span class="card-tag">
# Substitui por: <div class="card-placeholder">...</div><span class="card-tag">
html, n3 = re.subn(
    r'(<div class="card-placeholder">.*?</div>\s*</div>)(\s*<span class="card-tag">)',
    r'\1\2',
    html,
    flags=re.DOTALL
)

# --- Etapa 3: remover o parágrafo "Foto a substituir" do placeholder ---
html, n4 = re.subn(
    r'<p class="placeholder-sub">Foto a substituir</p>',
    '',
    html
)

# --- Etapa 4: atualizar ícones para significado (sem imagens) ---
icon_map = {
    'Pintura Residencial': '🎨',
    'Pintura Comercial': '🎨',
    'Massa Corrida': '🧱',
    'Grafiato': '🖌️',
    'Texturas': '🧱',
    'Efeito Mármore': '🖌️',
    'Cimento Queimado': '💧',
    'Aplicação de Verniz': '🪵',
    'Madeiramento': '🪚',
    'Portões': '🚪',
    'Telhados': '🏠',
    'Lavagem e Pintura de Telhados': '🏠',
}
for label, icon in icon_map.items():
    html = html.replace(
        f'<p class="placeholder-text">{label}</p>',
        f'<p class="placeholder-text">{icon} {label}</p>'
    )

print(f'Etapas: n1={n1}, n2={n2}, n3={n3}, n4={n4}')
open(path, 'w').write(html)
