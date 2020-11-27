
with open("texto.txt", "a") as f:
    nome  = input('Entre com seu nome: ')
    idade = input('Entre com sua idade ')
    f.write('Nome: {} \n'.format(nome))
    f.write('Idade: {} \n'.format(idade))

