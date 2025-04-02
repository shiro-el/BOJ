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
t = int(input())
for temp in range(t):
    n = int(input())
    L = [[6, -4],[1, 0]]

    power = list(str(bin(n-1)))[2:]
    power = power[::-1]

    for i in range(len(power)):
        power[i] = int(power[i])
    powL = [L]

    for i in range(1, len(power)):
        powL.append(mulMat(powL[len(powL)-1], powL[len(powL)-1]))

    M = [[0]*2 for _ in range(2)]
    for i in range(2):
        M[i][i] = 1
    for i in range(len(power)):
        if power[i] == 1:
            M = mulMat(M, powL[i])

    c = 28*M[1][0]+6*M[1][1]
    c -= 1
    c %= 1000

    if c == 0:
        x = '000'
    elif c < 10:
        x = '00' + str(c)
    elif c < 100:
        x = '0' + str(c)
    else:
        x = str(c)
    print('Case #{}: {}'.format(temp+1, x))