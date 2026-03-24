def reszta(kwota, bankomat):
    bankomat.sort(reverse=True)
    wynik = {}

    for m in bankomat:
        if kwota >= m:
            ilosc_nom = kwota // m
            kwota = kwota % m
            wynik[m] = ilosc_nom

    # 🔴 sprawdzamy czy coś zostało
    if kwota != 0:
        return "Nie można wypłacić dokładnej kwoty"

    return wynik


print(reszta(2150, [50, 100, 200]))