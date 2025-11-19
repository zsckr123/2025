
def ciag(n):
    if n == 1:
        return 2
    return 2 * ciag(n-1) - 1


for i in range(1,11):
    print(f'a({i})= {ciag(i)}')