import re

base = '/home/cliente/andre-luiz-pinturas'
html_path = os.path.join(base, 'index.html')
html = open(html_path).read()

# Build the new cards block (correct structure)
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

cards_block = '      <div class="cards">\n'
for title, desc, img_src in card_data:
    cards_block += f'''        <!-- {title} -->
        <article class="card">
          <div class="card-image">
            <img src="img/servicos/{img_src}" alt="{desc}" loading="lazy">
            <span class="card-tag">Serviço</span>
          </div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </article>
'''

# Find <div class="cards"> and the first </div> after it
cards_open = '      <div class="cards">'
cards_close = '    </div>\n  </section>'
start = html.find(cards_open)
end = html.find(cards_close, start)
if start == -1 or end == -1:
    print(f'ERRO: cards not found. start={start}, end={end}')
else:
    # end is end of 'cards_close', so replace from start to end with new block
    end += len(cards_close)
    new_html = html[:start] + cards_block + html[end:]
    open(html_path, 'w').write(new_html)
    print(f'restorado: {len(cards_block)} chars')
