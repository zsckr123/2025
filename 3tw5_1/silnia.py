
'''
0!=1
1!=1
2!=1!2=1*2=2
3!=2!3= 2*3=6


n!=(n-1)!n
'''
def silnia(n):
    if n == 1:
        return 1
    return silnia(n-1) * n

for i in range(1,20):
    print(f'{i}! = {silnia(i)}')