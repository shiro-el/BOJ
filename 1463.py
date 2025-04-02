from sys import setrecursionlimit

setrecursionlimit(10**6)

def find(x, time):
    if x%3 == 0 and x//3 > 0 and time+1 < L[x//3]:
        L[x//3] = time+1
        find(x//3, time+1)
    if x%2 == 0 and x//2 > 0 and time+1 < L[x//2]:
        L[x//2] = time+1
        find(x//2, time+1)
    if x-1 > 0 and time+1<L[x-1]:
        L[x-1] = time+1
        find(x-1, time+1)

n = int(input())
L = [n]*(n+1)
L[n] = 0
find(n, 0)
print(L[1])