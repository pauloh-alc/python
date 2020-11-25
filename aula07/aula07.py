
nome = 'Paulo'
idade = 20
altura = 1.86555

print(f'{nome} tem {idade} anos e altura {altura:.2f}')
print('{} tem {} anos e altura {:.2f}'.format(nome, idade, altura))
print('{0} tem {1} anos e altura {2:.2f}'.format(nome, idade, altura))
print('{n} tem {i} anos e altura {a}'.format(n=nome, i=idade, a=altura))
