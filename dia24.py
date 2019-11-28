import time
print '  ::: DESAFIO CODE EVERY DAY - DIA 24 :::\n\n'
time.sleep(1)
print '          >>> AGENDA TELEFONICA <<<\n\n'
time.sleep(1)
lista = []
tabela = {}
while 1:
    menu = raw_input('  DESEJA INSERIR OU CONSULTAR CONTATO?\n A = ALTERAR | I = INSERIR | C = CONSULTAR | R = REMOVER | S = SAIR\n\n')
    if menu == 'I' or menu == 'i':
        pessoa = raw_input('\n  INSIRA O NOME DO CONTATO: \n\n')
        pessoa = pessoa.upper()
        tel = raw_input('\n  INSIRA O NUMERO DE TELEFONE: \n\n ')
        texto = open("agenda.txt","r")
        ler = texto.read()
        texto.close()
        verifica = ler.split(',')
        if verifica.count(pessoa) == 0:
            arquivo = open("agenda.txt","w")
            arquivo.write(ler)
            arquivo.write(pessoa+',')
            arquivo.write(tel+',')
            arquivo.close()
        else:
            print '\n  ESTE CONTATO JA ESTA CADASTRADO\n'
    elif menu == 'C' or menu == 'c':
        agenda = open("agenda.txt","r")
        arquivo = agenda.read()
        lista = arquivo.split(',')
        agenda.close()
        final = len(lista)-1
        for item in lista[:final]:
            if lista.index(item) %2 == 0:
                end = lista.index(item)
                tabela[item] = lista[end+1]
        pessoa = raw_input('\n  NOME: \n\n' )
        pessoa = pessoa.upper()
        checar = lista.count(pessoa)
        if checar == 0:
            print pessoa,'nao esta na agenda\n\n' 
        else:
            tel = tabela[pessoa]
            print '  NOME: %s\n\n  TEL: %s\n\n'%(pessoa,tel)
    elif menu == 'S' or menu == 's':
        break
    elif menu == 'A' or menu == 'a':
        alvo = raw_input('\n\n  INSIRA O NOME OU NUMERO QUE DESEJA ALTERAR:\n\n')
        alvo = alvo.upper()
        agenda = open("agenda.txt","r")
        arquivo = agenda.read()
        lista = arquivo.split(',')
        agenda.close()
        end = lista.index(alvo)
        lista.remove(alvo)
        novo = raw_input('\n\n QUAL O NOVO VALOR?\n\n')
        novo = novo.upper()
        lista.insert(end,novo)
        agenda = open("agenda.txt","w")
        for item in lista:
            agenda.write(item)
            agenda.write(',')
        agenda.close()
        
    elif menu == 'R' or menu == 'r':
        alvo = raw_input('\n\n  INSIRA O NOME DO CONTATO QUE DESEJA REMOVER:\n\n')
        alvo = alvo.upper()
        abrir = open("agenda.txt","r")
        arquivo = abrir.read()
        lista = arquivo.split(',')
        agenda.close()
        end = lista.index(alvo)+1
        num = lista[end]
        lista.remove(num)
        lista.remove(alvo)
        agenda = open("agenda.txt","w")
        for item in lista:
            agenda.write(item)
            agenda.write(',')
        agenda.close()
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


