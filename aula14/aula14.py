"""
Manipulando Strings:

*Strings índices
* Fatiamento de strings [início: fim: passo]
* Functions built-in len, abs, type, print, etc

"""
#       [012345678]
texto = 'Python s2'
#      -[987654321]

# -1 representa o último caractere de uma string

print(texto[0])
print(texto[1])
print(texto[6])

url = "www.google.com.br/"
print(url)
print(url[:-1])


#  fatiamento de  string
nova_string = texto[2:6]
print(nova_string)

#  por padrão começa do início [0] e vai até a 7
print(texto[:8])

print(texto[:])

print(texto[0:-1:2])

