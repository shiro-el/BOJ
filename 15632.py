X = [None]*3
Y = [None]*3
R = [None]*3
for i in range(3):
    X[i], Y[i], R[i] = map(int,input().split())

minX = min(X[0]-R[0], X[1]-R[1], X[2]-R[2])
minY = min(Y[0]-R[0], Y[1]-R[1], Y[2]-R[2])
for i in range(3):
    X[i] -= minX
    Y[i] -= minY
maxX = max(X[0]+R[0], X[1]+R[1], X[2]+R[2])
maxY = max(Y[0]+R[0], Y[1]+R[1], Y[2]+R[2])

dot = 0
xBeet = maxX / 5000
yBeet = maxY / 5000
for i in range(5000):
    for j in range(5000):
        legX = i * xBeet
        legY = j * yBeet
        for k in range(3):
            if ((X[k]-legX)**2 + (Y[k]-legY)**2) <= R[k]**2:
                dot += 1
                break

print(dot/25000000*maxX*maxY)