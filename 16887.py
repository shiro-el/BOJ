import sys
import math

n = int(input())
input = sys.stdin.readline()
A = list(map(int, input.split()))

grundy = 0

for i in A:
    if i <= 3:
        grundy ^= 0
    if 4 <= i <= 15:
        grundy ^= 1
    if 16 <= i <= 81:
        grundy ^= 2
    if 82 <= i <= 6723:
        grundy ^= 0
    if 6724 <= i <= 50625:
        grundy ^= 3
    if 50626 <= i <= 2562991875:
        grundy ^= 1
    if 2562991876 <= i :
        grundy ^= 2
            

if grundy == 0:
    print('cubelover')
else:
    print('koosaga')