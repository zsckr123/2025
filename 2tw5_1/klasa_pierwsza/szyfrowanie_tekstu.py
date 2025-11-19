# lista = [1,'s']
# print(lista)
# print(ord('b'))
lista_zaszyfrowana =[]
wyraz = input('Podaj wyraz do zaszyfrowania')
for znak in wyraz:
    # print(ord(znak))
    lista_zaszyfrowana.append(ord(znak))
print(lista_zaszyfrowana)
