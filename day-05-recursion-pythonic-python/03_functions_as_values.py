"""
03 - Functions are Values
Functions are objects too: you can store them in variables, put them in
lists/dicts, pass them to other functions, and return them from functions.
"""


def square(x):
    return x * x

def double(x):
    return 2 * x

# ---- Store a function in a variable (note: no parentheses!) ----
f = square
print(f(5))                       # 25

# ---- Pass a function as an argument ----
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(square, 3))     # square(square(3)) = 81
print(apply_twice(double, 3))     # 12

def apply_to_all(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result

print(apply_to_all(square, [1, 2, 3, 4]))

print()

# ---- Functions in a dict: a tiny calculator ----
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

operations = {"+": add, "-": sub, "*": mul}
for op in ["+", "-", "*"]:
    print(f"7 {op} 3 = {operations[op](7, 3)}")

print()

# ---- Functions that RETURN functions ----
def make_multiplier(n):
    def multiply(x):
        return x * n              # remembers n from when it was created
    return multiply

triple = make_multiplier(3)
times10 = make_multiplier(10)
print(triple(5), times10(5))      # 15 50
