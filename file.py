from dis import dis
import funcoes

dict_final = funcoes.fun_dict_final()
music_names = funcoes.fun_music_names()
music_names_split = funcoes.fun_music_names_split(music_names)
disk_names = funcoes.fun_disk_names()
disk_names_split = funcoes.fun_disk_names_split(disk_names)
link_music = funcoes.fun_link_music()
qnt_music = funcoes.fun_qnt_music()
list_letras_completa = funcoes.fun_list_letras_completa(disk_names, qnt_music, dict_final)

#Pergunta 2.1
funcoes.pergunta2_1(disk_names_split)
#Pergunta 2.2
funcoes.pergunta2_2(music_names_split)
#Pergunta 2.3
funcoes.pergunta2_3(disk_names, qnt_music, dict_final)
#Pergunta 2.4
funcoes.pergunta2_4(list_letras_completa)
#Pergunta 2.5
funcoes.pergunta2_5(disk_names, dict_final)
#Pergunta 2.6
funcoes.pergunta2_6(disk_names, dict_final)