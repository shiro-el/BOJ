T = int(input())

for _ in range(T):
    N = int(input())
    Point = []
    
    for __ in range(N):
        Point.append(list(map(int, input().split())))
    
    mini = float("Inf")
    
    Line = []
    while len(Line)*2 != len(Point):
        for i in range(N-1):
            for j in range(i+1, N):
                pass