n = int(input())
if n == 4 or n == 7:
    print(-1)
else:
    k = n%5
    if k == 0:
        print(n//5)
    elif k == 1 or k == 3:
        print(n//5+1)
    else:
        print(n//5+2)