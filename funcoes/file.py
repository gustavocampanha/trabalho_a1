import requests
from bs4 import BeautifulSoup

link = 'https://www.vagalume.com.br/u2/with-or-without-you.html'

parte_music = list()
letra_music = list()

page = requests.get(link)
soup = BeautifulSoup(page.text, 'lxml')

word = soup.find_all('div', id='lyrics')
letra = str(word)
tam = letra.count('>')

for a in range(0, tam):
    
    find_ini = letra.find('>')
    find_fim = letra.find('<')
    adicionar = letra[find_ini+1:find_fim].lower()
    if adicionar != '':
        parte_music.append(adicionar+ ' ')
    letra = letra[find_fim+1:]


letra_total = ''

for a in range(0, len(parte_music)):
    letra_total += parte_music[a]

print(letra_total)

letra_total = letra_total.replace('.', '')
letra_total = letra_total.replace(',', '')
letra_total = letra_total.replace("'", ' ')
letra_total = letra_total.replace('!', '')
letra_total = letra_total.replace('(', '')
letra_total = letra_total.replace(')', '')

frase = letra_total

separado = frase.split()
dict = dict()
for word in separado:
    if word not in dict:
        dict[word] = frase.count(word)

print(dict)