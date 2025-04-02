from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            #path(x)
            return x

        if 0<=x*2<=200000 and dist[x*2]==None:
            q.appendleft(x*2)
            dist[x*2] = dist[x]
        
        for i in (x+1, x-1):
            if 0<=i<=200000 and dist[i]==None:
                q.append(i)
                dist[i] = dist[x] + 1

N, K = map(int, input().split())
dist = [None]*200001
dist[N] = 0
bfs()