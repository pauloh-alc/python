"""

  Gerador de cpf válido

"""
from random import randint
numero = str(randint(100000000, 999999999))


# Função: realiza calculo
def calculo(r):
    return 11 - (r % 11)


# Início:
cpf = numero
# Para remover os 2 últimos dígitos
cpf_puro = ''

for i, caractere in enumerate(cpf):
    if i != 9 and i != 10:
        cpf_puro += caractere

# Gerando 1° Dígito:

soma = 0
k = 0
for i in range(10, 1, -1):
    soma = soma + int(cpf_puro[k]) * i
    k += 1
formula = calculo(soma)
if formula > 9:
    digito1 = '0'
else:
    digito1 = str(formula)

# Gerando Dígito 2
cpf_puro = cpf_puro + digito1  # Concatenando CPF atual + dígito1
k = 0
soma = 0
for i in range(11, 1, -1):
    soma = soma + int(cpf_puro[k]) * i
    k += 1
formula = calculo(soma)

if formula > 9:
    digito2 = '0'
else:

    digito2 = str(formula)

cpf_puro = cpf_puro + digito2  # Concatenando CPF atual + dígito2

print('CPF gerado: '+cpf_puro)
