

while True:
    string = input('Entre com um string: ')
    tamanho = len(string)

    i = 0
    maior_frequencia = 0
    letra = ''
    while i < tamanho:
        cont = string.count(string[i])
        if cont > maior_frequencia and string[i].strip():
            letra = string[i]
            maior_frequencia = cont
        i += 1
    print("O caractere '{}' aparece mais vezes ({}) na string digitada !!".format(letra, maior_frequencia))
