L = []
k, n = map(int, input().split())
max_len = 0
longest_num = 0

for i in range(k):
    L.append(input())
    if max_len < len(L[-1]):
        max_len = len(L[-1])
        longest_num = L[-1]
    if max_len == len(L[-1]):
        longest_num = max(longest_num, L[-1])

for i in range(k):
    L[i] += "X"*(max_len-len(L[i]))

L.sort(reverse=True)

res = ""
for i in range(k):
    if L[i] == longest_num:
        res += longest_num * (n-k)
    res += L[i]

ans = ""
for s in res:
    if s != "X":
        ans += s

print(ans)