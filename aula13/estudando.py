nome = "Paulo henrique"

print('Nome minúsculo:', nome.lower())
print('Nome em maíusculo:', nome.upper())
print('Nome com iniciais maiúscula:',nome.title())


string1 = 'Paulo'
string2 = 'Luan'
string3 = 'Rilda'

print(string1)
string1 = '{:#^10}'.format(string1)
print(string1)

print(string2)
new_string1 = '{1:*>10}'.format(string1, string2)
print(new_string1, len(new_string1), type(new_string1))

print(string3.replace(string3, string1))

print('{s1} {s2} {s3} {s1} {s1}'.format(s1=string1, s2=string2, s3=string3))
print(f'{string1:.4s}')
print('{:.3s}'.format(string2))

numero = 10
print('{:@<10}'.format(numero))

print(bin(175))
print(max("Paulo", "PauloA"))
print(min("Paulo","PauloA"))
print(pow(2,2))
print(ord('A'))