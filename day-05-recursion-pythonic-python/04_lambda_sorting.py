"""
04 - Lambda Functions and Sorting with a key
A LAMBDA is a tiny, unnamed, one-expression function:
    lambda parameters: expression
Their #1 use: telling sorted/min/max HOW to compare things.
"""

square = lambda x: x * x      # same as: def square(x): return x * x
add = lambda a, b: a + b
print(square(4), add(2, 3))

print()

# ---- sorted() with key= : sort by "something about" each item ----
words = ["banana", "Kiwi", "apple", "fig", "cherry"]
print(sorted(words))                              # alphabetical (capitals first!)
print(sorted(words, key=str.lower))               # case-insensitive
print(sorted(words, key=len))                     # by length
print(sorted(words, key=lambda w: w[-1]))         # by LAST letter
print(sorted(words, key=len, reverse=True))       # longest first

print()

# ---- Sorting records ----
students = [("Ada", 95), ("Alan", 82), ("Grace", 95), ("Linus", 70)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)

# Sort by score (high to low), then by name (A to Z) to break ties:
by_score_then_name = sorted(students, key=lambda s: (-s[1], s[0]))
print(by_score_then_name)

# Works with dicts and objects too:
people = [{"name": "Ada", "age": 36}, {"name": "Alan", "age": 41}, {"name": "Grace", "age": 85}]
print([p["name"] for p in sorted(people, key=lambda p: p["age"])])

print()

# ---- min / max with key ----
print(max(words, key=len))                        # longest word
print(min(students, key=lambda s: s[1]))          # lowest score
oldest = max(people, key=lambda p: p["age"])
print(oldest["name"])

print()

# ---- map and filter (older style; comprehensions are usually clearer) ----
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 10, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
