"""
    Operação ternária em python
"""


logged_user = False
# SEM OPERADOR TERNÁRIO

# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa logar'
#
# print(msg)

# Utilizando operador ternário:

msg = 'Usuário logado' if logged_user else 'Usário precisa logar'
print(msg)

idade = input('Qual a sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas número inteiros e positivos')
else:
    idade = int(idade)

mensagem = 'Pode acessar' if idade >= 18 else 'Não pode acessar'
print(mensagem)

