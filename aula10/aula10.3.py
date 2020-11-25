
usuario = input("Nome do usuário: ")
senha = input("Digite sua senha: ")

usuario_bd = "Paulo Henrique"
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print(f'{usuario} você está logado no sistema', end='\n')
else:
    print(f'Erro: usuário ou senha inválidos')