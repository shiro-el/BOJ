s = input()
cur = None
ans = 1
for a in s:
    if a == "c": ans *= 25 if cur == a else 26
    else: ans *= 9 if cur == a else 10
    cur = a
print(ans)