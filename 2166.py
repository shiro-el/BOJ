from sys import stdin
n = int(input())
L = []
for i in range(n):
    L.append(list(map(int, stdin.readline().split())))
area = 0
for i in range(n):
    area += L[i][0] * L[i-1][1]
    area -= L[i][1] * L[i-1][0]
area = abs(area)
area *= 5
round(area)
area /= 10
print(area)