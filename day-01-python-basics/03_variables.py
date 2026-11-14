"""
03 - Variables and Types
A variable is a NAME that refers to a VALUE. Every value has a TYPE.
"""

# ---- Creating variables with = (assignment) ----
age = 16
print(age)

# Variables can be reassigned. The old value is replaced.
age = 17
print(age)

# ---- The 4 basic types ----

# int: whole numbers (positive, negative, or zero)
students = 25
print(students, type(students))

# float: numbers with a decimal point
price = 4.99
print(price, type(price))

# str: text, written inside quotes
name = "Ada Lovelace"
print(name, type(name))

# bool: True or False (capital T and F!)
is_raining = False
print(is_raining, type(is_raining))

print()

# ---- A preview: lists hold many values (much more on Day 3) ----
scores = [90, 85, 77]
print(scores, type(scores))

print()

# ---- Variable naming rules ----
# OK:     my_age, age2, _secret, totalScore
# NOT OK: 2age (can't start with a digit), my-age (no dashes), class (reserved word)
# Python style (PEP 8): use lowercase_with_underscores ("snake_case")
first_name = "Grace"
last_name = "Hopper"
print(first_name, last_name)

# Names are case-sensitive: `score` and `Score` are DIFFERENT variables
score = 10
Score = 20
print(score, Score)

# ---- Assigning from another variable copies the VALUE (for numbers & strings) ----
x = 5
y = x      # y gets the value 5
x = 100    # changing x later does NOT change y
print(x, y)
