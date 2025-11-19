'''
a_1=1
a_2 = 2
a_n+2 = a_n+1 / a_n dla n >=3
a_n-2,a_n-1,a_n,a_n+1,a_n+2,a_n+3,a_n+4
'''
def ciag(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ciag(n-1) / ciag(n-2)

print(ciag(30))