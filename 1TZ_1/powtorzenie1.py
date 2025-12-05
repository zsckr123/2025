def laczenie_lancuchow(a,b):
    return a+b,len(a+b)

a= input('Podaj pierwszy lancuch=')
b= input('Podaj drugi lancuch=')
print('polaczony lancuch ',laczenie_lancuchow(a,b)[0])
print('dlugosc polaczonego lancucha', laczenie_lancuchow(a,b)[1])