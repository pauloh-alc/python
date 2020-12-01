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
    mdc = 1
    while True:
        if x % i == 0 and y % i == 0:
            mdc = mdc * i

        if x % i == 0:
            x = x / i
        if y % i == 0:
            y = y / i

        if x % i != 0 and y % i != 0:
            i += 1

        if x == 1 and y == 1:
            break
    print(f"mdc({a},{b}) = {mdc}")

