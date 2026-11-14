"""
Exercise 4 (CHALLENGE) - Make It Faster  (SOLUTION)
---------------------------------------
Each problem has a SLOW O(n^2) version given to you. Write the FAST version
using a set or dict. Then the timing code at the bottom compares them.

1. has_duplicates: does any value appear twice?
2. two_sum: do any TWO DIFFERENT positions add up to target? Return their
   indices as a tuple (i, j) with i < j, or None.
   Hint for fast: as you walk the list, store {value: index} of what you've seen.
   For each x, is (target - x) already in the dict?
3. common_items: return a sorted list of values that appear in BOTH lists.
"""

import random
import time


def has_duplicates_slow(items):  # given
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def has_duplicates_fast(items):
    seen = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False


def two_sum_slow(nums, target):  # given
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    seen = {}
    for j, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], j)
        if x not in seen:
            seen[x] = j
    return None


def common_items_slow(a, b):  # given
    result = []
    for x in a:
        if x in b and x not in result:    # 'in' on a list is O(n) each time!
            result.append(x)
    return sorted(result)


def common_items_fast(a, b):
    return sorted(set(a) & set(b))


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


check("has_duplicates_fast yes", lambda: has_duplicates_fast([3, 1, 4, 1]), True)
check("has_duplicates_fast no", lambda: has_duplicates_fast([3, 1, 4]), False)
check("two_sum_fast", lambda: two_sum_fast([2, 7, 11, 15], 9), (0, 1))
check("two_sum_fast later", lambda: two_sum_fast([3, 2, 4], 6), (1, 2))
check("two_sum_fast none", lambda: two_sum_fast([1, 2], 10), None)
check("common_items_fast", lambda: common_items_fast([5, 1, 3, 3], [3, 5, 7]), [3, 5])


def race(label, slow, fast, *args):  # given
    start = time.perf_counter()
    slow_result = slow(*args)
    slow_time = time.perf_counter() - start
    start = time.perf_counter()
    fast_result = fast(*args)
    fast_time = time.perf_counter() - start
    same = "same answer" if slow_result == fast_result else "DIFFERENT ANSWERS!"
    print(f"{label:<15} slow {slow_time * 1000:8.1f} ms   fast {fast_time * 1000:6.2f} ms   ({same})")


print()
n = 3000
big = random.sample(range(10 * n), n)          # n distinct numbers (no duplicates: worst case)
race("has_duplicates", has_duplicates_slow, has_duplicates_fast, big)
race("two_sum", two_sum_slow, two_sum_fast, big, -1)
race("common_items", common_items_slow, common_items_fast, big, random.sample(range(10 * n), n))
