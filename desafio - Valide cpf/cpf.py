"""

  CPF = 168.995.350-09
  Validador de CPF

"""


# Função: realiza calculo
def calculo(r):
    return 11 - (r % 11)


# Início:
cpf = input("Entre com seu cpf no seguinte formato (168.995.350-09): ")

lista1 = cpf.split('.')  # Para remover o '.'
cpf_sem_pontos = ''.join(lista1)

# Para remover o - e os 2 últimos dígitos
cpf_puro = ''
cpf_completo = ''
for i, caractere in enumerate(cpf_sem_pontos):
    if caractere != '-' and i != 10 and i != 11:
        cpf_puro += caractere
    if caractere != '-':
        cpf_completo += caractere

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

if cpf_completo == cpf_puro:
    print(f'CPF: {cpf_puro} é válido !!')
else:
    print(f'CPF: {cpf_puro} inválido !!')
