"""
Exercise 6 (CHALLENGE) - The Collatz Conjecture
-----------------------------------------------
Start with any positive integer n. Repeat:
  - if n is even, n = n // 2
  - if n is odd,  n = 3 * n + 1
until n becomes 1.

Mathematicians believe EVERY starting number eventually reaches 1, but
nobody has ever proven it! It's one of the most famous unsolved problems.

1. collatz_steps(n): return how many steps it takes n to reach 1.
      collatz_steps(1) -> 0
      collatz_steps(6) -> 8   (6, 3, 10, 5, 16, 8, 4, 2, 1)
2. longest_under(limit): return the starting number below limit that
   takes the MOST steps.
      longest_under(10) -> 9   (9 takes 19 steps)
"""


def collatz_steps(n):
    pass


def longest_under(limit):
    pass


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
