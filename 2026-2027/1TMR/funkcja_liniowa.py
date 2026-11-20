# f(x)=ax+b
def liniowa(a,b,x):
    return a*x+b


a=float(input('Podaj wartość współczynnika a'))
b=float(input('Podaj wartość współczynnika b'))
# x = float(input('Podaj wartość argumentu x='))
for i in range(1,11):
    print(liniowa(a,b,i))
