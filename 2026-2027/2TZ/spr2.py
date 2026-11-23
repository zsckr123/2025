def e(n):
    if n==1:
        return 0
    return -3*e(n-1)+3


print(e(10))