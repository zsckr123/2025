
import random
import time

def babelek(t):
  for i in range(len(t)-1):
    if t[i] > t[i+1]:# znak > ma wpływ na rodzaj sortowania
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t

lista =[]
for _ in range(10000):
    liczba = random.randint(-1000,1000)
    lista.append(liczba)
# print(sorted(lista,reverse=True))
print('Lista nieposortowana ')
print(20*'-')
print(lista)
print('Lista posortowana ')
print(20*'-')
start = time.time()
print(sort_b(lista))
stop = time.time()
print("czas sortowania ", stop - start)