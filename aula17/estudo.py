minha_string = "Paulo Henrique Diniiiiiiiiiiiiiiiiiz de Lima Alencar"
tamanho_string = len(minha_string)

i = 0
maior = 0
letra = ''
while i < tamanho_string:
    cont = minha_string.count(minha_string[i])

    if cont > maior and minha_string[i].strip():
        maior = cont
        letra = minha_string[i]

    print(cont, minha_string[i])
    i += 1

print('A letra {} é a que aparece mais vezes: {}'.format(letra, maior))


