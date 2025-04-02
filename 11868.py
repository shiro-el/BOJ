n = int(input())
P = list(map(int, input().split()))

grundy = P[0]
for i in range(1,n):
    grundy ^= P[i]

if grundy == 0:
    print('cubelover')
else:
    print('koosaga')