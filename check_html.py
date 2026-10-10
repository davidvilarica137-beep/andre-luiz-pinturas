import os
from bs4 import BeautifulSoup

html = open('/home/cliente/andre-luiz-pinturas/index.html').read()
soup = BeautifulSoup(html, 'lxml')

# Contagem básica
print('Total de tags:', len(soup.find_all(True)))
print('Seções:', len(soup.find_all('section')))
print('Imagens:', len(soup.find_all('img')))
print('Links:', len(soup.find_all('a')))

# Verificar se todos os src de img existem
missing = []
for img in soup.find_all('img'):
    src = img.get('src')
    if src:
        p = src if src.startswith('/') else 'img/' + src
        if not os.path.exists(p):
            missing.append(src)

print('Caminhos MISSING:', missing if missing else 'nenhum')
