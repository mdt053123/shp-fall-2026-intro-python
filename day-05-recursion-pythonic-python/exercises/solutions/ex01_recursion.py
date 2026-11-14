"""
Exercise 1 - Recursion Practice  (SOLUTION)
-------------------------------
Solve each one RECURSIVELY: no for/while loops allowed! (Slicing is fine.)
For each: What's the base case? How do you make the problem smaller?
"""


def sum_digits(n):
    """Return the sum of the digits of a non-negative integer.

    sum_digits(4096) -> 19
    Hint: n % 10 is the last digit, n // 10 is the rest.
    """
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def count(items, target):
    """Return how many times target appears in the list items.

    count([1, 2, 1, 1], 1) -> 3
    """
    if len(items) == 0:
        return 0
    first = 1 if items[0] == target else 0
    return first + count(items[1:], target)


def largest(nums):
    """Return the largest number in a NON-EMPTY list (don't use max() on the whole list!).

    largest([3, 9, 2]) -> 9
    """
    if len(nums) == 1:
        return nums[0]
    rest = largest(nums[1:])
    return nums[0] if nums[0] > rest else rest


def remove_char(s, ch):
    """Return s with every occurrence of ch removed.

    remove_char("banana", "a") -> "bnn"
    """
    if s == "":
        return ""
    keep = "" if s[0] == ch else s[0]
    return keep + remove_char(s[1:], ch)


def to_binary(n):
    """Return the binary (base-2) representation of a non-negative integer, as a string.

    to_binary(5) -> "101",  to_binary(0) -> "0",  to_binary(10) -> "1010"
    Hint: the last binary digit is n % 2; the rest is to_binary(n // 2).
    """
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


def flatten(nested):
    """Flatten a list that may contain lists (that may contain lists...).

    flatten([1, [2, 3], [4, [5, [6]]]]) -> [1, 2, 3, 4, 5, 6]
    (You MAY use a for loop over the top-level items for this one.)
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def count_paths(rows, cols):
    """Count the paths from the top-left to the bottom-right corner of a grid
    with the given number of rows and columns, moving only RIGHT or DOWN.

    count_paths(1, 5) -> 1     (only one way: straight across)
    count_paths(2, 2) -> 2
    count_paths(3, 3) -> 6
    Hint: every path arrives from the square above or the square to the left.
    """
    if rows == 1 or cols == 1:
        return 1
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)


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


check("sum_digits(4096)", lambda: sum_digits(4096), 19)
check("sum_digits(7)", lambda: sum_digits(7), 7)
check("count([1, 2, 1, 1], 1)", lambda: count([1, 2, 1, 1], 1), 3)
check("count([], 5)", lambda: count([], 5), 0)
check("largest([3, 9, 2])", lambda: largest([3, 9, 2]), 9)
check("largest([-5])", lambda: largest([-5]), -5)
check("remove_char('banana', 'a')", lambda: remove_char("banana", "a"), "bnn")
check("to_binary(0)", lambda: to_binary(0), "0")
check("to_binary(5)", lambda: to_binary(5), "101")
check("to_binary(10)", lambda: to_binary(10), "1010")
check("to_binary(255)", lambda: to_binary(255), "11111111")
check("flatten", lambda: flatten([1, [2, 3], [4, [5, [6]]]]), [1, 2, 3, 4, 5, 6])
check("count_paths(1, 5)", lambda: count_paths(1, 5), 1)
check("count_paths(2, 2)", lambda: count_paths(2, 2), 2)
check("count_paths(3, 3)", lambda: count_paths(3, 3), 6)
check("count_paths(5, 5)", lambda: count_paths(5, 5), 70)
