usuario = input('Entre com seu nome: ')

tamanho = len(usuario)
if tamanho <= 4:
    print(f'Seu nome ({usuario}) é muito curto !!')
elif tamanho <= 6:
    print(f'Seu nome ({usuario}) é normal !!')
else:
    print(f'Seu nome ({usuario}) é muito grande !!')