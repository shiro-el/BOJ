n = int(input())
L = input().split()
for i in range(n):
    L[i]=int(L[i])

#######################################################################

X = []
Y = []
price = 0
for i in range(n-2):
    X += [min(L[i], L[i+1], L[i+2])]
while max(X) > 0:
    argmax = X.index(max(X))
    X[argmax] -= 1
    L[argmax] -= 1
    L[argmax + 1] -= 1
    L[argmax + 2] -= 1
    price+=7

for i in range(n-1):
    Y += [min(L[i], L[i+1])]
while max(Y) > 0 :
    argmax = Y.index(max(Y))
    Y[argmax] -= 1
    L[argmax] -= 1
    L[argmax + 1] -= 1
    price+=5
price+=sum(L)*3
print(price)