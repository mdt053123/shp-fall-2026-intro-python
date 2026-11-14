"""
06 - enumerate() and zip()
Cleaner loops when you need an index, or need to walk through two lists at once.
"""

names = ["Ada", "Alan", "Grace"]
scores = [95, 82, 99]

# ---- enumerate: gives (index, item) pairs ----
# Instead of:  for i in range(len(names)): print(i, names[i])
for i, name in enumerate(names):
    print(i, name)

for rank, name in enumerate(names, start=1):     # start counting at 1
    print(f"#{rank}: {name}")

print()

# ---- zip: walk through several lists side by side ----
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Build a dict from two lists
gradebook = dict(zip(names, scores))
print(gradebook)

# Pairwise differences (compare each item with the next)
temps = [60, 65, 63, 70]
changes = [b - a for a, b in zip(temps, temps[1:])]
print(changes)

# zip stops at the SHORTEST list
print(list(zip([1, 2, 3], ["a", "b"])))
