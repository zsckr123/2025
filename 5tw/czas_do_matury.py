from datetime import datetime
import time

# Podaj datę docelową
data_docelowa = datetime(2026, 4, 24, 8, 00, 00)

while True:
    teraz = datetime.now()
    roznica = data_docelowa - teraz

    if roznica.total_seconds() <= 0:
        print("Czas minął!")
        break

    dni = roznica.days
    sekundy = roznica.seconds

    godziny = sekundy // 3600
    minuty = (sekundy % 3600) // 60
    sek = sekundy % 60

    print(f"Pozostało: {dni} dni {godziny} godzin {minuty} minut {sek} sekund", end="\r")

    time.sleep(1)