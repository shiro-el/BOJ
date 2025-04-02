from bisect import bisect_left
from sys import  stdin

n = int(stdin.readline())
temp = []
for i in range(n):
    temp.append(list(map(int, stdin.readline().split())))
temp.sort(key=lambda x:x[0])
arr = []
rev_arr = {}
for i in temp:
    arr.append(i[1])
    rev_arr[i[1]] = i[0]

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
print(n-leg)

temp = [True]*n
for i in range(n, -1, -1):
    if d[i] == leg:
        try:
            temp[i] = False
            leg -= 1
        except: pass

for i in range(n):
    if temp[i]:
        print(rev_arr[arr[i]])