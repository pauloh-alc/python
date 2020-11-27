"""

    Formatando valores com modificadores:

    :s - Texto (strings)
    :d - Inteiros
    :f - Números de ponto flutuante (float)
    :.(NÚMERO)f - Quantidade de casas decimais (float)
    :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)


"""

#  < - direita
#  > - esquerda
#  ^ - centro

num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num1 = 1
print(f'{num1:0>10}')  # colocando a esquerda, coloca Zeros até num1 ter 10 dígitos
print(f'{num1:0<10}')  # colocando a direita ...

nome = 'Paulo Henrique'
print(f'{nome:#>20}')