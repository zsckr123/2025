a = float(input('Podaj współczynnik a:'))
b = float(input('Podaj współczynnik b:'))

def liniowa_1(x):
    return  a * x + b

for x in range(100,0,-2):
    print(f' Wartość funkcji: {liniowa_1(x)} '
      f'dla argumentu: {x}')