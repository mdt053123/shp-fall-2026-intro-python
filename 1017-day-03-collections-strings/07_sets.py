"""
07 - Sets
An UNORDERED collection of UNIQUE values. No duplicates, no indexing.
Great for: removing duplicates, fast membership checks, comparing groups.
"""

s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
print(s)                     # duplicates removed (order not guaranteed)
print(len(s))

empty = set()                # NOT {} -- that's an empty DICT!

s.add(100)
s.discard(3)                 # remove if present (no error if missing)
print(4 in s)                # membership check: super fast, even for huge sets

# s[0]                       # TypeError: sets have no order, so no indexing

print()

# ---- Remove duplicates from a list ----
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique = set(emails)
print(len(emails), "emails,", len(unique), "unique")

print()

# ---- Set math ----
chess_club = {"Ada", "Alan", "Grace", "Linus"}
robotics = {"Grace", "Guido", "Alan", "Margaret"}

print("Both clubs:  ", chess_club & robotics)    # intersection
print("Either club: ", chess_club | robotics)    # union
print("Chess only:  ", chess_club - robotics)    # difference
print("Exactly one: ", chess_club ^ robotics)    # symmetric difference

# The same operations as methods:
print(chess_club.intersection(robotics) == chess_club & robotics)
print({"Ada", "Alan"}.issubset(chess_club))      # True

print()

# ---- Which letters appear in a word? ----
print(sorted(set("mississippi")))                # ['i', 'm', 'p', 's']
