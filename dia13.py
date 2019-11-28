print '    ::::CODE EVERY DAY DIA 13::::    \n\n      >>> DATA POR EXTENSO <<<\n\n\n'
data = raw_input('Ola! Digite uma data no formato dd/mm/aaaa. \n\n')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

meses = {1:'janeiro',2:'fevereiro',3:'marco',4:'abril',5:'maio',6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}

if mes > 12 or mes < 1:
    print 'O mes inserido e invalido \n'
elif mes == 2 and dia > 29:
    print 'Fevereiro tem no maximo 29 dias, amigx. \n'
elif dia < 1 or dia > 31:
    print 'O dia inserido nao existe. \n'
else:
    print '\n\n   ',data
    print '\n\n   ',dia,' de ',meses[mes],' de ',ano
raw_input('\n  PRESSIONE ENTER PARA ENCERRAR')
