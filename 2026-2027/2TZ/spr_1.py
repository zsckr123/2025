def e(n):
    if n==1:
        return 2
    return 2*e(n-1)


print(e(10))