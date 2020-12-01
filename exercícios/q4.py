n = input("Entre com um número 'n': ")
n = int(n)

soma = 0
for i in range(0, n):
    numero = input(f"Número {i}: ")
    numero = int(numero)
    soma = soma + numero
print(f'Soma = {soma}')
