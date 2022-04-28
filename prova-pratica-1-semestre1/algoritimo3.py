valorA = int(input('Informe o valor de A: '))
valorB = int(input('Informe o valor de B: '))
valorC = int(input('Informe o valor de C: '))
valorD = int(input('Informe o valor de D: '))
if (valorB > valorC) and (valorD > valorA) and (valorC+valorD) > (valorA+valorB):
    print('Valores aceitos')
else:
    print('Valores não aceitos')