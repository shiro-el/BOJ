n, m = map(int, input().split())
Know = list(map(int, input().split()))[1:]
Party = []

for i in range(m):
    Party.append(list(map(int, input().split()))[1:])
    Party[i] = set(Party[i])
Conect = [set([]) for _ in range(n)]
for i in Party:
    for j in list(i):
        Conect[j] |= i

for i in range(m):
    Conect[i] = list(Conect[i])

for i in range(n):
    for j in Conect:
        for k in i:
            if k == True:
                for a in i:
                    Know[a] = True
                break
count = 0
for i in Know:
    if not i:
        count += 1
print(count)