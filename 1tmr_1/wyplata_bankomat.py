def reszta(kwota, bankomat):
    bankomat.sort(reverse=True)
    wynik = {}

    for m in bankomat:
        if kwota >= m:
            ilosc_nom = kwota // m
            kwota = kwota % m
            wynik[m] = ilosc_nom

    return wynik

print(reszta(1150, [50, 100, 200]))