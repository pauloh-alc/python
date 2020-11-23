"""
Tipo de dados:

str - string - textos 'Assim', "Assim"
int - inteiro 123456 0 -10 -50 1500 -900
float - real / ponto flutuante - 10.20 1.5 -6.002
bool - booleano / lógico - True / False 10==10?

"""

print('Luiz')  # Já sabe que que isso é uma string
print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))

# Realizando um Catching

print('Luiz', type('Luiz'), bool('Luiz'))
print('', type(""), bool(""))
print('10', type('10'), type(int('10')))


print('Paulo', type('Paulo'))
print(10, type(10))
print(1.87, type(1.87))
print(20 > 18, type(20 > 18))