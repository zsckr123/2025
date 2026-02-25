# Suma  dzielnikow wlasciwych
liczba = int(input('Podaj liczbe'))
suma =0
for i in range(2,liczba):
    if liczba % i == 0:
        suma +=i
print(f'Suma dzielnikow liczby {liczba} wynosi {suma}')