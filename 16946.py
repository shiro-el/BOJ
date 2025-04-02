from sys import stdin
from collections import deque
from copy import deepcopy

def bfs(a, b, L):
    queue = deque()
    queue.append((a,b))
    ans = 1
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        x0, y0 = queue.popleft()
        for d in move:
            x = x0 + d[0]
            y = y0 + d[1]
            if A[x][y] == 0:
                ans += 1
                A[x][y] = 1
                queue.append((x,y))
    return ans
        

n, m = map(int, stdin.readline().split())
L = []
for i in range(n):
    L.append(list(stdin.readline()))
    L[-1].append(1)
L.append([1]*m)

for i in range(n):
    for j in range(m):
        L[i][j] = int(L[i][j])

A = deepcopy(L)

for i in range(n):
    for j in range(m):
        if A[i][j] == 0:
            print(0, end = "")
        else:
            print(bfs(i,j,A), end = "")
    print()