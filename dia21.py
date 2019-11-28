import time
print '  ::: DESAFIO CODE EVERY DAY - DIA 21 :::\n\n'
time.sleep(1)
print '    >>> VERIFICADOR DE LISTA DE IP <<<\n\n'
time.sleep(1)
arquivo = raw_input('\n\n  NOME DO ARQUIVO COM A LISTA DE IP: \n\n')
ler = open(arquivo,"r").read()
ips = ler.split(',')
for item in ips:
    pos = ips.index(item)+1
    print '\n  ',item,'posicao: %d'%pos
partes = []
l = []
rel = open('relatorio.txt','w')
time.sleep(1)
for item in ips:
    partes = item.split('.')
    l.append(partes)
for item in l:
    time.sleep(1)
    pos = l.index(item)+1
    print '\n  Verificando IP numero:',pos
    for i in item:
        if int(i) > 255:
            ver = False
            valor = int(i)
            break
        else:
            ver = True
    if ver == False:
        print '  ...IP INVALIDO: %d fora do intervalo permitido'%valor
        local = l.index(item)
        texto = str(ips[local])
        rel.write(texto+' <<<< INVALIDO\n\n')
    else:
        print '  ...IP VALIDO'
        local = l.index(item)
        texto = str(ips[local])
        rel.write(texto+' <<< VALIDO\n\n')
rel.close()


raw_input('\n\n  > APERTE ENTER PARA SAIR <')
    
