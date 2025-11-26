

a = input('Wpisz zdanie:')
b= a.split(' ')
print('--------------')
for t in b:
    print(t)
print('--------------')

for t in b[::2]:
    print(t)