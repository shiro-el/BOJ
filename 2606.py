from sys import stdin
from collections import deque

n = int(input())
m = int(input())
Graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    Graph[a].append(b)
    Graph[b].append(a)

def bfs():
    CanGo = [True]*(n+1)
    queue = deque([1])
    ans = []
    while queue:
        node = queue.popleft()
        if CanGo[node]:
            CanGo[node] = False
            ans.append(node)
            for next in Graph[node]:
                if CanGo[next]:
                    queue.append(next)
    return ans

print(len(bfs())-1)