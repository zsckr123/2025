def a(n):
    if n==1:
        return 1
    return a(n-1)**2 -3

for i in range(1,11):
    print(a(i))