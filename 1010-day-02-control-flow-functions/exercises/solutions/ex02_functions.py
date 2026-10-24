"""Solution - Exercise 2: Function Practice"""


def max_of_three(a, b, c):
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


def ticket_price(age, is_student):
    if age < 5:
        return 0
    elif age >= 65:
        return 8
    elif is_student:
        return 10
    else:
        return 15


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def count_digits(n):
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return max(digits, 1)     # 0 still has 1 digit


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:          # only need to check up to sqrt(n)
        if n % d == 0:
            return False
        d += 1
    return True


def count_primes(limit):
    count = 0
    for n in range(2, limit + 1):
        if is_prime(n):
            count += 1
    return count


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
