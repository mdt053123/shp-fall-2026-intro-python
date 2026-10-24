"""
06 - Dictionaries
Store KEY -> VALUE pairs. Look things up by key instead of by position.
Like a real dictionary: word (key) -> definition (value).
"""

ages = {"Ada": 36, "Alan": 41, "Grace": 85}

# ---- Lookup by key ----
print(ages["Ada"])            # 36
# print(ages["Linus"])        # KeyError: 'Linus'
print(ages.get("Linus"))      # None  (safe: no error)
print(ages.get("Linus", 0))   # 0     (a default value)

# ---- Add or update: same syntax ----
ages["Linus"] = 56            # add a new key
ages["Ada"] = 37              # update an existing key
print(ages)

# ---- Remove ----
del ages["Linus"]
removed = ages.pop("Alan")    # remove and return the value
print(removed, ages)

# ---- Check for a KEY with 'in' ----
print("Grace" in ages)        # True
print(85 in ages)             # False: 'in' checks KEYS, not values

print()

# ---- Looping ----
capitals = {"France": "Paris", "Japan": "Tokyo", "Kenya": "Nairobi"}
for country in capitals:                    # loops over KEYS
    print(country, end=" ")
print()
for country, city in capitals.items():      # keys AND values together
    print(f"The capital of {country} is {city}")
print(list(capitals.keys()))
print(list(capitals.values()))

print()

# ---- THE counting pattern (you'll use this constantly) ----
votes = ["pizza", "tacos", "pizza", "sushi", "pizza", "tacos"]
counts = {}
for v in votes:
    if v in counts:
        counts[v] += 1
    else:
        counts[v] = 1
print(counts)

# Shorter version with .get():
counts2 = {}
for v in votes:
    counts2[v] = counts2.get(v, 0) + 1
print(counts2)

# Finding the key with the biggest value
winner = None
for food, n in counts.items():
    if winner is None or n > counts[winner]:
        winner = food
print("Winner:", winner)

print()

# ---- Values can be ANYTHING, including lists ----
rosters = {
    "period 1": ["Ada", "Alan"],
    "period 2": ["Grace", "Linus", "Guido"],
}
rosters["period 1"].append("Margaret")
for period, students in rosters.items():
    print(period, "has", len(students), "students:", students)

# Keys must be IMMUTABLE (str, int, tuple...). Lists can't be keys.
grid = {(0, 0): "start", (2, 3): "treasure"}
print(grid[(2, 3)])
