"""
Operadores Lógicos

and, or, not
in e not in

"""

# and:
"""
    [v] and [v] = [v]
    [v] and [f] = [f]
    [f] and [v] = [f]
    [f] and [f] = [f]
"""

# or:

"""
    [v] and [v] = [v]
    [v] and [f] = [v]
    [f] and [v] = [v]
    [f] and [f] = [f]
    
"""

# not:
"""
    operador inversor
    Se [f] -> not [f] = [v]
"""

a = 2
b = 4

if not b > a:
    print(f'{b} é maior que {a}')
else:
    print(f'{a} é maior que {b}')

var = ''
b = 0

if not var:
    print('Preencha o valor de var')

if b:
    print('b é verdadeiro')
else:
    print('b é falso')

nome = input('Digite seu nome: ')
if 'u' in nome:
    print('u existe em seu nome')
else:
    print('nao existe')