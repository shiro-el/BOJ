import math
from sys import stdin

def f(x):
    return x - (a*x + b*math.sin(x) - c)/(a + b*math.cos(x))

a, b, c = map(int, stdin.readline().split())

L = [c/a]
L.append(f(0))
while abs(L[-1]-L[-2]) >= 1e-10:
    L.append(f(L[-1]))

x = L[-1]
x //= 1e-07
if x % 10 >= 5:
    x //= 10
    x += 1
    x /= 1e+06
    print(x)
else:
    x //= 10
    x /= 1e+06
    print(x)