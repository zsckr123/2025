'''  a(1)=1, a(n+1) = a(n) +n'''
# def ciag(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return ciag(n - 1) + (n - 1)

def ciag(n):
    if n > 1:
       return ciag(n - 1) + (n - 1)
    return 1

for i in range(1,6):
    print(ciag(i))