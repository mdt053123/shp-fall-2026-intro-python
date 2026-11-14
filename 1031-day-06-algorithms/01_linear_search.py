"""
01 - Linear Search
Check each item one by one until you find the target.
Works on ANY list (sorted or not). Worst case: look at all n items -> O(n).
"""


def linear_search(items, target):
    """Return the index of target in items, or -1 if it's not there."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def linear_search_counting(items, target):
    """Same algorithm, but also returns how many comparisons it made."""
    comparisons = 0
    for i in range(len(items)):
        comparisons += 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


nums = [3, 7, -4, 5, 9, 10, -3]
print(linear_search(nums, 5))      # 3
print(linear_search(nums, 42))     # -1

print()

# How much work does it do?
big = list(range(1_000_000))       # underscores make big numbers readable
print(linear_search_counting(big, 10))          # found early: 11 comparisons
print(linear_search_counting(big, 999_999))     # found at the end: 1,000,000 comparisons
print(linear_search_counting(big, -1))          # not found: 1,000,000 comparisons
# Double the list -> double the work in the worst case. That's "linear": O(n).
