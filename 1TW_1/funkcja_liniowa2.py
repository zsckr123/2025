
'''y=ax-b'''
a = float(input('Podaj współczynnik a='))
b = float(input('Podaj współczynnik b='))

def liniowa(a , b , x):
    return a*x-b
    
for i in range(20):
    print(f'wartosc funkcji dla x={i} {liniowa(a,b,i)}')