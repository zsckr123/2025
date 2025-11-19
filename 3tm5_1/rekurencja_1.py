def ciag(n):
    if n > 1 :
        return ciag(n-1) + 5
    return 2
n = int(input('Podaj n'))
print(ciag(n))