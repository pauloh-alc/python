"""
    Interando strings
"""

minha_string = 'o rato roeu a roupa do rei de roma.'
#  minha_string = 'Paulo Henrique'  #  A variável minha_string mudou de valor, isso é um fato, porém minha string não, pois strings são imutáveis em python
tamanho_string = len(minha_string)
#  minha_string[2] = 'P' não posso fazer isso

print("A letra 'a' a aparece: {} vezes".format(minha_string.count('a')))

c = 0
nova_string = ''
qtd = 0
while c < tamanho_string:
     if minha_string[c] == 'r':
         #  pass
        nova_string = nova_string + minha_string[c].upper()#  ocrrendo a concatenação
     else:
         nova_string = nova_string + minha_string[c]
     if minha_string[c] == 'a':
         qtd += 1
     print(nova_string)
     c += 1

print(f'string final: {nova_string}')
print(qtd)
