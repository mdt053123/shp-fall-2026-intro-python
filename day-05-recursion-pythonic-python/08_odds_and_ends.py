"""
08 - Odds and Ends: Handy Python Features
"""

from collections import Counter, defaultdict

# ---- Conditional expression (a.k.a. ternary): value_if_true if condition else value_if_false ----
score = 72
status = "pass" if score >= 65 else "fail"
print(status)

# ---- Extended unpacking with * ----
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)          # 1 [2, 3, 4] 5

# ---- Counter: counting made easy ----
votes = ["pizza", "tacos", "pizza", "sushi", "pizza", "tacos"]
counts = Counter(votes)
print(counts)
print(counts.most_common(2))        # [('pizza', 3), ('tacos', 2)]
print(Counter("mississippi").most_common(1))

# ---- defaultdict: a dict with a default value for missing keys ----
groups = defaultdict(list)          # missing keys start as []
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    groups[word[0]].append(word)    # no "if key not in dict" check needed!
print(dict(groups))

print()

# ---- *args: accept any number of positional arguments ----
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print(average(90, 80), average(1, 2, 3, 4))

# ---- **kwargs: accept any number of keyword arguments (as a dict) ----
def describe(name, **details):
    extras = ", ".join(f"{k}={v}" for k, v in details.items())
    print(f"{name}: {extras}")

describe("Ada", born=1815, field="math")

# ---- Type hints: document what types a function expects (Python doesn't enforce them) ----
def greet(name: str, times: int = 1) -> str:
    return ("Hello, " + name + "! ") * times

print(greet("Grace", 2))

# ---- Underscore for "I don't need this variable" ----
for _ in range(3):
    print("hip hip hooray!")
