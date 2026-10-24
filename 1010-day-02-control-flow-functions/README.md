# Day 2 (Sat 10/3): Control Flow and Functions

**Big idea:** Programs become powerful when they can **make decisions** (`if`), **repeat work** (loops), and be **broken into reusable pieces** (functions).

## Learning goals
- [ ] Write conditions with comparison operators (`== != < > <= >=`) and logical operators (`and or not`)
- [ ] Choose between paths with `if` / `elif` / `else`
- [ ] Repeat code with `while` (unknown number of times) and `for` (known number of times, or over a sequence)
- [ ] Use `range()` with 1, 2, or 3 arguments, plus `break` and `continue`
- [ ] Use the accumulator pattern (sums, counts)
- [ ] Define functions with parameters and `return`, and explain the difference between `print` and `return`
- [ ] Explain local vs global scope
- [ ] Use the `random` module

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 1 review quiz (types, `//` and `%`, casting input) | |
| 0:15 | Booleans, comparisons, `if`/`elif`/`else` | `01`, `02` |
| 0:40 | `and` / `or` / `not` | `03` |
| 0:50 | `while` loops, `break`, `continue` | `04` |
| 1:10 | *Break* | |
| 1:20 | `for` loops, `range`, accumulators, nested loops | `05`, `06` |
| 1:45 | Functions, `return`, scope | `07`, `08` |
| 2:10 | `random` + Guess the Number | `09`, `10` |
| 2:20 | Exercises, and the Gradebook Project begins (M1) | `exercises/`, [project](../gradebook-project/) |

---

## Lecture notes

### 1. Comparisons produce booleans (`01`)
`==` (equal), `!=`, `<`, `>`, `<=`, `>=` all give `True` or `False`.
- **`=` stores a value. `==` compares two values.**
- Strings compare alphabetically, and case matters.
- Chained comparisons like `60 <= temp <= 80` work.

### 2. `if` / `elif` / `else` (`02`)
```python
if score >= 90:
    print("A")
elif score >= 80:     # only checked if the one above was False
    print("B")
else:                 # runs if nothing above was True
    print("F")
```
- **The colon and the indentation (4 spaces) are required.** Indentation is how Python knows which lines belong to the `if`.
- Python checks conditions **top to bottom** and runs only the **first** true branch, so order matters.

### 3. Logical operators (`03`)

| `A` | `B` | `A and B` | `A or B` | `not A` |
|-----|-----|-----------|----------|---------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

⚠️ `if color == "red" or "green":` is **always True**. You have to write `color == "red" or color == "green"`.

### 4. `while` loops (`04`)
```python
while condition:
    ...           # repeats as long as condition is True
```
- Something inside the loop must eventually make the condition `False`. Otherwise you get an **infinite loop**; press Stop / Ctrl+C to end it.
- `break` exits the loop immediately. `continue` skips to the next iteration.
- The `while True: ... break` pattern is great for "keep asking until the input is valid."

### 5. `for` loops and `range` (`05`, `06`)

| Code | Values |
|------|--------|
| `range(5)` | 0 1 2 3 4 |
| `range(2, 6)` | 2 3 4 5 |
| `range(0, 10, 3)` | 0 3 6 9 |
| `range(5, 0, -1)` | 5 4 3 2 1 |

The **stop value is never included.** `for ch in "hello":` loops over the characters of a string.

**The accumulator pattern:**
```python
total = 0                 # 1. start empty
for i in range(1, 101):   # 2. loop
    total += i            # 3. update
```

**Nested loops:** the inner loop runs completely for every step of the outer loop. An outer loop of 4 and an inner loop of 3 means the inner body runs 12 times.

**When to use which loop:** use `for` when you know how many times or have a collection to go through. Use `while` when you're repeating *until something happens*.

### 6. Functions (`07`)
```python
def rectangle_area(width, height):     # parameters
    """Return the area of a rectangle."""  # docstring
    return width * height

area = rectangle_area(3, 5)            # arguments -> area is 15
```
- **`return` hands a value back** and exits the function immediately. **`print` only shows it on screen.** A function with no `return` gives back `None`.
- Default values: `def power(base, exponent=2)`.
- A function can return several values: `return low, high`, then `a, b = f(...)`.
- **Why use functions?** They let you reuse code, give a name to an idea, test pieces separately, and build big programs out of small ones.

### 7. Scope (`08`)
- Variables created inside a function (including parameters) are **local**. They vanish when the function ends.
- A function can *read* a global variable, but it needs `global name` to *change* one. It's usually better to pass values in and `return` results.

### 8. `random` (`09`, `10`)
```python
import random
random.randint(1, 6)        # 1..6, both ends included
random.choice(["a", "b"])   # a random item
random.random()             # float in [0, 1)
random.seed(42)             # makes the results repeatable
```

---

## Common mistakes
- Writing `=` instead of `==` in a condition.
- Forgetting the colon `:` or getting the indentation wrong.
- Forgetting to update the loop variable in a `while` loop, which causes an infinite loop.
- Off-by-one errors: `range(1, 10)` stops at **9**.
- Using `print` inside a function when you meant `return`, and then getting `None`.
- Putting `return` inside a loop by accident, so the function stops on the first iteration.

## Key terms

| Term | Meaning |
|------|---------|
| **boolean** | `True` or `False` |
| **condition** | An expression that is `True` or `False` |
| **branch** | One path in an `if`/`elif`/`else` |
| **loop / iteration** | Repeating code / one pass through the loop |
| **infinite loop** | A loop whose condition never becomes `False` |
| **accumulator** | A variable that builds up a result across loop iterations |
| **function** | A named, reusable block of code (`def`) |
| **parameter / argument** | The variable in the definition / the value passed in the call |
| **return value** | The value a function hands back (`None` if there is no `return`) |
| **docstring** | A `"""description"""` right under `def` |
| **scope** | Where a variable exists (local = inside a function, global = the whole file) |
| **module** | A file of reusable code you can `import` (e.g. `random`) |

## Exercises → [`exercises/`](exercises/)
Files that have functions include **automatic checks**. Run the file and it prints `PASS`/`FAIL` for each test.

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | FizzBuzz | `if`/`elif` order, `%` |
| 2 | Function practice (8 functions, auto-checked) | conditions, loops, return |
| 3 | Patterns (square, staircase, pyramid, checkerboard) | nested loops |
| 4 | Dice simulator | `random`, counting, percentages |
| 5 | Rock, Paper, Scissors | functions, input validation, game loop |
| 6 | ⭐ Collatz conjecture | `while` loops, a famous unsolved problem |
| 7 | ⭐ Square roots by hand | Newton's method |

## 📘 Gradebook Project, Milestone 1
Build a grade calculator: enter scores until the user types `done`, then show the average and letter grade.
→ [gradebook-project/m1-grade-calculator](../gradebook-project/m1-grade-calculator/)

## Videos and reading
1. Conditionals and booleans: https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=6
2. Loops: https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=7
3. Functions: https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8
4. Random module: https://www.youtube.com/watch?v=KzqSDvzOFNA
5. Official tutorial, "More Control Flow Tools": https://docs.python.org/3/tutorial/controlflow.html
