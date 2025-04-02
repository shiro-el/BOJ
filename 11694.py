n = int(input())
P = list(map(int, input().split()))
if P == [1]*n:
    if n%2 == 1:
        print('cubelover')
    else:
        print('koosaga')
else:
    grundy = P[0]
    for i in range(1,n):
        grundy ^= P[i]

    if grundy == 0:
        print('cubelover')
    else:
        print('koosaga')