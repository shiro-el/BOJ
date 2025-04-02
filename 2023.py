def isPrime(p):
    if p <= 1:
        return False
    for i in range(2, p//2+1):
        if p%i == 0: 
            return False
    return True

N = int(input())
L = [[] for _ in range(N)]

for i in range(N):
    if i == 0:
        L[0] = [2, 3, 5, 7]
    else:
        for j in L[i-1]:
            for k in range(10):
                number = j*10 + k
                if isPrime(j*10 + k):
                    L[i].append(number)

for i in L[N-1]:
    print(i)