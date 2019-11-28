import time
print '  ::: DESAFIO CODE EVERY DAY - DIA 22 :::\n\n'
time.sleep(1)
print '          >>> TABELA DE PRECOS <<<\n\n'
time.sleep(1)
lista = []
tabela = {}
while 1:
    menu = raw_input('  DESEJA INSERIR OU CONSULTAR PRODUTO?\n I = INSERIR | C = CONSULTAR | S = SAIR\n\n')
    if menu == 'I' or menu == 'i':
        nprod = raw_input('\n  INSIRA O NOME DO PRODUTO: \n\n')
        nprod = nprod.upper()
        npreco = raw_input('\n  INSIRA O PRECO DO PRODUTO: \n\nRS ')
        texto = open("produtos.txt","r")
        ler = texto.read()
        texto.close()
        verifica = ler.split(',')
        if verifica.count(nprod) == 0:
            arquivo = open("produtos.txt","w")
            arquivo.write(ler)
            arquivo.write(nprod+',')
            arquivo.write(npreco+',')
            arquivo.close()
        else:
            print '\n  ESTE PRODUTO JA ESTA CADASTRADO\n'
    elif menu == 'C' or menu == 'c':
        arquivo = open("produtos.txt","r" ).read()
        lista = arquivo.split(',')
        #arquivo.close()
        final = len(lista)-1
        for item in lista[:final]:
            if lista.index(item) %2 == 0:
                end = lista.index(item)
                tabela[item] = lista[end+1]
        prod = raw_input('\n  PRODUTO: \n\n' )
        prod = prod.upper()
        checar = lista.count(prod)
        if checar == 0:
            print prod,'nao esta na tabela\n\n' 
        preco = tabela[prod]
        print '  Produto: %s\n\n  Preco: %s\n\n'%(prod,preco)
    elif menu == 'S' or menu == 's':
        break
##    elif menu == 'R' or menu == 'r':
##        abrir = open("produtos.txt","r" )
##        arquivo = abrir.read()
##        lista = arquivo.split(',')
##        final = len(lista)-1
##        for item in lista[:final]:
##            if lista.index(item) %2 == 0:
##                end = lista.index(item)
##                print lista[end],'RS',lista[end+1]
##        item = raw_input('\n\n  QUAL ITEM DESEJA REMOVER? \n\n')
##        item = item.upper()
##        pos = lista.index(item)
##        lista.pop(pos)
##        lista.pop(pos)
##        escreve = open("produtos.txt","w")
##        for item in lista:
##            escreve.write(str(item)+',')
##        abrir.close()


