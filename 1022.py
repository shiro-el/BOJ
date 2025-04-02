r1, c1, r2, c2 = map(int, input().split())
L = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
for i in range(c1, c2+1):
    for j in range(r1, r2+1):
        n = max(abs(i), abs(j))*2 + 1
        