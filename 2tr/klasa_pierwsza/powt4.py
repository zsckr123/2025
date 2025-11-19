def tekst():
    wyraz = input('Podaj dowolny ciąg znakowy')
    lista = []
    for i in wyraz[::-2]:
        # print(ord(i))
        lista.append(ord(i))
    return lista
print(tekst())


# [97, 110, 101, 114, 73]