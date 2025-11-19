def tekst(lista):
    tmp = ''
    for i in lista:
        tmp += chr(i)
    return tmp
print(tekst([97, 110, 101, 114, 73]))