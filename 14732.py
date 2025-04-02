from sys import stdin

n = int(stdin.readline())
ans = 0

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    ans += a*b*pow(2, b-1, 1000000007)

print(ans%1000000007)