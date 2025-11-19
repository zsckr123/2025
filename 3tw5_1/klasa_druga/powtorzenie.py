''' Instrukcja warunkowa'''

#
# while True:
#     liczba1 = float(input('Podaj  pierwszą liczbe'))
#     liczba2 = float(input('Podaj liczbe drugą'))
#     if liczba1 > liczba2:
#         print(f'Liczba {liczba1} jest większa od {liczba2}')
#     elif liczba1 < liczba2:
#         print(f'Liczba {liczba2} jest większa od {liczba1}')
#     else:
#         print('Podane liczby są identyczne')
#     key = input("Podaj x aby zakończyć")
#     if key=='x':
#         break

''' Instrukcja pętli'''

# for i in range(4,11,2):
#     print(i)
# print('-------------')
# for i in range(11,4,-2):
#     print(i)
''' Lista'''
lista = [1,2,3,4,'a',1,2,3,4,'a']
# #
#
for el in lista[:-1:2]:
    print(el)
print('-------------')
for i in range(len(lista)):
     print(lista[i])


