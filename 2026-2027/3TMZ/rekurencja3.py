def a(n):
    if n==1:
        return 3
    return a(n-1) + 5 * (n-1)

for i in range(1,11):
    print(f"a({i})={a(i)}") 