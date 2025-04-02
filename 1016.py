import math

def isPrimeNumbers(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]


def primeComplex(n):
    sqrt_n = math.sqrt(n)
    if sqrt_n % 1 != 0:
        sqrt_n += 1
    sqrt_n = int(sqrt_n)
    
    L = isPrimeNumbers(sqrt_n)

    for i in range(len(L)):
        L[i] **= 2
    
    return L
    
    
min_x, max_x = map(int, input().split())

numbers = [True]*(max_x - min_x + 1)
primeComplexNumbers = primeComplex(max_x)

for number in primeComplexNumbers:
    i = min_x // number
    while number * i - min_x< len(numbers):
        if number * i - min_x >= 0:
            numbers[number * i - min_x] = False
        i += 1

count = 0
for TF in numbers:
    if TF:
        count += 1

print(count)