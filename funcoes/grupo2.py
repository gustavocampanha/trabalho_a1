import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

link = 'https://www.vagalume.com.br/u2/discografia/'
music_names = list()
disk_names = list()
music_names_split = list()
disk_names_split = list()


page = requests.get(link)
soup = BeautifulSoup(page.text, 'lxml')

for word in soup.find_all('a'):
    if 'nameMusic' in str(word):
        music_names.append(word.get_text())

""" for a in range(0, len(music_names)):
    space = music_names[a].count(' ')
    palavra = music_names[a]
    for a in range(0, space):
        pos = palavra.find(' ')
        resto = palavra[pos:]
        palavra = palavra[:pos]
        music_names_split.append(palavra)
print(music_names_split) """
for a in range(0, len(music_names)):



    space = music_names[a].count(' ')
    palavra = music_names[a].lower()
    for a in range(0, space):
        pos = palavra.find(' ')
        adicionar = palavra[0:pos]
        music_names_split.append(adicionar)
        palavra = palavra[pos+1:]
        
    music_names_split.append(palavra)


""" print(pd.value_counts(np.array(music_names_split))) """

for a in range(0, len(music_names)):
    if '!@#$%&*(),.<>/[]{\}' in music_names[a]:
        print('a')

print(music_names[7])
if '(' in music_names[7]:
    print('erro')

for word in soup.find_all('h3'):
    if 'albumTitle' in str(word):
        disk_names.append(word.get_text())

""" link = 'https://www.vagalume.com.br/u2/' + music_names_split[0] + '.html'
print(link) """