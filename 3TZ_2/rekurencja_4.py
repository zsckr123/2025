'''
c(1)=3
c(n+1) = c(n) - n^2 +3
c(2) = c(1) - 1^2 +3 = 3 -1 +3 =5
'''

def ciag(n):
    if n == 1:
        return 3
    return ciag(n-1) - (n-1) ** 2 + 3


for i in range(1,20):
    print(f' c({i})={ciag(i)}')
