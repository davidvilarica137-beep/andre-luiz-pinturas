import os
from bs4 import BeautifulSoup

html = open('/home/cliente/andre-luiz-pinturas/index.html').read()
soup = BeautifulSoup(html, 'lxml')

missing = []
for img in soup.find_all('img'):
    src = img.get('src')
    if src:
        # caminhos relativos ao projeto
        if src.startswith('/'):
            p = src[1:]
        else:
            p = src
        if not os.path.exists(p):
            missing.append(src)

print('Caminhos MISSING:', missing if missing else 'nenhum')

# Verificar CSS também
css = open('/home/cliente/andre-luiz-pinturas/css/style.css').read()
import re
for m in re.findall(r'url\([\'"]?([^\'"\s]+)', css):
    p = m if m.startswith('/') else 'img/' + m
    if not os.path.exists(p):
        print('CSS MISS:', m)
print('Verificação CSS concluída.')
