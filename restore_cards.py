import re, os

base = '/home/cliente/andre-luiz-pinturas'
html_path = os.path.join(base, 'index.html')
html = open(html_path).read()

# Card data: (title, description, img_src)
card_data = [
    ('Pintura Residencial', 'Pintura de ambientes internos e externos, com preparação adequada das superfícies para um resultado duradouro.', 'pintura-residencial.jpg'),
    ('Pintura Comercial', 'Serviços de pintura para estabelecimentos comerciais e ambientes profissionais, com punção e rapidez.', 'pintura-comercial.jpg'),
    ('Massa Corrida', 'Preparação e nivelamento de paredes para receber pintura e acabamento, deixando a superfície lisa.', 'massa-corrida.jpg'),
    ('Grafiato', 'Aplicação de grafiato para acabamento decorativo e proteção das paredes.', 'grafiato.jpg'),
    ('Texturas', 'Aplicação de diferentes tipos de texturas decorativas para dar profundidade e aparência única às paredes.', 'texturas.jpg'),
    ('Efeito Mármore', 'Acabamento decorativo inspirado em mármore, com aplicação profissional e resultado homogêneo.', 'marmorado.jpg'),
    ('Efeito Cimento Queimado', 'Aplicação de acabamento moderno com aparência de cimento queimado, leve e durável.', 'cementio-animado.jpg'),
    ('Aplicação de Verniz', 'Proteção e acabamento de superfícies de madeira e outros materiais adequados.', 'verniz.jpg'),
    ('Madeiramento', 'Pintura, proteção e acabamento de estruturas e superfícies de madeira.', 'madeiramento.jpg'),
    ('Portões', 'Pintura e renovação de portões e estruturas metálicas, com proteção contra corrosão.', 'portoes.jpg'),
    ('Lavagem e Pintura de Telhados', 'Limpeza, preparação e pintura de telhados, melhorando a higiene e a durabilidade.', 'telhados.jpg'),
]

new_cards = ''
for title, desc, img_src in card_data:
    new_cards += f'''        <!-- {title} -->
        <article class="card">
          <div class="card-image">
            <img src="img/servicos/{img_src}" alt="{desc}" loading="lazy">
            <span class="card-tag">Serviço</span>
          </div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </article>
'''

# Replace the section between <div class="cards"> and the closing </div>
# Find from "<div class=\"cards\">" up to the "</div>" that closes the cards container
cards_open = '      <div class="cards">'
cards_close = '    </div>\n  </section>'
# Find the index of cards_open and the next occurrence of cards_close
start = html.find(cards_open)
end = html.find(cards_close, start)
if start == -1 or end == -1:
    print('ERROR: cards container not found')
    print('cards_open:', cards_open)
    print('cards_close:', cards_close)
    print('ERROR: cards container not found')
else:
    # The cards container
    cards_block = html[start:end]
    print(f'Found cards block: {len(cards_block)} chars')

    # Find the inner "</div>" for the cards container
    # The structure is: <div class="cards"> ... </div>
    # So we need to find the first "</div>" after cards_open that closes it
    # Actually, we already have the end marker
    # Let's replace from cards_open to end with the new cards
    replacement = f'{cards_open}\n{new_cards}    </div>'
    html_new = html[:start] + replacement + html[end+len(cards_close):]
    open(html_path, 'w').write(html_new)
    print(f'index.html atualizado: {len(html_new)} chars')
