import random
import time
def babelek(t):
  for i in range(len(t)-1):
    if t[i] > t[i+1]:
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t


lista =[]
for _ in range(20000):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)


# print(sorted(lista,reverse=True))
start = time.time()
print('---------------')
print(lista)
print('------------------')
print(sort_b(lista))
stop = time.time()
print('Czas metody ', stop - start)