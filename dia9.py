print '     DESAFIO CODE EVERY DAY - DIA 9 \n'
print '         SOMATORIO DE SEQUENCIA FINITA \n'
print '  Neste programa voce devera informar o valor de N, onde calcularemos \n o valor de H = 1 + 1/2 + 1/3 +...+ 1/N \n'
n = int(raw_input('\n  INFORME O VALOR DE N: \n\n'))
h = 1.000
intervalo = range(n+1)
for item in intervalo[1:]:
    h = h+(1.000/item)
    print 'H + %.3f = %.3f'%((1.000/item),h)
print '\n VALOR DE H COM %d TERMOS: \n \n %.3f'%(n,h)
raw_input('\n APERTE QUALQUER TECLA PARA ENCERRAR')
