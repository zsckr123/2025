
def f_liniowa(a,b, x):
    return a * x - b

print(f' Wartosc funkcji:  {f_liniowa(4,1 ,3)}') # f(3)=4 *3 - 1

def f_liniowa_1(x):
    a = float(input('podaj a'))
    b = float(input('podaj b'))
    return a * x - b
# Drugi sposób
print('--------------')
print('Drugi sposób')
print(f_liniowa_1(2))


