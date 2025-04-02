from collections import defaultdict

n, m = map(int, input().split())
L = []
for i in range(n):
    L.append(list(input()))
    for j in range(m):
        L[i][j] = int(L[i][j] == "L")

path = defaultdict(list)
for i in range(n):
    for j in range(m):
        if not L[i][j]:
            continue
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dy, dx = move
            y, x = i+dy, j+dx
            if not (0<=y<n and 0<=x<m):
                continue
            if L[y][x]:
                path[(i, j)].append((y, x))

def furthest_point(pt, path, visited):
    visited[pt] = True
    maxLen = 0
    for nxtPt in path[pt]:
        if nxtPt in visited:
            continue
        maxLen = max(maxLen, furthest_point(nxtPt, path, visited)+1)
    return maxLen

res = 0
for i in range(n):
    for j in range(m):
        if not L[i][j]:
            continue
        visited = defaultdict(bool)
        res = max(res, furthest_point((i, j), path, visited))

print(res+1)