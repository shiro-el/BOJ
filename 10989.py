import sys

n = int(input())
L=[0]*10000
for i in range(n):
    L[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    for j in range(L[i]):
        print(i + 1)