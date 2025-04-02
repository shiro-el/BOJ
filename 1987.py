from sys import stdin

n, m = map(int, stdin.readline().split())
L = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    temp = stdin.readline()
    for j in range(m):
        L[i][j] = ord(temp[j]) - 64

CanGo = [True] * 27
move = [(1,0), (0,1), (-1,0), (0,-1)]
maxMove = 0

def backTracking(x, y):
    for i in move:
        