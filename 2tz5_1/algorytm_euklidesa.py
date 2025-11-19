''' Dzielimy liczba1 przez liczba2 '''
liczba1 = int(input('podaj pierwszą liczbę: '))
liczba2 = int(input('podaj drugą liczbę: '))
a = liczba1
b = liczba2
licznik = 0
if liczba2 == 0:
      print("NWD to:",liczba1)
else:
    while liczba2 > 0:
        reszta = liczba1 % liczba2
        liczba1 = liczba2
        liczba2 = reszta

# koniec pętli
print("najwiekszy wspolny dzielnik to:",liczba1)
nww = a*b / liczba1
print(f'NWW {a} i {b} = {nww} ')
# NWW(a,b) = a * b / NWD(a,b)