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
    for i in range(n):
        for j in range(m):
            if L[i][j] == 1:
                A.push((i, j, 0))
                L[i][j] = -1

    while A.start != A.end:
        x, y, time = A.pop()
        for dx in (-1, 1):
            tx = x+dx
            if L[tx][y] == 0:
                A.push((tx, y, time+1))
                L[tx][y] = -1
        for dy in (-1, 1):
            ty = y+dy
            if L[x][ty] == 0:
                A.push((x, ty, time+1))
                L[x][ty] = -1
    
    for i in range(n):
        for j in range(m):
            if L[i][j] == 0:
                return -1
    return time

m, n = map(int,input().split())
L = [[0]*m for _ in range(n)]

for i in range(n):
    L[i] = list(map(int, input().split()))
    L[i].append(-1)
L.append([-1]*(m+1))

print(bfs(L))