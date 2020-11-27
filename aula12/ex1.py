
numero = input('Entre com um número inteiro e positivo: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é um número par', end='\n')
    else:
        print(f'{numero} é um número ímpar', end='\n')
else:
    print('Erro: a entrada não corresponde a um número inteiro e positivo !!', end='\n')