"""
Exercise 1 - Searching  (SOLUTION)
----------------------
Variations on linear and binary search. For each one, think: what's the Big-O?
"""


def last_occurrence(items, target):
    """Return the index of the LAST time target appears, or -1. (Linear search.)

    last_occurrence([1, 3, 1, 3], 3) -> 3
    Hint: loop backwards!
    """
    for i in range(len(items) - 1, -1, -1):
        if items[i] == target:
            return i
    return -1


def find_all(items, target):
    """Return a list of EVERY index where target appears.

    find_all([5, 1, 5, 5], 5) -> [0, 2, 3]
    """
    return [i for i in range(len(items)) if items[i] == target]


def binary_search_first(nums, target):
    """nums is SORTED and may contain duplicates. Return the index of the FIRST
    occurrence of target, or -1. Must be O(log n): when you find target, don't
    stop -- remember the index and keep searching the LEFT half.

    binary_search_first([1, 2, 2, 2, 3], 2) -> 1
    """
    left, right = 0, len(nums) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer


def insert_position(nums, target):
    """nums is SORTED. Return the index where target should be inserted to keep
    it sorted (if target is already there, return the index of the first one).
    O(log n)!

    insert_position([1, 3, 5, 7], 4) -> 2
    insert_position([1, 3, 5, 7], 0) -> 0
    insert_position([1, 3, 5, 7], 9) -> 4
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def integer_sqrt(n):
    """Return the largest integer r with r*r <= n, using BINARY SEARCH over
    possible answers from 0 to n. (No ** 0.5 or math.sqrt!)

    integer_sqrt(17) -> 4,   integer_sqrt(1_000_000) -> 1000
    """
    left, right = 0, n
    best = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return best


def guess_count(n):
    """In a guess-the-number game from 1 to n where you always guess the middle,
    return the WORST-CASE number of guesses needed. (How many times can you
    halve n before reaching 0?)

    guess_count(100) -> 7,   guess_count(1_000_000) -> 20
    """
    guesses = 0
    while n > 0:
        n = n // 2
        guesses += 1
    return guesses


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


check("last_occurrence", lambda: last_occurrence([1, 3, 1, 3], 3), 3)
check("last_occurrence missing", lambda: last_occurrence([1, 2], 9), -1)
check("find_all", lambda: find_all([5, 1, 5, 5], 5), [0, 2, 3])
check("binary_search_first", lambda: binary_search_first([1, 2, 2, 2, 3], 2), 1)
check("binary_search_first long", lambda: binary_search_first([0] * 50 + [1] * 50, 1), 50)
check("binary_search_first missing", lambda: binary_search_first([1, 3, 5], 4), -1)
check("insert_position middle", lambda: insert_position([1, 3, 5, 7], 4), 2)
check("insert_position start", lambda: insert_position([1, 3, 5, 7], 0), 0)
check("insert_position end", lambda: insert_position([1, 3, 5, 7], 9), 4)
check("integer_sqrt(17)", lambda: integer_sqrt(17), 4)
check("integer_sqrt(1_000_000)", lambda: integer_sqrt(1_000_000), 1000)
check("integer_sqrt(0)", lambda: integer_sqrt(0), 0)
check("guess_count(100)", lambda: guess_count(100), 7)
check("guess_count(1_000_000)", lambda: guess_count(1_000_000), 20)
