"""
    Split, Join, Enumerate em Python
    * Split - Dividir uma string # str
    * Join  - Juntar uma lista # str
    * Enumerate - Enumerar elementos da lista # list
"""
variavel = "O Brasil é o o o país do futebol, o Brasil é penta"

lista1 = variavel.split(' ')
lista2 = variavel.split(',')
print(lista1)
print(lista2)

maior = 0
nome = ''
for palavra in lista1:
    qtd = lista1.count(palavra)
    if qtd > maior:
        maior = qtd
        nome = palavra

print(f'A palavra que apareceu mais vezes foi {nome} ({maior}x)')
