from random import randint
print '  DESAFIO CODE EVERY DAY - DIA 12\n'
print '   SIMULADOR DE DADOS SEXTAVADOS\n\n ESTE PROGRAMA SIMULA O LANCAMENTO DE UM DADO\n100 VEZES SEGUIDAS:\n'
contador = 0
lista = []
while contador < 100:
    num = randint(1,6)
    lista.append(num)
    contador+=1
print 'OS RESULTADOS OBTIDOS FORAM: \n\n',lista
print 'O numero 1 foi gerado ',lista.count(1), ' vezes'
print 'O numero 2 foi gerado ',lista.count(2), ' vezes'
print 'O numero 3 foi gerado ',lista.count(3), ' vezes'
print 'O numero 4 foi gerado ',lista.count(4), ' vezes'
print 'O numero 5 foi gerado ',lista.count(5), ' vezes'
print 'O numero 6 foi gerado ',lista.count(6), ' vezes'
raw_input('\n\n  PRESSIONE ENTER PARA ENCERRAR')

