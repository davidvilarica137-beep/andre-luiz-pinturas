# André Luiz — Arte e Pinturas

Site corporativo profissional, moderno e responsivo para pintor autônomo.

## 📋 O que o site faz

- Apresenta quem é o André Luiz e o que ele faz.
- Mostra os serviços oferecidos em cards modernos.
- Exibe um portfólio preparado para inserção de fotos reais.
- Possibilita solicitar orçamento pelo WhatsApp com mensagem pré-preenchida.
- Botão flutuante de WhatsApp sempre visível.
- Totalmente responsivo: celulares, tablets e desktop.
- Feito apenas com HTML, CSS e JavaScript puro — sem frameworks, banco de dados ou serviços pagos.

---

## 📁 Estrutura do projeto

```
andre-luiz-pinturas/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── img/
│   ├── hero/
│   ├── servicos/
│   └── portfolio/
├── README.md
└── .gitignore
```

| Pasta / Arquivo | Função |
|---|---|
| `index.html` | Página principal com todas as seções |
| `css/style.css` | Estilos responsivos |
| `js/script.js` | Menu hamburger, rolagem suave e configurações JS |
| `img/hero/` | Imagens de destaque (hero, sobre, orçamento) |
| `img/servicos/` | Fotos ilustrativas dos serviços |
| `img/portfolio/` | Fotos dos trabalhos (antes e depois) |
| `README.md` | Este arquivo — instruções de execução e publicação |
| `.gitignore` | Arquivos ignorados no Git |

---

## 🚀 Como executar localmente

1. **Baixe os arquivos** para a sua máquina.

2. **Abra o arquivo `index.html`** em qualquer navegador:
   - No Linux: abra-o com o seu navegador (Firefox, Chrome, etc.) ou execute:
     ```bash
     xdg-open index.html
     ```
   - Ou simplesmente arraste o arquivo para o navegador.

3. **Não é necessário instalar nada** — HTML, CSS e JS são executados diretamente no navegador.

4. **Para testar o WhatsApp ou o telefone de telefone**, substitua o número nas URLs do código e rode um servidor local (veja abaixo).

> 💡 Dica: para testar links de WhatsApp e além, é recomendado rodar um servidor HTTP local:
> ```bash
> cd andre-luiz-pinturas
> python3 -m http.server 8000
> ```
> Em seguida acesse `http://localhost:8000`.

---

## 🖼️ Como substituir as imagens

O site já vem com imagens de **ilustração** (para não inventar trabalhos reais). Para trocar por fotos reais:

1. Substitua os arquivos em:
   - `img/hero/` — para a seção hero, sobre e orçamento.
   - `img/servicos/` — para as fotos dos serviços.
   - `img/portfolio/` — para os itens do portfólio.

2. O referido arquivo deve ser:
   - `JPG` ou `PNG`
   - Tamanho sugerido: 1200 × 630 pixels (hero) ou 600 × 400 (serviços)

3. **Importante:** o HTML está preparado para easymente substituição. Os caminhos nos `<img>` apontam para os arquivos corretos. Basta colocar a nova foto com o mesmo nome e substituí-la.

> ⚠️ Não é necessário alterar o código se você usar os mesmos nomes, apenas substitua o arquivo.

---

## 📷 Fotos reais necessárias — lista para solicitar ao cliente

Este projeto está preparado com **imagens de ilustração**. Para a versão final, as seguintes fotos reais são necessárias. Solicite ao cliente André Luiz as imagens indicadas abaixo e substitua os arquivos de exemplo pelos reais, mantendo os mesmos nomes e pastas.

### Pasta `img/hero/`

| Nome do arquivo | Qtd | Objetivo no site | Tamanho sugerido |
|---|---|---|---|
| `hero.jpg` | 1 | Seção hero (apresentação inicial) | 1200 × 630 px |
| `sobre.jpg` | 1 | Foto do André Luiz ou equipe no rodapé | 600 × 600 px |
| `orcamento.jpg` | 1 | Ilustração da seção Orçamento | 600 × 400 px |

> Essas 3 imagens substituem os atuais `or` (hero), `or` (orçamento) e `sobre.jpg`.

### Pasta `img/servicos/`

| Nome do arquivo | Serviço correspondente | Observação |
|---|---|---|
| `pintura-residencial.jpg` | Pintura Residencial | Parede interna sendo pintada |
| `pintura-comercial.jpg` | Pintura Comercial | Estabelecimento comercial pintando |
| `massa-corrida.jpg` | Massa Corrida | Parede nivelada/preparada |
| `grafiato.jpg` | Grafiato | Parede com grafiato aplicado |
| `texturas.jpg` | Texturas | Parede com textura decorativa |
| `marmorado.jpg` | Efeito Mármore | Parede com acabamento em mármore |
| `cementio-animado.jpg` | Efeito Cimento Queimado | Parede queimada, leve e moderna |
| `verniz.jpg` | Aplicação de Verniz | Madeira ou superfície com verniz |
| `madeiramento.jpg` | Madeiramento | Estrutura de madeira preparada |
| `portoes.jpg` | Portões | Portão metálico sendo pintado/renovado |
| `telhados.jpg` | Lavagem e Pintura de Telhados | Telhado limpo e preparado |
| `telhados.jpg` | Lavagem e Pintura de Telhados | (exemplo de telhado) |

