import time
print '   ::: DESAFIO CODE EVERY DAY - FINAL :::\n\n'
time.sleep(1)
print '         >>> MONTADOR DE SOFTWARE <<<\n\n'
time.sleep(1)
n = int(raw_input('  O SCRIPT ESTA DIVIDIDO EM QUANTAS PARTES? \n\n'))
partes = []
for item in range(n):
    cont = item+1
    nome = raw_input('  INSIRA O NOME DA %da PARTE \n\n'%cont)
    partes.append(nome)
print partes
novo = raw_input('  QUAL O NOME DO ARQUIVO MONTADO? \n\n')
arquivo = open(novo,"w")
for item in partes:
    a = open(item,"r")
    b = a.readlines()
    a.close()
    arquivo.write(b[0])
arquivo.close()
