# Day 1 (Sat 9/26): Python Basics

**Big idea:** A program is a list of instructions. Today we learn how to store values, do math with them, get input from a user, and show output.

## Learning goals
By the end of today you can:
- [ ] Explain what a programming language is, the difference between compiled and interpreted code, and where Python came from
- [ ] Run a Python file in Thonny and use the shell
- [ ] Print output, including escape sequences and multi-line text
- [ ] Create variables and name the 4 basic types: `int`, `float`, `str`, `bool`
- [ ] Use all 7 arithmetic operators, especially `//` and `%`
- [ ] Convert between types (`int()`, `float()`, `str()`)
- [ ] Get user input and format output with f-strings
- [ ] Read an error message and fix it

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Welcome, course overview, setup check | [SETUP.md](../SETUP.md) |
| 0:15 | What is programming? History of Python | [00_intro_to_programming.md](00_intro_to_programming.md) |
| 0:45 | First programs: print, comments | `01`, `02` |
| 1:00 | Variables and types | `03` |
| 1:15 | *Break* | |
| 1:25 | Operators; casting | `04`, `05` |
| 1:50 | f-strings, input | `06`, `07` |
| 2:05 | Errors and debugging | `08` |
| 2:15 | Put it together: mini-programs, then exercises | `09`–`11`, `exercises/` |

---

## Lecture notes

### 0. What is programming?
See **[00_intro_to_programming.md](00_intro_to_programming.md)** for:
- what a program is
- machine code vs high-level languages
- compiled vs interpreted
- a history of programming languages and of Python (Guido van Rossum, 1989–1991, Monty Python, Python 2 → 3)
- the Zen of Python
- why we're learning Python

### 1. `print()` and comments (`01_hello_world.py`, `02_print_output.py`)
```python
# This is a comment. Python ignores it.
print("Hello, World!")
print("Line 1\nLine 2")        # \n = newline, \t = tab, \\ = backslash
print('single', "double", """triple (multi-line)""")
print("a", "b", sep="-")       # a-b
print("no newline", end="")
```
- Python runs a file **top to bottom**.
- A string can use single, double, or triple quotes. Use one kind to hold the other: `'She said "hi"'`.

### 2. Variables and types (`03_variables.py`)
A **variable** is a name that refers to a value. `=` means **"store this value"**, not "is equal to."

| Type | Meaning | Examples |
|------|---------|----------|
| `int` | whole number | `3`, `-10`, `0` |
| `float` | decimal number | `3.14`, `2.0`, `-0.5` |
| `str` | text | `"hello"`, `'A'`, `""` |
| `bool` | true/false | `True`, `False` |

- `type(x)` tells you the type of a value.
- **Naming rules:** letters, digits, and `_` only. A name can't start with a digit, and names are case-sensitive. Use `snake_case`.

### 3. Operators (`04_operators.py`)

| Op | Meaning | Example | Result |
|----|---------|---------|--------|
| `+` | add | `17 + 5` | `22` |
| `-` | subtract | `17 - 5` | `12` |
| `*` | multiply | `17 * 5` | `85` |
| `/` | divide (**always float**) | `17 / 5` | `3.4` |
| `//` | floor divide (round **down**) | `17 // 5` | `3` |
| `%` | modulo (**remainder**) | `17 % 5` | `2` |
| `**` | power | `2 ** 10` | `1024` |

- **Order of operations:** `**`, then `* / // %`, then `+ -`. Use parentheses when in doubt.
- **Augmented assignment:** `x += 1` means `x = x + 1`.
- **Modulo tricks:**
  - `n % 2 == 0` means `n` is even.
  - `n % 10` is the last digit.
  - `n // 10` removes the last digit.

### 4. Casting (`05_casting.py`)
- `int("42")` gives `42`.
- `float("2.5")` gives `2.5`.
- `str(3.85)` gives `"3.85"`.
- `int(3.99)` gives `3`: it **chops off** the decimal. Use `round()` if you want rounding.
- `"Age: " + 16` is a **TypeError**. Use `"Age: " + str(16)`, or better, an f-string.

### 5. f-strings and input (`06_strings_fstrings.py`, `07_user_input.py`)
```python
name = input("Name? ")                 # input() ALWAYS returns a str
age = int(input("Age? "))              # cast it to do math
print(f"Hi {name}, next year you'll be {age + 1}")
print(f"Price: ${7.5:.2f}")            # Price: $7.50
```

### 6. Errors (`08_errors.py`)
Read the **last line** of the error first, then find the **line number**.

| Error | Cause | Example |
|-------|-------|---------|
| `SyntaxError` | Not valid Python | `print("hi)` |
| `NameError` | Unknown name (usually a typo) | `print(scroe)` |
| `TypeError` | Wrong type for an operation | `"a" + 1` |
| `ValueError` | Right type, bad value | `int("twelve")` |
| `ZeroDivisionError` | Dividing by zero | `5 / 0` |
| `IndentationError` | Unexpected spaces | a line indented for no reason |
| **Logic error** | Runs fine, gives the wrong answer | `a + b / 2` instead of `(a + b) / 2` |

### 7. Putting it together (`09_temperature.py`, `10_bio.py`, `11_mad_libs.py`)
Almost every program follows the same pattern: **input → process → output**.

---

## Common mistakes
- Forgetting that `input()` returns a **string**. For example, `"5" * 3` is `"555"`, not `15`.
- Writing `print("x")` (the letter x) when you mean `print(x)` (the variable).
- Mixing `str` and numbers with `+`.
- Expecting `/` to give an `int`. `4 / 2` is `2.0`.
- Writing `true` instead of `True`. Capitalization matters!

## Key terms

| Term | Meaning |
|------|---------|
| **variable** | A name that refers to a value |
| **assignment** | Storing a value in a variable with `=` |
| **type** | The kind of value: `int`, `float`, `str`, `bool`, ... |
| **string (`str`)** | Text in quotes |
| **escape sequence** | Special character like `\n` (newline) or `\t` (tab) |
| **operator** | A symbol that does an operation: `+ - * / // % **` |
| **floor division** | `//`: divide and round down |
| **modulo** | `%`: the remainder after division |
| **casting** | Converting a value's type: `int()`, `float()`, `str()` |
| **f-string** | `f"...{expression}..."`, a string with values plugged in |
| **input()** | Reads a line of text from the user (always a `str`) |
| **comment** | `# text` ignored by Python, written for humans |
| **traceback** | The error report Python prints when something goes wrong |
| **syntax / logic error** | Invalid code vs valid code that gives wrong results |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Tip calculator | input, casting, math, `:.2f` |
| 2 | Time converter | `//` and `%` |
| 3 | Debug me! | reading and fixing all error types |
| 4 | Store receipt | variables, formatting |
| 5 | Your own Mad Libs | f-strings, creativity |
| 6 | Coin change | `//` and `%` chains |
| 7 | ⭐ Digit sum (challenge) | modulo tricks |

Solutions are in [`exercises/solutions/`](exercises/solutions/). Try each exercise for real before you look!

## Videos and reading
*These may cover a bit more or less than we did. What matters is that you can understand, and recreate yourself, every file in this folder.*
1. Strings and output: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
2. Ints, floats, operators: https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3
3. User input: https://www.youtube.com/watch?v=we54H-T1AL0
4. Variables and types: https://www.youtube.com/watch?v=LKFrQXaoSMQ
5. The official Python tutorial, section 3 ("An Informal Introduction"): https://docs.python.org/3/tutorial/introduction.html

**Next week (Day 2):** making decisions with `if`, repeating with loops, and writing your own functions. That's also when the **[Gradebook Project](../gradebook-project/)** begins.
