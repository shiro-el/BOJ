def factorization(x):
    A = []
    
    for i in range(1, x+1):
        if x % i == 0:
            A.append(i)
    
    return A

n= int(input())

Factor = factorization(n)
for i in range(len(Factor)):
    Factor.append(2*Factor[i])
Factor = list(set(Factor))
Factor.sort()

ans = 0
if n % 2 == 0:
    for i in Factor:
        if i % 2 == 0:
            if n%i != 0 and n//i > i/2 - 1:
                ans += 1
        else:
            if n/i >= i/2:
                ans += 1

else:
    for i in Factor:
        if i % 2 == 0:
            if n//i > i/2 - 1:
                ans += 1
        else:
            if n/i >= i//2:
                ans += 1

print(ans)