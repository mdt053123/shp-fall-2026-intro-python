"""
06 - Nested Loops
A loop inside a loop. The inner loop runs COMPLETELY for each step of the outer loop.
"""

# ---- Multiplication table ----
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:4}", end="")    # :4 pads each number to width 4
    print()                                # new line after each row

print()

# ---- Patterns: a right triangle ----
height = 5
for row in range(1, height + 1):
    print("*" * row)

print()

# ---- Same triangle with a nested loop instead of "*" * row ----
for row in range(1, height + 1):
    for col in range(row):
        print("*", end="")
    print()

print()

# ---- How many times does the inner line run? ----
count = 0
for i in range(4):
    for j in range(3):
        count += 1
print("Inner line ran", count, "times")    # 4 * 3 = 12
