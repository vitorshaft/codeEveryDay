print '  ::: DESAFIO CODE EVERY DAY - DIA 17 :::\n\n'
print '     > CONTADOR DE VOGAIS E ESPACOS < \n\n'
palavra = raw_input('Insira uma frase: \n\n')
vogais = 'aeiou'
espaco = ' '
vog = 0
for item in vogais:
    cont = palavra.count(item)
    vog = vog+cont
esp = palavra.count(espaco)
print '\n  A frase "%s" tem: \n\n  %d VOGAIS\n\n  %d ESPACOS'%(palavra,vog,esp)
raw_input('\n\n  PRESSIONE ENTER PARA ENCERRAR')
