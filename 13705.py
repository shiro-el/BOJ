from decimal import *
from sys import stdin
D = Decimal
getcontext().rounding=ROUND_HALF_UP
getcontext().prec = 50

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762')
error = D('0.000000000000000000001')

def sin(x):
    x = x%(2*pi)
    i, bef, ans, fact, pow, sign = D(1), D(0), D(x), D(1), D(x), D(1)
    while ans != bef:
        bef = ans
        i += 2
        fact *= i * (i-1)
        pow *= x * x
        sign *= -1
        ans += pow / fact * sign
    return D(ans)
   
def cos(x):
    x = x%(2*pi)
    i, bef, ans, fact, pow, sign = D(0), D(0), D(1), D(1), D(1), D(1)
    while ans != bef:
        bef = ans
        i += 2
        fact *= i * (i-1)
        pow *= x * x
        sign *= -1
        ans += pow / fact * sign
    return D(ans)


def f(x):
    return x - (a*x + b*sin(x) - c)/(a + b*cos(x))

a, b, c = stdin.readline().split()
a, b, c = D(a), D(b), D(c)

L = [c/a]
L.append(f(0))
while abs(L[-1]-L[-2]) >= error:
    L.append(f(L[-1]))
x = L[-1]
x *= D('1000000')
x = round(x)
x *= D('0.000001')

print(x)