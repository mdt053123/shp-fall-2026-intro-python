"""
05 - Comprehensions
A compact way to build a list/dict/set from another sequence.
    [EXPRESSION for ITEM in SEQUENCE if CONDITION]
Read it as: "make a list of EXPRESSION, for each ITEM in SEQUENCE, keeping only if CONDITION"
"""

# ---- The loop way vs the comprehension way ----
squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

squares = [x * x for x in range(10)]            # same thing, one line
print(squares)

# ---- With a filter ----
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

words = ["python", "is", "a", "fun", "language"]
long_words = [w.upper() for w in words if len(w) > 3]
print(long_words)

# ---- if/else goes BEFORE the for (it's a "conditional expression") ----
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)

print()

# ---- Dict comprehension: {KEY: VALUE for ...} ----
lengths = {w: len(w) for w in words}
print(lengths)

scores = {"Ada": 95, "Alan": 72, "Grace": 88}
passed = {name: s for name, s in scores.items() if s >= 80}
print(passed)

# ---- Set comprehension: {EXPR for ...} ----
first_letters = {w[0] for w in ["apple", "avocado", "banana", "blueberry", "cherry"]}
print(first_letters)

print()

# ---- Nested comprehensions: build a 2D grid ----
grid = [[r * 3 + c for c in range(3)] for r in range(3)]
for row in grid:
    print(row)

# Flatten a 2D list
flat = [x for row in grid for x in row]
print(flat)

# ---- Built-in functions that pair well with comprehensions ----
nums = [4, 8, 15, 16, 23, 42]
print(sum(x * x for x in nums))                 # sum of squares (no [] needed!)
print(any(x > 40 for x in nums))                # is ANY item > 40?
print(all(x % 2 == 0 for x in nums))            # are ALL even?

# Tip: if a comprehension gets hard to read, use a regular loop instead!