> Os 12 arquivos acima substituem diretamente o conteúdo dos cards de serviço.

### Pasta `img/portfolio/`

| Nome do arquivo | Tipo de trabalho | Observação |
|---|---|---|
| `portfolio-01.jpg` | Antes e Depois | Mostrar a evolução de um projeto |
| `portfolio-02.jpg` | Pintura de Paredes | Trabalho real concluído |
| `portfolio-03.jpg` | Grafiato | Característica gráfica aplicada |
| `portfolio-04.jpg` | Texturas | Textura decorativa aplicada |
| `portfolio-05.jpg` | Cimento Queimado | Acabamento moderno |
| `portfolio-06.jpg` | Efeito Mármore | Acabamento em mármore |
| `portfolio-07.jpg` | Portões | Portão pintado ou renovado |
| `portfolio-08.jpg` | Telhados | Telhado pintado ou limpo |

> Os 8 arquivos acima substituem os placeholders de portfólio. Pode haver menos fotos se o cliente tiver menos trabalhos — o HTML está preparado para receber quantas forem fornecidas.

### Formato e Banco de Imagens

1. **Formato:** JPG ou PNG de alta qualidade.
2. **Nome dos arquivos:** use os mesmos nomes das tabelas acima, para manter a compatibilidade sem alterar o HTML.
3. **Dimensões:**
   - `img/hero/`: 1200 × 630 px (hero) e 600 × 600 px (foto de perfil/sobre).
   - `img/servicos/`: 600 × 400 px (cards de serviço).
   - `img/portfolio/`: 600 × 400 px (galeria).
4. **Compressão:** otimize o peso das imagens antes de enviar (ferramentas como TinyPNG ou Squoosh.app ajudam a manter qualidade e velocidade).
5. **Substituição:** copie as fotos reais para as pastas correspondentes, mantendo os mesmos nomes. O HTML e o CSS já apontam para esses caminhos — não é necessário alterar o código.

---

## ✏️ Como alterar os textos

1. Abra `index.html` (usa-se HTML puro).
2. Procure por um texto e edite-o diretamente.
3. **Mantenha o significado** e não adicione dados que não foram fornecidos.

Exemplo: para mudar a frase do "Sobre", procure pela tag `<p>` dentro da seção `<section class="sobre">`.

---

## 🌐 Como publicar gratuitamente

### Opção A — GitHub Pages

1. Crie uma conta no [GitHub](https://github.com).
2. Crie um repositório chamado, por exemplo, `andre-luiz-pinturas`.
3. Faça o **upload** de todos os arquivos do projeto.
4. No GitHub, vá em **Settings → Pages**.
5. Em **Source**, selecione a branch `main` (ou `master`) e a pasta `/root`.
6. Aguarde alguns minutos. O site ficará disponível em:
   ```
   https://seu-usuario.github.io/andre-luiz-pinturas/
   ```

### Opção B — Vercel

1. Acesse [vercel.com](https://vercel.com) e faça login.
2. Clique em **Add New Project** e selecione o repositório do GitHub.
3. Vercel detectará automaticamente o framework (este é um site estático, então ele detectará como "Static HTML").
4. Clique em **Deploy**.
5. O site ficará disponível em:
   ```
   https://andre-luiz-pinturas.vercel.app
   ```

### Opção C — Netlify

1. Acesse [netlify.com](https://netlify.com) e faça login.
2. Clique em **Add new site** e selecione o repositório do GitHub.
3. Clique em **Deploy site**.
4. O site ficará disponível em:
   ```
   https://andre-luiz-pinturas.netlify.app
   ```

> 💡 Qualquer uma dessas opções é **gratuita** para sites estáticos. Basta ter os arquivos em um repositório Git (GitHub, GitLab ou Bitbucket).

---

## ✅ Testes realizados

- [x] HTML válido e sem erros.
- [x] CSS sem erros.
- [x] JavaScript sem erros.
- [x] Links do WhatsApp funcionando.
- [x] Menu desktop e menu hamburger em celulares.
- [x] Layout responsivo (mobile-first, verificado em 320px, 768px e 1024px+).
- [x] Botões clicáveis e sem funcionalidade em branco.
- [x] Nenhum texto de exemplo presente.
- [x] Nessuma informação inventada no site.

---

## 📜 Licença

Copyright © 2026 André Luiz — Arte e Pinturas. Todos os direitos reservados.

Para uso comercial interno.
