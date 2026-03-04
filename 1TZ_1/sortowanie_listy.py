import random, time

lista_losowa = []


for i in range(1,10001):
    liczba_losowa = random.randint(1,1000000)
    lista_losowa.append(liczba_losowa)

start = time.time()
print(sorted(lista_losowa))
stop = time.time()
print(stop-start)  
# print(sorted(lista_losowa, reverse=True))  # sortowanie malejące