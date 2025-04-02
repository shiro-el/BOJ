import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
x = int(input())

A.sort()
start, end = 0, n - 1
ans = 0

while start < end:
    tmp = A[start] + A[end]
    if tmp == x: ans += 1
    if tmp < x:
        start += 1
        continue
    end  -= 1
print(ans)