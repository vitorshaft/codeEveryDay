import time
print '  ::: DESAFIO CODE EVERY DAY - DIA 20 :::\n\n'
time.sleep(1)
print '   >>> CORRETOR DE NUMERO DE CELULAR <<<\n\n'
time.sleep(1)
print '  Se voce tem um numero desatualizado, corrigimos para voce\n\n'
time.sleep(2)
#cel = raw_input('  Digite o numero do celular:\n\n')
#lista = []
cont = True
while cont == True:
    lista = []
    cel = raw_input('  Digite o numero do celular:\n\n')
    for item in cel:
        if item != '-':
            lista.append(item)
        else:
            time.sleep(1)
            #print '\n\n - removido'
    if len(lista) == 8:
        novo = '9'
        lista.insert(4,'-')
        for item in lista:
            novo = novo+item
        time.sleep(1)
        print '\n\n  SEU NUMERO NOVO E: ',novo
        cont = False
    elif len(lista) == 9 and lista[0] == '9':
        time.sleep(1)
        print '\n\n  SEU NUMERO PARECE OK, NAO PRECISA DE CORRECAO\n\n'
        cont = False
    elif len(lista) < 8:
        time.sleep(1)
        print '\n\n ACHO QUE TA FALTANDO ALGUM NUMERO AI, FERA\n\n'
    else:
        time.sleep(1)
        print '\n\n  ACHO QUE TEM NUMERO DEMAIS AI HEIN\n\n'
time.sleep(2)
print '\n\n  ...OBRIGADO POR USAR O CORRETOR!\n\n'
raw_input('   > APERTE ENTER PARA ENCERRAR < ')
