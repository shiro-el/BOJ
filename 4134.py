def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def res(n):
    while not isPrime(n):
        n+=1
    return n

n = int(input())
for _ in range(n):
    print(res(int(input())))