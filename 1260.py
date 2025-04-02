from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
Graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    Graph[a].append(b)
    Graph[b].append(a)

for i in range(1, n+1):
    Graph[i].sort()

def bfs():
    CanGo = [True]*(n+1)
    queue = deque([v])
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

def dfs():
    CanGo = [True]*(n+1)
    stack = deque([v])
    ans = []
    while stack:
        node = stack.pop()
        if CanGo[node]:
            CanGo[node] = False
            ans.append(node)
            for i in range(len(Graph[node])-1, -1, -1):
                next = Graph[node][i]
                if CanGo[next]:
                    stack.append(next)
    return ans

print(*dfs())
print(*bfs())