from collections import defaultdict

def isPrime(n):
    for k in range(int(n**0.5)+1, 0, -1):
        if n%k == 0:
            return k
    return n

def prime_factorization(n):
    prime = defaultdict(int)
    k = isPrime(n)
    prime[k] += 1
    n //= k
    k = 2
    while n != 1:
        if n%k == 0:
            prime[k] += 1
            n //= k
            k = 1
        k += 1
    return prime

def euler_phi(n):
    if n == 1:
        return 1
    prime = prime_factorization(n)
    phi = 1
    for i in prime.keys():
        phi *= i**prime[i] - i**(prime[i]-1)
    return phi

def main(n):
    for x in range(1, n+1):
        if n%x == 0 and x*euler_phi(x) == n:
            return x
    return -1

print(main(int(input())))