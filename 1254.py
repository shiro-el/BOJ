from sys import stdin
L = list(stdin.readline())
L.pop()
L.reverse()
inPal = len(L)
outPal = 0

while inPal > 0:
    temp = True
    for i in range(inPal//2):
        if L[i] != L[inPal-1-i]:
            temp = False
            break
    if temp:
        break
    inPal -= 1
    outPal += 1
print(inPal + outPal*2)