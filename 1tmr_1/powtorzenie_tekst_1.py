# print(chr(44))

lista = [102, 115, 100, 102, 109, 115, 100, 46, 102, 109, 115, 100, 46, 102, 46]
tmp = ''
for znak in lista:
    tmp += chr(znak) # tmp = tmp + chr(znak)
print(tmp.upper())