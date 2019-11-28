import time
print '   ::: DESAFIO CODE EVERY DAY - DIA 26/27 ::: \n\n'
time.sleep(1)
print '         >>> CONTADOR DE CARACTERES <<<\n\n'
arquivo = open("arquivo.csv","w")
while 1:
    menu = raw_input('  INSERIR ITEM? \n\n  S = SIM | N = NAO\n\n')
    if menu == 'S' or menu == 's':
        msg = raw_input('  DIGITE O ITEM A SER INSERIDO: \n\n')
        arquivo.write(msg)
        arquivo.write(',')
    elif menu == 'N'or menu == 'n':
        arquivo.close()
        break
import contador
        
        
