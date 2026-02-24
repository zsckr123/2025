# Suma wszystkich dzielnikow
liczba = int(input('Podaj liczbe'))
suma = 0
for i in range(1,liczba+1):
    if liczba % i == 0:
        suma +=i
print(f'Suma dzielnikow liczby {liczba} wynosi {suma}')