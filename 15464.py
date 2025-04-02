import sys
sys.setrecursionlimit(10 ** 6)

def seq(left, Stack):
    if left == 0:
        for st in Stack:
            print(st, end = ' ')
        print()
        return
    
    for i in range(0, n):
        yseq(left-1, Stack+[N[i]])

n, m = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
N.sort()

seq(m, [])