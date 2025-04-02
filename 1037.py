from collections import defaultdict

n = int(input())
L = list(map(int, input().split()))
L.sort()
print(L[0]*L[-1])