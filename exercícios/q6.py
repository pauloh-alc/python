n = input("Entre com um número 'n': ")
n = int(n)

i = 1
soma = 0
while i < n:
    if i % 2:
        soma += i
    i+=1
print(f"Soma dos número ímpares menores que {n} é: {soma}")