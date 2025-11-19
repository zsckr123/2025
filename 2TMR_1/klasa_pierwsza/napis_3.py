def dlugosc(tekst1, tekst2):
    if len(tekst1) > len(tekst2):
        return f'{tekst1} jest dłuższy {tekst2}'
    elif len(tekst2) > len(tekst1):
        return f'{tekst2} jest dłuższy {tekst1}'
    return f'napisy są jednakowej dlugości'

print(dlugosc('komiks1111','komiks_'))