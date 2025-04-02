from sys import stdin
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

L = [i for i in range(n, 0, -1)]

if A[-1] < 0:
    print(-1)
else:
    i = 0
    while i < n:
        if A[i] < 0:
            start = i
            while A[i] < 0 and i < n:
                i += 1
            temp = L[start:i+1]
            temp.reverse()
            for j in range(start, i+1):
                L[j] = temp[j-start]
        i += 1
    print(*L)