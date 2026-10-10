import re, os

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# Match: <img src="..." alt="..." loading="lazy"> (a tag img)
# We keep the following <span class="card-tag">...</span>
img_pattern = re.compile(r'(<img\s+src="([^"]+)"\s+alt="([^"]*)"\s+loading="lazy">)\s*(<span class="card-tag">.*?</span>)')

labels = {
    'pintura-residencial.jpg': 'Pintura Residencial',
    'pintura-comercial.jpg': 'Pintura Comercial',
    'massa-corrida.jpg': 'Massa Corrida',
    'grafiato.jpg': 'Grafiato',
    'texturas.jpg': 'Texturas',
    'marmorado.jpg': 'Efeito Mármore',
    'cementio-animado.jpg': 'Cimento Queimado',
    'verniz.jpg': 'Aplicação de Verniz',
    'madeiramento.jpg': 'Madeiramento',
    'portoes.jpg': 'Portões',
    'telhados.jpg': 'Telhados',
}

def replace_img(match):
    src = match.group(2)
    fname = os.path.basename(src)
    label = labels.get(fname, 'Serviço')
    return f'''<div class="card-placeholder">
            <span class="placeholder-icon">🖼️</span>
            <p class="placeholder-text">{label}</p>
            <p class="placeholder-sub">Foto a substituir</p>
          </div>
          {match.group(3)}'''

# Count only img tags that have the exact format
count = len(re.findall(r'<img\s+src="img/servicos/[^"]+\.jpg"', html))
html_new, n = img_pattern.subn(replace_img, html)
print('Imagens substituídas:', n)
open(path, 'w').write(html_new)
