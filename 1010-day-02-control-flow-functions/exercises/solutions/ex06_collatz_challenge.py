"""Solution - Exercise 6 (Challenge): The Collatz Conjecture"""


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def longest_under(limit):
    best_start = 1
    best_steps = 0
    for start in range(1, limit):
        steps = collatz_steps(start)
        if steps > best_steps:
            best_steps = steps
            best_start = start
    return best_start


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("collatz_steps(1)", collatz_steps(1), 0)
check("collatz_steps(6)", collatz_steps(6), 8)
check("collatz_steps(27)", collatz_steps(27), 111)
check("longest_under(10)", longest_under(10), 9)
check("longest_under(1000)", longest_under(1000), 871)
