"""
07 - Big-O Notation
Big-O describes how the amount of WORK grows as the input size n grows.
We ignore constants and smaller terms: 3n^2 + 5n + 100 is O(n^2).

  O(1)        constant       look up list[i], dict[key]
  O(log n)    logarithmic    binary search
  O(n)        linear         linear search, sum, min, max
  O(n log n)  "n log n"      merge sort, Python's sorted()
  O(n^2)      quadratic      selection/insertion sort, all pairs
  O(2^n)      exponential    naive recursive fibonacci
"""


def constant(n):                 # O(1): same work no matter what n is
    for i in range(500):         # 500 steps... but 500 doesn't depend on n
        pass


def linear(n):                   # O(n)
    total = 0
    for i in range(n):
        total += i
    return total


def quadratic(n):                # O(n^2): n iterations x n iterations
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def all_pairs(n):                # still O(n^2): n(n-1)/2 is about n^2/2
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count


def logarithmic(n):              # O(log n): n is HALVED each step
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps


def square_root_loop(n):         # O(sqrt n): stops when i*i reaches n
    i = 1
    while i * i < n:
        i += 1
    return i


def exponential(n):              # O(2^n): each call makes TWO more calls
    if n < 2:
        return n
    return exponential(n - 1) + exponential(n - 2)


# How many steps for different sizes?
print(f"{'n':>8} {'log n':>6} {'n^2':>12} {'pairs':>12}")
for n in [10, 100, 1000]:
    print(f"{n:>8} {logarithmic(n):>6} {quadratic(n):>12,} {all_pairs(n):>12,}")

# Rules of thumb:
#   - One loop over n items             -> O(n)
#   - A loop inside a loop (both n)     -> O(n^2)
#   - Two loops one AFTER the other     -> O(n) + O(n) = O(n)
#   - Halving the problem each step     -> O(log n)
#   - `x in list` is O(n);  `x in set` / `key in dict` is O(1) on average!
