
string = "paulo alencar"

print(string)
nova_string = ''
for i, letra in enumerate(string):
    if letra == 'p' or letra == 'a' and i == 6:
        nova_string = nova_string + string[i].upper()
    else:
        nova_string = nova_string + letra

print(nova_string)


l1 = [1,2,3,4]
l2 = [1,2,3,4]
if l1 == l2:
    print('l1 == l2')


l = ["Banana", "Uva", "Maça", "Mamão"]
i = 0
while i < len(l):
    print(l[i])
    i += 1


l.sort()
print(l)

h = [5,3,5,1,3,0]
h.sort()
h.reverse()
print(h)





