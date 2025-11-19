import random, time
lista =[]
for _ in range(2000):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)

start = time.time()
print('---------------')
print(lista)
print('------------------')
print(sorted(lista))
stop = time.time()
print('Czas metody ', stop - start)