
endereco = input("Entre com seu endereço: ")

mensagem = 'Seu endereço é: {}'.format(endereco) if endereco else 'Você precisa entrar com um valor'
print(mensagem)