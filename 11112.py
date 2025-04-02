import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
ans = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(board):
    count = 0
    for i in range(9):
        if ans[i] != board[i]:
            count += 1
    if count == 0: return 0
    return count - 1
    
for _ in range(n):
    input()
    board = [0]*9
    for i in range(3):
        line = input()
        for j in range(3):
            if line[j] == "#":
                continue
            board[3*i+j] = int(line[j])
    
    board = tuple(board)
    memo = {}
    pq = [(h(board), board)]
    
    while pq:
        g, node = heapq.heappop(pq)
        
        if node == ans:
            break
        
        nullIdx = node.index(0)
        nxtNodes = []
        if not nullIdx < 3:
            nxtnode = list(node)
            nxtnode[nullIdx], nxtnode[nullIdx-3] = nxtnode[nullIdx-3], nxtnode[nullIdx]
            nxtnode = tuple(nxtnode)
            nxtNodes.append(nxtnode)
        if not nullIdx > 5:
            nxtnode = list(node)
            nxtnode[nullIdx], nxtnode[nullIdx+3] = nxtnode[nullIdx+3], nxtnode[nullIdx]
            nxtnode = tuple(nxtnode)
            nxtNodes.append(nxtnode)
        if not nullIdx%3 == 0:
            nxtnode = list(node)
            nxtnode[nullIdx], nxtnode[nullIdx-1] = nxtnode[nullIdx-1], nxtnode[nullIdx]
            nxtnode = tuple(nxtnode)
            nxtNodes.append(nxtnode)
        if not nullIdx%3 == 2:
            nxtnode = list(node)
            nxtnode[nullIdx], nxtnode[nullIdx+1] = nxtnode[nullIdx+1], nxtnode[nullIdx]
            nxtnode = tuple(nxtnode)
            nxtNodes.append(nxtnode)
        
        for nxtNode in nxtNodes:
            heapq.heappush(pq, (g+1+h(nxtNode), nxtNode))
    
    print(g+1)