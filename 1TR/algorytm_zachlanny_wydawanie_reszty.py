def reszta(kwota, bankomat):
    bankomat.sort(reverse=True)
    wynik = []

    for m in bankomat:
        while kwota >= m:
            kwota -= m  
            wynik.append(m)

    return wynik

print(reszta(97, [1, 2, 5]))