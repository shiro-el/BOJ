def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def numPrime(a, b):
    if a>b:
        return 0
    res = 0
    for n in range(a, b+1):
        if isPrime(n):
            res += 1
    return res

a, b = map(int, input().split())
c, d = map(int, input().split())

p1, both, p2 = numPrime(a, b), numPrime(c, b), numPrime(c, d)

if both%2 == 0:
    if p1 > p2:
        print("yt")
    else:
        print("yj")
else:
    if p2 > p1:
        print("yj")
    else:
        print("yt")