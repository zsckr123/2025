def iloraz(a,b):
    if b==0:
        return 'Dzielenie nie wykonalne'
    return a/b

x = int(input('Podaj pierwszą liczbę'))
y = int(input('Podaj drugą liczbę'))
print('Iloraz ',iloraz(x,y))