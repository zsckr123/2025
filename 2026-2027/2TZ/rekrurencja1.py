def a(n):
    if n==1:
        return 2
    return a(n-1)+1
print(a(200))