
secreta = 'perfume'
digitadas = []
chances = 3
cont = 0
while True:

    if chances <= 0:
        print("Você perdeu!!")
        print(f"A palavra secreta era {secreta}")
        break

    letra = input('Entre com um letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra!')
        continue
    digitadas.append(letra)

    if letra in secreta:
        print(f"UHUULL, a letra '{letra}' existe na palavra secreta.")
    else:
        print(f"AFFFzz, a letra '{letra}' não existe na palavra secreta.")
        digitadas.pop()
        chances -= 1


    secreta_temporaria = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += '_'

    print(secreta_temporaria)
    if secreta == secreta_temporaria:
        print("Parabéns você ganhou !!")
        print(f"A palavra era {secreta}")
        break
    else:
        print(f"Você ainda tem {chances}")
        print(digitadas)









