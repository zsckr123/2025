import random, time

def babelek(t):
  for i in range(len(t)-1):
    if t[i] < t[i+1]:  #  tu zmieniamy znak zeby zmienić rodzaj sortowania 
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t

lista_losowa = []
start = time.time()

for i in range(1,10001):
    liczba_losowa = random.randint(1,1000000)
    lista_losowa.append(liczba_losowa)
sort_b(lista_losowa)
stop = time.time()
print(stop-start)
