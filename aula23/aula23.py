x = 10
y = 'Luiz'

print(f"x = {x}, y = {y}")
x, y = y, x  # Trocando valores
print(f"x = {x}, y = {y}")

# outra forma

# print(f"x = {x}, y =  {y}")
#
# aux = x
# x = y
# y = aux
#
# print(f"x = {x}, y =  {y}")

paulo = 'paulo'
rilda = 'rilda'
luara = 'luara'

print(paulo)
print(rilda)
print(luara)

paulo, luara, rilda = rilda, paulo, luara

print('\n')
print(paulo)
print(rilda)
print(luara)