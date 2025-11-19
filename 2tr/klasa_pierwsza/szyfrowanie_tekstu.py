# lista = [1,'s']
# print(len(lista))
# print(lista[1])
# print(ord('B')) # zamiana znaku na kod ASCII
lista_zaszyfrowana =[]
wyraz = input('Podaj wyraz do zaszyfrowania')
for znak in wyraz:
    # print(ord(znak))
    lista_zaszyfrowana.append(ord(znak)) # dodawanie zaszyfrowanego znaku do listy
print(lista_zaszyfrowana)
