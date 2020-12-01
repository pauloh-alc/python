"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
print('Com while: ')
print('i, j')
i = 0
j = 10
while i < 9:
    print(i, j)
    i += 1
    j -= 1

print('Com for: ')
print('i, j')
for i, j in enumerate(range(10, 1, -1)):
    print(i, j)  # 'i' representa o índice
