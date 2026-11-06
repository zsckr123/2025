def c(n):
    if n==1:
        return 3
    return c(n-1)-(n-1)**2+3

for i in range(1,11):
    print(f'c({i})={c(i)}')