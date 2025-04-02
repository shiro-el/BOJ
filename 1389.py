import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    
def circumCenter(p1, p2, p3):
    x_n = -1 *((p2.x**2 - p1.x**2 + p2.y**2 - p1.y**2)*(p3.y - p2.y) - (p2.x**2 - p3.x**2 + p2.y**2 - p3.y**2)*(p1.y - p2.y))
    x_d = 2*((p1.x - p2.x) * (p3.y - p2.y) - (p3.x - p2.x) * (p1.y - p2.y))
    y_n = -1 *((p2.y**2 - p1.y**2 + p2.x**2 - p1.x**2)*(p3.x - p2.x) - (p2.y**2 - p3.y**2 + p2.x**2 - p3.x**2)*(p1.x - p2.x))
    y_d = 2*((p1.y - p2.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p1.x - p2.x))
    
    if x_d == 0 or y_d == 0:
        return False
    return Point(x_n/x_d, y_n/y_d)

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return (dx**2+dy**2)**0.5

n = int(sys.stdin.readline())
Pt = []
for i in range(n):
    x, y = map(float, sys.stdin.readline().replace("−", "-").split())
    Pt.append(Point(x, y))

radius = 0
cc_x, cc_y = 0, 0
d = [0, 0, 0]
if n == 1:
    cc_x, cc_y = Pt[0].x, Pt[0].y

elif n == 2:
    cc_x, cc_y = (Pt[0].x + Pt[1].x)/2, (Pt[0].y + Pt[1].y)/2
    radius = distance(Pt[0], Pt[1])/2
else:
    for i in range(2, n):
        for j in range(1, i):
            for k in range(j):
                d[0], d[1], d[2] = distance(Pt[i], Pt[j]), distance(Pt[j], Pt[k]), distance(Pt[k], Pt[i])
                temp = 0
                
                for i in range(3):
                    temp += d[i] **2
                if 2* max(d) ** 2 < temp:
                    cc = circumCenter(Pt[i], Pt[j], Pt[k])
                    #print(i, j, k, cc, r)
                    if cc != False:
                        r = distance(cc, Pt[i])
                        if r > radius:
                            cc_x, cc_y = cc.x, cc.y
                            radius = r
                else:
                    r = max(d)/2
                    if r > radius:
                        ind = d.index(max(d))
                        if ind == 0:
                            a, b = i, j
                        elif ind == 1:
                            a, b = j, k
                        else:
                            a, b = k, i
                        cc_x, cc_y = (Pt[a].x + Pt[b].x)/2, (Pt[a].y + Pt[b].y)/2
                        radius = r

print(cc_x, cc_y, radius)