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
    # TODO
    pass


class Fraction:
    def __init__(self, num, den):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass

    def __add__(self, other):
        # TODO
        pass

    def __sub__(self, other):
        # TODO
        pass

    def __mul__(self, other):
        # TODO
        pass

    def __truediv__(self, other):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __lt__(self, other):
        # TODO
        pass

    def to_float(self):
        # TODO
        pass


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
