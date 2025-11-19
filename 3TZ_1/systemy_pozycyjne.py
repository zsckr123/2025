# Zamiana liczby z systemu 10 na inny
liczba = int(input('Podaj liczbę'))
podstawa = int(input('Podaj podstawę nowego systemu liczbowego'))
lista = []
while liczba > 0:
    reszta = liczba % podstawa
    wynik = liczba // podstawa
    lista.append(reszta)
    liczba = wynik

print(lista[::-1])