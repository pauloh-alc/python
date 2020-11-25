nome = 'Paulo'
idade = 20
altura = 1.86
peso = 65
imc = peso / altura ** 2
data_nascimento = 2000

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.', end='\n')
print(f'O imc de {nome} é {imc:.2f}.', end='\n')
print(f'{nome} nasceu em {data_nascimento}.', end='\n')