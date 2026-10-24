"""
04 - Arithmetic Operators
+  -  *  /  //  %  **  and the order of operations.
"""

a = 17
b = 5

print("a + b  =", a + b)    # 22  addition
print("a - b  =", a - b)    # 12  subtraction
print("a * b  =", a * b)    # 85  multiplication
print("a / b  =", a / b)    # 3.4 division: ALWAYS gives a float
print("a // b =", a // b)   # 3   floor division: divide, then round DOWN
print("a % b  =", a % b)    # 2   modulo: the REMAINDER after dividing
print("a ** b =", a ** b)   # 1419857  exponent (17 to the 5th power)

print()

# ---- / always makes a float, even when it divides evenly ----
print(4 / 2)     # 2.0
print(4 // 2)    # 2

# ---- // rounds DOWN (toward negative infinity), not toward zero ----
print(7 // 2)    # 3
print(-7 // 2)   # -4  (surprising! -3.5 rounded down is -4)

print()

# ---- Modulo (%) is super useful ----
print(10 % 2)    # 0 -> 10 is even (no remainder when divided by 2)
print(11 % 2)    # 1 -> 11 is odd
print(3 % 8)     # 3 -> if the first number is smaller, the remainder is itself
print(125 % 10)  # 5 -> % 10 gives the last digit
print(125 // 10) # 12 -> // 10 chops off the last digit

print()

# ---- Order of operations (PEMDAS): ** first, then * / // %, then + - ----
print(2 + 3 * 4)       # 14, not 20
print((2 + 3) * 4)     # 20, parentheses first
print(2 ** 3 ** 2)     # 512, ** goes right-to-left: 2 ** 9

print()

# ---- Augmented assignment: shortcuts for updating a variable ----
points = 10
points += 5    # same as points = points + 5
print(points)  # 15
points *= 2    # same as points = points * 2
print(points)  # 30
points -= 1
print(points)  # 29

# ---- Some operators work on strings too! ----
print("ha" * 3)          # hahaha
print("Py" + "thon")     # Python  (joining strings = "concatenation")
