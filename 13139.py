from collections import deque
import math

def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while y != 0:
        x, y = y, x%y
    return x

def isPrime(n):
    t = int(n**0.5)+1
    for i in range(2, t):
        if n%i == 0:
            return False
    return True

def bfs(x, y, p1, q1, p2, q2):
    queue = deque()
    queue.append((x, y, 0))
    
    CanGo = [[True]*(p2-p1) for _ in range(q2-q1)]
    for i in range(q2 - q1):
        CanGo[i].append(False)
    CanGo.append([False]*(p2-p1+1))
    CanGo[x-p1][y-q1] = False
    
    while queue:
        pt = queue.popleft()
        print(pt)
        
        if pt[0] == p1 and pt[1] == q1:
            return pt[2]
        
        else:
            move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in move:
                xd = pt[0] + d[0]
                yd = pt[1] + d[1]
                
                if gcd(xd, yd) < 2 and CanGo[yd-q1][xd-p1]:
                    CanGo[yd-q1][xd-p1] = False
                    queue.append((xd, yd, pt[2] + 1))
    return -1

def findSquare(x, y):
    p1, p2 = x, x
    while not isPrime(p1) and p1 > 1:
        p1 -= 1
    while not isPrime(p2) and p2 < 100000000:
        p2 += 1
    
    q1, q2 = y, y
    while (not isPrime(q1)) and p1 > 1 and math.ceil(p1/q1) != math.floor(p2/q1):
        q1 -= 1
    while not isPrime(q2) and p2 < 100000000 and math.ceil(p1/q2) != math.floor(p2/q2):
        q2 += 1
    
    return p1, q1, p2, q2

x, y = map(int, input().split())
p1, q1, p2, q2 = findSquare(x, y)
print(bfs(x, y, p1, q1, p2, q2) + p1 + q1)