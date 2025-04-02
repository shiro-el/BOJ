import copy
def mulMat(L, M):
    n = len(L)
    X = copy.deepcopy(L)
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(n):
                count += L[i][k] * M[k][j]
            X[i][j] = count%1000
    return X

n, b= map(int, input().split())
L = [[]*n for _ in range(n)]
for i in range(n):
    L[i] = list(map(int, input().split()))

power = list(str(bin(b)))[2:]
power = power[::-1]

for i in range(len(power)):
    power[i] = int(power[i])
powL = [L]

for i in range(1, len(power)):
    powL.append(mulMat(powL[len(powL)-1], powL[len(powL)-1]))
    
M = [[0]*n for _ in range(n)]
for i in range(n):
    M[i][i] = 1
for i in range(len(power)):
    if power[i] == 1:
        M = mulMat(M, powL[i])

for i in M:
    for j in i:
        print(j, end=' ')
    print()