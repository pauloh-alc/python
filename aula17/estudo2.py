
string1 = "Paulo Henrique Diniz de Lima Alencar"
string1 = "Luara Linda Lima Limpeza"
tamanho = len(string1)

i = 0
string1_nova = ''#  String vazia
while i < tamanho:
    if string1[i] == 'L':
        string1_nova += string1[i].lower()
    else:
        string1_nova += string1[i]
    i += 1

print(string1_nova)
