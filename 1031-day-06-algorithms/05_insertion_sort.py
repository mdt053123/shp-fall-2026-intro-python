"""
05 - Insertion Sort
Like sorting a hand of cards: take the next card and slide it LEFT into its
place among the cards you've already sorted.

Worst case O(n^2) (reverse-sorted input), but O(n) when the list is ALREADY
nearly sorted -- it's "adaptive". Python's built-in sort (Timsort) uses
insertion sort on small pieces for exactly this reason.
"""


def insertion_sort(items):
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        # shift bigger items one spot to the right
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current          # drop current into the gap
    return items


def insertion_sort_counting(items):
    """Returns the number of shifts, to compare different inputs."""
    shifts = 0
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
            shifts += 1
        items[j + 1] = current
    return shifts


print(insertion_sort([5, 2, 9, 1, 7, 3]))
print(insertion_sort(["pear", "apple", "fig"]))     # works on anything comparable

n = 1000
print("shifts, already sorted:", insertion_sort_counting(list(range(n))))          # 0
print("shifts, nearly sorted: ", insertion_sort_counting(list(range(n)) + [0]))    # ~n
print("shifts, reversed:      ", insertion_sort_counting(list(range(n, 0, -1))))   # ~n^2/2
