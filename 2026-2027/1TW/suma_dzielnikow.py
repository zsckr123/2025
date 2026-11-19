# Suma wszystkich dzielnikow właściwych 
liczba = int(input('Podaj liczbe'))
suma = 0
for i in range(2,int(liczba**0.5)+1):
    if liczba % i == 0:
        suma +=i
print(f'Suma dzielnikow właściwych liczby {liczba} wynosi {suma}')