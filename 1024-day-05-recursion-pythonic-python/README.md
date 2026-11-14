# Day 5 (Sat 10/24): Recursion and Pythonic Python

**Big idea:** Two new ways of thinking. **Recursion** solves a problem by solving a smaller copy of the same problem. **"Pythonic" tools** (lambdas, sorting with keys, comprehensions, `enumerate`/`zip`, exceptions) let you write clear, compact, robust code.

## Learning goals
- [ ] Write recursive functions with a base case and a recursive case, and trace the call stack
- [ ] Explain when recursion is natural (nested structures) and when it's slow (naive Fibonacci)
- [ ] Treat functions as values: pass them in, store them, return them
- [ ] Write lambdas and use `sorted`/`min`/`max` with `key=`
- [ ] Write list, dict, and set comprehensions, with filters
- [ ] Use `enumerate` and `zip`
- [ ] Catch exceptions with `try`/`except`/`else`/`finally`, and `raise` your own

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 4 review (write a small class together), check in on M3 | |
| 0:15 | Recursion: base case, call stack | `01` |
| 0:35 | Recursion examples (Fibonacci's blow-up, nested lists) | `02` |
| 0:55 | Functions as values | `03` |
| 1:05 | *Break* | |
| 1:15 | Lambda and sorting with `key` | `04` |
| 1:35 | Comprehensions; `enumerate` and `zip` | `05`, `06` |
| 1:55 | Exceptions | `07` |
| 2:10 | Odds and ends (`Counter`, `defaultdict`, `*args`...) | `08` |
| 2:15 | Exercises / Gradebook M4 | `exercises/`, [project](../gradebook-project/m4-rankings-validation/) |

---

## Lecture notes

### 1. Recursion (`01`, `02`)
```python
def factorial(n):
    if n == 0:                    # BASE CASE: small enough to answer directly
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE: shrink the problem, then combine
```
**How to think recursively:**
1. What's the smallest version of this problem, and what's its answer? That's the **base case**.
2. If someone handed you the answer to a *slightly smaller* problem, how would you finish the job?
3. Trust that the recursive call works. (This is the hard part!)

**The call stack:** each call waits for the call it made to return, and the answers bubble back up. Without a base case you get a `RecursionError` (Python's limit is about 1000 nested calls).

**Good fits for recursion:** nested structures (lists of lists, folders, trees), divide-and-conquer (binary search and merge sort on Day 6), Towers of Hanoi.
**Poor fits:** naive `fib(n)`, which recomputes the same values exponentially many times (`fib(25)` makes 242,785 calls!). Use a loop instead.

### 2. Functions are values (`03`)
```python
def apply_twice(func, x):
    return func(func(x))
apply_twice(square, 3)            # pass the function itself: no ()
ops = {"+": add, "*": mul}        # store functions in a dict
```

### 3. Lambdas and sorting (`04`)
```python
lambda x: x * x                                   # a tiny unnamed function
sorted(words, key=len)                            # sort by length
sorted(students, key=lambda s: s[1], reverse=True)
sorted(students, key=lambda s: (-s[1], s[0]))     # score high to low, then name A to Z
max(people, key=lambda p: p["age"])               # the oldest person
```
`key` tells Python *what to compare*. It's called once per item.

### 4. Comprehensions (`05`)

| Kind | Syntax | Example |
|------|--------|---------|
| list | `[expr for x in seq if cond]` | `[x*x for x in range(10) if x % 2 == 0]` |
| dict | `{k: v for x in seq}` | `{w: len(w) for w in words}` |
| set | `{expr for x in seq}` | `{w[0] for w in words}` |
| generator | `sum(expr for x in seq)` | `sum(x*x for x in nums)` |

`any(...)` and `all(...)` pair nicely with generators. **If a comprehension is hard to read, use a loop instead.**

### 5. `enumerate` and `zip` (`06`)
```python
for i, name in enumerate(names, start=1): ...
for name, score in zip(names, scores): ...
dict(zip(names, scores))
```

### 6. Exceptions (`07`)
```python
try:
    n = int(text)
except ValueError as e:
    print("bad input:", e)
else:
    print("worked!")         # only if there was no exception
finally:
    print("always runs")

raise ValueError("score must be 0-100")   # signal that a caller gave bad data
```
- Catch **specific** exceptions. A bare `except:` hides real bugs.
- The pattern for **robust input** is `while True:` + `try: int(input(...))` + `except ValueError: continue`.

### 7. Odds and ends (`08`)
- The conditional expression: `"pass" if score >= 65 else "fail"`
- Extended unpacking: `first, *rest = items`
- `Counter(items).most_common(3)` and `defaultdict(list)`
- `*args` and `**kwargs`, and type hints: `def f(name: str) -> str:`

---

## Common mistakes
- A recursive function with no base case, or a recursive call that doesn't get **smaller**.
- Forgetting to `return` the recursive call's result: `factorial(n - 1)` instead of `return n * factorial(n - 1)`.
- Writing `key=len()` instead of `key=len`. Pass the function; don't call it.
- Putting the `if/else` of a comprehension in the wrong place. A **filter** goes at the end (`[x for x in s if c]`); **choosing a value** goes at the front (`[a if c else b for x in s]`).
- Wrapping too much code in `try`, which catches errors you didn't expect.

## Key terms

| Term | Meaning |
|------|---------|
| **recursion** | A function that calls itself on a smaller problem |
| **base case** | The input the function answers directly, without recursing |
| **call stack** | The chain of function calls waiting to finish |
| **first-class function** | Functions are values that can be passed, stored, and returned |
| **lambda** | An anonymous one-expression function |
| **key function** | Tells `sorted`/`min`/`max` what to compare |
| **comprehension** | Compact syntax that builds a list, dict, or set from a sequence |
| **exception** | An error object; it can be raised and caught |
| **try / except / else / finally** | Blocks for handling exceptions |
| **raise** | Signal an error yourself |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Recursion (7 functions, no loops!) | digits, binary, flatten, grid paths |
| 2 | Comprehensions (9 one-liners) | list, dict, set, generator |
| 3 | Sorting with keys (7 functions) | leaderboards, closest value, tie-breaking |
| 4 | Exceptions (4 functions) | `try`/`except`, `raise` |
| 5 | ⭐ Towers of Hanoi and permutations | classic recursion |

## 📘 Gradebook Project, Milestone 4
Add rankings, an honor roll, and a letter-grade distribution. Make the menu crash-proof with `try`/`except`, and make `add_score` **raise** errors for bad scores.
→ [gradebook-project/m4-rankings-validation](../gradebook-project/m4-rankings-validation/)

## Videos and reading
1. Recursion (CS Dojo): https://www.youtube.com/watch?v=B0NtAFf4bvU
2. Sorting with keys: https://www.youtube.com/watch?v=D3JvDWO-BY4
3. Comprehensions: https://www.youtube.com/watch?v=3dt4OGnU5sM
4. try/except: https://www.youtube.com/watch?v=NIWwJbo-9_8
5. Official tutorial, "Errors and Exceptions": https://docs.python.org/3/tutorial/errors.html
