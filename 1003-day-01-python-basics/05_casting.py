"""
05 - Type Casting (Converting Between Types)
int(), float(), str(), bool()
"""

# ---- int -> float ----
x = 3
print(float(x))         # 3.0

# ---- float -> int: CHOPS OFF the decimal (does not round!) ----
print(int(3.99))        # 3
print(round(3.99))      # 4  <- use round() if you want rounding
print(round(3.14159, 2))  # 3.14  (round to 2 decimal places)

# ---- str -> int / float ----
num_text = "42"
print(int(num_text) + 1)      # 43
print(float("2.5") * 2)       # 5.0

# ---- number -> str ----
print(str(3.85) + " dollars")  # "3.85 dollars"

# ---- Why does this matter? You can't mix str and int with + ----
age = 16
# print("I am " + age)       # TypeError! can't add str and int
print("I am " + str(age))    # works

# ---- Not every string can become a number ----
# int("hello")   # ValueError: invalid literal for int()
# int("3.5")     # ValueError: int() can't read decimals directly...
print(int(float("3.5")))     # ...but you can go str -> float -> int

# ---- bool(): what counts as True/False? ----
print(bool(0), bool(1), bool(-5))      # False True True
print(bool(""), bool("hi"))            # False True  (empty string is False)
