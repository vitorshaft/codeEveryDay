import random
from random import randint
import time
a = open("palavras.txt","r").read()
#print a
p = ''
lista = []
for item in range(len(a)):
    if a[item] != ' ':
        p = p+a[item]
    else:
        lista.append(p)
        p = ''
palavra = lista[randint(0,len(lista)-1)]
emb = ''
e = []
for item in range(len(palavra)):
    e.append(item)
random.shuffle(e)
for item in e:
    emb = emb+palavra[item]
print ' ::: DESAFIO CODE EVERY DAY DIA 19 ::: \n\n'
time.sleep(1)
print '     >>> JOGO DE ADIVINHACAO <<< \n\n'
time.sleep(2)
contador = 0
print ' TEMOS AQUI UMA PALAVRA EMBARALHADA:\n\n'
time.sleep(1)
print '  ',emb
time.sleep(2)
while contador < 5:
    palpite = raw_input('\n\n TENTE DESCOBRIR QUAL E: \n\n')
    if palpite == palavra:
        time.sleep(1)
        print '\n\n  ...PARABENS, VOCE ACERTOU EM CHEIO!!!'
        contador = 5
    else:
        time.sleep(1)
        print '\n\n  ERRRROOOOOOOU!!!\nTente novamente'
        contador = contador+1
time.sleep(2)
raw_input('\n\nxxxxxxxxxxx FIM DE JOGO xxxxxxxxxxxxx\n\n  PRESSIONE ENTER PARA ENCERRAR')
