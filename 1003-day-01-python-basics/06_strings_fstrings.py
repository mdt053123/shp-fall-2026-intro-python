"""
06 - Strings and f-strings
Building text that includes variables.
"""

name = "Ada"
age = 36

# ---- Three ways to mix text and variables ----
print("Name: " + name + ", age: " + str(age))   # 1. concatenation (needs str())
print("Name:", name, "age:", age)               # 2. commas in print
print(f"Name: {name}, age: {age}")              # 3. f-string  <- BEST!

# ---- f-strings: put an f before the quote, and {expressions} inside ----
print(f"Next year, {name} will be {age + 1}.")  # any expression works in {}
print(f"{name} has {len(name)} letters.")       # len() = length of a string

# ---- Formatting numbers ----
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")            # 3.14
price = 7.5
print(f"Total: ${price:.2f}")                   # $7.50
big = 1234567
print(f"Population: {big:,}")                   # 1,234,567

print()

# ---- A few handy string methods (much more on Day 3) ----
word = "Python"
print(word.upper())     # PYTHON
print(word.lower())     # python
print(len(word))        # 6
