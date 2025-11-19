import time
import random
def sort_insert(A):
    start = time.time()
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    delta = time.time() - start
    print(f'Czas sortowania {delta}')
    return A
lista = []
for _ in range(10000):
    liczba = random.randint(-10000,10000)
    lista.append(liczba)


print(lista)
print(sort_insert(lista))