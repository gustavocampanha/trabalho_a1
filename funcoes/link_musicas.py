import requests
from bs4 import BeautifulSoup

link = 'https://www.vagalume.com.br/u2/discografia/'

link_music = list()
link_padrao = 'https://www.vagalume.com.br'

page = requests.get(link)
soup = BeautifulSoup(page.text, 'lxml')

for word in soup.find_all('div', class_='lineColLeft'):
    secao = str(word)
    if 'href="' in secao:
        pos = secao.find("href=")
        add = secao[pos+6:]
        pos2 = add.find('"')
        add = add[:pos2]
        add = link_padrao+add
        link_music.append(add)

print(len(link_music))

