A, B = map(int, input().split())

count = 1
a = True
while B >= A:
    if B % 2 == 0:
        B //= 2
        count += 1
    elif B % 10 == 1:
        B //= 10
        count += 1
    else:
        print(-1)
        a = False
        break
    if A == B:
        print(count)
        a = False
        break
if a:
    print(-1)