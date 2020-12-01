while True:
    n = input("Entre com um número 'n': ")
    if not n.isnumeric():
        print("Erro: você precisa digitar um número inteiro e positivo !!")
        continue

    lista = []
    n = int(n)
    for i in range(1, n+1):
        if n % i == 0:
            lista.append(i)

    print(f"O divisores do número {n} são: { lista}")

    opcao = input("Deseja continuar? [s][N]: ")
    if opcao.lower() == 'n':
        break

