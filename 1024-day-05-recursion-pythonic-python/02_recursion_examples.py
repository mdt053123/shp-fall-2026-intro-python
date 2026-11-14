"""
02 - Recursion Examples
The recipe: "If the problem is tiny, answer it. Otherwise, shrink it, solve the
smaller one, and combine."
"""


# ---- Sum of a list: first item + sum of the rest ----
def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])

print(sum_list([3, 1, 4, 1, 5]))           # 14


# ---- Reverse a string: last char + reverse of everything else ----
def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])

print(reverse("recursion"))


# ---- Palindrome: first == last, AND the middle is a palindrome ----
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"), is_palindrome("rocket"))


# ---- Power: base^exp = base * base^(exp-1) ----
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))


# ---- GCD (Euclid's algorithm, ~300 BC): gcd(a, b) = gcd(b, a % b) ----
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))                          # 6

print()


# ---- Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ... Each is the sum of the two before. ----
calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)          # TWO recursive calls

for n in [10, 20, 25]:
    calls = 0
    print(f"fib({n}) = {fib(n)}  took {calls:,} calls!")
# The number of calls explodes because the same values are recomputed over
# and over. A loop (or "memoization") fixes this:

def fib_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_fast(100))

print()


# ---- Where recursion SHINES: nested structures ----
# A list that can contain lists that contain lists... Loops struggle; recursion is natural.
def deep_sum(item):
    if isinstance(item, list):
        total = 0
        for sub in item:
            total += deep_sum(sub)          # each sub-item might itself be a list
        return total
    return item                             # base case: a plain number

print(deep_sum([1, [2, 3], [4, [5, [6]]]]))  # 21

# Similar recursive structures: folders inside folders, family trees,
# HTML pages, game trees, fractals...
