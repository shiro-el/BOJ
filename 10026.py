from sys import stdin
from collections import deque

def bfs(L):
    queue = deque()
    point = [[True]*n for i in range(n)]
    count = n**2
    area = 0
    
    while count != 0:
        if not queue:
            check = False
            for i in range(n):
                for j in range(n):
                    if point[i][j]:
                        point[i][j] = False
                        queue.append((i, j))
                        area += 1
                        count -= 1
                        
                        check = True
                        break
                if check:
                    break
        else:
            x, y = queue.pop()
            color = L[x][y]
            
            for dxy in move:
                mx = x + dxy[0]
                my = y + dxy[1]
                if 0 <= mx < n and 0 <= my < n and point[mx][my] and L[mx][my] == color:
                    point[mx][my] = False
                    queue.append((mx, my))
                    count -= 1

    return area

n = int(stdin.readline())
picture = []
for i in range(n):
    picture.append(list(stdin.readline()[:n]))

move = [[1,0], [-1, 0], [0, 1], [0, -1]]

print(bfs(picture))

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

print(bfs(picture))