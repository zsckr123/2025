def ciag(n):
    if n >1:
        return (n-1) * ciag(n-1) -1
    return 3

for i in range(1,5):
    print(ciag(i))