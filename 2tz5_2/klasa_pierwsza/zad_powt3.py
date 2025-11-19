def tekst():
    wyraz = input('Podaj dowolny ciąg znakowy')
    return wyraz[-1:0:-1]
print(tekst())