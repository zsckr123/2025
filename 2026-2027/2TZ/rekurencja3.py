def b(n):
    if n==1:
        return 7
    return b(n-1)-3

for i in range(1,11):
    print(f'b({i})={b(i)}')