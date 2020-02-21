# from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        reduce = gcd(numer, denom)
        self.numer = numer // reduce
        self.denom = denom // reduce

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(((self.numer * other.denom) + (other.numer * self.denom)), (self.denom * other.denom))

    def __sub__(self, other):
        return Rational(((self.numer * other.denom) - (other.numer * self.denom)), (self.denom * other.denom))

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        elif power < 0:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))
        else:
            return Rational(1, 1)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1.0 / self.denom)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
