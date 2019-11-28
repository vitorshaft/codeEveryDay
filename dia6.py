print '      GERADOR DE TABUADAS SHAFT      \n'
num = int(raw_input('    DE QUAL NUMERO VOCE QUER VER A TABUADA? \n\n    '))
print 'TABUADA DE %d: \n' %num
for item in range(11):
    print '%d x %d = ' %(num,item)+str(num*item)
raw_input('\n PRESSIONE ENTER PARA SAIR')
