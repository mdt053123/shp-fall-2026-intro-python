"""
02 - Binary Search
Only works on a SORTED list. Check the middle; throw away the half that
can't contain the target. Repeat.

Each step halves the search space:
  1,000,000 -> 500,000 -> 250,000 -> ... -> 1   (about 20 steps!)
That's O(log n).
"""


def binary_search(nums, target):
    """Return the index of target in the SORTED list nums, or -1."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1           # target must be in the RIGHT half
        else:
            right = mid - 1          # target must be in the LEFT half

    return -1                        # left passed right: nothing left to search


def binary_search_traced(nums, target):
    """Same algorithm, but prints each step so you can watch it work."""
    left, right = 0, len(nums) - 1
    step = 0
    while left <= right:
        step += 1
        mid = (left + right) // 2
        print(f"  step {step}: left={left} right={right} mid={mid} -> nums[mid]={nums[mid]}")
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(nums, target, left=0, right=None):
    """The same idea written recursively: search one half of the list."""
    if right is None:
        right = len(nums) - 1
    if left > right:                 # base case: empty range, so not found
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


nums = [-5, -3, -1, 2, 5, 7, 9, 12, 15, 20, 31]
print(binary_search(nums, 12))                 # 7
print(binary_search(nums, 4))                  # -1
print(binary_search_recursive(nums, 20))       # 9

print("\nSearching for 15:")
binary_search_traced(nums, 15)

print("\nSearching a list of 1,000,000 numbers for 777,777:")
big = list(range(1_000_000))
binary_search_traced(big, 777_777)

# WARNING: binary search on an UNSORTED list gives wrong answers (without any error!)
print("\nUnsorted list:", binary_search([9, 2, 7, 1, 5], 1))   # -1 even though 1 is there!
