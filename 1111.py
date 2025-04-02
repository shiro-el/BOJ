N = int(input())
L = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if L[0] == L[1]:
        print(L[0])
    else:
        print("A")
elif L[0] == L[1]:
    a = 1
    b = 0
else:
    b = L[1] % L[0]
    a = L[1] // L[0]
    x = L[2] - (L[1] * a + b)
    
    check  = True
    while not L[2] == L[1] * a + b:
        a -= 1
        b += L[0]
        if x * (L[2] - (L[1] * a + b)) < 0:
            print("B")
            check = False
            break
    #길이 3 넘어가면 다 되는지 검증도 해야함
    
    if check:
        print(L[len(L) - 1]*a + b)