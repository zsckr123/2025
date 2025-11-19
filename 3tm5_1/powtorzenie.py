''' Instrukcja warunkowa'''
#

# #
# while True:
#     liczba1 = float(input('Podaj liczbe pierwszą'))
#     liczba2 = float(input('Podaj liczbe drugą'))
#     if liczba1 > liczba2:
#         print(f'Liczba {liczba1} jest większa od {liczba2}')
#     elif liczba1 < liczba2:
#         print(f'Liczba {liczba2} jest większa od {liczba1}')
#     else:
#         print('Podane liczby są identyczne')
#     key = input('Podaj x aby zakończyć')
#     if key == 'x':
#         break

''' Instrukcja pętli'''

# for i in range(10,3,-2):
#     print(i)
# print('-----------------')
# for i in range(3,10,2):
#     print(i)
''' Lista'''
lista = [1,2,3,4,'a','b','c']
print(lista[1:4])
print(lista[5:2:-2])
print(lista)
for el in lista:
    print(el)
print('-------------')
# # #
for i in range(0,len(lista),2):
     print(lista[i])