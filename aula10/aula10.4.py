nome = input('Entre com algum nome: ')
letra = input('Entre com algum letra para verificar se ela existe no nome:')

if letra in nome:
    print(f'{letra} existe no nome {nome}.')
else:
    print(f'{letra} não existe no nome {nome}.')
