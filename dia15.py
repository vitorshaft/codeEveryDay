from random import randint
lista = []
for item in range(10):
    um = randint(0,9)
    dois = randint(0,9)
    tres = randint(0,9)
    linha = []
    linha.append(um)
    linha.append(dois)
    linha.append(tres)
    lista.append(linha)
tab = []
for i in lista:
    soma = i[0]+i[1]+i[2]
    for a in 
