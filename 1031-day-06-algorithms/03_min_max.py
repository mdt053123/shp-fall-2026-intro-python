"""
03 - Finding the Minimum and Maximum
One pass through the list, remembering the best so far. O(n).
"""


def minimum(items):
    if len(items) == 0:
        return None
    smallest = items[0]
    for x in items[1:]:
        if x < smallest:
            smallest = x
    return smallest


def maximum(items):
    if len(items) == 0:
        return None
    largest = items[0]
    for x in items[1:]:
        if x > largest:
            largest = x
    return largest


def index_of_min(items, start=0):
    """Index of the smallest item at position start or later. (Selection sort uses this!)"""
    best = start
    for i in range(start + 1, len(items)):
        if items[i] < items[best]:
            best = i
    return best


nums = [4, 8, -2, 15, 16, -23, 42]
print(minimum(nums), maximum(nums), index_of_min(nums))
print(minimum([]))
print(index_of_min(nums, 6))       # only looks at index 6 onward
