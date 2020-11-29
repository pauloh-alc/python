"""

while / else

contadores
acumuladores

"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else: #  Só é executado quando a expressão do while for False
    print('Cheguei no Else')