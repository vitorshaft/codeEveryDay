import os
import time
from random import randint

chave = {'q':'1','w':'2','e':'3','r':'4','t':'5','y':'6','u':'7','i':'8','o':'9','p':'0','a':'q','s':'w','d':'e','f':'r','g':'t','h':'y','j':'u','k':'i','l':'o','z':'a','x':'s','c':'d','v':'f','b':'g','n':'h','m':'j','.':'l','_':'k',' ':'z'}
cadeado = {'1':'q','2':'w','3':'e','4':'r','5':'t','6':'y','7':'u','8':'i','9':'o','0':'p','q':'a','w':'s','e':'d','r':'f','t':'g','y':'h','u':'j','i':'k','o':'l','a':'z','s':'x','d':'c','f':'v','g':'b','h':'n','j':'m','l':'.','k':'_','z':' '}

print '  ::: DESAFIO CODE EVERY DAY - DIA 23 :::\n\n'
time.sleep(1)
print '      >>> ENCRIPTADOR DE ARQUIVOS <<<\n\n'
time.sleep(1)

while 1:
    menu = ''
    menu = raw_input('\n\n  E = ENCRIPTAR ARQUIVO | L = LIBERAR ARQUIVO | S = SAIR\n\n')

    if menu == 'E' or menu == 'e':
        nome = raw_input('  Qual arquivo deseja encriptar? \n\n')
        cripto = ''
        cripto2 = ''
        abrir = open(nome,'r')
        texto = abrir.read()
        abrir.close()
        for item in texto:
            cripto2 = cripto2+chave[item]
        abrir = open(nome,'w')
        abrir.write(cripto2)
        abrir.close()
        for item in nome:
            cripto = cripto+chave[item]
            #print cripto
        os.rename(nome,cripto)
        print '\n\n  ARQUIVO ENCRIPTADO COMO %s\n\n'%cripto

    elif menu == 'L' or menu == 'l':
        cripto = raw_input('  Qual arquivo deseja liberar? \n\n')
        nome = ''
        for item in cripto:
            nome = nome+cadeado[item]
        os.rename(cripto,nome)
        abrir = open(nome,'r')
        texto = abrir.read()
        abrir.close()
        cripto2=''
        for item in texto:
            cripto2 = cripto2+cadeado[item]
        abrir = open(nome,'w')
        abrir.write(cripto2)
        abrir.close()
        print '\n\n  ARQUIVO %s LIBERADO\n\n'%nome
        os.startfile(nome)
        
    elif menu == 'S' or menu == 's':
        break
