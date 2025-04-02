import math
from sys import stdin

def combination(n, r):
    if n < 2*r:
        r = n-r
    
    numerator = 1
    denominator = 1
    
    for i in range(r):
        numerator *= n-i
        denominator *= i+1
    
    return numerator//denominator

n, k = map(int, stdin.readline().split())
L = [n, (n)*(n+1)//2, n*(n+1)*(2*n+1)//6]

for i in range(3, k+1):
    next = pow(n+1, i+1, 1000000007) - 1
    
    for p in range(0, i):
        next -= combination(i+1, p)*L[p]%1000000007
    
    next *= pow(i+1, 1000000005, 1000000007)
    next %= 1000000007

    L.append(next)

print(L[k]%1000000007)