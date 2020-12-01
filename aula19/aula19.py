"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend + min, max
range
"""
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1

string = 'ABCDE'
print(string[1])
print(lista[1])

lista2 = ['A', 'B', 'C', "Dado", 10.5]
print(lista2[3])
lista2[4] = "Holanda"
print(lista2[4])
print(lista2[0:2])
print(lista2)
print(lista2[::-1]) #  Invertendo a lista

string1 = "Paulo"
print(string1[::-1]) # Invertendo a string

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l1.extend(l2)
print(l1)
l1.extend('a')
print(l1)


l2.append('b') # append insere um novo valor no final da lista
print(l2)

listinha = [1, 2, 3, 4]
listinha.insert(0, 'Banana')
print(listinha)

listinha.pop(1)
print(listinha)

k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(k)
del(k[3:5])
print(k)

t = list(range(1, 10))
print(t)
soma = 0
for valor in t:
    soma = soma + valor
print(soma)


e = ["String", True, 10, -20.5]
for elemento in e:
    print(f'{elemento} é do tipo {type(elemento)}')

j = [1,2,3,4,5]
p = str(j)
print(p[0])

s = 'Paulo'
w = 'Pfulo'
if w == s:
    print('iguais')