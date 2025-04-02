def unfold(W, H, f, c, x1, y1, x2, y2):
    L = [[1]*W for _ in range(H)]
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            L[x][y] = 0

    for j in range(c):
        if j % 2 == 0:
            for x in range(x1, x2):
                for y in range(y1 + H//c*j, y2 + H//c*j):
                    L[x][y] = 0
        else:
            for x in range(x1, x2):
                for y in range(H//c*(j+1) - y1, H//c*(j+1) - y2):
                    L[x][y] = 0
    
    pass

W,H,K=map(int,input().split())

F = [0]*K
C = [0]*K
X1 = [0]*K
Y1 = [0]*K
X2 = [0]*K
Y2 = [0]*K

for i in range(K):
    F[i], C[i], X1[i], Y1[i], X2[i], Y2[i] = map(int, input().split())

paper = [[1]*W for _ in range(H)]

n = len(f)

for i in range(n):
    f = F[i]
    c = C[i]
    x1 = X1[i]
    y1 = Y1[i]
    x2 = X2[i]
    y2 = Y2[i]
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[x][y] = 0
    
    for j in range(c):
        if j % 2 == 0:
            for x in range(x1, x2):
                for y in range(y1 + H//c*j, y2 + H//c*j):
                    paper[x][y] = 0
        else:
            for x in range(x1, x2):
                for y in range(H//c*(j+1) - y1, H//c*(j+1) - y2):
                    paper[x][y] = 0
    
    

'''
f=min(f,W-f)
x=x2-x1
y=y2-y1
x+=min(max(f-x1,0),x2-x1)
'''