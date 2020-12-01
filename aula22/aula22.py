"""

Desempacotamento de listas e Python

"""

lista = ['Luiz', 'João', 'Maria', 1 , 2, 3, 4, 5, 6]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1)
print(n2)
print(n3)
print(outra_lista)
print(ultimo_da_lista)


frutas = ['Uva', 'Melão', 'Maçã', 'Pera']

ultimo = frutas[-1]
print(ultimo, type(ultimo))

