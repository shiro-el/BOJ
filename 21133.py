from sys import setrecursionlimit
setrecursionlimit(10**9)

def backtracking(n, k):
    if k == n:
        return 1
    count = 0
    for i in range(n):
        if (not CantUseRow[i]) and (not CantUseMainDiagonal[n-1-k + i]) and (not CantUseSkewDiagonal[k + i]):
            CantUseRow[i] += 1
            CantUseMainDiagonal[n-1-k + i] += 1
            CantUseSkewDiagonal[k + i] += 1
            
            count += backtracking(n, k+1)
            
            CantUseRow[i] -= 1
            CantUseMainDiagonal[n-1-k + i] -= 1
            CantUseSkewDiagonal[k + i] -= 1
    
    return count

n = int(input())
CantUseRow = [0]*n
CantUseMainDiagonal = [0]*(2*n + 1)
CantUseSkewDiagonal = [0]*(2*n + 1)

print(backtracking(n, 0))