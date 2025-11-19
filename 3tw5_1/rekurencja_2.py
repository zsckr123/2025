'''
d(1)=-10
d(n+1)=d(n)+9
'''

def ciag(n):
    if n == 1:
        return -10
    return ciag(n-1) +9

for i in range(1,20):
    print(f'a({i})= {ciag(i)}')