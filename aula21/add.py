#
# string = "O Brasil é o país do futebol, o Brasil é penta"
#
# lista = string.split(',')
# print(lista)
#
# for palavra in lista:
#     print(palavra.strip().capitalize())


# Join - transforma uma lista em string

text = "O Brasil é penta"
lista1 = text.split(' ')
print(lista1)

text2 = ' '.join(lista1)
print(text2)

print(''.join(['1', '2', '3']))
