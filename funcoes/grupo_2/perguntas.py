# Importando as bibliotecas
import pandas as pd
import numpy as np
from .extract import fun_disk_names_split, fun_music_names_split, fun_disk_names, fun_qnt_music, fun_dict_final, fun_ajuste_word  
#Primeira Pergunta
def pergunta2_1(disk_names_split):
    pergunta2_1 = pd.value_counts(np.array(disk_names_split))
    print(f'As 3 palavras mais comuns nos títulos dos álbuns são: "{pergunta2_1.index[0]}", aparecendo {pergunta2_1.values[0]} vez(es). "{pergunta2_1.index[1]}", aparecendo {pergunta2_1.values[1]} vez(es). "{pergunta2_1.index[2]}", aparecendo {pergunta2_1.values[2]} vez(es)')
    
#Segunda Pergunta
def pergunta2_2(music_names_split):
    pergunta2_2 = pd.value_counts(np.array(music_names_split))
    print(f'As 3 palavras mais comuns nos títulos das músicas são: "{pergunta2_2.index[0]}", aparecendo {pergunta2_2.values[0]} vez(es). "{pergunta2_2.index[1]}", aparecendo {pergunta2_2.values[1]} vez(es). "{pergunta2_2.index[2]}", aparecendo {pergunta2_2.values[2]} vez(es)')

#Terceira Pergunta
def pergunta2_3(disk_names, qnt_music, dict_final):
    for y in range(0, len(disk_names)):
        list_letra = list()

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
            list_letra.append(add)   

        pergunta2_3 = pd.value_counts(np.array(list_letra))

        print(f'As 3 palavras mais comuns nas letras das músicas do álbum "{disk_names[y]}" são: "{pergunta2_3.index[0]}", aparecendo {pergunta2_3.values[0]} vez(es). "{pergunta2_3.index[1]}", aparecendo {pergunta2_3.values[1]} vez(es). "{pergunta2_3.index[2]}", aparecendo {pergunta2_3.values[2]} vez(es)')

#Quarta Pergunta
def pergunta2_4(list_letras_completa):
    pergunta2_4 = pd.value_counts(np.array(list_letras_completa))
    print(f'As 3 palavras mais comuns nas letras das músicas de toda discografia são: "{pergunta2_4.index[0]}", aparecendo {pergunta2_4.values[0]} vez(es). "{pergunta2_4.index[1]}", aparecendo {pergunta2_4.values[1]} vez(es). "{pergunta2_4.index[2]}", aparecendo {pergunta2_4.values[2]} vez(es)')


#Quinta Pergunta
def pergunta2_5(disk_names, dict_final):
    for y in range(0, len(disk_names)):
        list_new = list()
        x = dict_final[disk_names[y]]['Nome Album Split:']
        
        letra_musica = str(dict_final[disk_names[y]]['Letras Musicas:'])
        letra_musica = fun_ajuste_word(letra_musica)

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
def pergunta2_6(disk_names, dict_final):
    for p in range(0, len(disk_names)):
        
        nome_musicas = dict_final[disk_names[p]]['Musicas:']
        
        for y in range(0, len(nome_musicas)):
            lista_split_indv = list()
            letra_musica = str(dict_final[disk_names[p]]['Letras Musicas:'][y])
            
            letra_musica = fun_ajuste_word(letra_musica)

            space = nome_musicas[y].count(' ')
            palavra = nome_musicas[y].lower()
            for h in range(0, space):
                pos = palavra.find(' ')
                adicionar = palavra[0:pos]
                add = str(adicionar)
                add = fun_ajuste_word(add)
                lista_split_indv.append(add)
                palavra = palavra[pos+1:]

            palavra = str(palavra)
            palavra = fun_ajuste_word(palavra)
            
            lista_split_indv.append(palavra)
            print(lista_split_indv)
            list_new = list()
            for b in range(0, len(lista_split_indv)):
                
                if lista_split_indv[b] in letra_musica:
                    list_new.append(lista_split_indv[b])
                    v = letra_musica.count(lista_split_indv[b])
                    list_new.append(v)
                else:
                    continue

            word_list = letra_musica.split()
            number_of_words = len(letra_musica)
            print(f'Quantidade de vezes que as palavras do nome da música "{nome_musicas[y]}" apareceu(apareceram) na letra: {list_new}, de {number_of_words} palavras')