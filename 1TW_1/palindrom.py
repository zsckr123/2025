def czy_palindrom(n):
    if str(n) == str(n)[::-1]:
      return 'tak'
    return 'nie'
liczba = int(input('podaj liczbe='))
print(czy_palindrom(liczba))
