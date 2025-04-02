from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
L = [[False]*(m+1) for _ in range(n+1)]
for i in range(n):
    temp = stdin.readline()
    for j in range(m):
        if temp[j] == '1':
            L[i][j] = True

Visited = [[0]*m for _ in range(n)]
Visited[0][0] = 1
queue = deque()
queue.append((0,0))
move = [(1,0), (0,1), (-1,0), (0,-1)]

while queue:
    pt = queue.popleft()
    for d in move:
        x, y = pt[0]+d[0], pt[1]+d[1]
        if L[x][y]:
            if not Visited[x][y]:
                Visited[x][y] = Visited[pt[0]][pt[1]] + 1
                queue.append((x, y))

print(Visited[n-1][m-1])