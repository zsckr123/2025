liczba = int(input('Podaj liczbe '))
podziel_4 = str(liczba)
dlugosc = len(podziel_4)
print(f'dlugosc liczby {podziel_4} wynosi {dlugosc}')
print('ostatnia cyfra ', podziel_4[-1])
print('przedostatnia cyfra ', podziel_4[-2])
print('dwie ostatnie cyfry ', int(podziel_4[-2]+podziel_4[-1]) )
if int(podziel_4[-2]+podziel_4[-1]) % 4 ==0:
    print(f'{liczba} jest podzielna przez 4')
else:
    print(f'{liczba} NIE  jest podzielna przez 4')