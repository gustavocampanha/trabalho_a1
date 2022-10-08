import pandas as pd
from services.deezer_service import get_albums_info
import funcoes

try:
    df_artist = pd.read_csv("U2.csv", encoding="utf-8-sig", sep=";")
    df_albuns = pd.read_csv("U2_albuns.csv", encoding="utf-8-sig", sep=";")
except FileNotFoundError:
    df_artist, df_albuns = get_albums_info('U2')
    df_artist.to_csv("U2.csv", sep=";", encoding="utf-8-sig", index=False)
    df_albuns.to_csv("U2_albuns.csv", sep=";", encoding="utf-8-sig", index=False)

dict_final = funcoes.fun_dict_final()
music_names = funcoes.fun_music_names()
music_names_split = funcoes.fun_music_names_split(music_names)
disk_names = funcoes.fun_disk_names()
disk_names_split = funcoes.fun_disk_names_split(disk_names)
link_music = funcoes.fun_link_music()
qnt_music = funcoes.fun_qnt_music()
list_letras_completa = funcoes.fun_list_letras_completa(disk_names, qnt_music, dict_final)

## Grupo perguntas 1

# 1 - Músicas mais ouvidas e músicas menos ouvidas por Álbum
df_pergunta_1 = funcoes.pergunta_1(df_artist)
funcoes.plt_pergunta_1_mais_ouvidas(df_pergunta_1)
funcoes.plt_pergunta_1_menos_ouvidas(df_pergunta_1)

# 2 - Músicas mais longas e músicas mais curtas por Álbum
df_pergunta_2 = funcoes.pergunta_2(df_artist)
funcoes.plt_pergunta_2_mais_longas(df_pergunta_2)
funcoes.plt_pergunta_2_menos_longas(df_pergunta_2)

# 3 - Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
df_less_listen, df_more_listen = funcoes.pergunta_3(df_artist)
funcoes.plt_pergunta_3_mais_ouvidas(df_more_listen)
funcoes.plt_pergunta_3_menos_ouvidas(df_less_listen)

# 4 - Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
df_shorter_five, df_longer_five = funcoes.pergunta_4(df_artist)
funcoes.plt_pergunta_4_mais_longas(df_longer_five)
funcoes.plt_pergunta_4_menos_longas(df_shorter_five)

# 6 - Existe alguma relação entre a duração da música e sua popularidade?
funcoes.plt_correlacao_duracao_popularidade(df_artist)

## Grupo perguntas 2

#Pergunta 2.1
# Quais são as palavras mais comuns nos títulos dos Álbuns?
funcoes.pergunta2_1(disk_names_split)
funcoes.wcloud(disk_names_split,"img/pythonlogo.png", "./respostas/pergunta2_1")
#Pergunta 2.2
# Quais são as palavras mais comuns nos títulos das músicas?
funcoes.pergunta2_2(music_names_split)
funcoes.wcloud(music_names_split,"img/brazil.png", "./respostas/pergunta2_2")
#Pergunta 2.3
# Quais são as palavras mais comuns nas letras das músicas, por Álbum?
funcoes.pergunta2_3(disk_names, qnt_music, dict_final)
#Pergunta 2.4
# Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?
funcoes.pergunta2_4(list_letras_completa)
funcoes.wcloud(list_letras_completa,"img/fgvlogo.png", "./respostas/pergunta2_4")
#Pergunta 2.5
# O título de um álbum é tema recorrente nas letras?
funcoes.pergunta2_5(disk_names, dict_final)
#Pergunta 2.6
# O título de uma música é tema recorrente nas letras?
funcoes.pergunta2_6(disk_names, dict_final)

## Grupo perguntas 3

# 1 - Quais os albuns com mais fans?
funcoes.plt_pergunta_1_mais_fans(df_albuns)
# 2 - Existe relação entre duração e fans no album?
funcoes.plt_correlacao_duracao_fans(df_albuns)
# 3 - Um album fica mais famoso por ter letras explícitas?
funcoes.plt_correlacao_duracao_fans_explicit(df_albuns)