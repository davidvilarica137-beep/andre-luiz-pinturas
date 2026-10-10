import os
import re

base = '/home/cliente/andre-luiz-pinturas'
html_path = os.path.join(base, 'index.html')
html = open(html_path).read()

# 1. Substitui o bloco do carrossel (carrossel, carrossel-gallery, portfolio-item)
#    por um container "portfolio-grid" com itens "portfolio-card"
old_carousel = r'''      <div class="carrossel">
        <div class="carrossel-gallery">
          <!-- Cada item é uma "foto" do portfólio: troque src pelo trabalho real -->
          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">Antes e Depois</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">Pintura de Paredes</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">🖌️ Grafiato</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">🧱 Texturas</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">💧 Cimento Queimado</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">🖌️ Efeito Mármore</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">🚪 Portões</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>

          <div class="portfolio-item">
            <div class="portfolio-placeholder">
              <span class="placeholder-icon">🖼️</span>
              <p class="placeholder-text">🏠 Telhados</p>
              <p class="placeholder-sub">Fotografia a substituir</p>
            </div>
          </div>
        </div>
      </div>'''

new_portfolio_grid = '''      <div class="portfolio-grid">
        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-01.jpg" alt="Antes e Depois" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🖼️</span>
            <p class="placeholder-text">Antes e Depois</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-02.jpg" alt="Pintura de Paredes" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🖼️</span>
            <p class="placeholder-text">Pintura de Paredes</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-03.jpg" alt="Grafiato" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🖌️</span>
            <p class="placeholder-text">Grafiato</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-04.jpg" alt="Texturas" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🧱</span>
            <p class="placeholder-text">Texturas</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-05.jpg" alt="Cimento Queimado" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">💧</span>
            <p class="placeholder-text">Cimento Queimado</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-06.jpg" alt="Efeito Mármore" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🖌️</span>
            <p class="placeholder-text">Efeito Mármore</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-07.jpg" alt="Portões" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🚪</span>
            <p class="placeholder-text">Portões</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>

        <div class="portfolio-card">
          <img src="img/portfolio/portfolio-08.jpg" alt="Telhados" loading="lazy">
          <div class="portfolio-text">
            <span class="placeholder-icon">🏠</span>
            <p class="placeholder-text">Telhados</p>
            <p class="placeholder-sub">Fotografia a substituir</p>
          </div>
        </div>
      </div>'''

# Substitui o bloco do carrossel
if old_carousel in html:
    html = html.replace(old_carousel, new_portfolio_grid)
    print('Bloco carrossel substituído por portfolio-grid.')
else:
    print('Bloco carrossel nao encontrado. Verificando...')
    # Tenta encontrar vagamente
    if 'portfolio-item' in html:
        print('  Found portfolio-item in HTML.')
    else:
        print('  No portfolio-item found.')

# 2. Substitui o texto de placeholder (se necessário)
html = html.replace(
    '<span class="placeholder-icon">🖼️</span>',
    '<span class="placeholder-icon">🖼️</span>'
)

open(html_path, 'w').write(html)
print('Arquivo index.html atualizado.')
