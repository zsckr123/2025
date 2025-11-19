'''
a_1=1
a_2 = 2
a_n+2 = a_n+1 / a_n dla n >=3
'''
def ciag(n):
    if n == 1:
         return 1
    if n == 2:
         return 2

    return ciag(n - 1) / ciag(n-2)

print('10 ty wyraz ', ciag(10))