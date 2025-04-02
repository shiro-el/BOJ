n = int(input())
A = list(input().split())

k = True
for i in range(n):
    if A[0][0] != A[i][0] and k:
        print(0)
        k = False
if k:
    print(1)