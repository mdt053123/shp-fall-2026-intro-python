"""
06 - Merge Sort (Divide and Conquer)
  1. DIVIDE:  split the list in half
  2. CONQUER: recursively sort each half
  3. COMBINE: merge the two sorted halves into one sorted list

The list is halved log2(n) times, and each "level" of merging does n work,
so merge sort is O(n log n) -- MUCH faster than O(n^2) for big lists.
"""


def merge(left, right):
    """Merge two SORTED lists into one sorted list (the "two pointers" technique)."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])      # one of these is empty;
    result.extend(right[j:])     # the other has the leftovers (already sorted)
    return result


def merge_sort(items):
    if len(items) <= 1:          # base case: 0 or 1 items are already sorted
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def merge_sort_traced(items, depth=0):
    indent = "  " * depth
    print(f"{indent}sort {items}")
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort_traced(items[:mid], depth + 1)
    right = merge_sort_traced(items[mid:], depth + 1)
    merged = merge(left, right)
    print(f"{indent}merge {left} + {right} -> {merged}")
    return merged


print(merge([1, 4, 9], [2, 3, 10, 11]))
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print()
merge_sort_traced([38, 27, 43, 3, 9, 82, 10])
