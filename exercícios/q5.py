
#  5! = 5 * 4 * 3 * 2 * 1
#  fat(5) = fat(4) * 5
#         = fat(n-1) * n

def fat(n):
    if n <= 0:
        return 1
    else:
        return n * fat(n-1)

n = input("Entre com um valor para 'n' para saber seu fatorial: ")
n = int(n)

fatorial = fat(n)
print(fatorial)


#  ou

n = input("Entre com um valor para 'n' para saber seu fatorial: ")
n = int(n)

fat = 1
#  for (i = 1; i < n + 1; i++)
for i in range(1, n + 1):
    fat = fat * i
print(f'fatorial de {n}! = {fat}')

