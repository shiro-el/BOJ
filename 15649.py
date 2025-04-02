def backtracking(k):
    global maxi
    if k == 0:
        print(*Visited)
        return
    for i in range(n):
        #if L[i] >= maxi:
            Visited.append(L[i])
            x = maxi
            maxi = L[i]
            backtracking(k-1)
            maxi = x
            Visited.pop()
    

n, m = map(int, input().split())
L = sorted(list(map(int, input().split())))

maxi = 0
Visited = []
backtracking(m)