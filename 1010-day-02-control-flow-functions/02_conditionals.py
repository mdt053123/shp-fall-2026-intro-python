"""
02 - Conditionals: if / elif / else
Run different code depending on a condition.
"""

# ---- if / else: choose between two paths ----
is_raining = True

if is_raining:                 # same as: if is_raining == True:
    print("Bring an umbrella!")
else:
    print("Enjoy the sunshine!")

# NOTE the colon (:) and the INDENTATION (4 spaces).
# Indentation is how Python knows which lines belong to the if.

print()

# ---- if / elif / else: choose among many paths ----
# Python checks each condition IN ORDER and runs only the FIRST one that's True.
score = 84

if score >= 90:
    print("A")
elif score >= 80:
    print("B")        # <- this one runs; the rest are skipped
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

print()

# ---- Order matters! This version is WRONG. Why? ----
if score >= 60:
    print("D")        # 84 >= 60 is True, so this runs first... oops
elif score >= 90:
    print("A")

print()

# ---- if without else: sometimes you only act when something is true ----
temperature = 101
if temperature > 100:
    print("Warning: it's very hot!")
print("This line always runs (it's not indented under the if).")

print()

# ---- Nested ifs: an if inside an if ----
has_ticket = True
age = 15

if has_ticket:
    if age >= 13:
        print("Enjoy the PG-13 movie!")
    else:
        print("You need a parent with you.")
else:
    print("Please buy a ticket first.")
