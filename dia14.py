import random
print ' ::: DESAFIO CODE EVERY DAY DIA 14 ::: \n\n'
print '   >>>> GERADOR DE ANAGRAMAS <<<< \n\n Vamos embaralhar algumas palavras? \n\n'
palavra = raw_input('  Digite uma palavra pra gente embaralhar: \n\n')
nova = ''
#for item in range(len(palavra)):
#    pos = randint(0,len(palavra))
#nova = nova+palavra[pos]
#print nova
lista = []
for item in range(len(palavra)):
    lista.append(item)
random.shuffle(lista)
for item in lista:
    nova = nova+palavra[item]
print '\n  Olha como ficou:\n\n ',palavra,' >>> ',nova.upper()
raw_input('\n\n\n PRESSIONE ENTER PARA ENCERRAR')
