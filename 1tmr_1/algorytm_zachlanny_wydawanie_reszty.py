def reszta(kwota, bankomat):
    bankomat.sort(reverse=True)
    wynik = []

    for m in bankomat:
        while kwota >= m:
            kwota -= m  
            wynik.append(m)

    return wynik

print(reszta(1150, [50, 100, 200]))