inicio = 'CALCULADORA DE TINTA'
print '       %s \n'%inicio
a = raw_input('Digite a area total a ser pintada (m2): \n')
tinta = float(a)/3
lata = tinta/18
preco = 80*lata
print '       A previsao e de: \n       '+'%.1f latas de tinta'%lata
print '       Preco: RS %.2f \n'%preco
fim = raw_input('Aperte qualquer tecla para encerrar')
