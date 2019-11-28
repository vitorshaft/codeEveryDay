print '      DESAFIO CODE EVERY DAY - DIA 7 \n'
print '           ESTATISTICA DE IDADES \n'
print '  Vamos calcular a media das idades de uma turma \n'
chave = 'S'
lista = []
soma = 0
while chave == 'S' or chave == 's':
    idade = raw_input('\n Insira uma idade: \n \n')
    lista.append(int(idade))
    chave = raw_input('Digite S para inserir outra idade, N para encerrar \n')
#print lista
for item in lista:
    soma = soma+item
media = float(soma)/float(len(lista))
print '\n Media das idades inseridas: %.1f anos \n' %media
if media < 26:
    print 'Temos aqui uma turma jovem! \n'
elif media > 25 and media < 60:
    print 'Temos aqui uma turma adulta! \n'
elif media > 59:
    print 'Temos aqui uma turma idosa. \n'
raw_input('\n PRESSIONE ENTER PARA ENCERRAR')
