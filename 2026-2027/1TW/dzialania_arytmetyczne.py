print('działania arytmetyczne')
a=float(input('podaj pierwszą liczbę='))
b=float(input('podaj drugą liczbę='))
print('Dodawanie:', a+b)
print('odejmowanie:', a-b)
print('mnożenie:', a*b)
if b==0:
    print('dzielenie niewykonalne')
else:    
    print('dzielenie:', a/b)
print('potęgowanie:', a**b)