
while True:
    n = input("Entre com um 'n' inteiro e positivo: ")
    if not n.isdigit():
        continue
    else:
        n = int(n);
        for i in range(1, n+1):
            print(i)
