numeroDDD = int(input('Digite o ddd: '))

def solucionarDDD(ddd):
    if ddd == 61:
        print(f'O DDD {ddd} é de Brasilia')
    elif ddd == 71:
        print(f'O DDD {ddd} é de Salvador')
    elif ddd == 11:
        print(f'O DDD {ddd} é de Sao Paulo')
    elif ddd == 21:
        print(f'O DDD {ddd} é de Rio de Janeiro')
    elif ddd == 32:
        print(f'O DDD {ddd} é de Juíz de fora')
    elif ddd == 19:
        print(f'O DDD {ddd} é de Campinas')
    elif ddd == 27:
        print(f'O DDD {ddd} é de Vitoria')
    elif ddd == 31:
        print(f'O DDD {ddd} é de Belo Horizonte')
    else:
        print('DDD não cadastrado')

solucionarDDD(numeroDDD)