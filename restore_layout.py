import re, os, shutil

base = '/home/cliente/andre-luiz-pinturas'

# ---------- 1. BACKUP CURRENT FILES (remake for traceability) ----------
os.makedirs(os.path.join(base, '.backup'), exist_ok=True)
shutil.copy2(os.path.join(base, 'index.html'),
             os.path.join(base, '.backup', 'index.html.current.bak'))
shutil.copy2(os.path.join(base, 'css/style.css'),
             os.path.join(base, '.backup', 'style.css.current.bak'))
shutil.copy2(os.path.join(base, 'js/script.js'),
             os.path.join(base, '.backup', 'script.js.current.bak'))
print('Backups atuais feitos:')
for f in os.listdir(os.path.join(base, '.backup')):
    print('  .backup/' + f)

# ---------- 2. RESTORE index.html: cards with <img src> (original layout) ----------
html_path = os.path.join(base, 'index.html')
html = open(html_path).read()

# Each broken card has the structure:
#   <div class="card-image"> (sometimes nested twice)
#     <div class="card-placeholder">
#       <span class="placeholder-icon">...</span>
#       <p class="placeholder-text">NAME</p>
#       (optionally <p class="placeholder-sub">...</p>)
#     </div>
#   (extra </div>)
#   <span class="card-tag">Serviço</span>
# </div>

# Strip all placeholder content from cards, leaving only the card-image div,
# and place the <img> back.

# Define the original img tags per card
cards = [
    ('pintura-residencial.jpg', 'Parede sendo pintada com rolo e pincel'),
    ('pintura-comercial.jpg', 'Fazendinha ou loja sendo pintada'),
    ('massa-corrida.jpg', 'Massa corrida em parede'),
    ('grafiato.jpg', 'Parede com grafiato'),
    ('texturas.jpg', 'Parede com textura aplicada'),
    ('marmorado.jpg', 'Parede com efeito mármore'),
    ('cementio-animado.jpg', 'Parede com acabamento de cimento queimado'),
    ('verniz.jpg', 'Madeira recebendo verniz'),
    ('madeiramento.jpg', 'Estrutura de madeira sendo preparada'),
    ('portoes.jpg', 'Portão metálico sendo pintado'),
    ('telhados.jpg', 'Telhado sendo limpo e preparado'),
]

def build_card(img_src, alt_text):
    return f'''        <article class="card">
          <div class="card-image">
            <img src="img/servicos/{img_src}" alt="{alt_text}" loading="lazy">
            <span class="card-tag">Serviço</span>
          </div>
          <h3>TITLE</h3>
          <p>DESCRIPTION</p>
        </article>'''

# Find each card's title and description for replacement
# The current cards have: <h3>TITLE</h3> <p>DESCRIPTION</p> after the placeholder
for img_src, alt in cards:
    # Replace the broken card with the original card using the image
    # We find: <div class="card-placeholder">...</div> then <span class="card-tag">Serviço</span>
    # and rebuild the whole card
    pass

# Actually, let's do a cleaner approach: replace each broken card
for img_src, alt in cards:
    # Build the replacement card
    card_html = f'''        <article class="card">
          <div class="card-image">
            <img src="img/servicos/{img_src}" alt="{alt}" loading="lazy">
            <span class="card-tag">Serviço</span>
          </div>
          <h3>{TITLE}</h3>
          <p>{DESC}</p>
        </article>'''

# Let me do it differently - regex replace each broken card block
# Pattern: from <article class="card"> to </article>, with the broken structure
# We'll replace with the original card structure

# First, let's find all card titles and descriptions in order
# The cards in order (from the HTML):
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

# Build the full replacement
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

# Replace the broken cards section between <div class="cards"> and </div>
# Find from "<div class=\"cards\">" to "</div>" (the closing of cards container)
# But we need to find the exact blocks.
pattern = re.compile(
    r'<div class="cards">\s*'
    r'(?:<!--.*?-->)?'
    r'(?:<article class="card">.*?</article>\s*){11}'
    r'</div>',
    re.DOTALL
)

# Count how many cards are in the current HTML
cards_found = re.findall(r'<article class="card">', html)
print(f'Cards encontrados: {len(cards_found)}')

