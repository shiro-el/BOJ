a, b, c = map(int, input().split())
if b == 1:
    print(a%c)
else:
    L = list(bin(b))[2:]
    L.reverse()
    for i in range(len(L)):
        L[i] = int(L[i])
    A = [a%c]
    for i in range(len(L)-1):
        A.append(A[i]**2 % c)
    x = 1
    for i in range(len(A)):
        if L[i] == 1:
            x *= A[i]
            x %= c
    print(x)