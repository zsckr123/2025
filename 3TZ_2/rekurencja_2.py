'''
b1=7
b(n+1)=b(n)-3
'''

def ciag(n):
    if n == 1:
        return 7
    return ciag(n-1) - 3

for i in range(1,9):
    print(ciag(i))