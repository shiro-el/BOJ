#첫번째 코드입니다. (시간초과)
from collections import deque

def bfs():
    A = deque()
    A.append((n, [n]))
    point = -1
    while point != k:
        point, path = A.popleft()
        if point >= 0 and point <= 100000 and L[point]:
            L[point] = False
            if point == k:
                return path
            else:
                A.append((point*2, path + [point*2]))
                A.append((point+1, path + [point+1]))
                A.append((point-1, path + [point-1]))

n, k = map(int, input().split())
L = [True]*100001
path = bfs()
print(len(path)-1)
print(*path)

################################################################################
################################################################################
################################################################################

#두번째 코드입니다. (정답)
from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    arr.reverse()
    print(*arr)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()