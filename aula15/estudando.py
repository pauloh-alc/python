while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador [*, +, -, /]: ')

    if num1.isdigit() == False or num2.isdigit() == False:
       continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '*':
        print(num1 * num2)
    elif operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Erro: operador digitado inválido')

    opcao = input('Sair: [S][n]: ')
    if opcao.lower() == 's':
        break
