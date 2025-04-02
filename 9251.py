def lcs(a, b):
    if a == len(A) or b == len(B):
        return 0
    
    temp = False
    for i in range(a, len(A)):
        if A[i] == B[b]:
            temp = True
            break
    x = lcs(a, b+1)
    if temp:
        return max(lcs(a+i, b+1)+1, x)
    return x


A = list(input())
B = list(input())
print(lcs(0, 0))