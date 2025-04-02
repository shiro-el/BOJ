from sys import stdin
n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

def moveDist(x):
    ans = 0
    for i in range(n):
        ans += abs(L[i] - x*i)
    return ans

lo, hi = 0, L[n-1]
while hi - lo > 3:
    p = (lo*2 + hi)//3
    q = (lo + hi*2)//3
    if moveDist(p) <= moveDist(q):
        hi = q
    else:
        lo = p

temp = []
for i in range(lo, hi+1):
    temp.append(moveDist(i))

print(min(temp))