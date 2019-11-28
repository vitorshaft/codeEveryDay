print '     DESAFIO CODE EVERY DAY - DIA 11 \n\n'
print '  APRESENTOLES ===== MEDIA DE SALTOS SHAFT\n\n'
m = {}
s = {}
media = []
a = 0
while a == 0:
    comp = raw_input('\n Insira o nome do competidor: \n')
    if comp == '':
        a = 1
    else:
        saltos = []
        soma = 0
        for i in range(6)[1::]:
            saltos.append(float(raw_input('\n %do SALTO EM m:\n\n '%i)))
        s[comp] = saltos
        for item in saltos:
            soma += item
        m[comp] = (soma/5)
r = 's'
while r == 's' or r == 'S':
    quem = raw_input('\n\n DESEJA VER OS DADOS DE QUAL COMPETIDOR? \n\n')
    print 'Competidor: ',quem,'\n\nSALTOS:'
    for item in s[quem]:
        print '\n',item
    print '\nMedia: ',m[quem]
    r = raw_input('\nCONSULTAR OUTRO COMPETIDOR? ')
raw_input('\n\n  PRESSIONE ENTER PARA ENCERRAR')

