from itertools import combinations

n, m = map(int, input().split())
L = []
for i in range(1, n+1):
    L.append(i)

A = list(combinations(L, m))

for i in A:
    for j in range(m):
        print(i[j], end=' ')
    print()