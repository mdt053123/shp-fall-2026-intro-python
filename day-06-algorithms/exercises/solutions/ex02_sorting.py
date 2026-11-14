"""
Exercise 2 - Sorting  (SOLUTION)
--------------------
Implement these WITHOUT using sort() or sorted() (except where noted).
"""


def is_sorted(items):
    """Return True if items is in non-decreasing order. O(n).

    is_sorted([1, 2, 2, 5]) -> True,   is_sorted([3, 1]) -> False
    """
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Bubble sort: repeatedly walk through the list, swapping neighbors that are
    out of order. After each pass, the largest remaining item has "bubbled" to
    the end. Stop early if a pass makes no swaps. Sort in place and return items.
    """
    n = len(items)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items


def selection_sort_descending(items):
    """Selection sort, but LARGEST first. Sort in place and return items."""
    n = len(items)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if items[j] > items[max_idx]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
    return items


def insertion_sort_by(items, key):
    """Insertion sort that compares key(item) instead of item (like sorted's key=).

    insertion_sort_by(["ccc", "a", "bb"], len) -> ["a", "bb", "ccc"]
    """
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and key(items[j]) > key(current):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    return items


def merge_three(a, b, c):
    """Merge three SORTED lists into one sorted list.
    Hint: you can reuse a two-list merge!
    """
    def merge(left, right):
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]
    return merge(merge(a, b), c)


def counting_sort_scores(scores):
    """Sort a list of integer test scores (each 0-100) in O(n) time -- no comparisons!
    Count how many times each score 0..100 appears, then rebuild the list.

    counting_sort_scores([90, 70, 90, 100, 0]) -> [0, 70, 90, 90, 100]
    """
    counts = [0] * 101
    for s in scores:
        counts[s] += 1
    result = []
    for score in range(101):
        result.extend([score] * counts[score])
    return result


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


import random  # noqa: E402  (used only by the checks)
random.seed(6)
data = [random.randint(-50, 50) for _ in range(30)]

check("is_sorted yes", lambda: is_sorted([1, 2, 2, 5]), True)
check("is_sorted no", lambda: is_sorted([3, 1]), False)
check("is_sorted empty", lambda: is_sorted([]), True)
check("bubble_sort", lambda: bubble_sort(list(data)), sorted(data))
check("selection_sort_descending", lambda: selection_sort_descending(list(data)), sorted(data, reverse=True))
check("insertion_sort_by len", lambda: insertion_sort_by(["ccc", "a", "bb"], len), ["a", "bb", "ccc"])
check("insertion_sort_by abs", lambda: insertion_sort_by([-5, 2, -1], abs), [-1, 2, -5])
check("merge_three", lambda: merge_three([1, 7], [2, 3, 9], [0, 8]), [0, 1, 2, 3, 7, 8, 9])
check("counting_sort_scores", lambda: counting_sort_scores([90, 70, 90, 100, 0]), [0, 70, 90, 90, 100])
