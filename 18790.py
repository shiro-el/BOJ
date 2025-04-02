def findMul(checkNum, leftNum, remainder):
    if leftNum == 0:
        if remainder != 0:
            return False
        return True
    if checkNum == 0 and leftNum != 0:
        return False
    
    if findMul(checkNum - 1, leftNum - 1, (remainder - Numbers[i])%n):
        Num.append(Numbers[i])
        checkNum += 1
        leftNum -= 1
        remainder = remainder - Numbers[i]%n
        return findMul(checkNum - 1, leftNum - 1, (remainder - Numbers[i])%n)
    else:
        checkNum += 1
        return findMul(checkNum, leftNum, remainder)


n = int(input())
Numbers = list(map(int, input().split()))
Num = []

for i in range(len(Numbers)):
    Numbers[i] %= n

print(findMul(2*n - 1, n, 0))