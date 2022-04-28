from math import floor

numeroTestes = int(input('Número de casos de teste: '))
if numeroTestes < 1 or numeroTestes > 3000:
    print('Numero de testes inválidos')

testesRestantes = numeroTestes
arrayResultados = []

while(testesRestantes > 0):
    dados = input('Digite os dados: ')
    arrayDados = dados.split(' ')
    populacaoA = int(arrayDados[0])
    populacaoB = int(arrayDados[1])
    crescimentoA = float(arrayDados[2])
    crescimentoB = float(arrayDados[3])

    novaPopulacaoA = populacaoA
    novaPopulacaoB = populacaoB
    qtdAnos = 0
    while(novaPopulacaoA <= novaPopulacaoB):
        novaPopulacaoA = floor(novaPopulacaoA * (1 + (crescimentoA/100)))
        novaPopulacaoB = floor(novaPopulacaoB * (1 + (crescimentoB/100)))
        qtdAnos += 1
    if(qtdAnos > 100):
        arrayResultados.append('Mais de 1 seculo')
    else:
        arrayResultados.append(f'{qtdAnos} anos')

    testesRestantes -= 1
for resultado in arrayResultados:
    print(resultado)
    