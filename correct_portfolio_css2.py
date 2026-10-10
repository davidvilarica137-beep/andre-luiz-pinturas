import os
import re

base = '/home/cliente/andre-luiz-pinturas'
css_path = os.path.join(base, 'css/style.css')
css = open(css_path).read()

# --- CSS CORRIGIDO: PORTFÓLIO em grade de 4 colunas (desktop), 2 (tablet) e 1 (mobile) ---
new_portfolio_css = '''
/* ---------- PORTFÓLIO ---------- */
.portfolio {
  background: var(--cor-slide);
}

/* Grid unificado para o portfólio: 4 colunas em desktop, 2 em tablet e 1 em mobile */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 20px;
  width: 100%;
  align-items: stretch;
}

/* Itens do portfólio: área de imagem grande e alinhada */
.portfolio-card {
  width: 100%;
  min-width: 0;
  overflow: hidden;
  border-radius: var(--border-radius);
  background: var(--cor-fundo);
  border: 1px solid var(--cor-separador);
  box-shadow: 0 6px 18px var(--cor-sombra);
}

.portfolio-card img {
  display: block;
  width: 100%;
  height: 240px;
  object-fit: cover;
  object-position: center;
}

/* Texto do portfólio: título e descrição abaixo da imagem */
.portfolio-card .portfolio-text {
  padding: 16px 16px 12px;
  text-align: center;
}

.portfolio-card .portfolio-text .placeholder-icon {
  font-size: 2rem;
  color: var(--cor-primaria);
  margin-bottom: 8px;
}

.portfolio-card .portfolio-text .placeholder-text {
  font-weight: 700;
  font-size: 1rem;
  color: var(--cor-primaria);
  margin-bottom: 4px;
  word-break: break-word;
}

.portfolio-card .portfolio-text .placeholder-sub {
  font-size: 0.85rem;
  color: var(--cor-texto-secundario);
}

/* Responsividade do portfólio */
@media (max-width: 1024px) {
  .portfolio-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .portfolio-grid {
    grid-template-columns: repeat(1, minmax(0, 1fr));
    gap: 16px;
  }
}

@media (max-width: 480px) {
  .portfolio-grid {
    grid-template-columns: repeat(1, minmax(0, 1fr));
    gap: 12px;
  }
}

/* ---------- SERVIÇOS (cards) ---------- */
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

.card-tag {
  position: absolute;
  top: 12px;
  right: 12px;
  background: var(--cor-primaria);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 4px 12px;
  border-radius: 20px;
}

.card h3 {
  font-size: 1.15rem;
  color: var(--cor-primaria);
  margin: 16px 16px 8px;
}

.card p {
  font-size: 0.95rem;
  color: var(--cor-texto-secundario);
  margin: 0 16px 16px;
}
'''

# Substitui o bloco do carrossel (início em .portfolio até o fim do .portfolio-item)
# e todas as regras do carrossel que não servem mais.
pattern = r'/\* ---------- PORTFÓLIO ---------- \*/\n\.portfolio \{\n  background: var\(--cor-slide\);\n}\n\n\.carrossel \{[^}]*\}\n\n\.carrossel::-webkit-scrollbar \{[^}]*\}\n\n\.carrossel::-webkit-scrollbar-thumb \{[^}]*\}\n\n\.carrossel-gallery \{[^}]*\}\n\n\.portfolio-item \{[^}]*\}\n\n\.portfolio-placeholder \{[^}]*\}\n\n\.placeholder-icon \{[^}]*\}\n\n\.placeholder-text \{[^}]*\}\n\n\.placeholder-sub \{[^}]*\}'

replacement = new_portfolio_css
css, n = re.subn(pattern, replacement, css, flags=re.DOTALL)

# Se não encontrou o padrão, tenta alternativa: apenas substituir de "/* ---------- PORTFÓLIO ---------- */"
# até a parte do ORÇAMENTO.
if n == 0:
    # Encontra o início do portfolio e o fim do orcamento
    start = css.find('/* ---------- PORTFÓLIO ---------- */')
    end = css.find('/* ---------- ORÇAMENTO ---------- */', start)
    if start != -1 and end != -1:
        end += len('/* ---------- ORÇAMENTO ---------- */')
        css = css[:start] + new_portfolio_css + css[end:]
        n = 1

print(f'Respostas substituídas: {n}')
open(css_path, 'w').write(css)
