cyfry = [0,1,2,3,4,5,6,7,8,9]
zbior_palindromow = []


for j in cyfry:
    for i in cyfry:
        palindrom = int(str(j) + str(i) + str(j))
        zbior_palindromow.append(palindrom)
print(zbior_palindromow)
