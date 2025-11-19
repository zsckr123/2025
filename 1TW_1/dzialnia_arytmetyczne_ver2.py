def suma(a, b):
    return f'Wynik działania {a}+{b}= {a+b}'

def odejmowanie(a, b):
    return f'Wynik działania {a}-{b}= {a-b}'

def iloczyn(a, b):
    return f'Wynik działania {a}*{b}= {a*b}'

def iloraz(a, b):
    if b==0:
        return f'Dzielenie niewykonalne'
    return f'Wynik działania {a}/{b}= {a/b}'

print(suma(2,3))
print(odejmowanie(2,3))
print(iloczyn(3,4 ))
print(iloraz(2,0))


