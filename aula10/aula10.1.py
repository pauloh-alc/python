"""
    Operadores relacionais
    == > >= < <= !=
"""

print(2 == 1)  #  False

num1 = 1
num2 = '1'
print(num1 == num2)  # False

num1 = 2
num2 = 2
expressao = num1 == num2
print(expressao)

num1 = 2
num2 = 4
print(num1 < num2)

num1 = 5
num2 = 5

print(num1 >= num2)

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

idade_menor = 18
idade_maior = 30
if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} você pode pegar o emprestimo')
elif idade >= 10 and idade < idade_menor:
    print(f'{nome} você não pode pegar o emprestimo')
elif idade > idade_maior:
    print(f'{nome} pode preparar os documentos da sua aposetadoria')
else:
    print(f'{nome} sua idade é muito baixa')
