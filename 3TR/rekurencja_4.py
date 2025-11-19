'''
a(n+1) = a(n) +n
'''

def ciag(n):
    if n == 1:
        return 1
    return ciag(n-1) + (n-1)


for i in range(1,11):
    print(f'a({i})= {ciag(i)}')