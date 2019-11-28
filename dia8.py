# -*- coding: cp1252 -*-
import msvcrt
print '        DESAFIO CODE EVERY DAY - DIA 8 \n'
print '   SENSO DE CONDICIONAMENTO FISICO DE CLIENTES \n'
a = 1
clientes = {}
alturas = []
pesos = []
for i in range(512):
    alturas.append(0)
    pesos.append(0)
while a == 1:
    print '     INSIRA OS DADOS DO CLIENTE: \n \n'
    cod = int(raw_input('INSIRA SEU CODIGO DE CLIENTE: \n \n'))
    if cod == 0:
        a = 0
    elif cod !=0:
        altura = int(raw_input('INSIRA SUA ALTURA EM CM: \n \n'))
        peso = int(raw_input('INSIRA SEU PESO EM KG: \n \n'))
        #CRIANDO DICIONÁRIO DE CLIENTES: codigo:(altura,peso)
        clientes[cod] = (altura,peso)
        #CRIANDO DUAS LISTAS: UMA PARA ALTURAS, OUTRA PARA PESOS
        alturas.insert(cod,altura)
        pesos.insert(cod,peso)

#ENCONTRANDO MAIOR ALTURA
maiorA = alturas[0]
contA = -1
c = 0
for item in alturas:
    contA +=1
    if item > maiorA:
        maiorA = item
        c = contA
#print maiorA, c
        
#ENCONTRANDO MENOR ALTURA
    #removendo os zeros da lista "alturas"
while alturas.count(0) !=0:
    alturas.remove(0)

menorA = alturas[0]
contB = 0
pos = 0
for item in alturas:
    contB +=1
    if item < menorA or item == menorA:
        menorA = item
        pos = contB

#ENCONTRANDO MAIOR PESO
maiorP = pesos[0]
contP = -1
d = 0
for item in pesos:
    contP +=1
    if item > maiorP:
        maiorP = item
        d = contP
#print maiorP, d

#ENCONTRANDO MENOR PESO
    #removendo os zeros da lista "pesos"
while pesos.count(0) != 0:
    pesos.remove(0)

menorP = pesos[0]
contQ = 0
cl = 0
for item in pesos:
    contQ +=1
    if item < menorP or item == menorP:
        menorP = item
        cl = contQ

#DEFININDO MAIS ALTO, BAIXO, PESADO E LEVE
alto = clientes[c]
baixo = clientes[pos]
pesado = clientes[d]
leve = clientes[cl]

print '  CLIENTE MAIS ALTO: CODIGO %d, COM %d cm DE ALTURA \n \n'%(c,alto[0])
print '  CLIENTE MAIS BAIXO: CODIGO %d, COM %d cm DE ALTURA \n \n'%(pos,baixo[0])
print '  CLIENTE MAIS PESADO: CODIGO %d, COM %d kg \n \n'%(d,pesado[1])
print '  CLIENTE MAIS LEVE: CODIGO %d COM %d kg \n \n'%(cl,leve[1])

raw_input('APERTE ENTER PARA ENCERRAR')

#print clientes
    
