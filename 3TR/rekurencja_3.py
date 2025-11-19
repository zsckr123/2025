'''
c(n+1)=c(n) - n^2 + 3
'''

def ciag(n):
    if n == 1:
        return 3
    return ciag(n-1) - (n-1) ** 2 +3

for i in range(1,11):
    print(f'a({i})= {ciag(i)}')