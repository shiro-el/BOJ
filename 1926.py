from collections import deque
from sys import stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        print("({},{})".format(self.x, self.y))

def bfs(start):
    queue = deque()
    queue.append(start)
    area = 1
    while queue:
        pt = queue.pop()
        for i in udrl:
            y = pt.y + i.y
            x = pt.x + i.x
            if Paper[y][x] == 1:
                area += 1
                Paper[y][x] = 0
                queue.append(Point(x, y))
    return area

n, m = map(int, stdin.readline().split())
Paper = []
for i in range(n):
    Paper.append(list(map(int, stdin.readline().split())))
    Paper[i].append(0)
Paper.append([0]*(m+1))

maxArea = 0
picture = 0

udrl = [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1)]

for i in range(n):
    for j in range(m):
        if Paper[i][j]:
            Paper[i][j] = 0
            picture += 1
            maxArea = max(maxArea, bfs(Point(j, i)))

print(picture)
print(maxArea)