def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while y != 0:
        x, y = y, x%y
    return x

class Rational:
    def __init__(self, num, den):
        n = gcd(num, den)
        self.n = num//n
        self.d = den//n
    
    def sum(self, p):
        num = self.n*p.d + self.d*p.n
        den = self.d*p.d
        
        return Rational(num, den)

