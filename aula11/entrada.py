"""
    verifica se tem somente números positivos e inteiros
    isdecimal, isnumeric isdigit
    Retorna True, se inteiro positivo
    Retorna False, se diferente de inteiro positivo
"""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print('ERRO: não foi possível converter os números para realizar a conta')