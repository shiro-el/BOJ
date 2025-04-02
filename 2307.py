import sys
import heapq
import math

input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.edge = {}

n, m = map(int, input().split())

Graph = [Node(i) for i in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    Graph[a-1].edge[b-1] = t
    Graph[b-1].edge[a-1] = t

def dijkstra(Graph:list[Node], n:int, a, b):
    d = [math.inf]*n
    visited = [False]*n
    d[0] = 0
    visited[0] = True
    
    curr = 0
    q = []
    pre = [-1]*n
    
    while True:
        for nxt in Graph[curr].edge.keys():
            if visited[nxt] or curr == a and nxt == b or curr == b and nxt == b:
                continue
            cmp = d[curr]+Graph[curr].edge[nxt]
            if  d[nxt] >= cmp:
                d[nxt] = cmp
                pre[nxt] = curr
                heapq.heappush(q, (cmp, nxt))
        visited[curr] = True
        if visited[n-1]:
            break
        if not q:
            return math.inf, []
        curr = heapq.heappop(q)[1]

    bef = n-1
    path = []
    while bef != -1:
        path.append(bef)
        bef = pre[bef]
    path.reverse()
    
    return d[n-1], path

defaultTime, defaultPath = dijkstra(Graph, n, -1, -1)
maxDelay = 0

for i in range(len(defaultPath)-1):
    experimentTime, experimentPath = dijkstra(Graph, n, defaultPath[i], defaultPath[i+1])
    if experimentTime == math.inf:
        maxDelay = -1
        break
    maxDelay = max(maxDelay, experimentTime-defaultTime)
print(maxDelay)