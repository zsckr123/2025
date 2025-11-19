def ciag(n):
    if n >1:
        return ciag(n-1) +3
    return 1

for i in range(1,5):
    print(ciag(i))