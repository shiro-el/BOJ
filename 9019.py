from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    
    L = [[None, None] for __ in range(10000)]
    L[a] = [0, '']
    
    queue = deque([a])
    
    while L[b][0] == None:
        x = queue.popleft()
        
        d = x*2%10000
        s = (x-1)%10000
        l = x*10%10000+x//1000
        r = x//10+x%10*1000
        
        if L[d][0] == None:
            L[d][0] = x
            L[d][1] = 'D'
            queue.append(d)
        if L[s][0] == None:
            L[s][0] = x
            L[s][1] = 'S'
            queue.append(s)
        if L[l][0] == None:
            L[l][0] = x
            L[l][1] = 'L'
            queue.append(l)
        if L[r][0] == None:
            L[r][0] = x
            L[r][1] = 'R'
            queue.append(r)
    
    pointer = b
    ans = ''
    while pointer != a:
        ans = L[pointer][1] + ans
        pointer = L[pointer][0]
    
    print(ans)