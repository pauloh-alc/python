"""
    For in em Python
    Iterando strings com for
    Função range (start = 0, stop, step=1)
"""

# texto = 'python'
# for letra in texto:
#     print(letra)

#
# texto = 'Python'
# for i, letra in enumerate(texto):
#     print(i, letra)

for n in range(10): #  range (start = 0, stop, step=1)
    print(n)        #  default start = 0 e step = 1

print('Novo for - decrementando')

for i in range(20, 10, -1):
    print(i)

print('Novo for - multiplos')

for i in range(0, 100, 8):
    print(i)

print('Novo for - interando em strings')

# continue - pula para o próximo laço
# break - encerra a nossa interação
text = 'paulo'
new_text = ''
for letra in text:
    if letra == 'p':
        continue
        new_text += letra.upper()
    elif letra == 'u':
        new_text += letra.upper()
        break
    else:
        new_text += letra
print(new_text)
