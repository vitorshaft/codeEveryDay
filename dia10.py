print '     DESAFIO CODE EVERY DAY - DIA 10 \n'
print '  Por favor, insira IDADE e ALTURA de 5 pessoas: \n \n'
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p1.append(int(raw_input(' Digite a IDADE da 1a pessoa:\n\n')))
p1.append(int(raw_input(' Digite a ALTURA em cm da 1a pessoa:\n\n')))
p2.append(int(raw_input(' Digite a IDADE da 2a pessoa:\n\n')))
p2.append(int(raw_input(' Digite a ALTURA em cm da 2a pessoa:\n\n')))
p3.append(int(raw_input(' Digite a IDADE da 3a pessoa:\n\n')))
p3.append(int(raw_input(' Digite a ALTURA em cm da 3a pessoa:\n\n')))
p4.append(int(raw_input(' Digite a IDADE da 4a pessoa:\n\n')))
p4.append(int(raw_input(' Digite a ALTURA em cm da 4a pessoa:\n\n')))
p5.append(int(raw_input(' Digite a IDADE da 5a pessoa:\n\n')))
p5.append(int(raw_input(' Digite a ALTURA em cm da 5a pessoa:\n\n')))
print '\n\n AGORA VAMOS LISTAR AS ALTURAS E IDADES DA ULTIMA PARA \n A PRIMEIRA INSERIDA:\n\n'
lista = [p1,p2,p3,p4,p5]
for item in lista[::-1]:
    print '  ALTURA: ',item[1],'IDADE: ',item[0]
raw_input('\n\n  ===== PRESSIONE ENTER PARA ENCERRAR ====')
    
