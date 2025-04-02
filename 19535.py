import sys
from math import factorial

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    temp = sys.stdin.readline().split()
    a, b = int(temp[0]), int(temp[1])
    tree[a].append(b)
    tree[b].append(a)

def comb(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n-r))

def line(node):
    global tree
    ans = 0
    for i in tree[node]:
        ans += len(tree[i])-1
    ans *= len(tree[node])-1
    return ans

d, g = 0 , 0
for i in range(1, n+1):
    g += comb(len(tree[i]), 3)
    d += line(i)
d //= 2

if d>g*3:
    print('D')
elif d<g*3:
    print('G')
else:
    print('DUDUDUNGA')