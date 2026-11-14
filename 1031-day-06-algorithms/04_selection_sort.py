"""
04 - Selection Sort
Repeatedly SELECT the smallest remaining item and swap it into place.

  [5, 2, 9, 1]    smallest of everything is 1  -> swap into position 0
  [1, 2, 9, 5]    smallest of the rest is 2    -> already at position 1
  [1, 2, 9, 5]    smallest of the rest is 5    -> swap into position 2
  [1, 2, 5, 9]    done!

Comparisons: (n-1) + (n-2) + ... + 1 = n(n-1)/2, which is about n^2/2 -> O(n^2)
"""


def selection_sort(items):
    n = len(items)
    for i in range(n - 1):
        # find the index of the smallest item from i to the end
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        # swap it into position i
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def selection_sort_traced(items):
    n = len(items)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
        print(f"  after pass {i + 1}: {items[:i + 1]} | {items[i + 1:]}")   # sorted | unsorted
    return items


print(selection_sort([64, 25, 12, 22, 11]))
print()
selection_sort_traced([5, 2, 9, 1, 7, 3])
