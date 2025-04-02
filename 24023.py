from sys import stdin
n, k = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

now = 0
start = 1
end = 1
check = False
for i in range(n):
    now = now|A[i]
    if now == k:
        check = True
        break
    if k != k|now:
        now = 0
        start = i+2
        end = i+1
    end += 1

if check:
    print(start, end)
else:
    print(-1)