from sys import stdin

def findArea(Map):




n, m = map(int, stdin.readline().split())
L = []
for i in range(n):
    L.append(list(map(int, stdin.readline().split())))

Cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= L[i][j] <= 5:
            Cctv.append((i,j))
