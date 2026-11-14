# Day 6 (Sat 10/31): Algorithms (Searching, Sorting, and Big-O)

**Big idea:** There are many ways to solve the same problem, and some are *dramatically* faster than others. Today we learn classic search and sort algorithms, and **Big-O**, the language computer scientists use to compare them. 🎃

## Learning goals
- [ ] Implement linear search and binary search (both the loop and recursive versions), and explain why binary search needs sorted data
- [ ] Implement selection sort, insertion sort, and merge sort, and trace them by hand
- [ ] Describe running time with Big-O: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- [ ] Estimate an algorithm's Big-O from its loops
- [ ] Measure running time and see Big-O in real data
- [ ] Explain why `x in set` is fast and `x in list` is slow

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 5 review (recursion + sorting with a key), check in on M4 | |
| 0:15 | **Game:** guess my number (1–1000) in 10 guesses. Why does halving work? | |
| 0:20 | Linear search; binary search (loop and recursive) | `01`, `02` |
| 0:50 | Min/max; selection sort | `03`, `04` |
| 1:10 | *Break* | |
| 1:20 | Insertion sort; merge sort (divide and conquer) | `05`, `06` |
| 1:50 | Big-O notation and the timing experiment | `07`, `08` |
| 2:15 | Exercises / Gradebook M5 | `exercises/`, [project](../gradebook-project/m5-sort-search/) |

> **Teaching tip:** act out the sorts with volunteers holding numbered cards, or use https://visualgo.net/en/sorting.

---

## Lecture notes

### 1. Searching (`01`, `02`)

| | Linear search | Binary search |
|--|---------------|---------------|
| Idea | Check every item in order | Check the middle, discard half |
| Needs sorted data? | No | **Yes** |
| Worst case | O(n) | O(log n) |
| 1,000,000 items | up to 1,000,000 checks | about 20 checks |

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:  return mid
        elif nums[mid] < target: left = mid + 1
        else:                    right = mid - 1
    return -1
```
⚠️ Binary search on **unsorted** data silently gives wrong answers.

### 2. Sorting (`04`–`06`)

| Algorithm | Idea | Best | Worst | Notes |
|-----------|------|------|-------|-------|
| **Selection sort** | Find the smallest remaining item and swap it to the front | O(n²) | O(n²) | Always does n²/2 comparisons |
| **Insertion sort** | Slide each item left into its place in the sorted part | **O(n)** | O(n²) | Fast on nearly sorted data |
| **Merge sort** | Split in half, sort each half recursively, merge | O(n log n) | O(n log n) | Divide and conquer; uses extra memory |
| `sorted()` / `.sort()` | Timsort (a merge + insertion hybrid) | O(n) | O(n log n) | Written in C. **Use this in real code!** |

**Merging** two sorted lists uses "two pointers": compare the fronts, take the smaller one, repeat. That's O(n).

**Why merge sort is O(n log n):** the list gets halved log₂(n) times ("levels"), and each level does n work merging.

### 3. Big-O (`07`)
Big-O describes how work **grows** as the input grows. It ignores constants and smaller terms: 3n² + 5n + 100 is **O(n²)**.

| Big-O | Name | n = 1,000 → about... | Example |
|-------|------|----------------------|---------|
| O(1) | constant | 1 | `lst[i]`, `d[key]`, `x in set` |
| O(log n) | logarithmic | 10 | binary search |
| O(n) | linear | 1,000 | linear search, `sum`, `max`, `x in list` |
| O(n log n) | linearithmic | 10,000 | merge sort, `sorted()` |
| O(n²) | quadratic | 1,000,000 | selection sort, all pairs |
| O(2ⁿ) | exponential | 10³⁰⁰ 😱 | naive recursive Fibonacci |

**Rules of thumb:**
- One loop → O(n).
- Nested loops → O(n²).
- Loops one after another → add them (O(n) + O(n) = O(n)).
- Halving each step → O(log n).

### 4. The timing experiment (`08`)
When n doubles: O(n) takes about **2×** as long, O(n²) about **4×**, and O(n log n) a bit more than 2×. The script shows this with real measurements. Try it on your own laptop!

---

## Common mistakes
- Using `while left < right` instead of `<=` in binary search, which misses the last candidate.
- Forgetting `+ 1` / `- 1` when moving `left`/`right`, which causes an infinite loop.
- Running binary search on unsorted data.
- In merge, forgetting to add the leftovers (`result.extend(left[i:])`).
- Thinking a *faster computer* fixes a bad algorithm. O(n²) on 10× the data is 100× slower.

## Key terms

| Term | Meaning |
|------|---------|
| **algorithm** | A step-by-step procedure for solving a problem |
| **linear / binary search** | Check everything / repeatedly halve a sorted range |
| **in-place** | Rearranges the original list without making a new one (selection, insertion) |
| **stable sort** | Equal items keep their original order |
| **divide and conquer** | Split the problem, solve the parts recursively, combine |
| **Big-O** | How running time grows with input size (worst case, ignoring constants) |
| **best / worst case** | The fastest / slowest the algorithm can be for inputs of size n |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Searching (6 functions) | last occurrence, leftmost binary search, insert position, integer square root |
| 2 | Sorting (6 functions) | bubble sort, descending selection, insertion with a key, 3-way merge, counting sort |
| 3 | Big-O quiz (12 questions) | analyzing code |
| 4 | ⭐ Make it faster | O(n²) → O(n) with sets and dicts, then timing |

## 📘 Gradebook Project, Milestone 5
Write `merge_sort(items, key)` and `binary_search(items, target, key)` in `algorithms.py`. Your gradebook uses them for rankings and lookups, and you race your merge sort against `sorted()`.
→ [gradebook-project/m5-sort-search](../gradebook-project/m5-sort-search/)

## Videos and reading
1. Binary search (HackerRank): https://www.youtube.com/watch?v=P3YID7liBug
2. Big-O notation (CS Dojo): https://www.youtube.com/watch?v=D6xkbGLQesk
3. Merge sort in 3 minutes: https://www.youtube.com/watch?v=4VqmGXwpLqc
4. Sorting animations: https://visualgo.net/en/sorting
5. 15 sorting algorithms in 6 minutes (just for fun): https://www.youtube.com/watch?v=kPRA0W1kECg
