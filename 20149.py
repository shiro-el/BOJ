from sys import stdin

def check(ax, ay, bx, by, cx, cy, dx, dy):
    temp1 = ((bx - ax) * (cy - ay) - (by - ay)* (cx - ax)) * ((bx - ax) * (dy - ay) - (by - ay)* (dx - ax))
    temp2 = ((dx - cx) * (ay - cy) - (dy - cy)* (ax - cx)) * ((dx - cx) * (by - cy) - (dy - cy)* (bx - cx))
    assert temp1 != 0 and temp2 != 0
    if temp1 < 0 and temp2 < 0:
        return True
    return False

def crosspoint(ax, ay, bx, by, cx, cy, dx, dy):
    return ((ax * by - ay * bx) * (cx - dx) - (ax - bx) * (cx* dy - cy * dx)) / ((ax - bx) * (cy - dy)- (ay- by) * (cx - dx)),\
        ((ax * by - ay * bx) * (cy - dy) - (ay - by) * (cx * dy - cy * dx)) / ((ax - bx) * (cy - dy) - (ay - by) * (cx - dx))

x1, y1, x2, y2 = map(int, stdin.readline().split())
x3, y3, x4, y4 = map(int, stdin.readline().split())

if x1 > x2:
    x1, y1, x2, y2 = x2, y2, x1, y1
if x3 > x4:
    x3, y3, x4, y4 = x4, y4, x3, y3

if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
    print(1)
    if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4):
        print(x1, y1)
    else:
        print(x2, y2)
else:
    if x1 - x2 == 0 or x3 - x4 == 0:
        if x1 - x2 == 0 and x3 - x4 == 0:
            if x1 == x3:
                ya, yb = min(y1, y2), max(y1, y2)
                yc, yd = min(y3, y4), max(y3, y4)
                if ya < yb == yc < yd or yc < yd == ya < yb:
                    print(1, 'a')
                    print(x1, yb)
                elif ya < yb < yc < yd or yc < yd < ya < yb:
                    print(0, 'b')
                else:
                    print(1, 'c')
            else:
                print(0, 'd')
        else:
            if check(x1, y1, x2, y2, x3, y3, x4, y4):
                print(1, 'e')
                print(crosspoint(x1, y1, x2, y2, x3, y3, x4, y4))
            else:
                print(0, 'f')
    else:
        if (y1 - y2)/(x1 - x2) == (y3 - y4)/(x3 - x4):
            if x1 == x3:
                ya, yb = min(y1, y2), max(y1, y2)
                yc, yd = min(y3, y4), max(y3, y4)
                if ya < yb == yc < yd or yc < yd == ya < yb:
                    print(1, 'g')
                    print(x1, yb)
                elif ya < yb < yc < yd or yc < yd < ya < yb:
                    print(0, 'h')
                else:
                    print(1, 'i')
            else:
                print(0, 'j')
        else:
            if check(x1, y1, x2, y2, x3, y3, x4, y4):
                print(1, 'k')
                print(crosspoint(x1, y1, x2, y2, x3, y3, x4, y4))
            else:
                print(0, 'l')