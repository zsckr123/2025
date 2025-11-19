''' Zamiana na system o podstawie "10" '''
liczba_w_innym_systemie = [1,1,1,0,1,1]
podstawa = int(input('Podaj podstawę')) # tu jest podstawa tego nowego systemu
liczba_p = 0
potega = 0

for i in liczba_w_innym_systemie[::-1]:
    liczba_p += i * podstawa ** potega

    potega +=1
print(f'Liczba w innym  systemie : {liczba_p}')