"""
    while em python
"""
# while True:
#     nome = input('Qual o seu nome: ')
#     print(f'Nome digitado foi {nome}')

# x = 0
# while x < 100:
#     print(x)
#     x += 1

# x = 0
# while x < 5:
#     print(x)
#     x += 1

#-----------------------------------------

# x = 0
# while x < 10:
#     if x == 2:
#         x += 1
#         continue
#     print(x)
#     x += 1
#------------------------------------------
# i = 0
# while i < 100:
#     cont = 0
#     for k in range(1, i+1):
#         if i % k == 0:
#             cont += 1
#     if cont == 2:
#         print(f'{i} é primo')
#     if i % 2:
#         print(f'{i} é impar')
#     if i == 50 or i == 63:
#         break
#     i += 1
#--------------------------------------------


x = 0

while x < 10:
    y = 0
    while y < 5:
        print(f'x = {x}; y {y}')
        y += 1
    print(end='\n')
    x += 1

