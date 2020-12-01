"""
    - Programa:
    * Adiciona em uma lista;
    * Remove em uma lista;
    * Busca elementos em uma lista.

"""

opcaoPrincipal = 1
lista = []

while True:
    if opcaoPrincipal == 0:
        lista = []

    print('\n[1] Adicionar elemento na lista')
    print('[2] Remover elemento na lista')
    print('[3] Buscar elemento na lista')
    print('[0] SAIR')
    opcaoPrincipal = input("Entre com uma opcao: ")
    if not opcaoPrincipal.isnumeric():
        print('Erro: você precisa inserir um número inteiro e positivo !!')
        continue
    opcaoPrincipal = int(opcaoPrincipal)

    if opcaoPrincipal == 0:
        break

    if opcaoPrincipal < 0 or opcaoPrincipal > 4:
        print("Erro: você precisa digitar uma opção entre [1-3]")
        continue

    # [1] Adiciona elementos em uma lista
    if opcaoPrincipal == 1:
        while True:
            print('\n[1] Adicionar no final da lista')
            print('[2] Adicionar em um índice específico')
            print('[0] SAIR')
            opcao = input("Entre com uma opcao: ")

            if not opcao.isnumeric():
                print('Erro: você precisa inserir um número inteiro e positivo !!')
                continue
            opcao = int(opcao)
            if opcao == 0:
                break

            if opcao < 0 or opcao > 4:
                print("Erro: você precisa digitar uma ocpao entre [1-2]")
                continue

            # [1] Adicionar no final da lista
            if opcao == 1:
                elemento = input("Digite o elemento: ")
                opcao = input("Elemento int [int] ou str [str]: ")
                if opcao == "int":
                    elemento = int(elemento)
                lista.append(elemento)
                print(f"Lista atual: {lista}")

            # [2] Adicionar em um índice específico
            elif opcao == 2:
                posicao = int(input("Digite a posição para inserir: "))
                elemento = input("Digite o elemento: ")
                opcao = input("Elemento int [int] ou str [str]: ")
                if opcao == "int":
                    elemento = int(elemento)
                lista.insert(posicao, elemento)
                print(f"Lista atual: {lista}")

            # Opção inválida
            else:
                print('Erro: opcao inválida')
                continue

    # [2] Remove elementos em uma lista
    elif opcaoPrincipal == 2:
        while True:

            print('\n[1] Remover ultimo elemento da lista')
            print('[2] Remover elemento específico')
            print('[0] SAIR')
            opcao = input("Entre com uma opcao: ")
            if not opcao.isnumeric():
                print('Erro: você precisa inserir um número inteiro e positivo !!')
                continue
            opcao = int(opcao)

            if opcao == 0:
                break
            if opcao < 0 or opcao > 3:
                print('Erro: você precisa digitar uma opção entre [1-2]')
                continue

            # [1] Remover ultimo elemento da lista
            if opcao == 1:
                if bool(lista) is not False:
                    lista.pop()
                print(f"Lista atual: {lista}")
            # [2] Remover elemento específico
            elif opcao == 2:
                posicao = int(input("Digite a posição para remover: "))
                if bool(lista) is not False:
                    lista.pop(posicao)
                print(f"Lista atual: {lista}")

            # Opção inválida
            else:
                print('Erro: opção inválida')
                continue

    # [3] Buscar elemento na lista
    elif opcaoPrincipal == 3:
        while True:
            print('\n[1] Buscar por posição')
            print('[2] Buscar por elemento')
            print('[0] SAIR')
            opcao = input('Digite sua opcao: ')
            if not opcao.isnumeric():
                print('Erro: você precisa inserir um número inteiro e positivo !!')
                continue
            opcao = int(opcao)

            if opcao == 0:
                break
            if opcao < 1 or opcao > 2:
                print('Erro: você precisa digitar uma opção entre [1-2]')
                continue

            # [1] Buscar por posição
            if opcao == 1:
                sinalizador = False
                posicao = int(input("Entre a posiçao do elemento que você buscar: "))

                for i in range(0, len(lista)):
                    if i == posicao:
                        print(f"Elemento na posição {posicao}: {lista[i]}")
                        sinalizador = True
                        break

                if sinalizador is not True:
                    print('Posição digitada não corresponde a nenhuma posição válida')

            # [1] Buscar por elemento
            elif opcao == 2:
                sinalizador = False
                elemento = input('Elemento que deseja buscar: ')
                escolha = input('Elemento é um [inteiro] int ou [str] str: ')
                if escolha == 'int':
                    elemento = int(elemento)

                for i, j in enumerate(lista):
                    if elemento == j:
                        print(f"Elemento na posição {i} é: {j}")
                        sinalizador = True
                        break

                if sinalizador is not True:
                    print('Elemento não encontrado')

            # Opção inválida
            else:
                print('Erro: opcao inválida')
