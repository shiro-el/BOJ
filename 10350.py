import sys
import math
n = int(input())
input = sys.stdin.readline()
K = list(map(int, input.split()))

PartSumK = [0]*n
for i in range(n):
    PartSumK[i] = sum(K[:i])

angel = 0
sumK = sum(K)
for i in range(n):
    for j in range(i, n):
        sumPart = PartSumK[j] - PartSumK[i]
        if sumPart < 0:
            angel += math.ceil(abs(sumPart)/sumK)
        elif sumPart > sumK:
            angel += math.ceil(abs(sumK - sumPart)/sumK)

print(angel)