"""
03 - Common List Patterns
These few patterns show up in almost every program. Learn them by heart!
"""

temps = [68, 74, 59, 81, 77, 90, 62]

# ---- 1. Accumulate: sum / average ----
total = 0
for t in temps:
    total += t
print("Average:", total / len(temps))

# ---- 2. Find the max (by hand; this is how max() works inside) ----
hottest = temps[0]
for t in temps:
    if t > hottest:
        hottest = t
print("Hottest:", hottest)

# ---- 3. Find the INDEX of the max ----
best_i = 0
for i in range(len(temps)):
    if temps[i] > temps[best_i]:
        best_i = i
print(f"Hottest day was day {best_i} ({temps[best_i]} degrees)")

# ---- 4. Filter: build a new list with only some items ----
warm_days = []
for t in temps:
    if t >= 75:
        warm_days.append(t)
print("Warm days:", warm_days)

# ---- 5. Transform (map): build a new list by changing each item ----
celsius = []
for f in temps:
    celsius.append(round((f - 32) * 5 / 9, 1))
print("Celsius:", celsius)

# ---- 6. Count matches ----
cold = 0
for t in temps:
    if t < 65:
        cold += 1
print("Cold days:", cold)

# ---- 7. Search: is something there? where? ----
def find_first(items, target):
    """Return the index of the first target, or -1 if not found."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

print(find_first(temps, 81), find_first(temps, 100))

# ---- 8. Compare neighbors: look at items[i] and items[i + 1] ----
for i in range(len(temps) - 1):          # stop one early so i + 1 is valid!
    change = temps[i + 1] - temps[i]
    print(f"Day {i} -> {i + 1}: {change:+}")   # :+ always shows the sign
