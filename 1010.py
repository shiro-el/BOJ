T = int(input())
for _ in range(T):
    N, M =map(int, input().split())
    #(M-N)C(M)
    numerator = 1
    denominator = 1
    for i in range(N):
        numerator *= M-i
    for i in range(N):
        denominator *= i+1
    print(numerator//denominator)