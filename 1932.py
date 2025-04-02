n = int(input())
L = []
sumL = []
for i in range(n):
    L.append(list(map(int, input().split())))
    sumL.append([0]*(i+1))

sumL[0][0] = L[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            sumL[i][0] = sumL[i-1][0] + L[i][j]
        elif j == i:
            sumL[i][i] = sumL[i-1][i-1] + L[i][j]
        else:
            sumL[i][j] = max(sumL[i-1][j-1], sumL[i-1][j]) + L[i][j]

print(max(sumL[n-1]))