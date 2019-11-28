#Verificar CPF: Dar mensagem de erro quando for:
# 1. Vazio
# 2. Nao-numero
# 3. Tamanho != 11
# 4. Digito verificador -> https://gurudoexcel.com/como-e-feito-o-calculo-de-validacao-cpf/
print '    ::: DESAFIO CODE EVERY DAY - DIA 18 :::\n\n'
print '             > VERIFICADOR DE CPF <\n\n'
entrada = raw_input('  DIGITE UM CPF PARA VERIFICAR A VALIDADE:\n\n')
e = entrada[:9]
p1 = []
for item in e:
    p1.append(int(item))
linha = [11,10,9,8,7,6,5,4,3,2]
soma = 0

for item in range(10)[1:]:
    i = item-1
    soma = soma+(int(e[i])*linha[item])
#print soma

resto1 = soma%11
d1 = 11-resto1

#CPF ja com o primeiro digito verificador
if d1 < 10:
    beta = e+str(d1) 
else:
    beta = e+'0'
#print beta
soma = 0
for item in range(10):
    soma = soma+(int(beta[item])*linha[item])
#print soma

resto2 = soma%11
d2 = 11-resto2

#CPF com o segundo digito verificador
if d2 < 10:
    cpf = beta+str(d2) 
else:
    cpf = beta+'0'
#print cpf
if entrada != str(cpf):
    print '\n\n  CPF INVALIDO!   :('
else:
    print '\n\n  CPF VALIDO!   :D'
raw_input('\n\n  > APERTE ENTER PARA ENCERRAR <' )
