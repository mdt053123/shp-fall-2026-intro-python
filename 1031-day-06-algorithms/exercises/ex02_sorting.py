"""
Exercise 2 - Sorting
--------------------
Implement these WITHOUT using sort() or sorted() (except where noted).
"""


def is_sorted(items):
    """Return True if items is in non-decreasing order. O(n).

    is_sorted([1, 2, 2, 5]) -> True,   is_sorted([3, 1]) -> False
    """
    # TODO
    pass


def bubble_sort(items):
    """Bubble sort: repeatedly walk through the list, swapping neighbors that are
    out of order. After each pass, the largest remaining item has "bubbled" to
    the end. Stop early if a pass makes no swaps. Sort in place and return items.
    """
    # TODO
    pass


def selection_sort_descending(items):
    """Selection sort, but LARGEST first. Sort in place and return items."""
    # TODO
    pass


def insertion_sort_by(items, key):
    """Insertion sort that compares key(item) instead of item (like sorted's key=).

    insertion_sort_by(["ccc", "a", "bb"], len) -> ["a", "bb", "ccc"]
    """
    # TODO
    pass


def merge_three(a, b, c):
    """Merge three SORTED lists into one sorted list.
    Hint: you can reuse a two-list merge!
    """
    # TODO
    pass


def counting_sort_scores(scores):
    """Sort a list of integer test scores (each 0-100) in O(n) time -- no comparisons!
    Count how many times each score 0..100 appears, then rebuild the list.

    counting_sort_scores([90, 70, 90, 100, 0]) -> [0, 70, 90, 90, 100]
    """
    # TODO
    pass


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
