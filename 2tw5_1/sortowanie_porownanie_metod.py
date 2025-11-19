import time
import random
from random import random, randint

# Sortowanie przez wstawianie
def sort_insert(A):

    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz

    return A
# Sortowanie bąbelkowe
def babelek(t):
  for i in range(len(t)-1):
    if t[i] > t[i+1]:   # zmiana znak = zmiana trybu sortowania
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t

def porownanie_metod(lista):
    print('Metoda bąbelkowa')
    start = time.time()
    sort_b(lista) # metoda babelkowa
    stop = time.time()
    print('czas metody ', stop - start)
    print('Metoda przez wstawianie')
    start = time.time()
    sort_insert(lista)
    stop = time.time()
    print('czas metody ', stop - start)
    print('Metoda wbudowana sorted')
    start = time.time()
    sorted(lista)
    stop = time.time()
    print('czas metody ', stop - start)

def lista():
    lista = []

    for _ in range(5000):
        liczba = randint(-10000,20000)
        lista.append(liczba)
    return lista

print('Lista nieposortowana')
print(lista())
porownanie_metod(lista())