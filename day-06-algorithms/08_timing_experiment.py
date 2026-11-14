"""
08 - Timing Experiment: See Big-O With Your Own Eyes
Time each algorithm as n doubles and look at the RATIO between rows:
  O(n)       -> time roughly x2 when n doubles
  O(n^2)     -> time roughly x4 when n doubles
  O(n log n) -> time a little more than x2
(Exact numbers depend on your computer!)
"""

import random
import time


def selection_sort(items):
    n = len(items)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if items[j] < items[m]:
                m = j
        items[i], items[m] = items[m], items[i]
    return items


def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def time_it(func, data):
    """Return how many seconds func takes on a COPY of data."""
    copy = list(data)
    start = time.perf_counter()
    func(copy)
    return time.perf_counter() - start


algorithms = [("selection sort", selection_sort), ("merge sort", merge_sort), ("sorted()", sorted)]

print(f"{'n':>6} | " + " | ".join(f"{name:>16}" for name, _ in algorithms))
print("-" * 64)
previous = None
for n in [500, 1000, 2000, 4000]:
    data = [random.randint(0, 1_000_000) for _ in range(n)]
    times = [time_it(func, data) for _, func in algorithms]
    cells = []
    for k, t in enumerate(times):
        ratio = f" (x{t / previous[k]:.1f})" if previous else ""
        cells.append(f"{t * 1000:8.2f}ms{ratio:>6}")
    print(f"{n:>6} | " + " | ".join(f"{c:>16}" for c in cells))
    previous = times

# Search: list 'in' is O(n), set 'in' is O(1) on average
n = 1_000_000
as_list = list(range(n))
as_set = set(as_list)
start = time.perf_counter()
for _ in range(100):
    (n - 1) in as_list
list_time = time.perf_counter() - start
start = time.perf_counter()
for _ in range(100):
    (n - 1) in as_set
set_time = time.perf_counter() - start
print(f"\n100 lookups in a list of 1,000,000: {list_time * 1000:.1f} ms")
print(f"100 lookups in a set  of 1,000,000: {set_time * 1000:.3f} ms")
