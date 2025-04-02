import sys
sys.setrecursionlimit(10 ** 9)

def leg(point):
    for i in Connect[point]:
        if Parents[i] == 0:
            Parents[i] = point + 1
            leg(i)

n = int(sys.stdin.readline())
Line = []
for i in range(n-1):
    Line.append(list(map(int, sys.stdin.readline().split())))

Connect = [[] for _ in range(n)]
for i in Line:
    Connect[i[0]-1].append(i[1]-1)
    Connect[i[1]-1].append(i[0]-1)

Parents = [0]*n
Parents[0] = True
leg(0)

print(*Parents[1:], sep='\n')