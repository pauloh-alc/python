while True:
    n = input("Entre com um número para saber se o mesmo é primo: ")
    if not n.isnumeric():
        print("O número digitado precisa ser um número inteiro e positivo !!")
        continue

    n = int(n)

    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1

    if cont == 2:
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} Não é primo")
