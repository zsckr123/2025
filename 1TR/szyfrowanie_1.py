

''' Kod ASCII  https://pl.wikipedia.org/wiki/ASCII'''
''' Zamiana wpisanego znaku na kod ASCII'''
print(ord('@'))
lista = [1,'s']
for znak in lista:
    print(ord(str(znak)))
# # 
# Szyfrowanie
#
#
#
lista_zaszyfrowana =[]

text = input('Podaj tekst do zaszyfrowania')
for znak in text:
    z = ord(znak)
    lista_zaszyfrowana.append(z)
print(lista_zaszyfrowana)