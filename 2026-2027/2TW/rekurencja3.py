def a(n):
    if n==1:
        return 3
    return (n-1+5) * a(n-1)

for i in range(1,11):
    print(a(i))