def a(n):
    if n==1:
        return 2
    return a(n-1)**2-5


for i in range(1,11):
    print(a(i))