import sys

n = int(sys.stdin.readline())
MassLim = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
Mass = list(map(int, sys.stdin.readline().split()))

MassLim = sorted(MassLim)[::-1]
Mass = sorted(Mass)[::-1]
box = len(Mass)
time = 0
while box != 0:
    for i in MassLim:
        if Mass != []:
            if i >= min(Mass):
                for j in range(len(Mass)):
                    if i >= Mass[j]:
                        Mass.pop(j)
                        box -= 1
                        break
        else:
            break
    time += 1
print(time)