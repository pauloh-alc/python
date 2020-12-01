while True:
    a = input("Entre com o primeiro número: ")
    b = input("Entre com o segundo número: ")

    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
    else:
        continue

    x = a
    y = b
    i = 2
    mmc = 1
    while x != 1 or y != 1:

        if x % i == 0 or y % i == 0:
            mmc = mmc * i

        if x % i == 0:
            x = x / i

        if y % i == 0:
            y = y / i

        if x % i != 0 and y % i != 0:
            i += 1

    print(f'mmc({a},{b}) = {mmc}')
