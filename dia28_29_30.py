import time
print '   ::: DESAFIO CODE EVERY DAY - FINAL :::\n\n'
time.sleep(1)
print '         >>> DIVISOR DE SOFTWARE <<<\n\n'
time.sleep(1)
nome = raw_input('  QUAL SCRIPT DESEJA DIVIDIR? \n\n')
prog = open(nome,"r")
lista = prog.readlines() #texto = prog.read()
#print texto
prog.close()
#lista = texto.split(' ')
print lista
cont = 1
for item in lista:
    parte = open("p%d.txt"%cont,"w")
    parte.write(item)
    parte.close()
    cont+=1
montar = ''
for item in lista:
    montar = montar+item#+' '
print montar
time.sleep(1)
print "  PROGRAMA '%s' DIVIDIDO EM %d PARTES"%(nome,cont-1)

time.sleep(3)






#arq = open("vitor.py","w")
#arq.write("print 'deu certo'")
#arq.close()
