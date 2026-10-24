"""Solution - Exercise 7 (Challenge): Square Roots by Hand (Newton's / Babylonian method)"""


def sqrt(x, show_steps=False):
    if x < 0:
        return None
    if x == 0:
        return 0

    guess = x
    steps = 0
    while abs(guess * guess - x) > 0.000001:
        guess = (guess + x / guess) / 2
        steps += 1
        if show_steps:
            print(f"  step {steps}: {guess}")
    return guess


print("sqrt(2), step by step:")
sqrt(2, show_steps=True)
print()


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
