'''
y=ax+b
'''

def liniowa(a,b,x):
    print(f'Wartość funkcji y={a}*x+{b} dla argumentu {x}')
    return a*x+b
print(liniowa(-2,3,4))