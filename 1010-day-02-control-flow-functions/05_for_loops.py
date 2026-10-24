"""
05 - For Loops and range()
Repeat once for each item in a sequence.
Use for when you know how many times (or have a collection to go through).
"""

# ---- range(stop): 0, 1, ..., stop - 1 ----
for i in range(5):
    print(i, end=" ")        # 0 1 2 3 4   (5 is NOT included)
print()

# ---- range(start, stop) ----
for i in range(3, 8):
    print(i, end=" ")        # 3 4 5 6 7
print()

# ---- range(start, stop, step) ----
for i in range(0, 20, 5):
    print(i, end=" ")        # 0 5 10 15
print()

for i in range(10, 0, -1):
    print(i, end=" ")        # 10 9 8 ... 1  (counting down)
print()

print()

# ---- Loop over a string, character by character ----
for letter in "Python":
    print(letter, end="-")
print()

# ---- Loop over a list (more on lists next week) ----
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

print()

# ---- The ACCUMULATOR pattern: build up a result in a loop ----
total = 0                    # 1. start with an empty result
for i in range(1, 101):      # 2. loop
    total += i               # 3. update the result each time
print("1 + 2 + ... + 100 =", total)   # 5050

# Counting is an accumulator too
evens = 0
for i in range(1, 51):
    if i % 2 == 0:
        evens += 1
print("Even numbers from 1 to 50:", evens)

# ---- for vs while: these do the same thing ----
for i in range(3):
    print("for", i)

i = 0
while i < 3:
    print("while", i)
    i += 1
