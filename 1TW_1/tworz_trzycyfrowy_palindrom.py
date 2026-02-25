cyfrowa_srodkowa=[0,1,2,3,4,5,6,7,8,9]
liczba = input('podaj pierwsza liczbe')
lista_palindromow = []
for i in cyfrowa_srodkowa:
    palindrom = liczba + str(i) + liczba
    lista_palindromow.append(palindrom)
print(lista_palindromow)
