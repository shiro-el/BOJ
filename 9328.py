from sys import stdin
from collections import deque

def bfs(L, keys):
    h = len(L)-1
    w = len(L[0])-1
    CanGo = [[True]*(w+1) for _ in range(h+1)]
    ans = 0
    queue = deque()
    door = deque()
    
    for i in range(w):
        if L[-2][i] == '.':
            queue.append((h-1, i))
        elif 97 <= ord(L[-2][i]) <= 122:
            keys[ord(L[-2][i])-97] = True 
            queue.append((h-1, i))
        elif 65 <= ord(L[-2][i]) <= 90:
            door.append((h-1, i, ord(L[-2][i])-65))
        elif L[-2][i] == '$':
            ans += 1
            queue.append((h-1, i))
        
        if L[0][i] == '.':
            queue.append((0, i))
        elif 97 <= ord(L[0][i]) <= 122:
            keys[ord(L[0][i])-97] = True
            queue.append((0, i))
        elif 65 <= ord(L[0][i]) <= 90:
            door.append((0, i, ord(L[0][i])-65))
        elif L[0][i] == '$':
            ans += 1
            queue.append((0, i))
        
    for i in range(1, h-1):
        if L[i][0] == '.':
            queue.append((i, 0))
        elif 97 <= ord(L[i][0]) <= 122:
            keys[ord(L[i][0])-97] = True
            queue.append((i, 0))
        elif 65 <= ord(L[i][0]) <= 90:
            door.append((i, 0, ord(L[i][0])-65))
        elif L[i][0] == '$':
            ans += 1
            queue.append((i, 0))
        
        if L[i][-2] == '.':
            queue.append((i, w-1))
        elif 97 <= ord(L[i][-2]) <= 122:
            keys[ord(L[i][-2])-97] = True 
            queue.append((i, w-1))
        elif 65 <= ord(L[i][-2]) <= 90:
            door.append((i, w-1, ord(L[i][-2])-65))
        elif L[i][-2] == '$':
            ans += 1
            queue.append((i, w-1))
    
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    for pt in queue:
        CanGo[pt[0]][pt[1]] = False
    
    while queue or door:
        if queue:
            pt = queue.popleft()
            x = pt[0]
            y = pt[1]
            
            for d in move:
                dx = x + d[0]
                dy = y + d[1]
                if CanGo[dx][dy]:
                    uniCode = ord(L[dx][dy])
                    if uniCode == 46:
                        CanGo[dx][dy] = False
                        queue.append((dx, dy))
                    elif 65 <= uniCode <= 90:
                        CanGo[dx][dy] = False
                        door.append((dx, dy, uniCode-65))
                    elif 97 <= uniCode <= 122:
                        keys[uniCode-97] = True
                        CanGo[dx][dy] = False
                        queue.append((dx, dy))
                    elif uniCode == 36:
                        ans += 1
                        CanGo[dx][dy] = False
                        queue.append((dx, dy))
        else:
            check = True
            for _ in range(len(door)):
                pt = door.popleft()
                if keys[pt[2]]:
                    queue.append((pt[0], pt[1]))
                    check = False
                else:
                    door.append(pt)
            if check:
                break

    return ans

t = int(stdin.readline())
temp = []
for _ in range(t):
    h, w = map(int, stdin.readline().split())
    L = []
    for i in range(h):
        L.append(list(stdin.readline()))
        L[i][-1] = '*'
    L.append(['*']*(w+1))
    key = list(stdin.readline())
    keys = [False]*1000
    for k in key:
        keys[ord(k)-97] = True
    
    temp.append(bfs(L, keys))
print(*temp, sep='\n')