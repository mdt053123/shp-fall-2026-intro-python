"""
Exercise 4 (CHALLENGE) - A Fraction Class  (SOLUTION)
-----------------------------------------
Build a Fraction class that does exact math (no floating-point rounding!).

  Fraction(6, 8)                 -> stored in lowest terms: 3/4
  Fraction(1, -2)                -> the sign goes on top: -1/2
  str(Fraction(3, 4))            -> "3/4"; whole numbers print plainly: str(Fraction(4, 2)) -> "2"
  Fraction(1, 2) + Fraction(1, 3)   -> 5/6     (define __add__)
  Fraction(1, 2) - Fraction(1, 3)   -> 1/6     (define __sub__)
  Fraction(2, 3) * Fraction(3, 4)   -> 1/2     (define __mul__)
  Fraction(1, 2) / Fraction(1, 4)   -> 2       (define __truediv__)
  Fraction(1, 2) == Fraction(2, 4)  -> True    (define __eq__)
  Fraction(1, 3) < Fraction(1, 2)   -> True    (define __lt__)
  Fraction(3, 4).to_float()         -> 0.75

Step 1: write gcd(a, b) (greatest common divisor) using a loop.
        Euclid's algorithm (about 2,300 years old!):
            while b != 0:
                a, b = b, a % b
            return a
Step 2: in __init__, divide the numerator and denominator by their gcd.

Fun fact: Python has this built in (from fractions import Fraction), but
building it yourself is the best way to understand operator overloading.
"""


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("denominator can't be zero")
        if den < 0:
            num, den = -num, -den
        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def to_float(self):
        return self.num / self.den


# ----------------------- Checks (don't change below) -----------------------
def check(label, get_actual, expected):
    try:
        actual = get_actual()
    except Exception as e:
        print(f"FAIL  {label}: crashed with {type(e).__name__}: {e}")
        return
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


def telescoping_sum():
    total = Fraction(0, 1)
    for n in range(1, 11):
        total = total + Fraction(1, n * (n + 1))
    return str(total)


check("gcd(12, 18)", lambda: gcd(12, 18), 6)
check("lowest terms", lambda: str(Fraction(6, 8)), "3/4")
check("negative denominator", lambda: str(Fraction(1, -2)), "-1/2")
check("whole number", lambda: str(Fraction(4, 2)), "2")
check("add", lambda: str(Fraction(1, 2) + Fraction(1, 3)), "5/6")
check("sub", lambda: str(Fraction(1, 2) - Fraction(1, 3)), "1/6")
check("mul", lambda: str(Fraction(2, 3) * Fraction(3, 4)), "1/2")
check("div", lambda: str(Fraction(1, 2) / Fraction(1, 4)), "2")
check("eq", lambda: Fraction(1, 2) == Fraction(2, 4), True)
check("lt", lambda: Fraction(1, 3) < Fraction(1, 2), True)
check("to_float", lambda: Fraction(3, 4).to_float(), 0.75)
check("1/(1*2) + 1/(2*3) + ... + 1/(10*11)", telescoping_sum, "10/11")
