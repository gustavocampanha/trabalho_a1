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

#Criando dicionário final
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


# Adicionando nome split de cada album em uma lista
for a in range(0, len(disk_names)):

    space = disk_names[a].count(' ')
    palavra = disk_names[a].lower()
    for a in range(0, space):
        pos = palavra.find(' ')
        adicionar = palavra[0:pos]
        add = str(adicionar)
        add = add.replace("'", '')
        add = add.replace('(', '')
        add = add.replace(')', '')
        add = add.replace('.', '')
        add = add.replace('/', '')
        disk_names_split.append(add)
        palavra = palavra[pos+1:]
        
    disk_names_split.append(palavra)


link_music = list()
link_padrao = 'https://www.vagalume.com.br'

for word in soup.find_all('div', class_='lineColLeft'):
    secao = str(word)
    if 'href="' in secao:
        pos = secao.find("href=")
        add = secao[pos+6:]
        pos2 = add.find('"')
        add = add[:pos2]
        add = link_padrao+add
        link_music.append(add)


# Ajustando o dicionário
for a in range(0, len(disk_names)):
    dict_final[disk_names[a]] = dict()

    words = disk_names[0].count(' ') + 1
    dict_final[disk_names[a]]['Nome Álbum Split:'] = disk_names_split[0:words]
    del disk_names_split[0:words]

    list_music_names_fake = list()
    mus = qnt_music[a]
    list_music_names_fake = music_names[:mus]
    del music_names[:mus]
    dict_final[disk_names[a]]['Músicas:'] = list_music_names_fake

    list_music_names_split = list()
    
    for b in range(0, len(list_music_names_fake)):
        
        space = list_music_names_fake[b].count(' ')
        palavra = list_music_names_fake[b].lower()
        for c in range(0, space+1):
            pos = palavra.find(' ')
            if pos == -1:
                add = str(palavra)
            else:
                add = str(palavra[0:pos])

            add = add.replace("'", '')
            add = add.replace('(', '')
            add = add.replace(')', '')
            add = add.replace('.', '')
            add = add.replace('/', '')
            list_music_names_split.append(add)
            palavra = palavra[pos+1:]

    
    dict_final[disk_names[a]]['Nome Músicas Split:'] = list_music_names_split
    dict_final[disk_names[a]]['Quantidade de Musicas'] = qnt_music[a]
    
    links = list()
    links = link_music[0:mus]
    del link_music[0:mus]

    dict_final[disk_names[a]]['Links Musicas'] = links


    letras_mus = list()
    for d in range(0, len(links)):
        
        link = links[d]
        
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'lxml')
        letra = soup.find_all('div', id='lyrics')

        letra = str(letra[0])
        x = letra.find('>')
        letra = letra[x+1:]

        partes = letra.count('>')

        lirics = ''

        for g in range(0, partes):

            x = letra.find('<')
                
            lirics += letra[0:x]
            if x != 0:
                lirics += ' '

            y = letra.find('>')
            letra = letra[y+1:]

        letras_mus.append(lirics.lower())

    dict_final[disk_names[a]]['Letras Músicas:'] = letras_mus

print(dict_final)