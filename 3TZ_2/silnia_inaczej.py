def silnia(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return silnia(n-1) * n
print(silnia(10))