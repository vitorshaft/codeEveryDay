# -*- coding: cp1252 -*-
print '          ORGANIZADOR DE NUMEROS SHAFT \n'
print '          Voce devera informar 3 numeros \n'
n1 = int(raw_input('Qual o primeiro? \n'))
n2 = int(raw_input('E o segundo? \n'))
n3 = int(raw_input('Agora o ultimo. \n'))
lista = []
for i in range((n1+n2+n3)):
    lista.append(0)
lista.insert(n1,n1)
lista.insert(n2,n2)
lista.insert(n3,n3)
print 'ORGANIZAMOS NA ORDEM DECRESCENTE PARA VOCE: \n'
for item in lista[::-1]:
    if item != 0:
        print item
raw_input('APERTE QUALQUER TECLA PARA SAIR')
