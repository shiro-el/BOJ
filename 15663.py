import sys
sys.setrecursionlimit(10 ** 6)

def seq(left, Stack):
    if left == 0:
        temp = []
        for i in Stack:
            temp.append(int(i))
        L.append(temp)
        return
    
    for i in range(0, n):
        if Stack.count(N[i]) < N.count(N[i]):
            seq(left-1, Stack+[N[i]])

n, m = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
N.sort()

L = []
seq(m, [])

L = sorted(L)


for j in L[0]:
        print(j, end=' ')
print()
for i in range(1, len(L)):
    if L[i] != L[i-1]:
        for j in L[i]:
            print(j, end=' ')
        print()