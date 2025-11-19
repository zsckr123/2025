import time
import random


def sort_insert(A):
    start = time.time()
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] < klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz

    return A

lista =[]
for _ in range(200):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)
print('Lista nieposortowana')
print(lista)
print(20*'-')
start = time.time()
print('Lista posortowana')
print(sort_insert(lista))
stop = time.time()
print('Czas metody ', stop - start)

print('Sortowanie za pomoca metdy sorted')
start = time.time()
print('Lista posortowana')
print(sorted(lista, reverse=True))
stop = time.time()
print('Czas metody sorted ', stop - start)

