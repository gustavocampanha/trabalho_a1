import requests
from bs4 import BeautifulSoup

link = 'https://www.vagalume.com.br/u2/discografia/'

music_names = list()
letra_music = list()

page = requests.get(link)
soup = BeautifulSoup(page.text, 'lxml')


for word in soup.find_all('div', class_='trackWrapper'):
    qnt = word.get_text()
    f = qnt.find('f')
    qnt = qnt[2:f-1]
    qnt = int(qnt)

    music_names.append(qnt)

print(music_names)
print(len(music_names))