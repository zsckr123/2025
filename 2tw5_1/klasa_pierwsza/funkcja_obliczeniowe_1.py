'''
y = a x + b
f(x) = ax +b
f(-1) = 2x+1 = 2 * (-1) +1
'''

def liniowa_1(x):
    return x, 2 * x + 1

print(f' Wartość funkcji:{liniowa_1(-1)[1]} '
      f'dla argumentu {liniowa_1(-1)[0]:}')