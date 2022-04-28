primeiroTipo = input('Primeiro tipo: ')
segundoTipo = input('Segundo tipo: ')
terceiroTipo = input('Terceiro tipo: ')

if primeiroTipo == 'vertebrado':
    if(segundoTipo == 'ave'):
        if terceiroTipo == 'carnivoro':
            print('aguia')
        elif terceiroTipo == 'onivoro':
            print('pomba')
    elif(segundoTipo == 'mamifero'):
        if terceiroTipo == 'herbivoro':
            print('vaca')
        elif terceiroTipo == 'onivoro':
            print('homem')
elif primeiroTipo == 'invertebrado':
    if(segundoTipo == 'inseto'):
        if terceiroTipo == 'hematofago':
            print('pulga')
        elif terceiroTipo == 'herbivoro':
            print('lagarta')
    elif(segundoTipo == 'anelideo'):
        if terceiroTipo == 'hematofago':
            print('sanguessuga')
        elif terceiroTipo == 'onivoro':
            print('minhoca')