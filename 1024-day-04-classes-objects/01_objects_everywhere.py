"""
01 - Everything is an Object
Every value in Python is an OBJECT: it has a TYPE (its class), DATA, and
METHODS (functions attached to it). You've been using objects all along!
"""

name = "ada lovelace"
nums = [3, 1, 2]

# The type of a value is its CLASS
print(type(name))       # <class 'str'>
print(type(nums))       # <class 'list'>
print(type(42))         # <class 'int'>
print(type(print))      # even functions are objects!

print()

# Methods are functions that belong to an object: object.method(...)
print(name.title())     # "Ada Lovelace"  -> a method of str
nums.append(4)          # a method of list
print(nums)

# dir() lists everything an object can do (ignore the __double_underscore__ ones for now)
print([m for m in dir(name) if not m.startswith("_")][:10], "...")

print()

# Different types have different methods:
# nums.upper()          # AttributeError: 'list' object has no attribute 'upper'

# isinstance() checks if an object is of a certain type
print(isinstance(name, str), isinstance(nums, str))

# TODAY: we'll create our OWN types with 'class'!
