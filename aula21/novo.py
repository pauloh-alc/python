
nome = "Paulo Henrique Diniz de Lima Alencar"
lista_nome = nome.split(' ')
print(lista_nome)

for indice, elemento in enumerate(lista_nome):
    print(indice, elemento, lista_nome[indice])


lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista:
    print(v[0])


lista2 = [
    [0, "Paulo"],
    [1, "Luara"],
    [2, "Débora"]
]

for indice, nome in lista2:
    print(indice, nome)


n1, n2, n3 = lista2

i, n = n1
print(i, n)



