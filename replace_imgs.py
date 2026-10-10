import re, os

path = '/home/cliente/andre-luiz-pinturas/index.html'
html = open(path).read()

# Exata: <img src="..." alt="..." loading="lazy">   (sem />)
img_pattern = re.compile(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"\s+loading="lazy">')

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
    src = match.group(1)
    fname = os.path.basename(src)
    label = labels.get(fname, 'Serviço')
    return f'''<div class="card-image">
            <div class="card-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">{label}</p>
              <p class="placeholder-sub">Foto a substituir</p>
            </div>
          </div>'''

html_new, count = img_pattern.subn(replace_img, html)
print('Imagens substituídas:', count)
open(path, 'w').write(html_new)
