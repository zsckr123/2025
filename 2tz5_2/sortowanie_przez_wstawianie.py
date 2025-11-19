import time
import random
from random import random, randint


def sort_insert(A):

    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz

    return A

lista =[]
for _ in range(10000):
    liczba = randint(-10000,10000)
    lista.append(liczba)
print('Lista nieposortowana')
print(20*'-')
print(lista)
print('Lista posortowana')
print(20*'-')
start = time.time()
print(sort_insert(lista))
stop = time.time()
print("czas sortowania", stop - start)