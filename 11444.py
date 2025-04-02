def mulMat(L, M):
    n = len(L)
    X = [[None]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(n):
                count += L[i][k] * M[k][j]
            X[i][j] = count%1000000007
    
    return X


n = int(input())
L = [[1, 1],[1, 0]]
if n == 1:
    print(1)
else:
    power = list(str(bin(n-2)))[2:]
    power = power[::-1]

    for i in range(len(power)):
        power[i] = int(power[i])
    powL = [L]
    v 
    for i in range(1, len(power)):
        powL.append(mulMat(powL[len(powL)-1], powL[len(powL)-1]))

    M = [[0]*2 for _ in range(2)]
    for i in range(2):
        M[i][i] = 1
    for i in range(len(power)):
        if power[i] == 1:
            M = mulMat(M, powL[i])

    c = M[0][0] + M[0][1]
    c %= 1000000007

    print(c)