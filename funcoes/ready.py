# Importando as bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Links
link_discografia = 'https://www.vagalume.com.br/u2/discografia/'

#Criando listas necessárias
music_names = list()
disk_names = list()
qnt_music = list()

music_names_split = list()
disk_names_split = list()

dict_final = dict()

# Fazendo a leitura na pagina
page = requests.get(link_discografia)
soup = BeautifulSoup(page.text, 'lxml')

# Adicionando o nome da musica na lista music_names
for word in soup.find_all('a'):
    if 'nameMusic' in str(word):
        music_names.append(word.get_text())

# Adicionando o nome do ábum na lista disk_names
for word in soup.find_all('h3'):
    if 'albumTitle' in str(word):
        disk_names.append(word.get_text())

# Adicionando a quantidade de músicas em cada album na lista qnt_music
for word in soup.find_all('div', class_='trackWrapper'):
    qnt = word.get_text()
    f = qnt.find('f')
    qnt = qnt[2:f-1]
    qnt = int(qnt)
    qnt_music.append(qnt)