# Replace all broken cards
# Pattern: for each card, find from <article class="card"> to </article>
def replace_one_card(m):
    return new_cards

html_new, n = re.subn(
    r'<article class="card">.*?</article>',
    replace_one_card,
    html,
    flags=re.DOTALL
)
print(f'Removidos {n} cards quebrados')

open(html_path, 'w').write(html_new)
print('index.html restaurado')

# ---------- 3. RESTORE css/style.css ----------
css_path = os.path.join(base, 'css/style.css')
css = open(css_path).read()

# Replace the broken .card-image and .card-placeholder rules with original
# Original .card-image
original_card_image = '''/* ---------- SERVIÇOS (cards) ---------- */
.servicos {
  background: #fff;
}

.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.card {
  background: var(--cor-fundo);
  border: 1px solid var(--cor-separador);
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: 0 4px 14px var(--cor-sombra);
  transition: transform 0.25s, box-shadow 0.25s;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 10px 28px var(--cor-sombra);
}

.card-image {
  position: relative;
  height: 200px;
  overflow: hidden;
  border-radius: var(--border-radius) var(--border-radius) 0 0;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s;
}

.card:hover .card-image img {
  transform: scale(1.06);
}

.card-tag {'''

# Replace the broken card rules
css = re.sub(
    r'\.card-image \{[^}]*\}',
    original_card_image,
    css,
    flags=re.DOTALL
)

# Also replace the broken .card-placeholder rules (they are separate)
# Find .card-placeholder and .placeholder-icon etc and remove them
css = re.sub(
    r'\.card-placeholder \{[^}]*\}',
    '',
    css,
    flags=re.DOTALL
)
css = re.sub(
    r'\.placeholder-icon \{[^}]*\}',
    '',
    css,
    flags=re.DOTALL
)
css = re.sub(
    r'\.placeholder-text \{[^}]*\}',
    '',
    css,
    flags=re.DOTALL
)
css = re.sub(
    r'\.placeholder-sub \{[^}]*\}',
    '',
    css,
    flags=re.DOTALL
)

open(css_path, 'w').write(css)
print('css/style.css restaurado')

# ---------- 4. Recreate img structure ----------
# Ensure img/servicos has the original files
orig_servicos = {
    'pintura-residencial.jpg': 'pexels-mitchel3uo-4115537.jpg',
    'pintura-comercial.jpg': 'pexels-ted-mcdonnell-18880226.jpg',
    'massa-corrida.jpg': 'pexels-mikhail-nilov-8391475.jpg',
    'grafiato.jpg': 'pexels-marcu-ioachim-440423-12901948.jpg',
    'texturas.jpg': 'pexels-shkrabaanthony-5493654.jpg',
    'marmorado.jpg': 'pexels-shkrabaanthony-5493669.jpg',
    'cementio-animado.jpg': 'pexels-turgay-koca-405356598-14916714.jpg',
    'verniz.jpg': 'pexels-tima-miroshnichenko-6474480.jpg',
    'madeiramento.jpg': 'pexels-tiago-alves-710726839-19919870.jpg',
    'portoes.jpg': 'pexels-mikhail-nilov-8391475.jpg',
    'telhados.jpg': 'pexels-turgay-koca-405356598-14916714.jpg',
}

# These are placeholders mapped to real downloaded files in img/fotos-cliente/
# But the user wants to confirm real photos. So we keep them as files but NOT referenced.
# Actually, let's keep img/servicos as is (original Pexels placeholders) and NOT touch.

# Remove the broken img/data and img/servicos/img folders
for d in ['img/data', 'img/servicos/img']:
    if os.path.exists(os.path.join(base, d)):
        shutil.rmtree(os.path.join(base, d))
        print(f'Removida pasta: {d}')

# Create img/data as a real data folder (if needed)
os.makedirs(os.path.join(base, 'img/data'), exist_ok=True)

print('Estrutura de img/ confirmada:')
for root, dirs, files in os.walk(os.path.join(base, 'img')):
    for f in sorted(files):
        print('  ' + os.path.relpath(os.path.join(root, f), base))
