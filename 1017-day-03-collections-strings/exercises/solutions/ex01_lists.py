"""
Exercise 1 - List Practice  (SOLUTION)
--------------------------
Fill in each function. Run the file to see PASS/FAIL for each check.
Try to write these with loops rather than shortcuts (no [::-1], no set()).
"""


def first_occurrence(nums, target):
    """Return the index of the first time target appears in nums, or -1.

    first_occurrence([4, 2, 7, 2], 2) -> 1
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def reverse_list(items):
    """Return a NEW list with the items in reverse order (don't use [::-1] or .reverse()).

    reverse_list([1, 2, 3]) -> [3, 2, 1]
    """
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


def second_largest(nums):
    """Return the second-largest DISTINCT value in nums, or None if there isn't one.

    second_largest([5, 9, 3, 9, 7]) -> 7
    second_largest([4, 4]) -> None
    """
    largest = None
    second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second


def remove_duplicates(items):
    """Return a new list without duplicates, keeping the FIRST occurrence order.

    remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
    """
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def running_total(nums):
    """Return a list where each item is the sum of everything up to that point.

    running_total([1, 2, 3, 4]) -> [1, 3, 6, 10]
    """
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


def rotate_left(items, k):
    """Return a new list rotated left by k positions (k may be bigger than the length).

    rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
    Hint: slicing + the % operator
    """
    if len(items) == 0:
        return []
    k = k % len(items)
    return items[k:] + items[:k]


def merge_alternating(a, b):
    """Return a list alternating items from a and b; leftovers go at the end.

    merge_alternating([1, 2, 3], ["x", "y"]) -> [1, "x", 2, "y", 3]
    """
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    return result


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("first_occurrence([4, 2, 7, 2], 2)", first_occurrence([4, 2, 7, 2], 2), 1)
check("first_occurrence([1, 0], 5)", first_occurrence([1, 0], 5), -1)
check("reverse_list([1, 2, 3])", reverse_list([1, 2, 3]), [3, 2, 1])
check("reverse_list([])", reverse_list([]), [])
check("second_largest([5, 9, 3, 9, 7])", second_largest([5, 9, 3, 9, 7]), 7)
check("second_largest([4, 4])", second_largest([4, 4]), None)
check("second_largest([-2, -8])", second_largest([-2, -8]), -8)
check("remove_duplicates([3, 1, 3, 2, 1])", remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])
check("running_total([1, 2, 3, 4])", running_total([1, 2, 3, 4]), [1, 3, 6, 10])
check("rotate_left([1, 2, 3, 4, 5], 2)", rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
check("rotate_left([1, 2, 3], 7)", rotate_left([1, 2, 3], 7), [2, 3, 1])
check("merge_alternating([1, 2, 3], ['x', 'y'])", merge_alternating([1, 2, 3], ["x", "y"]), [1, "x", 2, "y", 3])
