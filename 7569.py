import sys

class Queue():
    def __init__(self):
        self.q = []
        self.start = 0
        self.end = 0
    
    def __str__(self):
        return str(self.q[self.start:self.end])
    
    def push(self, temp):
        if len(self.q) == self.end:
            self.q.append(temp)
            self.end += 1
        else:
            self.q[self.end] = temp
            self.end += 1
    
    def pop(self):
        self.start += 1
        #print( self.q[self.start-1])
        return self.q[self.start-1]

def bfs(L):
    A = Queue()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if L[i][j][k] == 1:
                    A.push((i, j, k, 0))
                    L[i][j][k] = -1

    while A.start != A.end:
        x, y, z, time = A.pop()
        for dx in (-1, 1):
            tx = x+dx
            if L[tx][y][z] == 0:
                A.push((tx, y, z, time+1))
                L[tx][y] [z]= -1
        for dy in (-1, 1):
            ty = y+dy
            if L[x][ty][z] == 0:
                A.push((x, ty, z, time+1))
                L[x][ty][z] = -1
        for dz in (-1, 1):
            tz = z+dz
            if L[x][y][tz] == 0:
                A.push((x, y, tz, time+1))
                L[x][y][tz] = -1
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if L[i][j][k] == 0:
                    return -1
    return time

m, n, h = map(int,input().split())
L = [[[0]*m for _ in range(n)] for __ in range(h)]

for i in range(h):
    for j in range(n):
        L[i][j] = list(map(int, sys.stdin.readline().split()))
        L[i][j].append(-1)
    L[i].append([-1]*(m+1))
L.append([[-1]*(m+1) for _ in range(n+1)])

print(bfs(L))