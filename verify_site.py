import os
import re

base = '/home/cliente/andre-luiz-pinturas'
index_html = os.path.join(base, 'index.html')
css_path = os.path.join(base, 'css/style.css')
js_path = os.path.join(base, 'js/script.js')

# Load files
with open(index_html, 'r', encoding='utf-8') as f:
    html = f.read()

# Check if the card with fachada has been updated
if 'fachada-casa-residencial.jpg' in html:
    print('Card Pintura Residencial: atualizado com fachada-casa-residencial.jpg')
else:
    print('Card Pintura Residencial: NÃO encontrado na pasta fotos-cliente')

# Find the cards section
cards_open = '      <div class="cards">'
cards_close = '    </div>\n  </section>'
start = html.find(cards_open)
end = html.find(cards_close, start)
if start != -1 and end != -1:
    end += len(cards_close)
    section = html[start:end]
    # Count images and card tags
    img_count = section.count('<img src=')
    card_count = section.count('<article class="card">')
    print(f'Cards no site: {card_count}')
    print(f'Imagens em cards: {img_count}')

# Check CSS for card-image rules
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Check if .card-image and .card-image img are present
if '.card-image {' in css:
    print('CSS: .card-image presente')
else:
    print('CSS: .card-image NÃO presente')

# Check if .card-image img is present
if '.card-image img {' in css:
    print('CSS: .card-image img presente')
else:
    print('CSS: .card-image img NÃO presente')

# Check for placeholder styles (should not have card-placeholder)
if '.card-placeholder {' in css:
    print('CSS: .card-placeholder ainda presente (indesejado)')
else:
    print('CSS: .card-placeholder removido')

# Check for object-fit: cover
if 'object-fit: cover' in css:
    print('CSS: object-fit: cover presente')
else:
    print('CSS: object-fit: cover NÃO presente')
