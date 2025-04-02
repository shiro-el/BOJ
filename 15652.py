import sys
sys.setrecursionlimit(10 ** 6)

def seq(left, Stack):
    if left == 0:
        for st in Stack:
            print(st, end = ' ')
        print()
        return
    
    if Stack != []:
        for i in range(max(Stack), n+1):
            seq(left-1, Stack+[i])
    else:
        for i in range(1, n+1):
            seq(left-1, Stack+[i])

n, m = map(int, sys.stdin.readline().split())

seq(m, [])