# Importando as bibliotecas
import requests
from bs4 import BeautifulSoup

#Funçao scrapping
def fun_scrap():
    # Precisamos disso para termos a URL de cada música
    link_padrao = 'https://www.vagalume.com.br'
    link_discografia = link_padrao + '/u2/discografia/'
    page = requests.get(link_discografia)
    soup = BeautifulSoup(page.text, 'lxml')
    return soup

#Funcao para ajustar strings
def fun_ajuste_word(word):
    word = str(word)
    word = word.replace(',', '')
    word = word.replace("'", '')
    word = word.replace('"', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('.', '')
    word = word.replace('/', '')
    word = word.replace('?', '')
    word = word.replace('!', '')
    return word

#Função para checar quantidade de música em cada álbum
def fun_qnt_music():
    #Criando listas necessárias
    qnt_music = list()
    #Fazendo scrapping da página
    soup = fun_scrap()

    #Loop para pegar todas as quantidades de músicas de cada álbum
    for word in soup.find_all('div', class_='trackWrapper'):
        qnt = word.get_text()
        f = qnt.find('f')
        qnt = qnt[2:f-1]
        qnt = int(qnt)
        qnt_music.append(qnt)
    return qnt_music

def fun_disk_names():
    disk_names = list()
    soup = fun_scrap()
    for word in soup.find_all('h3'):
        if 'albumTitle' in str(word):
            disk_names.append(word.get_text())
    return disk_names

def fun_disk_names_split(disk_names):
    disk_names_split = list()
    for a in range(0, len(disk_names)):
        space = disk_names[a].count(' ')
        palavra = disk_names[a].lower()
        for a in range(0, space):
            pos = palavra.find(' ')
            adicionar = palavra[0:pos]
            add = str(adicionar)
            add = fun_ajuste_word(add)
            disk_names_split.append(add)
            palavra = palavra[pos+1:]    
        disk_names_split.append(palavra)
    return disk_names_split


def fun_music_names():
    music_names = list()
    soup = fun_scrap()
    for word in soup.find_all('a'):
        if 'nameMusic' in str(word):
            music_names.append(word.get_text())

    return music_names


def fun_music_names_split(music_names):
    music_names_split = list()
    for a in range(0, len(music_names)):

        space = music_names[a].count(' ')
        palavra = music_names[a].lower()
        for a in range(0, space):
            pos = palavra.find(' ')
            adicionar = palavra[0:pos]
            add = str(adicionar)
            add = fun_ajuste_word(add)

            music_names_split.append(add)
            palavra = palavra[pos+1:]
            
        music_names_split.append(palavra)
    return music_names_split

def fun_link_music():
    link_padrao = 'https://www.vagalume.com.br'
    link_music = list()
    soup = fun_scrap()
    for word in soup.find_all('div', class_='lineColLeft'):
        secao = str(word)
        if 'href="' in secao:
            pos = secao.find("href=")
            add = secao[pos+6:]
            pos2 = add.find('"')
            add = add[:pos2]
            add = link_padrao+add
            link_music.append(add)
    return link_music

def fun_dict_final():
    #Criando dicionário final
    dict_final = dict()

    # Fazendo a leitura na pagina
    soup = fun_scrap()
    # Adicionando o nome da musica na lista music_names
    music_names = fun_music_names()
    # Adicionando o nome do ábum na lista disk_names
    disk_names = fun_disk_names()
    # Adicionando a quantidade de músicas em cada album na lista qnt_music
    qnt_music = fun_qnt_music()
    # Adicionando nome split de cada album em uma lista
    disk_names_split = fun_disk_names_split(disk_names)
    # Colocando os links das musicas em uma lista
    link_music = fun_link_music()

    # Ajustando o dicionário
    for a in range(0, len(disk_names)):

        #Gerando um dicionário para cada álbum
        dict_final[disk_names[a]] = dict()

        #Checando quantas palavras tem no nome do álbum
        words = disk_names[a].count(' ') + 1

        #Colocando no dicionário cada palavra presente no nome do álbum
        dict_final[disk_names[a]]['Nome Album Split:'] = disk_names_split[0:words]
        del disk_names_split[0:words]

        #Checando quantas músicas esse álbum possui
        mus = qnt_music[a]

        #Colocando as musicas desse álbum em uma lista
        list_music_names_now = list()
        list_music_names_now = music_names[:mus]
        del music_names[:mus]

        #Adicionando as musicas de cada álbum no diionário
        dict_final[disk_names[a]]['Musicas:'] = list_music_names_now

        #Colocando as palavras do nome das musicas em uma lista para cada album
        list_music_names_split = list()
        for b in range(0, len(list_music_names_now)):
            
            space = list_music_names_now[b].count(' ')
            palavra = list_music_names_now[b].lower()
            for c in range(0, space+1):
                pos = palavra.find(' ')
                if pos == -1:
                    add = str(palavra)
                else:
                    add = str(palavra[0:pos])

                add = fun_ajuste_word(add)
                
                list_music_names_split.append(add)
                palavra = palavra[pos+1:]

        #Adicionando as palavras dos nomes das músicas no dicionário de cada álbum
        dict_final[disk_names[a]]['Nome Musicas Split:'] = list_music_names_split
        #Adicionando a quantidade de musicas de cada álbum no dicionario 
        dict_final[disk_names[a]]['Quantidade de Musicas'] = qnt_music[a]
        
        links = list()
        links = link_music[0:mus]
        del link_music[0:mus]

        #Adicionando as URLs de cada música no dicionário do álbum
        dict_final[disk_names[a]]['Links Musicas'] = links

        #Criando uma lista para a letra das músicas
        letras_mus = list()
        #Colocando as letras das musicas na lista
        for d in range(0, len(links)):
            
            link = links[d]
            
            #Fazendo a leitura do site
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

        dict_final[disk_names[a]]['Letras Musicas:'] = letras_mus
    
    return dict_final

def fun_list_letras_completa(disk_names, qnt_music, dict_final):
    list_letras_completa = list()
    for y in range(0, len(disk_names)):
        letra = str()
        for w in range(0, qnt_music[y]):
            letra += dict_final[disk_names[y]]['Letras Musicas:'][w]
        letra += ' '
        letra = fun_ajuste_word(letra)
        wordx = letra.count(' ') + 1
        for t in range(0, wordx):
            space = letra.find(' ')
            add = letra[0:space]
            if space < 1:
                continue
            letra = letra[space+1:]
            list_letras_completa.append(add)
    return list_letras_completa