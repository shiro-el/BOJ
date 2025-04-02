import math

def sieve(a, b):
    t = list(range(3, b+1, 2))
    sqrtn = int(math.sqrt(b))
    i = 0
    while t[i] <= sqrtn:
        p = t[i]
        for j in range(len(t)-1, i, -1):
            if t[j] % p == 0:
                t.pop(j)
        i += 1
    
    while t[i] < a:
        i += 1
    
    return len(t[i:]) + 2, t

A, B = map(int, input().split())
n = 2
count = 0
while math.floor(B**(1/n)) > 2:
    a, b = math.ceil(A**(1/n)), math.floor(B**(1/n))
    x = sieve(a, b)
    print(n, a, b, x)
    count += x[0]
    n += 1

print(count)