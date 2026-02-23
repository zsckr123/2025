'''Szukanie liczb pierwszych'''
liczba_pierwsza = int(input('Podaj liczbę do badania'))
licznik_dzielnikow = 0


for i in range(2,int(liczba_pierwsza ** 0.5)+1): # 2**3 oznacza 2^3
    if liczba_pierwsza % i == 0:
        licznik_dzielnikow += 1
if licznik_dzielnikow > 0:
    print(f'Liczba {liczba_pierwsza} NIE  jest liczbą pierwszą')
else:
    print(f'Liczba {liczba_pierwsza}  jest liczbą pierwszą')
