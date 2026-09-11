''' 3. Suma liczb od 1 do n 
Za pomocą pętli for oblicz sumę 
liczb naturalnych 
od 1 do podanego przez użytkownika n.'''

n = int(input("podaj ilość liczb"))
suma = 0
for i in range(1,n+1):
    suma+=i
print(f"Suma {n} liczba wynosi {suma}")
