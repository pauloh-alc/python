
"""
For / Else em python
"""

var = ['Luiz Otávio', 'foãozinho', 'Maria']


for valor in var:
    if valor.lower().startswith('j'):
        print("Existe uma palavra que começa com J ou j")
        break # se cair no break, não vai executar o else
else:
    print("Não existe")
