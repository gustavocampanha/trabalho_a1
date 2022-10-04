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

music_names_backup = music_names[:]


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

# Adicionando nome split de cada musica em uma lista
for a in range(0, len(music_names)):

    space = music_names[a].count(' ')
    palavra = music_names[a].lower()
    for a in range(0, space):
        pos = palavra.find(' ')
        adicionar = palavra[0:pos]
        add = str(adicionar)
        add = add.replace("'", '')
        add = add.replace('(', '')
        add = add.replace(')', '')
        add = add.replace('.', '')
        add = add.replace('/', '')
        add = add.replace('\ ', '')
        music_names_split.append(add)
        palavra = palavra[pos+1:]
        
    music_names_split.append(palavra)


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

disk_names_split_backup = disk_names_split[:]

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

    words = disk_names[a].count(' ') + 1
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
            add = add.replace(",", '')
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

#Primeira Pergunta
pergunta2_1 = pd.value_counts(np.array(disk_names_split_backup))

print(f'As 3 palavras mais comuns nos títulos dos álbuns são: "{pergunta2_1.index[0]}", aparecendo {pergunta2_1.values[0]} vez(es). "{pergunta2_1.index[1]}", aparecendo {pergunta2_1.values[1]} vez(es). "{pergunta2_1.index[2]}", aparecendo {pergunta2_1.values[2]} vez(es)')


#Segunda Pergunta
pergunta2_2 = pd.value_counts(np.array(music_names_split))

print(f'As 3 palavras mais comuns nos títulos das músicas são: "{pergunta2_2.index[0]}", aparecendo {pergunta2_2.values[0]} vez(es). "{pergunta2_2.index[1]}", aparecendo {pergunta2_2.values[1]} vez(es). "{pergunta2_2.index[2]}", aparecendo {pergunta2_2.values[2]} vez(es)')

#Terceira Pergunta
list_letras_completa = list()
for y in range(0, len(disk_names)):
    list_letra = list()

    letra = str()
    
    for w in range(0, qnt_music[y]):
        letra += dict_final[disk_names[y]]['Letras Músicas:'][w]
    letra += ' '

    letra = letra.replace(',', '')
    letra = letra.replace("'", '')
    letra = letra.replace('(', '')
    letra = letra.replace(')', '')
    letra = letra.replace('.', '')
    letra = letra.replace('/', '')
    letra = letra.replace('?', '')
    letra = letra.replace('!', '')

    wordx = letra.count(' ') + 1
    for t in range(0, wordx):
        space = letra.find(' ')
        add = letra[0:space]
        if space < 1:
            continue
        letra = letra[space+1:]
        list_letra.append(add)
        list_letras_completa.append(add)    

    pergunta2_3 = pd.value_counts(np.array(list_letra))

    print(f'As 3 palavras mais comuns nas letras das músicas do álbum "{disk_names[y]}" são: "{pergunta2_3.index[0]}", aparecendo {pergunta2_3.values[0]} vez(es). "{pergunta2_3.index[1]}", aparecendo {pergunta2_3.values[1]} vez(es). "{pergunta2_3.index[2]}", aparecendo {pergunta2_3.values[2]} vez(es)')

#Quarta Pergunta
pergunta2_4 = pd.value_counts(np.array(list_letras_completa))

print(f'As 3 palavras mais comuns nas letras das músicas de toda discografia são: "{pergunta2_4.index[0]}", aparecendo {pergunta2_4.values[0]} vez(es). "{pergunta2_4.index[1]}", aparecendo {pergunta2_4.values[1]} vez(es). "{pergunta2_4.index[2]}", aparecendo {pergunta2_4.values[2]} vez(es)')


#Quinta Pergunta
for y in range(0, len(disk_names)):
    list_new = list()
    x = dict_final[disk_names[y]]['Nome Álbum Split:']
    
    letra_musica = str(dict_final[disk_names[y]]['Letras Músicas:'])
    letra_musica = letra_musica.replace(',', '')
    letra_musica = letra_musica.replace("'", '')
    letra_musica = letra_musica.replace('"', '')
    letra_musica = letra_musica.replace('(', '')
    letra_musica = letra_musica.replace(')', '')
    letra_musica = letra_musica.replace('.', '')
    letra_musica = letra_musica.replace('/', '')
    letra_musica = letra_musica.replace('?', '')
    letra_musica = letra_musica.replace('!', '')

    for i in range(0, len(x)):
        if x[i] in letra_musica:
            list_new.append(x[i])
            v = letra_musica.count(x[i])
            list_new.append(v)
        else:
            continue

    
    word_list = letra_musica.split()
    number_of_words = len(letra_musica)
    print(f'Quantidade de vezes que as palavras do nome do álbum "{disk_names[y]}" apareceu(apareceram) nas letras das músicas: {list_new}, de {number_of_words} palavras')


#Sexta Pergunta
print(music_names_backup)