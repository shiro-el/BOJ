t = int(input())
for _ in range(t):
    n = int(input())
    L = [1, 2, 4]
    for i in range(2, n-1):
        L.append(L[i] + L[i-1] + L[i-2])
    print(L[n-1])