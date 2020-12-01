
while True:
    n = input("Entre com um valor para 'n' [1-9]: ")
    if not n.isdigit():
        print("Erro: digite um número inteiro e positivo !!")
        continue
    else:
        n = int(n)

    if n >= 1 and n <= 9:
        for i in range(1, 10):
            print(f"{n} * {i} = {n*i}")

