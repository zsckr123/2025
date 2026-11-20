import random

sekret = random.randint(1, 20)
proba =  int(input("Twoja propozycja od 1 do 20: "))
licznik = 0

print("Wylosowałem liczbę od 1 do 20. Zgadnij ją!")

while proba != sekret:
    proba = int(input("Twoja propozycja od 1 do 20: "))
    licznik += 1

    if proba < sekret:
        print("Za mało!")
    elif proba > sekret:
        print("Za dużo!")

print(f"Brawo! Zgadłeś w {licznik} próbach.")