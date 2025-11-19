text = 'napis 2'
print(text)
'''' CTRL + /'''
# print(text[0]) # pierwszy element
# print(text[-1]) # ostatni element
# '''
# Drukowanie od początku do elementu o indeksie 2 ale
# bez tego elementu
# '''
print(text[:2])
print(text[1:4])
print(text[1:4:2])
#
for t in text:
    print(t)