while True:
    n = input("Quantos números 'n' você quer ler: ")
    if not n.isnumeric():
        print('Erro: valor digitado deve ser um número inteiro e positivo !!')
        continue
    n = int(n)
    i = 1
    maior = 0
    while i <= n:
        #  numero = input(f"Número {i}: ")
        numero = input("Número {}: ".format(i))
        numero = int(numero)
        if numero > maior:
            maior = numero
        i += 1
    print(f"Maior número digitado foi: {maior}")
