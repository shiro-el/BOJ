n = int(input())
P = list(map(int, input().split()))

def grundy(n, P):
    grundy = P[0]
    for i in range(1,n):
        grundy ^= P[i]

    if grundy == 0:
        return 1
    return 0

if grundy(n, P) == 1:
    print(0)
else:
    count = 0
    for i in range(len(P)):
        for j in range(1, P[i]+1):
            E = P[:]
            E[i] -= j
            count += grundy(n, E)
    print(count)