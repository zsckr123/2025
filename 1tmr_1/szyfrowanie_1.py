

''' Kod ASCII  https://pl.wikipedia.org/wiki/ASCII'''
''' Zamiana wpisanego znaku na kod ASCII'''
print(ord('A'))
lista = [1,'s']
for znak in lista:
    print(ord(str(znak)))
#
# #Szyfrowanie
#
#
#
lista_zaszyfrowana =[]

wyraz = input('Podaj wyraz do zaszyfrowania')
for znak in wyraz:
    z = ord(znak)
    lista_zaszyfrowana.append(z)
print(lista_zaszyfrowana)