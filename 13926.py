def factorization(x):
    num = x
    d = 2
    L = []
    while x != 1 and d <= num**0.5:
        if x % d == 0:
            L.append(d)
            x /= d
        else:
            d = d + 1
    if x != 1:
        L.append(x)
    return L

n = int(input())

factor = factorization(n)
for i in range(factor):
    for j in range(i):
        pass