liczba = int(input('Podaj liczbę'))
podstawa = int(input('Podaj podstawę'))
lista = []
while liczba > 0:
    reszta = liczba % podstawa
    wynik = liczba // podstawa
    lista.append(reszta)
    liczba = wynik

print(lista[::-1])