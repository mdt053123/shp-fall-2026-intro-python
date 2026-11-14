# Exercise 3: Big-O Quiz (Answers)

1. **O(1)**: one step, no matter how long the list is.
2. **O(n)**: one loop over n items.
3. **O(n)**: two loops *one after the other* is n + n = 2n, and we drop the constant.
4. **O(n²)**: a loop of n *inside* a loop of n is n × n.
5. **O(log n)**: n is halved each step, so it takes about log₂(n) steps.
6. **O(1)**: always exactly 10 steps. (It doesn't depend on n; this assumes the list has at least 10 items.)
7. **O(n³)**: three nested loops of n.
8. **O(n²)**: `t in nums` on a **list** is O(n), and it runs up to n times.
9. **O(n)**: building the set is O(n), then each of the n lookups is O(1). Total O(n) + O(n) = O(n). *This is why sets are so useful!*
10. **O(n log n)**: the outer loop runs n times, and the inner loop doubles `j` until it reaches n, which is log₂(n) steps.
11. Fastest-growing (worst) to slowest-growing (best): **O(2ⁿ) > O(n²) > O(n log n) > O(n) > O(log n) > O(1)**
12. (a) about **2 seconds**. (b) about **4 seconds** (2² = 4). (c) about **1.1 seconds**. log(2000) is only slightly bigger than log(1000): log₂ goes from about 10 to about 11.
