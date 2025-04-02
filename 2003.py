import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    A[i] += A[i-1]
A.append(0)

ans = 0

start, end = -1, 0

while end <= n-1:
    tmp = A[end] - A[start]
    if tmp == m:
        ans += 1
    elif tmp < m:
        end += 1
        continue
    start += 1
print(ans)