import math

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True: 
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

maxi = max(max(A), max(B))

primeList = prime_list(int(math.sqrt(maxi)) + 1)
La = [0]*len(primeList)
Lb = [0]*len(primeList)

for i in range(len(primeList)):
    for j in range(len(A)):
        while A[j] % primeList[i] == 0:
            La[i] += 1
            A[j] //= primeList[i]
    for j in range(len(B)):
        while B[j] % primeList[i] == 0:
            Lb[i] += 1
            B[j] //= primeList[i]
            

L = [0]*len(primeList)
for i in range(len(primeList)):
    L[i] = min(La[i], Lb[i])

a = 1
b = 1
for i in A:
    a *= i
for i in B:
    b *= i

gcd = math.gcd(a, b)

for i in range(len(primeList)):
    if L[i] != 0:
        gcd *= primeList[i] ** L[i]
if gcd >= 1000000000:
    print(str(gcd)[len(str(gcd))-9:])
else:
    print(gcd)