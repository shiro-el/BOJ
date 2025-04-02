n = int(input())
P = list(map(int, input().split()))

count = 0

for i in range(len(P)):
    if P[i] % 2 == 1:
        P[i] = (P[i]+1)//2
    else:
        P[i] = P[i]//2-1

grundy = P[0]
for i in range(1,len(P)):
    grundy ^= P[i]

if grundy == 0:
    print('cubelover')
else:
    print('koosaga')