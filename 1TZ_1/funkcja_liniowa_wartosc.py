'''
y=ax+b
'''

def liniowa(a,b,x):
    print(f'Wartość funkcji y={a}*x+{b} dla argumentu {x}')
    return a*x+b

for i in range(20):
    print(liniowa(-2,3,i))