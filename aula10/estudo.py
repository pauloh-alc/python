numero = int(input('Entre com um número: '))

cont = 0
i = 1
while (i <= numero):
    if not (numero % i):
        cont += 1
    i += 1
if cont == 2:
    print(f'{numero} é um número primo', end='\n')
else:
    print(f'{numero} não é um número primo', end='\n')