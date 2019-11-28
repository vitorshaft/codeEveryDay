print '    ::::CODE EVERY DAY DIA 4::::    \n'
data = raw_input('Ola! Digite uma data no formato dd/mm/aaaa e verificaremos se ela existe de verdade! \n')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
if mes > 12 or mes < 1:
    print 'O mes inserido e invalido \n'
elif mes == 2 and dia > 29:
    print 'Fevereiro tem no maximo 29 dias, amigx. \n'
elif dia < 1 or dia > 31:
    print 'O dia inserido nao existe. \n'
else:
    print '\n MUITO BEM! ESTA DATA ESTA PERFEITA! \n'
raw_input('      PRESSIONE ENTER PARA ENCERRAR')
