import math
from sys import stdin
from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = None
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def angle(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        self.theta = math.atan2(dy, dx)

def leftSide(p1, p2, p3): #p1->p2, p3
    return (p2.x-p1.x)*(p3.y-p1.y)-(p3.x-p1.x)*(p2.y-p1.y) > 0

def grahamScan(points):
    n = len(points)
    
    minIdx = 0
    for i in range(1,n):
        if points[i].y < points[minIdx].y or (points[i].y == points[minIdx].y and points[i].x < points[minIdx].x):
            minIdx = i
    minPt = points[minIdx]
    
    L = points[:minIdx] + points[minIdx+1:]
    
    for i in range(n-1):
        L[i].angle(minPt)
    
    L.sort(key = lambda x:x.theta)
    print(*L)
    Stack = deque([minPt, L[0]])
    for i in range(1, n-1):
        top = Stack.pop()
        second = Stack.pop()
        
        left = False
        if leftSide(second, top, L[i]):
            left = True
        Stack.append(second)
        if left:
            Stack.append(top)
        Stack.append(L[i])
        
    return Stack


n = int(stdin.readline())

Pt = []
for i in range(n):
    x, y = map(int, stdin.readline().split())
    Pt.append(Point(x, y))

print(*grahamScan(Pt))