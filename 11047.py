n, k = map(int, input().split())

A = [0]*n
for i in range(n):
    A[i] = int(input())
A.sort(reverse=True)

pointer = 0
ans = 0

while k > 0:
    if A[pointer] <= k:
        ans += 1
        k -= A[pointer]
    else:
        pointer += 1

print(ans)