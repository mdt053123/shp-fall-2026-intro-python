"""
Exercise 7 (CHALLENGE) - Computing Square Roots by Hand
-------------------------------------------------------
How does a calculator find sqrt(2)? One ancient method (used by the
Babylonians around 4,000 years ago) is:

    1. Start with a guess, e.g. guess = x
    2. Improve it: guess = (guess + x / guess) / 2
    3. Repeat until guess * guess is VERY close to x
       (e.g. abs(guess * guess - x) < 0.000001)

Write sqrt(x) using this method. DON'T use x ** 0.5 or math.sqrt!
  - If x is negative, return None.
  - If x is 0, return 0.

Bonus: print the guess at every step for sqrt(2). How many steps does it take?
"""


def sqrt(x):
    pass


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    ok = (actual is None and expected is None) or (
        actual is not None and expected is not None and abs(actual - expected) < 1e-5)
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + ("" if ok else f": expected {expected!r}, got {actual!r}"))


check("sqrt(4)", sqrt(4), 2.0)
check("sqrt(2)", sqrt(2), 1.41421356)
check("sqrt(1000000)", sqrt(1000000), 1000.0)
check("sqrt(0)", sqrt(0), 0)
check("sqrt(-9)", sqrt(-9), None)
