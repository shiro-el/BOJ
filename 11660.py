import sys
import copy

n, m = map(int, sys.stdin.readline().split())

Table = []
for i in range(n):
    Table.append(list(map(int, sys.stdin.readline().split())))

Points = []
for i in range(m):
    Points.append(list(map(int, sys.stdin.readline().split())))

SumTable = copy.deepcopy(Table)
for i in range(n):
    for j in range(1, n):
        SumTable[i][j] += SumTable[i][j-1]
for i in range(1, n):
    for j in range(n):
        SumTable[i][j] += SumTable[i-1][j]

for i in range(n):
    SumTable[i].append(0)
SumTable.append([0]*(n+1))

#print(*SumTable, sep='\n')
for i in range(m):
    x1, x2 = Points[i][0]-1, Points[i][2]-1
    y1, y2 = Points[i][1]-1, Points[i][3]-1
    #print(x1, y1, x2, y2)
    sumPoint =  SumTable[x2][y2] -\
                SumTable[x2][y1-1] -\
                SumTable[x1-1][y2] +\
                SumTable[x1-1][y1-1]
    #print(SumTable[y2][x2], SumTable[y1-1][x2], SumTable[y2][x1-1], SumTable[y1-1][x1-1])
    print(sumPoint)