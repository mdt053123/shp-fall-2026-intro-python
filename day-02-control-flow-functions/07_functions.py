"""
07 - Functions
A function is a named, reusable block of code.
  def name(parameters):
      body
      return result
"""

# ---- Defining and calling ----
def greet(name):                     # 'name' is a PARAMETER
    print(f"Hello, {name}!")

greet("Ada")                         # "Ada" is an ARGUMENT
greet("Grace")

print()

# ---- return sends a value BACK to whoever called the function ----
def square(x):
    return x * x

result = square(7)
print(result)                        # 49
print(square(3) + square(4))         # 25 -- you can use calls inside expressions

# ---- Multiple parameters ----
def rectangle_area(width, height):
    return width * height

print(rectangle_area(3, 5))          # 15

print()

# ---- print vs return: a VERY common confusion ----
def add_print(a, b):
    print(a + b)                     # shows the value on screen, gives nothing back

def add_return(a, b):
    return a + b                     # gives the value back so you can USE it

x = add_return(2, 3)                 # x is 5
y = add_print(2, 3)                  # prints 5, but y is None!
print("x =", x, " y =", y)

print()

# ---- return exits the function immediately ----
def is_even(n):
    """Return True if n is even, False otherwise."""   # <- a DOCSTRING
    if n % 2 == 0:
        return True
    return False                     # only reached if the if was False

for i in range(5):
    print(i, is_even(i))

# Even shorter: a comparison is already True/False
def is_odd(n):
    return n % 2 == 1

print()

# ---- Default parameter values ----
def power(base, exponent=2):
    return base ** exponent

print(power(5))        # 25  (exponent defaults to 2)
print(power(2, 10))    # 1024

# ---- Keyword arguments: name them when calling, in any order ----
print(power(exponent=3, base=2))   # 8

print()

# ---- Functions can return more than one value ----
def min_and_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_and_max(8, 3, 5)
print(low, high)       # 3 8

# ---- Functions calling functions: build big things out of small pieces ----
def hypotenuse(a, b):
    return (square(a) + square(b)) ** 0.5

print(hypotenuse(3, 4))   # 5.0
