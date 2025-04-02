def factorization(x):
    d = 2
    L = []
    while d <= x:
        if x % d == 0:
            if L == []:
                L.append([d,1])
            elif L[len(L)-1][0] == d:
                L[len(L)-1][1] += 1
            else:
                L.append([d, 1])
            x = x / d
        else:
            d = d + 1
    return L
    
for _ in range(5):
    n, k = map(int, input().split())
    factor  = factorization(k)
    if n == 0 or n == 1:
        print(1)
    gcd = 1
    
    for i in factor:
        if n >= i[0]:
            x = n
            count = 0
            while x != 0:
                count += x//i[0]
                x //= i[0]
            gcd *= i[0]**min(count, i[1])

    print(gcd)