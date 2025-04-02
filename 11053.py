import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

LongestIncSeq = [1]*n

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and LongestIncSeq[i] < LongestIncSeq[j] + 1:
            LongestIncSeq[i] = LongestIncSeq[j] + 1
    #LongestIncSeq[i] += 1

print(max(LongestIncSeq))