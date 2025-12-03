def iloraz(a,b):
    if b==0:
        return 'Dzielnie niewykonalne'
    return a/b


x = int(input('Podaj pierwszą liczbę'))
y = int(input('Podaj drugą liczbę'))
print('iloraz wynosi: ', iloraz(x,y))