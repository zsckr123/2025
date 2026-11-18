# print(10 % 3)

a=int(input('podaj  liczbę parzystą ='))
if a % 2 ==0:
    for i in range(a,a+20,2): 
        print(i)
else:
    print('podales blędną liczbe')