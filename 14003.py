from bisect import bisect_left
from sys import  stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
d = [0] * (n+1)
L = [-1000000001]
leg = 0

for i in range(n):
    if L[-1] < arr[i]:
        L.append(arr[i])
        d[i] = len(L) - 1
        leg = d[i]
    else:
        d[i] = bisect_left(L, arr[i])
        L[d[i]] = arr[i]
print(leg)

temp = []
for i in range(n, -1, -1):
    if d[i] == leg:
        temp.append(arr[i])
        leg -= 1
temp.reverse()
print(*temp)