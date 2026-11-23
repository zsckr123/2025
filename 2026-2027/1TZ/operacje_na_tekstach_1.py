
text = 'napis 2'
#       0123456
print(text)

print('pierwszy element: ',text[0]) # pierwszy element
print('ostatni element: ', text[-1]) # ostatni element
# # '''

# # '''
print(' drukowanie od elementu drugiego do piątego ale bez piątego:',text[1:4]) # drukowanie od elementu drugiego do piątego ale bez piątego
'''
# drukowanie od elementu drugiego 
do piątego ale bez piątego - co drugi element
'''
print('drukowanie od elementu drugiego o piątego ale bez piątego - co drugi element:',text[1:4:2])

# #
print('--------------')
for t in text:
    print(t)