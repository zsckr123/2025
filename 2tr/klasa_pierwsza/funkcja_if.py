'''
if warunek:
    instrukcja1
else:
    instrukcja2
'''

a = int(input('Podaj liczbe'))
if a > 0:
    print('Liczba dodatnia')
elif a < 0:
    print('Liczba ujemna')
else:
    print('Liczba zero')