def iloraz(a,b):
    if b==0:
        return 'Dzielnie niewykonalne'
    return a/b


x = float(input('Podaj pierwszą liczbę='))
y = float(input('Podaj drugą liczbę='))
print('iloraz wynosi: ', iloraz(x,y))