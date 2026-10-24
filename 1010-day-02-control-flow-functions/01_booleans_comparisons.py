"""
01 - Booleans and Comparisons
Comparisons produce True or False. These are the building blocks of decisions.
"""

x = 7

print(x == 7)    # True   equal to (TWO equals signs! one = is assignment)
print(x != 7)    # False  not equal to
print(x > 5)     # True   greater than
print(x < 5)     # False  less than
print(x >= 7)    # True   greater than or equal to
print(x <= 6)    # False  less than or equal to

print()

# You can store a comparison's result in a variable
is_adult = x >= 18
print(is_adult, type(is_adult))

# Strings can be compared too
print("apple" == "apple")    # True
print("apple" == "Apple")    # False: case matters!
print("apple" < "banana")    # True: alphabetical ("dictionary") order

print()

# Chained comparisons: Python lets you write math-style ranges
temp = 72
print(60 <= temp <= 80)      # True: same as (60 <= temp) and (temp <= 80)
