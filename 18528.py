import sys
from collections import deque

deq = deque()
n = int(input())
for i in range(n):
    df = sys.stdin.readline().split()
    if df[0] == 'push':
        deq.append(df[1])
    elif df[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif df[0] == 'size':
        print(len(deq))
    elif df[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif df[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif df[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)