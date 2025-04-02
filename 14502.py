from sys import stdin
from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(lab):
    queue = deque()
    point = [[False]*m for i in range(n)]
    safe = 0
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                point[i][j] = True
                safe += 1
            elif lab[i][j] == 2:
                queue.append((i, j))
    #print(queue)
    while queue:
        x, y = queue.pop()
        
        for dxy in move:
            mx = x + dxy[0]
            my = y + dxy[1]
            if 0 <= mx < n and 0 <= my < m and point[mx][my]:
                point[mx][my] = False
                queue.append((mx, my))
                safe -= 1
    return safe

n, m = map(int, stdin.readline().split())

Lab = []
for i in range(n):
    Lab.append(list(map(int, stdin.readline().split())))

move = [[1,0], [-1, 0], [0, 1], [0, -1]]

safearea = 0
L = deepcopy(Lab)
blank = []

for i in range(n):
    for j in range(m):
        if Lab[i][j] == 0:
            blank.append((i, j))

kind = combinations(blank, 3)

for pts in kind:
    for pt in pts:
        L[pt[0]][pt[1]] = 1
    safearea = max(safearea, bfs(L))
    for pt in pts:
        L[pt[0]][pt[1]] = 0
#print(*L, sep='\n')
print(safearea)