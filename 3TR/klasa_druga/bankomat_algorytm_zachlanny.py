def ile_moneta(kwota, banknot):
    licznik = 0
    if kwota >= banknot:
        licznik = kwota // banknot
        # kwota = kwota - banknot * licznik
        kwota = kwota % banknot
    return licznik, kwota

def rozmien_kwota(kwota, lista):
    kwota_oryg = kwota
    kwota_spr = 0
    bankomat = {}
    for el in lista:
        bankomat[str(el)] = ile_moneta(kwota, el)[0]
        kwota = ile_moneta(kwota, el)[1]
    for el in bankomat.keys():
        kwota_spr += int(el) * bankomat[el]
    if kwota_spr == kwota_oryg:
        return bankomat
    return 'blaedna kwota'
# print(ile_moneta(120,30))
# print(ile_moneta(120,30)[1])
print(rozmien_kwota(1241,[100,50,20]))