'''
a_1 =2
a_2 = 4
a_n+2 = (a_n+1 +a_n) /2 dla n >=3

..., a_n-2, a_n-1, a_n, a_n+1,a_n+2,...
'''

def ciag(n):
    if n==1:
        return 2
    if n==2:
        return 4

    return (ciag(n-1) + ciag(n-2)) /2

print('10 ty wyraz ', ciag(10))