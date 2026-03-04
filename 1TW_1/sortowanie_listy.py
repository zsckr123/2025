import random, time

lista_losowa = []
start = time.time()

for i in range(1,10001):
    liczba_losowa = random.randint(1,1000000)
    lista_losowa.append(liczba_losowa)
stop = time.time()

print(sorted(lista_losowa))
print(stop-start)  # sortowanie rosnące
# print(sorted(lista_losowa, reverse=True))  # sortowanie malejące