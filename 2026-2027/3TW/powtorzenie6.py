licznik=1
magazyn = []
while licznik<=10:
    liczba = int(input("Podaj liczbe"))
    if liczba >=10 and liczba <=99 and  liczba % 3==0:
        magazyn.append(liczba)
        licznik+=1
print(magazyn)
