frase = "see the stone set in your eyes see the thorn twist in your side i wait for you sleight of hand and twist of fate on a bed of nails she makes me wait and i wait... without you with or without you with or without you through the storm we reach the shore you give it all but i want more and i'm waiting for you with or without you with or without you ohoo i can't live with or without you and you give yourself away and you give yourself away and you give and you give and you give yourself away my hands are tied my body bruised, she's got me with nothing to win and nothing left to lose and you give yourself away and you give yourself away and you give and you give and you give yourself away with or without you with or without you i can't live with or without you"
print(type(frase))
print(frase)
print(frase.count('um'))

separado = frase.split()
dict = dict()
for word in separado:
    if word not in dict:
        dict[word] = frase.count(word)

print(dict)
