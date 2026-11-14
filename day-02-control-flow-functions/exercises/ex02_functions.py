"""
Exercise 2 - Function Practice
------------------------------
Fill in each function so it does what its docstring says. Replace `pass`
with your code. Then run this file: the checks at the bottom print PASS
or FAIL for each one.

Don't change the checks!
"""


def max_of_three(a, b, c):
    """Return the largest of a, b, c. Don't use the built-in max()!

    max_of_three(1, 5, 3) -> 5
    """
    pass


def ticket_price(age, is_student):
    """Return the price of a museum ticket:
      - under 5: free (0)
      - 65 or older: 8
      - students (any other age): 10
      - everyone else: 15

    ticket_price(30, False) -> 15
    ticket_price(17, True)  -> 10
    """
    pass


def is_leap_year(year):
    """Return True if year is a leap year.
    Rule: divisible by 4, except years divisible by 100 unless also divisible by 400.

    is_leap_year(2024) -> True,  is_leap_year(1900) -> False,  is_leap_year(2000) -> True
    """
    pass


def sum_to_n(n):
    """Return 1 + 2 + ... + n using a loop.

    sum_to_n(4) -> 10
    """
    pass


def count_digits(n):
    """Return how many digits the positive integer n has, using a while loop
    (not str() or len()!). Hint: keep doing n = n // 10.

    count_digits(7) -> 1,  count_digits(2026) -> 4
    """
    pass


def factorial(n):
    """Return n! = 1 * 2 * ... * n  (and 0! = 1), using a loop.

    factorial(5) -> 120
    """
    pass


def is_prime(n):
    """Return True if n is prime (only divisible by 1 and itself).
    Numbers less than 2 are NOT prime.

    is_prime(7) -> True,  is_prime(9) -> False,  is_prime(1) -> False
    """
    pass


def count_primes(limit):
    """Return how many primes there are from 2 up to and including limit.
    Use your is_prime function!

    count_primes(10) -> 4   (2, 3, 5, 7)
    """
    pass


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("max_of_three(1, 5, 3)", max_of_three(1, 5, 3), 5)
check("max_of_three(9, 2, 9)", max_of_three(9, 2, 9), 9)
check("max_of_three(-1, -5, -3)", max_of_three(-1, -5, -3), -1)
check("ticket_price(3, False)", ticket_price(3, False), 0)
check("ticket_price(70, True)", ticket_price(70, True), 8)
check("ticket_price(17, True)", ticket_price(17, True), 10)
check("ticket_price(30, False)", ticket_price(30, False), 15)
check("is_leap_year(2024)", is_leap_year(2024), True)
check("is_leap_year(2026)", is_leap_year(2026), False)
check("is_leap_year(1900)", is_leap_year(1900), False)
check("is_leap_year(2000)", is_leap_year(2000), True)
check("sum_to_n(4)", sum_to_n(4), 10)
check("sum_to_n(100)", sum_to_n(100), 5050)
check("count_digits(7)", count_digits(7), 1)
check("count_digits(2026)", count_digits(2026), 4)
check("factorial(0)", factorial(0), 1)
check("factorial(5)", factorial(5), 120)
check("is_prime(1)", is_prime(1), False)
check("is_prime(2)", is_prime(2), True)
check("is_prime(9)", is_prime(9), False)
check("is_prime(97)", is_prime(97), True)
check("count_primes(10)", count_primes(10), 4)
check("count_primes(100)", count_primes(100), 25)
