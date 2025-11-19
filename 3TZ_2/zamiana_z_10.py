''' Zamiana liczby w systemie dziesiątkowym na inny o podstawie
"podstawa_1"  '''

liczba = int(input('Podaj liczbę'))
podstawa_1 = int(input('Podaj podstawę'))
lista = []
while liczba > 0:
    reszta = liczba % podstawa_1
    wynik = liczba // podstawa_1
    lista.append(reszta)
    liczba = wynik

print(lista[::-1])