"""
03 - Logical Operators: and, or, not
Combine conditions.

  A      B      | A and B | A or B | not A
  True   True   | True    | True   | False
  True   False  | False   | True   | False
  False  True   | False   | True   | True
  False  False  | False   | False  | True
"""

age = 16
has_permit = True

# and: BOTH must be true
if age >= 16 and has_permit:
    print("You can practice driving.")

# or: AT LEAST ONE must be true
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# not: flips True <-> False
is_raining = False
if not is_raining:
    print("No umbrella needed.")

print()

# ---- Classic example: leap years ----
# A year is a leap year if it's divisible by 4,
# EXCEPT years divisible by 100, UNLESS they're also divisible by 400.
for year in [1900, 2000, 2024, 2026]:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(year, is_leap)

print()

# ---- A common bug ----
color = "blue"
# if color == "red" or "green":     # BUG: always True! "green" by itself counts as True
if color == "red" or color == "green":   # correct: compare BOTH times
    print("warm-ish color")
else:
    print("not red or green")
