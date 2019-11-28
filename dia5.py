# -*- coding: cp1252 -*-
print '     CALCULADORA DE COMBUSTIVEIS SHAFT     \n'
comb = raw_input('Insira o combustivel: \n \n A - Alcool \n G - Gasolina \n')
litros = float(raw_input('\n Quantos litros vai levar? \n'))
if litros < 20 and comb == 'A':
    valor = litros*1.9
    desc = (0.03*litros)*valor
    preco = valor-desc
elif litros > 20 and comb == 'A':
    valor = litros*1.9
    desc = (0.05*litros)*valor
    preco = valor-desc
elif litros < 20 and comb == 'G':
    valor = litros*2.5
    desc = (0.04*litros)*valor
    preco = valor-desc
elif litros > 20 and comb == 'G':
    valor = litros*2.5
    desc = (0.06*litros)*valor
    preco = valor-desc
print ' VALOR TOTAL: %.2f reais \n VALOR COM DESCONTO: %.2f reais \n'%(valor, preco)
raw_input('     \n PRESSIONE ENTER PARA SAIR')
