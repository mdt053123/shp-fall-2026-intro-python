# Day 3 (Sat 10/10): Collections and Strings

**Big idea:** Real programs work with *lots* of data. Python has four built-in collections (**lists, tuples, dicts, sets**), and **strings** behave like collections of characters. Picking the right structure makes a problem easy.

## Learning goals
- [ ] Create, index (including negative indices), slice, and loop over lists
- [ ] Use list methods (`append`, `insert`, `pop`, `remove`, `sort`...) and explain `sort()` vs `sorted()`
- [ ] Apply the core list patterns: accumulate, find max, filter, transform, count, search
- [ ] Use tuples for fixed groups, and use unpacking
- [ ] Index, slice, and transform strings (`split`, `join`, `strip`, `replace`...)
- [ ] Use dicts for lookups and **counting**
- [ ] Use sets for uniqueness and set math
- [ ] Choose the right structure for a problem, and combine structures (a list of dicts, a dict of lists)

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 2 review (loops + functions), check in on Gradebook M1 | |
| 0:15 | Lists: indexing, slicing, looping | `01` |
| 0:35 | List methods; common list patterns | `02`, `03` |
| 1:00 | Tuples and unpacking | `04` |
| 1:10 | *Break* | |
| 1:20 | Strings as sequences | `05` |
| 1:40 | Dictionaries and the counting pattern | `06` |
| 2:00 | Sets; combining structures | `07`, `08` |
| 2:15 | Exercises / Gradebook M2 | `exercises/`, [project](../gradebook-project/m2-roster/) |

---

## Lecture notes

### 1. Lists (`01`, `02`)
```python
nums = [3, 7, -4, 5, 9]
nums[0]      # 3       first item (indices start at 0!)
nums[-1]     # 9       last item
nums[1:3]    # [7, -4] slice: start is included, stop is not
nums[::-1]   # reversed copy
len(nums)    # 5
7 in nums    # True
nums[0] = 100  # lists are mutable
```

| Method | Does | Returns |
|--------|------|---------|
| `lst.append(x)` | add `x` to the end | `None` |
| `lst.insert(i, x)` | insert `x` at index `i` | `None` |
| `lst.extend(other)` | add every item from `other` | `None` |
| `lst.pop()` / `lst.pop(i)` | remove the last item / item at `i` | the removed item |
| `lst.remove(x)` | remove the first `x` | `None` |
| `lst.index(x)` / `lst.count(x)` | find / count `x` | int |
| `lst.sort()` / `lst.reverse()` | change the list in place | `None` ⚠️ |
| `sorted(lst)` | — | a **new** sorted list |
| `sum`, `min`, `max`, `len` | built-in functions | a number |

### 2. The list patterns (`03`)
These eight patterns (accumulate, find max, find the index of the max, filter, transform, count, search, compare neighbors) solve most list problems. **Learn them by heart.** When comparing neighbors, loop over `range(len(lst) - 1)` so that `lst[i + 1]` stays valid.

### 3. Tuples (`04`)
```python
point = (3, 4)          # immutable
x, y = point            # unpacking
a, b = b, a             # swap
for name, score in [("Ada", 95), ("Alan", 88)]:   # unpack in a loop
```
A 1-item tuple needs a comma: `(5,)`.

### 4. Strings (`05`)
Strings are **immutable sequences**, so indexing, slicing, `len`, `in`, and `for` loops all work on them.

| Method | Example | Result |
|--------|---------|--------|
| `strip()` | `"  hi  ".strip()` | `"hi"` |
| `lower()` / `upper()` | `"Hi".lower()` | `"hi"` |
| `replace(a, b)` | `"cat".replace("c", "b")` | `"bat"` |
| `split()` | `"a b c".split()` | `["a", "b", "c"]` |
| `sep.join(list)` | `"-".join(["a", "b"])` | `"a-b"` |
| `find(sub)` | `"hello".find("l")` | `2` (-1 if missing) |
| `startswith` / `endswith` | `"hi.py".endswith(".py")` | `True` |
| `isdigit` / `isalpha` / `isalnum` | `"42".isdigit()` | `True` |

Methods return **new** strings. `s.upper()` alone does nothing useful; you need `s = s.upper()`.

### 5. Dictionaries (`06`)
```python
ages = {"Ada": 36, "Alan": 41}
ages["Ada"]              # 36 (KeyError if missing)
ages.get("Zed", 0)       # 0  (safe, with a default)
ages["Grace"] = 85       # add or update
del ages["Alan"]
"Ada" in ages            # checks KEYS
for name, age in ages.items(): ...
```
**The counting pattern:**
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```
Keys must be **immutable** (str, int, tuple). Values can be anything, including lists and other dicts.

### 6. Sets (`07`)
`{1, 2, 3}` holds unique items with no order. `set()` makes an empty set, because `{}` is an empty *dict*. `in` checks are very fast.

| Op | Meaning |
|----|---------|
| `a & b` | in both (intersection) |
| `a \| b` | in either (union) |
| `a - b` | in `a` but not `b` (difference) |
| `a ^ b` | in exactly one |

### 7. Choosing a structure (`08`)

| Need | Use |
|------|-----|
| Ordered items, duplicates OK, access by position | **list** |
| A small fixed group (coordinates, a pair) | **tuple** |
| Look up values by a name or key | **dict** |
| Unique items, fast membership, group math | **set** |
| A table of records | **list of dicts** |
| Grouping items by category | **dict of lists** |
| A grid | **list of lists** |

---

## Common mistakes
- Off-by-one errors: the last index is `len(lst) - 1`.
- `lst = lst.sort()` sets `lst` to `None`. Use `lst.sort()` on its own, or `lst = sorted(lst)`.
- Calling a string method without saving the result: `name.strip()` alone changes nothing.
- `{}` is an empty **dict**, not a set.
- Changing a list while looping over it. Build a new list instead.
- `in` on a dict checks **keys**, not values.

## Key terms

| Term | Meaning |
|------|---------|
| **index** | An item's position (starts at 0; negative counts from the end) |
| **slice** | `seq[start:stop:step]`, a copy of part of a sequence |
| **mutable / immutable** | Can / can't be changed after creation (list, dict, set / str, tuple) |
| **method** | A function that belongs to a value: `lst.append(x)` |
| **unpacking** | `a, b = (1, 2)` |
| **key / value** | The lookup label / the data it maps to in a dict |
| **hashable** | Can be a dict key or set item (immutable types) |
| **KeyError / IndexError** | A missing dict key / an index out of range |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | List practice (7 functions, auto-checked) | list patterns, slicing |
| 2 | String practice (7 functions, auto-checked) | palindromes, run-length encoding, Caesar cipher |
| 3 | Dicts and sets (7 functions, auto-checked) | counting, word frequency, anagrams, grouping |
| 4 | Contact book | a dict-based menu program |
| 5 | ⭐ Hangman | strings, sets, game loop |

## 📘 Gradebook Project, Milestone 2
Handle a whole class: `{"Ada": [95, 88], ...}`, with averages, a top student, a report table, and a menu.
→ [gradebook-project/m2-roster](../gradebook-project/m2-roster/)

## Videos and reading
1. Lists, tuples, sets: https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4
2. Dictionaries: https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=5
3. Strings: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
4. Official tutorial, "Data Structures": https://docs.python.org/3/tutorial/datastructures.html
