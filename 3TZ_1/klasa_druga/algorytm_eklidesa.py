''' Dzielimy liczba1 przez liczba2 '''
while True:
    liczba1 = int(input('podaj pierwszą liczbę: '))
    liczba2 = int(input('podaj drugą liczbę: '))
    licznik = 0
    if liczba2 == 0:
          print("Nie dzielimy przez zero")
    else:
        while liczba2 > 0:
            reszta = liczba1 % liczba2
            liczba1 = liczba2
            liczba2 = reszta
    print("najwiekszy wspolny dzielnik to:", liczba1)
    key = input('Podaj x aby zakończyć')
    if key == 'x':
        break

# koniec pętli
