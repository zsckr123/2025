''' Zamiana na system dziesiątkowy'''
# 1100  2^0 2^1 , 2^2, 2^3
podstawa = int(input('Podaj podstawę='))
liczba= input(f'Podaj liczbe w systemie {podstawa} ')

liczba_10 =0 
potega = 0
for i in liczba[::-1]:
    liczba_10 += int(i) * podstawa ** potega
    potega +=1
print(f'Liczba w systemie dziesiątkowym: {liczba_10}')