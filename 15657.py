import sys
sys.setrecursionlimit(10 ** 6)

def seq(left, Stack):
    if left == 0:
        for st in Stack:
            print(st, end = ' ')
        print()
        return
    
    if Stack != []:
        for i in range(N.index(max(Stack)), n):
            seq(left-1, Stack+[N[i]])
    else:
        for i in range(0, n):
            seq(left-1, Stack+[N[i]])

n, m = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
N.sort()

seq(m, [])